#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
translate_sync.py — keeps all language versions of the docs in sync.

Structure: the primary language (i18n.json) owns the canonical paths; every
other language is a mirror tree under translations/<lang>/ with identical
file names — markdown, the BOM CSV and generated figures included.

What drives the work is translations/.sync-state.json: for every
(document, language) pair it records the hash of the primary content the
translation was made from, and for every labels.json key the primary value it
was translated from. A pair is stale when those no longer match. The push diff
is used only to tell WHO edited WHAT (so a human edit is never overwritten and
a non-primary edit can propagate back to the primary) — never to decide what
still owes work. That is what makes an interrupted run resumable: whatever did
not get done stays stale and is picked up by the next push or the nightly run.

Logic per run:
  1. A doc edited in exactly one non-primary language propagates to the primary
     first; then the primary propagates to every language the human did not
     touch in this push.
  2. labels.json: same two phases, per key.
  3. Adding a language to i18n.json bootstraps its whole mirror tree.
  4. The language-switcher line under every H1 and all links to files that are
     not part of the mirror are rewritten deterministically, not by the model,
     on every run.

Model: any OpenAI-compatible chat-completions endpoint. The default is Ollama
Cloud (OLLAMA_API_KEY) with the open-weights glm-5.2; GitHub Models was the
original provider and was retired on 2026-07-30. Substitute another endpoint or
model via OPENAI_BASE_URL / TRANSLATE_MODEL — for a local daemon that is
OPENAI_BASE_URL=http://localhost:11434/v1 with no key.

Usage: python tools/translate_sync.py [--base <sha>] [--dry-run]
       [--no-model] runs the deterministic passes only and exits 0;
       without it, a missing API key is an error, not a warning.
"""

import argparse
import copy
import difflib
import hashlib
import json
import os
import re
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import i18n_render  # sibling module in tools/

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "i18n.json").read_text(encoding="utf-8"))
PRIMARY = CFG["primary"]
NAMES = CFG["names"]
LANGS = list(NAMES)
TR_DIR = "translations"
DOC_EXTS = (".md", ".csv")

STATE_PATH = ROOT / TR_DIR / ".sync-state.json"
STATE_VERSION = 1

ENDPOINT = os.environ.get("OPENAI_BASE_URL", "https://ollama.com/v1")
MODEL = os.environ.get("TRANSLATE_MODEL", "glm-5.2")
# Deliberately no GITHUB_TOKEN fallback: the endpoint is now a third party, and
# a GitHub token must never be sent to it.
TOKEN = (os.environ.get("OLLAMA_API_KEY") or os.environ.get("OPENAI_API_KEY")
         or "").strip()  # a secret pasted with stray whitespace still authenticates
TIMEOUT_S = 300
MAX_TOKENS = 16384
MAX_CHARS = 40_000
MAX_TASKS = 80
# A translation much shorter than its source has lost content — but the floor
# is per-script: CJK packs the same content into roughly half the Latin
# character count (the zh/ja bootstrap measured 45-51% on good translations),
# so the generic floor would reject every CJK document forever.
MIN_LENGTH_RATIO = 0.55
MIN_LENGTH_RATIO_CJK = 0.25
CJK_LANGS = {"zh", "ja", "ko"}
BOT_MARKER = "[bot]"     # matches github-actions[bot] in both %an and %ae

GLOSSARY_RU = (
    "ланжевен = Langevin transducer; свип-карта = sweep map; АЧХ = frequency response; "
    "гребёнка толщинных резонансов = comb of thickness resonances; ионистор = supercapacitor; "
    "мост Гретца/Шоттки = full-wave/Schottky bridge; нагрузочная модуляция = load modulation; "
    "обвязка = support passives; мёртвое время = dead time; струбцина = clamp; "
    "смазка = grease couplant; заваренная коробка = welded-shut box; врезка = penetration; "
    "истёкшиеся патенты = expired patents; стенд = test rig; макет = breadboard prototype"
)


def glossary_for(src_lang: str, dst_lang: str) -> str:
    """Return the glossary block only when Russian is involved in the pair."""
    if "ru" in (src_lang, dst_lang):
        return GLOSSARY_RU
    return ""


class ModelUnavailable(Exception):
    """The endpoint could not be reached at all — nothing after this will work.

    Raised instead of exiting on the spot: main() catches it, saves the state of
    whatever DID get translated and returns cleanly, so the next run resumes
    from exactly there.
    """


class BadReply(Exception):
    """This one answer is unusable — a truncated completion, a non-JSON label
    batch, an unexpected envelope. Only the current item is skipped; it stays
    stale and gets another go next run. Never written to disk: that is how
    translations/pt/README.md ended up a 478-byte stub cut off mid-link.
    """


class AuthRejected(Exception):
    """The endpoint rejected the credentials (401/403).

    Kept apart from ModelUnavailable on purpose. An outage is weather: warn,
    keep the queue, exit 0, and the next run resumes. A key the provider
    refuses is a misconfiguration that will refuse every future run too, and
    reporting it as success is how three days of translating nothing looked
    like three days of green checks.
    """


class GitError(Exception):
    pass


# Every path this run wrote. The workflow stages exactly this list rather than
# guessing at a pathspec: the previous hand-written `git add translations/ ...`
# left out the primary tree, so the language bars the deterministic pass
# rewrites in README.md and the other canonical docs were produced on the
# runner, never staged, and thrown away with the workspace — the mirrors listed
# fifteen languages while English still listed six.
WRITTEN: set[str] = set()


def write_out(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    WRITTEN.add(path.relative_to(ROOT).as_posix())


# ---------- paths ----------

def tr_path(canon: str, lang: str) -> str:
    return canon if lang == PRIMARY else f"{TR_DIR}/{lang}/{canon}"


def parse_doc(f: str):
    """Return (canonical_path, lang) for a repo doc path, or None."""
    # .github/ holds GitHub UI text (PR template etc.) — English only
    if not f.endswith(DOC_EXTS) or f.startswith(("LICENSES/", ".github/")):
        return None
    if f.startswith(TR_DIR + "/"):
        parts = f.split("/", 2)
        if len(parts) == 3 and parts[1] in LANGS:
            return parts[2], parts[1]
        return None
    return f, PRIMARY


def canonical_docs() -> list[str]:
    docs = []
    for ext in DOC_EXTS:
        for p in ROOT.rglob(f"*{ext}"):
            rel = p.relative_to(ROOT).as_posix()
            if rel.startswith((".git", "LICENSES/", TR_DIR + "/")):
                continue
            docs.append(rel)
    return sorted(docs)


def label_files() -> list[str]:
    return sorted(p.relative_to(ROOT).as_posix() for p in ROOT.rglob("labels.json")
                  if TR_DIR + "/" not in p.as_posix() and ".git" not in p.parts)


_TREE: dict[str, list[str]] | None = None


def tree_index() -> dict[str, list[str]]:
    """basename -> canonical paths. Built once; no globbing, so a model-supplied
    name full of glob metacharacters is just a dict miss.

    Excludes the entire translations/ subtree (not just the root entry) so the
    unique-basename fallback never resolves to a translation file instead of
    the canonical original.
    """
    global _TREE
    if _TREE is None:
        _TREE = {}
        skip_top = {".git", TR_DIR, "LICENSES"}
        for dirpath, dirnames, filenames in os.walk(ROOT):
            rel = Path(dirpath).relative_to(ROOT)
            at_root = rel == Path(".")
            # prune __pycache__ everywhere; prune translations/ at any depth
            dirnames[:] = [d for d in dirnames
                           if d != "__pycache__"
                           and not (at_root and d in skip_top)
                           and TR_DIR not in rel.parts]
            for fn in filenames:
                _TREE.setdefault(fn, []).append(fn if at_root else (rel / fn).as_posix())
    return _TREE


def _inside(p: Path) -> bool:
    try:
        p.relative_to(ROOT)
        return True
    except ValueError:
        return False


# ---------- language bar ----------

def langbar(canon: str, lang: str) -> str:
    here = Path(tr_path(canon, lang)).parent
    parts = []
    for l in LANGS:
        label = NAMES[l] + (" (primary)" if l == PRIMARY else "")
        if l == lang:
            parts.append(label)
        else:
            rel = os.path.relpath(tr_path(canon, l), here)
            parts.append(f"[{label}]({rel})")
    return "> " + " · ".join(parts)


def apply_langbar(text: str, canon: str, lang: str) -> str:
    lines = text.splitlines()
    bar = langbar(canon, lang)
    for i, line in enumerate(lines):
        if line.startswith("# "):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].startswith("> "):
                lines[j] = bar
            else:
                lines.insert(i + 1, "")
                lines.insert(i + 2, bar)
            break
    else:
        print(f"  ! {tr_path(canon, lang)}: no H1 — language bar not inserted")
    return "\n".join(lines).rstrip() + "\n"


# ---------- link repair ----------

# Two destination forms: a markdown ](...) and an html src="...". The markdown
# branch deliberately swallows everything up to the closing paren — a model that
# leaves a space in a file name must still be seen, otherwise the broken link is
# invisible to both the repair pass and the position alignment below.
LINK_RE = re.compile(r'\]\(([^)]*)\)|src="([^"]*)"')


def _split_dest(raw: str) -> tuple[str, str]:
    """Split a link destination into (path, suffix).

    The suffix carries the #fragment and an optional ' "title"' verbatim so a
    rewrite of the path cannot lose them.
    """
    title = ""
    m = re.search(r'(\s+"[^"]*")\s*$', raw)
    if m:
        title, raw = m.group(1), raw[:m.start()]
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    path, sep, frag = raw.partition("#")
    return path, sep + frag + title


def _strip_updirs(target: str) -> str:
    parts = list(Path(target).parts)
    i = 0
    while i < len(parts) and parts[i] in ("..", "."):
        i += 1
    return "/".join(parts[i:])


def fix_asset_links(text: str, canon: str, lang: str, src_text: str | None = None) -> str:
    """Repoint relative links whose target does not resolve from the mirror.

    Inside a mirror the relative structure matches the canonical tree, so doc
    and figure links keep working as-is. Links to code, CSVs that are not
    mirrored, license texts etc. must climb out of translations/<lang>/ — that
    rewrite is mechanical, so the model is never trusted with it.

    Repair ladder, first hit wins:
      a. the model kept the canonical path — resolve it against the canonical
         directory and repoint;
      b. the model miscounted `../` — the tail resolves from the repo root;
      c. unique basename in the canonical tree;
      d. same position in the primary source (only when both files hold the
         same number of links). This is what survives a model that translated
         the file name itself, which no path arithmetic can undo.
    Whenever a canonical file is picked, its mirror twin wins if it exists, so a
    German reader is not bounced into the English tree.

    This runs for the primary language too. A doc translated back into the
    primary arrives carrying the mirror's `../../` prefixes, and the primary
    tree used to have no repair pass at all to notice.
    """
    here = Path(tr_path(canon, lang)).parent
    canon_dir = Path(canon).parent

    def rel(p: Path) -> str:
        return Path(os.path.relpath(p, ROOT / here)).as_posix()

    def mirror_or_canon(canon_rel: str) -> Path:
        m = ROOT / tr_path(canon_rel, lang)
        return m if m.exists() else ROOT / canon_rel

    def resolve(target: str) -> str | None:
        if not target or target.startswith(("http", "mailto:", "/")):
            return target
        if (ROOT / here / target).exists():
            return target
        cand = Path(os.path.normpath(ROOT / canon_dir / target))
        if _inside(cand) and cand.exists():
            return rel(mirror_or_canon(cand.relative_to(ROOT).as_posix()))
        tail = _strip_updirs(target)
        if tail and (ROOT / tail).exists():
            return rel(mirror_or_canon(tail))
        hits = tree_index().get(Path(target).name, [])
        if len(hits) == 1:
            return rel(mirror_or_canon(hits[0]))
        return None

    src_dests = None
    if src_text is not None:
        src_dests = [_split_dest(m.group(1) if m.group(1) is not None else m.group(2))[0]
                     for m in LINK_RE.finditer(src_text)]
        if len(src_dests) != len(LINK_RE.findall(text)):
            src_dests = None  # shapes diverged — position alignment is meaningless

    idx = -1

    def sub(m):
        nonlocal idx
        idx += 1
        md = m.group(1) is not None
        path, suffix = _split_dest(m.group(1) if md else m.group(2))
        out = resolve(path)
        if out is None and src_dests is not None:
            out = resolve(src_dests[idx])
        if out is None or out == path:
            return m.group(0)
        return f"]({out}{suffix})" if md else f'src="{out}{suffix}"'

    return LINK_RE.sub(sub, text)


# ---------- git ----------

def sh(*args) -> str:
    r = subprocess.run(args, capture_output=True, text=True, cwd=ROOT)
    if r.returncode != 0:
        raise GitError(f"{' '.join(args)}: {r.stderr.strip()[:200]}")
    return r.stdout


def git_show(path: str, base: str) -> str | None:
    """Content of `path` at `base`, or None when it was not there / base is gone.

    None and "" are different answers and callers rely on that: an empty file is
    not the same as an unreachable base commit.
    """
    r = subprocess.run(["git", "show", f"{base}:{path}"],
                       capture_output=True, text=True, cwd=ROOT)
    return r.stdout if r.returncode == 0 else None


def changed_files(base: str) -> list[str]:
    """Files touched by HUMAN commits in base..HEAD.

    The bot's own commits must never read as human intent. A sync commit that
    updated only translations/pt/README.md looks exactly like "a human edited
    just the Portuguese file", so it gets propagated back into the English
    primary — carrying the mirror's ../../ link prefixes with it. That is how
    README.md acquired 39 broken links on the first scheduled run: for a
    schedule there is no push range, HEAD~1 is simply the previous sync commit.
    """
    try:
        revs = sh("git", "rev-list", f"{base}..HEAD").split()
    except GitError as e:
        print(f"::warning::cannot walk {base}..HEAD ({e}) — "
              "falling back to the sync state alone")
        return []
    files: set[str] = set()
    for r in revs:
        if BOT_MARKER in sh("git", "log", "-1", "--format=%an%ae", r):
            continue
        try:
            # first parent, so a merge commit reports what it brought in
            out = sh("git", "diff", "--name-only", "--diff-filter=ACMR", f"{r}^", r)
        except GitError:
            continue  # root commit — nothing to compare against
        files.update(l.strip() for l in out.splitlines() if l.strip())
    return sorted(files)


# ---------- state ----------

def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def seed_state() -> dict:
    """First run: treat every translation that already exists as up to date.

    Without this the first run would call the model on the entire mirror tree
    to reproduce files that are already correct — except for the mirrors that
    are visibly NOT correct. A file that lost headings or whole tables relative
    to its source is the residue of an earlier interrupted sync; leaving it
    unseeded marks it stale so the pipeline regenerates it.
    """
    st = {"version": STATE_VERSION, "docs": {}, "labels": {}}
    for c in canonical_docs():
        src = ROOT / c
        if not src.exists():
            continue
        text = src.read_text(encoding="utf-8")
        h = sha(text)
        for l in LANGS:
            if l == PRIMARY:
                continue
            twin = ROOT / tr_path(c, l)
            if not twin.exists():
                continue
            bad = implausible(text, twin.read_text(encoding="utf-8"), c, l)
            if bad:
                print(f"  ! {tr_path(c, l)}: {bad} — queued for re-translation")
                continue
            st["docs"][f"{c}|{l}"] = h
    for f in label_files():
        cur = json.loads((ROOT / f).read_text(encoding="utf-8"))
        prim = cur.get(PRIMARY, {})
        st["labels"][f] = {l: {k: v for k, v in prim.items() if k in cur[l]}
                           for l in cur if l != PRIMARY}
    return st


def load_state() -> dict:
    if STATE_PATH.exists():
        try:
            st = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print("::warning::sync state is unreadable — reseeding from the working tree")
            st = {}
        if st.get("version") == STATE_VERSION:
            st.setdefault("docs", {})
            st.setdefault("labels", {})
            return st
    return seed_state()


def save_state(state: dict, dry: bool) -> None:
    if dry:
        return
    live = {f"{c}|{l}" for c in canonical_docs() for l in LANGS if l != PRIMARY}
    state["docs"] = {k: v for k, v in state["docs"].items() if k in live}
    files = set(label_files())
    state["labels"] = {k: v for k, v in state["labels"].items() if k in files}
    write_out(STATE_PATH,
              json.dumps(state, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


# ---------- model ----------

def udiff(old: str, new: str, name: str) -> str:
    return "".join(difflib.unified_diff(
        old.splitlines(keepends=True), new.splitlines(keepends=True),
        fromfile=f"old/{name}", tofile=f"new/{name}"))[:20000]


def system_doc(dst_lang: str) -> str:
    glossary = glossary_for(PRIMARY, dst_lang)
    glossary_line = f" Terminology (ru = en): {glossary}." if glossary else ""
    return f"""You are the translation-sync bot of an open-hardware repository
(ultrasonic power/data through steel walls). The primary language is
{NAMES[PRIMARY]}; every other language is a mirror tree under
translations/<lang>/ with identical file names.{glossary_line}

Target language now: {NAMES[dst_lang]} ({dst_lang}).

Rules:
- Update the target file so it exactly mirrors the meaning and structure of the
  new source content. Keep the lively engineering tone.
- Preserve markdown structure, tables, code blocks (do not translate commands),
  numbers, part numbers, file paths.
- Keep ALL relative links exactly as they are in the source, byte for byte —
  the mirror tree makes them resolve. NEVER translate a file name inside a link
  target; translate only the visible link text in square brackets.
- For CSV files: keep the column count, order and quoting; translate only
  human-readable text (item names, notes); numbers and part numbers unchanged.
- The user message includes the diff of what changed in the source: EVERY
  added, removed or reworded fragment there must be reflected in the target.
  Do not make unrelated edits. If the target already reflects all the changes,
  return it exactly as it is.
- Return ONLY the full content of the target file. No code fences, no comments."""


def system_json(src_lang: str, dst_lang: str) -> str:
    glossary = glossary_for(src_lang, dst_lang)
    glossary_line = f" Terminology (ru = en): {glossary}." if glossary else ""
    return f"""You translate UI label strings for an open-hardware project
(ultrasonic power through steel).{glossary_line}
Input: a JSON object with strings in the source language. Return ONLY a JSON
object with the same keys and translated values. Keep placeholders like {{d}},
{{r}}, {{q}}, {{tau}}, units and part numbers intact — same placeholders, same
spelling, no new ones. No code fences."""


def chat(system: str, user: str) -> str:
    req = urllib.request.Request(
        ENDPOINT.rstrip("/") + "/chat/completions",
        data=json.dumps({
            "model": MODEL, "temperature": 0.2, "max_tokens": MAX_TOKENS,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
        }).encode(),
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=TIMEOUT_S) as r:
                payload = json.loads(r.read())
            break
        except urllib.error.HTTPError as e:  # subclass of URLError — must come first
            if e.code in (429, 503) and attempt < 2:
                wait = 2 ** attempt * 5
                print(f"  ! HTTP {e.code}, retrying in {wait}s...")
                time.sleep(wait)
                continue
            body = e.read().decode(errors="replace")[:300]
            if e.code in (401, 403):
                raise AuthRejected(f"HTTP {e.code}: {body}") from e
            raise ModelUnavailable(f"HTTP {e.code}: {body}") from e
        except (urllib.error.URLError, socket.timeout, TimeoutError, OSError) as e:
            raise ModelUnavailable(f"transport error: {e}") from e
        except json.JSONDecodeError as e:
            raise ModelUnavailable(f"response body is not JSON: {e}") from e
    else:
        raise ModelUnavailable("exhausted all retry attempts")
    try:
        choice = payload["choices"][0]
        out = choice["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise BadReply(f"unexpected response shape: {str(payload)[:300]}") from e
    # the single most damaging failure mode: the completion hit the token
    # ceiling and the tail of the document simply is not there
    if choice.get("finish_reason") not in (None, "stop"):
        raise BadReply(f"completion did not finish (finish_reason="
                       f"{choice.get('finish_reason')!r}) — output would be truncated")
    if not isinstance(out, str) or not out.strip():
        raise BadReply("empty completion")
    return re.sub(r"^.*?```[a-z]*\n|\n```\S*$", "", out.strip(), flags=re.DOTALL)  # guard against code fences


# ---------- documents ----------

def doc_shape(text: str) -> tuple[int, int]:
    """(headings, table rows) — the part of a document a translation must keep.

    Deliberately blind to wording and to link count: a translator legitimately
    rewrites prose and may inline a link differently, but it never drops half
    the headings or an entire table. Those are the fingerprints of a truncated
    or half-generated reply.
    """
    return (len(re.findall(r"(?m)^#{1,6} ", text)),
            len(re.findall(r"(?m)^\|", text)))


def split_sections(text: str) -> list[str] | None:
    """Split a markdown document at its top-level (##) headings.

    Every document at or under ~6 kB translated cleanly; the two above 8 kB came
    back as summaries in all fourteen languages, whole-document retries and an
    explicit "reproduce N headings" instruction included. Sections are the size
    the model demonstrably handles, so a document that fails as a whole is
    translated a section at a time and reassembled.
    """
    lines = text.splitlines(keepends=True)
    heads = [i for i, l in enumerate(lines) if l.startswith("## ")]
    if len(heads) < 2:
        return None
    chunks = []
    if heads[0]:
        chunks.append("".join(lines[:heads[0]]))       # preamble: H1, intro
    for a, b in zip(heads, heads[1:] + [len(lines)]):
        chunks.extend(_split_oversized("".join(lines[a:b])))
    return chunks


SECTION_MAX = 5000  # the largest input size observed translating faithfully


def _split_oversized(chunk: str) -> list[str]:
    """Cut an over-long section at blank lines, never inside a fence or table.

    README's repository map is a single 9 kB section, so splitting on headings
    alone still hands the model more than it handles. Blank lines outside
    fenced code are safe cut points: markdown tables contain none, and neither
    do the <details> blocks this document is built from.
    """
    if len(chunk) <= SECTION_MAX:
        return [chunk]
    lines = chunk.splitlines(keepends=True)
    fence = False
    cuts = []
    for i, l in enumerate(lines):
        if l.lstrip().startswith("```"):
            fence = not fence
        elif not fence and not l.strip():
            cuts.append(i)
    if not cuts:
        return [chunk]
    out, start, last = [], 0, 0
    for i in cuts:
        if sum(len(x) for x in lines[start:i]) >= SECTION_MAX:
            cut = last if last > start else i
            out.append("".join(lines[start:cut]))
            start = cut
        last = i
    out.append("".join(lines[start:]))
    return [c for c in out if c.strip()]


def implausible(src_text: str, out: str, name: str, lang: str) -> str | None:
    """Reason the reply must not be written, or None when it looks like a real
    translation."""
    ratio = MIN_LENGTH_RATIO_CJK if lang in CJK_LANGS else MIN_LENGTH_RATIO
    # absolute floor: very short docs can legitimately compress heavily in
    # concise languages, so the ratio check is skipped below this threshold
    if len(out) >= 30 and len(out) < ratio * len(src_text):
        return (f"{len(out)} chars against {len(src_text)} in the source "
                f"(<{ratio:.0%}) — content is missing")
    if len(out) < 30 and len(src_text) > 0 and len(out) < len(src_text) * 0.1:
        return (f"{len(out)} chars against {len(src_text)} in the source "
                f"(severe truncation) — content is missing")
    if name.endswith(".md"):
        want, got = doc_shape(src_text), doc_shape(out)
        if want != got:
            return (f"structure {got} != source {want} "
                    "(headings, table rows) — content is missing")
    return None


def translate_doc(src: str, dst: str, dst_lang: str, old_src: str, dry: bool) -> bool:
    src_p, dst_p = ROOT / src, ROOT / dst
    if not src_p.exists():
        return False  # source deleted — a human removes the twins
    text = src_p.read_text(encoding="utf-8")
    if len(text) > MAX_CHARS:
        print(f"  ! {src}: too large ({len(text)} chars), skipping")
        return False
    print(f"  -> {src} -> {dst}")
    if dry:
        return True
    old_dst = dst_p.read_text(encoding="utf-8")[:MAX_CHARS] if dst_p.exists() else "(missing)"
    # A bootstrap has no previous source, so udiff() re-emits the entire file as
    # additions: the document goes into the prompt twice and is then framed as a
    # change set to "reflect". The two largest documents came back as summaries
    # in all fourteen languages because of it — README.md at a ~27 kB prompt and
    # CONTRIBUTING.md at ~17 kB, while everything at 13 kB and below translated
    # cleanly. With no previous version there is nothing to diff against, so ask
    # for a plain full translation and send the source once.
    diff = udiff(old_src, text, src) if old_src.strip() else ""
    if diff:
        task = (f"What changed in the source (unified diff):\n<<<\n{diff}\n>>>\n\n"
                f"Target file `{dst}` — CURRENT (possibly outdated) content:\n"
                f"<<<\n{old_dst}\n>>>\n\n"
                "Produce the full updated target file, reflecting every change "
                "from the diff.")
    else:
        task = ("Translate the source file above into the target language in "
                "full. Reproduce every heading, table row, list item and code "
                "block: the result must mirror the structure of the source, "
                "not summarise it.")

    try:
        out = chat(system_doc(dst_lang),
                   f"Source file `{src}` — content:\n<<<\n{text}\n>>>\n\n{task}")
    except BadReply as e:
        print(f"  ! {dst}: {e} — left stale, will be retried")
        return False

    bad = implausible(text, out, dst, dst_lang)
    if bad:
        # Asking again, even naming the exact heading and table-row counts, was
        # tried and failed 28 times out of 28. The model does not need better
        # instructions, it needs smaller inputs.
        chunks = split_sections(text) if dst.endswith(".md") else None
        if not chunks:
            print(f"  ! {dst}: {bad} — not written, will be retried")
            return False
        print(f"  ~ {dst}: {bad} — retranslating in {len(chunks)} sections")
        try:
            parts = [chat(system_doc(dst_lang),
                          f"This is section {i} of {len(chunks)} of `{src}`. "
                          f"Translate this section in full and return only it, "
                          f"keeping its heading, tables, lists and code blocks "
                          f"exactly as they are:\n<<<\n{c}\n>>>")
                     for i, c in enumerate(chunks, 1)]
        except BadReply as e:
            print(f"  ! {dst}: section {e} — left stale, will be retried")
            return False
        out = "\n\n".join(p.strip() for p in parts) + "\n"
        bad = implausible(text, out, dst, dst_lang)
        if bad:
            print(f"  ! {dst}: {bad} section by section too — not written")
            return False
    canon, _ = parse_doc(dst)
    if dst.endswith(".md"):
        primary_text = (ROOT / canon).read_text(encoding="utf-8") if (ROOT / canon).exists() else None
        # repair first, bar last: the deterministic bar must never go through
        # the repair ladder — a bar link into a not-yet-bootstrapped mirror is
        # "broken", and the ladder repoints it at whatever exists (usually the
        # document itself)
        out = fix_asset_links(out, canon, dst_lang, primary_text)
        out = apply_langbar(out, canon, dst_lang)
    write_out(dst_p, out.rstrip() + "\n")
    return True


def reverse_tasks(touched: dict[str, set[str]], base: str):
    """A doc edited in exactly one non-primary language propagates to primary."""
    tasks = []
    for c, langs in sorted(touched.items()):
        if PRIMARY not in langs and len(langs) == 1:
            l = next(iter(langs))
            src = tr_path(c, l)
            tasks.append((src, c, PRIMARY, git_show(src, base) or ""))
    return tasks


def stale_pairs(touched: dict[str, set[str]], state: dict):
    """(canon, lang) pairs whose translation no longer matches the primary.

    A language the human edited in this push is accepted as-is and recorded, so
    hand-written translations are never overwritten and never stay stale.
    """
    tasks = []
    for c in canonical_docs():
        src = ROOT / c
        if not src.exists():
            continue
        h = sha(src.read_text(encoding="utf-8"))
        for l in LANGS:
            if l == PRIMARY:
                continue
            key = f"{c}|{l}"
            if l in touched.get(c, set()):
                state["docs"][key] = h
                continue
            if state["docs"].get(key) != h or not (ROOT / tr_path(c, l)).exists():
                tasks.append((c, l, h))
    return tasks


# ---------- labels ----------

def placeholders(s: str) -> set[str]:
    return set(re.findall(r"\{([^{}]*)\}", s))


def vet_labels(source: dict, out: dict) -> dict:
    """Keep only translations that are safe to render.

    labels.json values are fed to str.format() by the figure renderers, so a
    dropped, renamed or invented placeholder is not a typo — it is a crash in
    CI. Anything that does not match the source placeholder set keeps its old
    value and stays stale, to be retried next run.
    """
    good = {}
    for k, src in source.items():
        v = out.get(k)
        if not isinstance(v, str) or not v.strip():
            print(f"     ! {k}: missing in the reply — keeping the old value")
            continue
        if placeholders(v) != placeholders(src):
            print(f"     ! {k}: placeholders {sorted(placeholders(src))} -> "
                  f"{sorted(placeholders(v))} — keeping the old value")
            continue
        good[k] = v
    return good


def sync_labels(changed: list[str], base: str, new_langs: list[str],
                state: dict, dry: bool) -> int:
    n = 0
    for f in label_files():
        cur = json.loads((ROOT / f).read_text(encoding="utf-8"))
        # frozen snapshot: all deltas are computed against the human-pushed
        # state, never against sections the bot itself just rewrote
        cur0 = copy.deepcopy(cur)
        rec = state["labels"].setdefault(f, {})
        old_raw = git_show(f, base)
        old = json.loads(old_raw) if old_raw and old_raw.strip() else {}
        dirty = False

        def translate(a: str, b: str, delta: dict) -> dict:
            nonlocal n, dirty
            print(f"  -> {f}: {a} -> {b}, keys: {len(delta)}")
            n += 1
            if dry:
                return {}
            try:
                raw = chat(system_json(a, b), json.dumps(
                    {"source_language": a, "target_language": b, "strings": delta},
                    ensure_ascii=False))
            except BadReply as e:
                print(f"     ! {e} — section left stale")
                return {}
            try:
                parsed = json.loads(raw)
            except json.JSONDecodeError:
                print(f"     ! reply is not JSON ({raw[:120]!r}) — section left stale")
                return {}
            if not isinstance(parsed, dict):
                print("     ! reply is not an object — section left stale")
                return {}
            good = vet_labels(delta, parsed.get("strings", parsed))
            # the ja sections of both labels.json files shipped filled with
            # Russian: every placeholder matched and every length was sane, so
            # the script is the only thing left that can tell
            off = i18n_render.wrong_script(b, " ".join(good.values()))
            if off:
                print(f"     ! reply {off} — section left stale, will be retried")
                return {}
            if good:
                cur.setdefault(b, {}).update(good)
                dirty = True
            return good

        # phase 1: a changed non-primary section propagates into primary — only
        # keys where primary itself was untouched by the human AND which the
        # state does not already record as translated from the current primary.
        #
        # In practice that means a hand edit to a label the bot has already
        # produced stays local: labels flow primary -> mirrors, and to change
        # what a label SAYS you edit the primary section. Prose docs keep the
        # bidirectional contract; labels do not, deliberately. A label edit is
        # almost always someone fixing the machine's wording, and letting that
        # rewrite the primary would silently redefine the source that all
        # fourteen mirrors are generated from — which is how a back-propagated
        # Portuguese README once rewrote the English one. Keys the bot has
        # never touched still flow back, so hand-authored labels are not
        # trapped in one language.
        src_of: dict[str, str] = {}
        for a in LANGS:
            if a == PRIMARY or a in new_langs or a not in cur0:
                continue
            delta = {k: v for k, v in cur0[a].items()
                     if old.get(a, {}).get(k) != v
                     and old.get(PRIMARY, {}).get(k) == cur0.get(PRIMARY, {}).get(k)
                     and rec.get(a, {}).get(k) != cur0.get(PRIMARY, {}).get(k)}
            if delta:
                for k in delta:
                    src_of[k] = a
                for k in translate(a, PRIMARY, delta):
                    # `a` is the source of truth for this key now
                    rec.setdefault(a, {})[k] = cur[PRIMARY][k]

        # phase 2: staleness comes from the recorded primary value, not from
        # this push's diff — that is what makes an interrupted run resumable
        primary_now = cur.get(PRIMARY, {})
        for b in LANGS:
            if b == PRIMARY:
                continue
            done = rec.setdefault(b, {})
            # a section the human edited by hand is accepted, not overwritten
            for k, v in primary_now.items():
                if old.get(b, {}).get(k) != cur0.get(b, {}).get(k):
                    done[k] = v
            if b in new_langs:  # bootstrap: the whole section from primary
                delta = dict(primary_now)
            else:
                delta = {k: v for k, v in primary_now.items()
                         if done.get(k) != v and src_of.get(k) != b}
            if delta:
                for k, v in translate(PRIMARY, b, delta).items():
                    done[k] = primary_now[k]

        if dirty:
            write_out(ROOT / f,
                      json.dumps(cur, ensure_ascii=False, indent=2) + "\n")
    return n


def detect_new_langs() -> list[str]:
    """A language with no labels.json section anywhere has never been bootstrapped."""
    new = []
    for l in LANGS:
        if l == PRIMARY:
            continue
        for f in label_files():
            if l not in json.loads((ROOT / f).read_text(encoding="utf-8")):
                new.append(l)
                break
    return new


# ---------- deterministic pass ----------

def refresh_langbars(dry: bool) -> int:
    """Rewrite bars and asset links in every language tree. Runs every time:
    it is cheap, deterministic, and it is what heals links the model mangled."""
    n = 0
    for c in canonical_docs():
        if not c.endswith(".md"):
            continue
        src = ROOT / c
        primary_text = src.read_text(encoding="utf-8") if src.exists() else None
        for l in LANGS:
            p = ROOT / tr_path(c, l)
            if not p.exists():
                continue
            text = p.read_text(encoding="utf-8")
            # same order as translate_doc: the bar goes on after link repair
            new = apply_langbar(fix_asset_links(text, c, l, primary_text), c, l)
            if new != text:
                n += 1
                print(f"  ~ {tr_path(c, l)}")
                if not dry:
                    write_out(p, new)
    return n


# ---------- main ----------

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--base", default="HEAD~1", help="commit to diff against")
    p.add_argument("--dry-run", action="store_true")
    p.add_argument("--no-model", action="store_true",
                   help="run only the deterministic passes (language bars, link "
                        "repair); do not expect an API key")
    p.add_argument("--touched-list", metavar="PATH",
                   help="write the newline-separated list of paths this run "
                        "modified, for `git add --pathspec-from-file`")
    a = p.parse_args()
    base = a.base
    if not base or set(base) == {"0"}:  # first push of a branch
        base = "HEAD~1"

    state = load_state()
    changed = changed_files(base)
    touched: dict[str, set[str]] = {}
    for f in changed:
        parsed = parse_doc(f)
        if parsed:
            touched.setdefault(parsed[0], set()).add(parsed[1])

    new_langs = detect_new_langs()
    print(f"Base: {base}; model: {MODEL} @ {ENDPOINT}; languages: {', '.join(LANGS)}")
    if new_langs:
        print(f"Bootstrapping: {', '.join(new_langs)}")

    if not TOKEN:
        # An unreachable endpoint is transient and must not fail the pipeline —
        # that is what ModelUnavailable is for. No key at all is not transient,
        # it is a misconfiguration, and treating the two alike hid one for three
        # days: the workflow's `environment:` was renamed without moving the
        # secret, every run reported success, and nothing was translated the
        # whole time. Pass --no-model to run the deterministic passes on purpose.
        total = 0
        try:
            total += refresh_langbars(a.dry_run)
        finally:
            save_state(state, a.dry_run)
            if a.touched_list and not a.dry_run:
                Path(a.touched_list).write_text(
                    "".join(f"{p}\n" for p in sorted(WRITTEN)), encoding="utf-8")
        print(f"Synced: {total}")
        if a.no_model or a.dry_run:
            print("No API key; deterministic passes only, as requested.")
            return 0
        print("::error::No OLLAMA_API_KEY or OPENAI_API_KEY reached this job — "
              "nothing was translated and every stale pair stays queued. Check "
              "that the secret exists in the environment the job declares: an "
              "environment secret is only visible to a job naming that exact "
              "environment. Use --no-model if this run was meant to be "
              "deterministic-only.")
        return 1

    total = 0
    auth_failed: AuthRejected | None = None
    try:
        # phase 1 — non-primary edits flow back into the primary file first, so
        # phase 2 hashes below are taken from the up-to-date primary
        for t in reverse_tasks(touched, base):
            if translate_doc(*t, a.dry_run):
                total += 1

        # phase 2 — everything the state says is stale, this push or older
        pending = stale_pairs(touched, state)
        if len(pending) > MAX_TASKS:
            print(f"{len(pending)} stale pairs — doing {MAX_TASKS} now, "
                  f"{len(pending) - MAX_TASKS} left for the next run")
            pending = pending[:MAX_TASKS]
        for c, l, h in pending:
            if translate_doc(c, tr_path(c, l), l, git_show(c, base) or "", a.dry_run):
                total += 1
                state["docs"][f"{c}|{l}"] = h

        total += sync_labels(changed, base, new_langs, state, a.dry_run)
    except AuthRejected as e:
        auth_failed = e
    except ModelUnavailable as e:
        # keep everything already translated; the state file still marks the
        # rest as stale, so the next push or the nightly run picks it up
        print(f"::warning::Model unavailable ({e}) — {total} synced, the rest stays queued")
    finally:
        total += refresh_langbars(a.dry_run)
        save_state(state, a.dry_run)
        if a.touched_list and not a.dry_run:
            Path(a.touched_list).write_text(
                "".join(f"{p}\n" for p in sorted(WRITTEN)), encoding="utf-8")
            print(f"Touched {len(WRITTEN)} path(s) -> {a.touched_list}")

    print(f"Synced: {total}")
    if auth_failed is not None:
        print(f"::error::{ENDPOINT} rejected the credentials ({auth_failed}). "
              "Nothing was translated and every stale pair stays queued. The key "
              "reached the job, so this is the value itself — check that the "
              "secret holds a current key for this endpoint and that "
              "TRANSLATE_MODEL is one the account may use.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

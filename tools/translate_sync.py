#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
translate_sync.py — keeps all language versions of the docs in sync.

Structure: the primary language (i18n.json) owns the canonical paths; every
other language is a mirror tree under translations/<lang>/ with identical
file names — markdown, the BOM CSV and generated figures included.

Logic per push:
  1. If only one language of a doc changed — translate the change into the
     others: non-primary edits propagate to primary first, then primary
     propagates to every remaining language. Docs where a human touched
     several languages are left alone.
  2. labels.json: only the keys that changed in one section are translated
     into the sections that did not change (two-phase, frozen snapshot).
  3. Adding a language to i18n.json bootstraps its whole mirror tree.
  4. The language-switcher line under every H1 and all links to files that
     are not part of the mirror are rewritten deterministically, not by the
     model.

Model: GitHub Models in CI (free with GITHUB_TOKEN), default is the
open-weights meta/llama-3.3-70b-instruct. A different OpenAI-compatible
endpoint/model can be substituted via OPENAI_BASE_URL / TRANSLATE_MODEL.

Usage: python tools/translate_sync.py [--base <sha>] [--dry-run]
"""

import argparse
import difflib
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "i18n.json").read_text(encoding="utf-8"))
PRIMARY = CFG["primary"]
NAMES = CFG["names"]
LANGS = list(NAMES)
TR_DIR = "translations"
DOC_EXTS = (".md", ".csv")

ENDPOINT = os.environ.get("OPENAI_BASE_URL", "https://models.github.ai/inference")
MODEL = os.environ.get("TRANSLATE_MODEL", "meta/llama-3.3-70b-instruct")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("OPENAI_API_KEY") or "none"
MAX_CHARS = 40_000
MAX_TASKS = 80

GLOSSARY = (
    "ланжевен = Langevin transducer; свип-карта = sweep map; АЧХ = frequency response; "
    "гребёнка толщинных резонансов = comb of thickness resonances; ионистор = supercapacitor; "
    "мост Гретца/Шоттки = full-wave/Schottky bridge; нагрузочная модуляция = load modulation; "
    "обвязка = support passives; мёртвое время = dead time; струбцина = clamp; "
    "смазка = grease couplant; заваренная коробка = welded-shut box; врезка = penetration; "
    "истёкшие патенты = expired patents; стенд = test rig; макет = breadboard prototype"
)


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
    return "\n".join(lines).rstrip() + "\n"


LINK_RE = re.compile(r'(\]\(|src=")([^)#"\s]+)([)"])')


def fix_asset_links(text: str, canon: str, lang: str) -> str:
    """Repoint relative links whose target is not part of the mirror tree.

    Inside a mirror the relative structure matches the canonical tree, so doc
    and figure links keep working as-is. Links to code, CSVs that are not
    mirrored, license texts etc. must climb out of translations/<lang>/ — that
    rewrite is mechanical, so the model is never trusted with it.
    """
    if lang == PRIMARY:
        return text
    here = Path(tr_path(canon, lang)).parent
    canon_dir = Path(canon).parent

    def sub(m):
        pre, target, post = m.groups()
        if target.startswith(("http", "mailto:", "/")):
            return m.group(0)
        if (ROOT / here / target).exists():
            return m.group(0)
        cand = (canon_dir / target)
        cand_norm = Path(os.path.normpath(ROOT / cand))
        if cand_norm.exists():
            return pre + os.path.relpath(cand_norm, ROOT / here) + post
        return m.group(0)

    return LINK_RE.sub(sub, text)


def sh(*args) -> str:
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout


def git_show(path: str, base: str) -> str:
    return sh("git", "show", f"{base}:{path}")


def udiff(old: str, new: str, name: str) -> str:
    return "".join(difflib.unified_diff(
        old.splitlines(keepends=True), new.splitlines(keepends=True),
        fromfile=f"old/{name}", tofile=f"new/{name}"))[:8000]


def system_doc(dst_lang: str) -> str:
    return f"""You are the translation-sync bot of an open-hardware repository
(ultrasonic power/data through steel walls). The primary language is
{NAMES[PRIMARY]}; every other language is a mirror tree under
translations/<lang>/ with identical file names. Terminology (ru = en):
{GLOSSARY}.

Target language now: {NAMES[dst_lang]} ({dst_lang}).

Rules:
- Update the target file so it exactly mirrors the meaning and structure of the
  new source content. Keep the lively engineering tone.
- Preserve markdown structure, tables, code blocks (do not translate commands),
  numbers, part numbers, file paths.
- Keep ALL relative links exactly as they are in the source — the mirror tree
  makes them resolve; the pipeline fixes the rest afterwards.
- For CSV files: keep the column count, order and quoting; translate only
  human-readable text (item names, notes); numbers and part numbers unchanged.
- The user message includes the diff of what changed in the source: EVERY
  added, removed or reworded fragment there must be reflected in the target.
  Do not make unrelated edits. If the target already reflects all the changes,
  return it exactly as it is.
- Return ONLY the full content of the target file. No code fences, no comments."""


SYSTEM_JSON = f"""You translate UI label strings for an open-hardware project
(ultrasonic power through steel). Terminology (ru = en): {GLOSSARY}.
Input: a JSON object with strings in the source language. Return ONLY a JSON
object with the same keys and translated values. Keep placeholders like {{d}},
{{r}}, {{q}}, {{tau}}, units and part numbers intact. No code fences."""


def chat(system: str, user: str) -> str:
    req = urllib.request.Request(
        ENDPOINT.rstrip("/") + "/chat/completions",
        data=json.dumps({
            "model": MODEL, "temperature": 0.2,
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": user}],
        }).encode(),
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            out = json.loads(r.read())["choices"][0]["message"]["content"]
    except urllib.error.HTTPError as e:
        body = e.read().decode(errors="replace")[:300]
        # model unavailable (budget/quota/permissions) — do not fail the
        # pipeline: whatever was translated stays, the rest syncs next time
        print(f"::warning::Model unavailable ({e.code}): {body} — sync postponed")
        sys.exit(0)
    out = out.strip()
    out = re.sub(r"^```[a-z]*\n|\n```$", "", out)  # guard against code fences
    return out


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
    old_dst = dst_p.read_text(encoding="utf-8") if dst_p.exists() else "(missing)"
    out = chat(system_doc(dst_lang), (
        f"Source file `{src}` — NEW content:\n<<<\n{text}\n>>>\n\n"
        f"What changed in the source (unified diff):\n<<<\n{udiff(old_src, text, src)}\n>>>\n\n"
        f"Target file `{dst}` — CURRENT (possibly outdated or missing) content:\n"
        f"<<<\n{old_dst}\n>>>\n\n"
        "Produce the full updated target file, reflecting every change from the diff."))
    canon, _ = parse_doc(dst)
    if dst.endswith(".md"):
        out = apply_langbar(out, canon, dst_lang)
        out = fix_asset_links(out, canon, dst_lang)
    dst_p.parent.mkdir(parents=True, exist_ok=True)
    dst_p.write_text(out.rstrip() + "\n", encoding="utf-8")
    return True


def canonical_docs() -> list[str]:
    docs = []
    for ext in DOC_EXTS:
        for p in ROOT.rglob(f"*{ext}"):
            rel = p.relative_to(ROOT).as_posix()
            if rel.startswith((".git", "LICENSES/", TR_DIR + "/")):
                continue
            docs.append(rel)
    return sorted(docs)


def plan_docs(changed: list[str], base: str, new_langs: list[str]):
    """Return (src, dst, dst_lang, old_src) translation tasks."""
    touched: dict[str, set[str]] = {}
    for f in changed:
        parsed = parse_doc(f)
        if parsed:
            touched.setdefault(parsed[0], set()).add(parsed[1])

    tasks = []
    # phase 1: a single non-primary edit propagates to the primary file
    for c, langs in sorted(touched.items()):
        if PRIMARY not in langs and len(langs) == 1:
            l = next(iter(langs))
            src = tr_path(c, l)
            tasks.append((src, c, PRIMARY, git_show(src, base)))
    # phase 2: primary (freshly edited or just updated) propagates to the rest
    for c, langs in sorted(touched.items()):
        if PRIMARY in langs or (PRIMARY not in langs and len(langs) == 1):
            for l in LANGS:
                if l != PRIMARY and l not in langs:
                    tasks.append((c, tr_path(c, l), l, git_show(c, base)))
    # bootstrap: a new language gets the whole mirror tree
    for l in new_langs:
        for c in canonical_docs():
            tasks.append((c, tr_path(c, l), l, ""))
    return tasks


def sync_labels(changed: list[str], base: str, new_langs: list[str], dry: bool) -> int:
    n = 0
    label_files = sorted({c for c in changed if c.endswith("labels.json")})
    if new_langs:
        label_files = sorted({p.relative_to(ROOT).as_posix() for p in ROOT.rglob("labels.json")
                              if TR_DIR + "/" not in p.as_posix()})
    for f in label_files:
        cur = json.loads((ROOT / f).read_text(encoding="utf-8"))
        # frozen snapshot: all deltas are computed against the human-pushed
        # state, never against sections the bot itself just rewrote
        cur0 = json.loads(json.dumps(cur))
        old_raw = git_show(f, base)
        old = json.loads(old_raw) if old_raw.strip() else {}
        dirty = False

        def translate(a: str, b: str, delta: dict) -> None:
            nonlocal n, dirty
            print(f"  -> {f}: {a} -> {b}, keys: {len(delta)}")
            n += 1
            if dry:
                return
            out = json.loads(chat(SYSTEM_JSON, json.dumps(
                {"source_language": a, "target_language": b, "strings": delta},
                ensure_ascii=False)))
            cur.setdefault(b, {}).update(out.get("strings", out))
            dirty = True

        # phase 1: a changed non-primary section propagates into primary —
        # only keys where primary itself was untouched by the human
        src_of: dict[str, str] = {}
        for a in LANGS:
            if a == PRIMARY or a in new_langs or a not in cur0:
                continue
            delta = {k: v for k, v in cur0[a].items()
                     if old.get(a, {}).get(k) != v
                     and old.get(PRIMARY, {}).get(k) == cur0.get(PRIMARY, {}).get(k)}
            if delta:
                for k in delta:
                    src_of[k] = a
                translate(a, PRIMARY, delta)

        # phase 2: every key whose primary value is new (edited by the human or
        # just updated in phase 1) goes to the remaining languages
        primary_now = cur.get(PRIMARY, {})
        pk = {k: v for k, v in primary_now.items()
              if old.get(PRIMARY, {}).get(k) != v}
        for b in LANGS:
            if b == PRIMARY:
                continue
            if b in new_langs:  # bootstrap: the whole section from primary
                delta = dict(primary_now)
            else:
                delta = {k: v for k, v in pk.items()
                         if src_of.get(k) != b
                         and old.get(b, {}).get(k) == cur0.get(b, {}).get(k)}
            if delta:
                translate(PRIMARY, b, delta)

        if dirty:
            (ROOT / f).write_text(
                json.dumps(cur, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return n


def refresh_langbars(dry: bool) -> int:
    """Deterministically rewrite bars and asset links in every language tree."""
    n = 0
    for c in canonical_docs():
        if not c.endswith(".md"):
            continue
        for l in LANGS:
            p = ROOT / tr_path(c, l)
            if not p.exists():
                continue
            text = p.read_text(encoding="utf-8")
            new = fix_asset_links(apply_langbar(text, c, l), c, l)
            if new != text:
                n += 1
                if not dry:
                    p.write_text(new, encoding="utf-8")
    return n


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--base", default="HEAD~1", help="commit to diff against")
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    base = a.base
    if not base or set(base) == {"0"}:  # first push of a branch
        base = "HEAD~1"

    changed = [l for l in sh("git", "diff", "--name-only", "--diff-filter=ACMR",
                             f"{base}..HEAD").splitlines() if l.strip()]

    new_langs = []
    if "i18n.json" in changed:
        old_raw = git_show("i18n.json", base)
        old_langs = list(json.loads(old_raw)["names"]) if old_raw.strip() else LANGS
        new_langs = [l for l in LANGS if l not in old_langs]

    tasks = plan_docs(changed, base, new_langs)
    if len(tasks) > MAX_TASKS:
        print(f"{len(tasks)} translation tasks — over the {MAX_TASKS} cap, sync skipped")
        sys.exit(0)
    if len(changed) > 40 and not new_langs:
        print(f"{len(changed)} files changed — looks like a bulk edit, sync skipped")
        sys.exit(0)

    print(f"Base: {base}; model: {MODEL} @ {ENDPOINT}; languages: {', '.join(LANGS)}")
    total = sum(translate_doc(*t, a.dry_run) for t in tasks)
    total += sync_labels(changed, base, new_langs, a.dry_run)
    if new_langs:
        total += refresh_langbars(a.dry_run)
    print(f"Synced: {total}")

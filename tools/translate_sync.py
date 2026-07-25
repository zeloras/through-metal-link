#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
translate_sync.py — keeps all language versions of the docs in sync.

Languages live in i18n.json: the primary language owns the canonical file
names (X.md), every other language gets a suffixed twin (X.<lang>.md); the
same suffix scheme applies to generated figures (name.<lang>.png).

Logic per push:
  1. If only one side of a language pair changed — translate the change into
     the others: non-primary edits propagate to primary first, then primary
     propagates to every remaining language. Pairs where a human touched both
     sides are left alone.
  2. labels.json: only the keys that changed in one section are translated
     into the sections that did not change.
  3. Adding a language to i18n.json bootstraps it: every canonical doc and the
     labels.json section are translated, figures follow via the workflow.
  4. The language-switcher line under every H1 is rewritten deterministically
     (not by the model) from i18n.json.

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

ENDPOINT = os.environ.get("OPENAI_BASE_URL", "https://models.github.ai/inference")
MODEL = os.environ.get("TRANSLATE_MODEL", "meta/llama-3.3-70b-instruct")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("OPENAI_API_KEY") or "none"
MAX_CHARS = 40_000
MAX_TASKS = 60

GLOSSARY = (
    "ланжевен = Langevin transducer; свип-карта = sweep map; АЧХ = frequency response; "
    "гребёнка толщинных резонансов = comb of thickness resonances; ионистор = supercapacitor; "
    "мост Гретца/Шоттки = full-wave/Schottky bridge; нагрузочная модуляция = load modulation; "
    "обвязка = support passives; мёртвое время = dead time; струбцина = clamp; "
    "смазка = grease couplant; заваренная коробка = welded-shut box; врезка = penetration; "
    "истёкшие патенты = expired patents; стенд = test rig; макет = breadboard prototype"
)


def suf(lang: str) -> str:
    return "" if lang == PRIMARY else f".{lang}"


def md_name(base: str, lang: str) -> str:
    return f"{base}{suf(lang)}.md"


def parse_md(f: str):
    """Return (base, lang) for a repo .md path, or None if not a doc file."""
    if not f.endswith(".md") or f.startswith("LICENSES/"):
        return None
    for l in LANGS:
        if l != PRIMARY and f.endswith(f".{l}.md"):
            return f[: -(len(l) + 4)], l
    return f[:-3], PRIMARY


def langbar(base: str, lang: str) -> str:
    parts = []
    for l in LANGS:
        label = NAMES[l] + (" (primary)" if l == PRIMARY else "")
        if l == lang:
            parts.append(label)
        else:
            parts.append(f"[{label}]({Path(md_name(base, l)).name})")
    return "> " + " · ".join(parts)


def apply_langbar(text: str, base: str, lang: str) -> str:
    lines = text.splitlines()
    bar = langbar(base, lang)
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


def sh(*args) -> str:
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout


def git_show(path: str, base: str) -> str:
    return sh("git", "show", f"{base}:{path}")


def udiff(old: str, new: str, name: str) -> str:
    return "".join(difflib.unified_diff(
        old.splitlines(keepends=True), new.splitlines(keepends=True),
        fromfile=f"old/{name}", tofile=f"new/{name}"))[:8000]


def system_md(dst_lang: str) -> str:
    s = suf(dst_lang)
    return f"""You are the translation-sync bot of an open-hardware repository
(ultrasonic power/data through steel walls). The primary language is
{NAMES[PRIMARY]}; other languages live in suffixed twin files. Terminology
(ru = en): {GLOSSARY}.

Target language now: {NAMES[dst_lang]} ({dst_lang}).

Rules:
- Update the target file so it exactly mirrors the meaning and structure of the
  new source content. Keep the lively engineering tone.
- Preserve markdown structure, tables, code blocks (do not translate commands),
  numbers, part numbers, file paths.
- In the target file, links to the repository's translated .md docs must point
  to their twins for the target language: `X{s}.md`; generated images use the
  `name{s}.png` / `name{s}.svg` twins. Links to code, CSV, directories and
  external URLs stay as they are.
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


def translate_md(src: str, dst: str, dst_lang: str, old_src: str, dry: bool) -> bool:
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
    out = chat(system_md(dst_lang), (
        f"Source file `{src}` — NEW content:\n<<<\n{text}\n>>>\n\n"
        f"What changed in the source (unified diff):\n<<<\n{udiff(old_src, text, src)}\n>>>\n\n"
        f"Target file `{dst}` — CURRENT (possibly outdated or missing) content:\n"
        f"<<<\n{old_dst}\n>>>\n\n"
        "Produce the full updated target file, reflecting every change from the diff."))
    base, _ = parse_md(dst)
    dst_p.write_text(apply_langbar(out, base, dst_lang), encoding="utf-8")
    return True


def canonical_docs() -> list[str]:
    docs = []
    for p in ROOT.rglob("*.md"):
        rel = p.relative_to(ROOT).as_posix()
        if rel.startswith((".git", "LICENSES/")):
            continue
        parsed = parse_md(rel)
        if parsed and parsed[1] == PRIMARY:
            docs.append(rel)
    return sorted(docs)


def plan_markdown(changed: list[str], base: str, new_langs: list[str]):
    """Return (src, dst, dst_lang, old_src) translation tasks."""
    touched: dict[str, set[str]] = {}
    for f in changed:
        parsed = parse_md(f)
        if parsed:
            touched.setdefault(parsed[0], set()).add(parsed[1])

    tasks = []
    # phase 1: a single non-primary edit propagates to the primary file
    for b, langs in sorted(touched.items()):
        if PRIMARY not in langs and len(langs) == 1:
            l = next(iter(langs))
            src = md_name(b, l)
            tasks.append((src, md_name(b, PRIMARY), PRIMARY, git_show(src, base)))
    # phase 2: primary (freshly edited or just updated) propagates to the rest
    for b, langs in sorted(touched.items()):
        if PRIMARY in langs or (PRIMARY not in langs and len(langs) == 1):
            src = md_name(b, PRIMARY)
            for l in LANGS:
                if l != PRIMARY and l not in langs:
                    tasks.append((src, md_name(b, l), l, git_show(src, base)))
    # bootstrap: a new language gets every canonical doc translated
    for l in new_langs:
        for src in canonical_docs():
            tasks.append((src, md_name(src[:-3], l), l, ""))
    return tasks


def sync_labels(changed: list[str], base: str, new_langs: list[str], dry: bool) -> int:
    n = 0
    label_files = sorted({c for c in changed if c.endswith("labels.json")})
    if new_langs:
        label_files = sorted({p.relative_to(ROOT).as_posix() for p in ROOT.rglob("labels.json")})
    for f in label_files:
        cur = json.loads((ROOT / f).read_text(encoding="utf-8"))
        old_raw = git_show(f, base)
        old = json.loads(old_raw) if old_raw.strip() else {}
        dirty = False
        for a in LANGS:
            if a not in cur:
                continue
            for b in LANGS:
                if b == a:
                    continue
                if b in cur and b not in new_langs:
                    delta = {k: v for k, v in cur[a].items()
                             if old.get(a, {}).get(k) != v
                             and old.get(b, {}).get(k) == cur[b].get(k)}
                else:  # bootstrap: whole section from the primary language
                    delta = dict(cur[a]) if a == PRIMARY and b in new_langs else {}
                if not delta:
                    continue
                print(f"  -> {f}: {a} -> {b}, keys: {len(delta)}")
                n += 1
                if dry:
                    continue
                out = json.loads(chat(SYSTEM_JSON, json.dumps(
                    {"source_language": a, "target_language": b, "strings": delta},
                    ensure_ascii=False)))
                cur.setdefault(b, {}).update(out.get("strings", out))
                dirty = True
        if dirty:
            (ROOT / f).write_text(
                json.dumps(cur, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return n


def refresh_langbars(dry: bool) -> int:
    """Deterministically rewrite the switcher line in every doc of every language."""
    n = 0
    for src in canonical_docs():
        b = src[:-3]
        for l in LANGS:
            p = ROOT / md_name(b, l)
            if not p.exists():
                continue
            text = p.read_text(encoding="utf-8")
            new = apply_langbar(text, b, l)
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

    tasks = plan_markdown(changed, base, new_langs)
    if len(tasks) > MAX_TASKS:
        print(f"{len(tasks)} translation tasks — over the {MAX_TASKS} cap, sync skipped")
        sys.exit(0)
    if len(changed) > 40 and not new_langs:
        print(f"{len(changed)} files changed — looks like a bulk edit, sync skipped")
        sys.exit(0)

    print(f"Base: {base}; model: {MODEL} @ {ENDPOINT}; languages: {', '.join(LANGS)}")
    total = sum(translate_md(*t, a.dry_run) for t in tasks)
    total += sync_labels(changed, base, new_langs, a.dry_run)
    if new_langs:
        total += refresh_langbars(a.dry_run)
    print(f"Synced: {total}")

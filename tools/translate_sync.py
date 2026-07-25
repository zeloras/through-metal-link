#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
translate_sync.py — keeps the English and Russian doc versions in sync.

Logic: look at which files changed since a base commit. If only one side of a
(X.md <-> X.ru.md) pair changed — translate and update the other side. For
labels.json, translate only the keys that changed in one language section into
the other. If both sides changed, a human did the work — leave them alone.

Model: GitHub Models in CI (free with GITHUB_TOKEN), default is the
open-weights meta/llama-3.3-70b-instruct. A different OpenAI-compatible
endpoint/model can be substituted via OPENAI_BASE_URL / TRANSLATE_MODEL.

Usage: python tools/translate_sync.py [--base <sha>] [--dry-run]
"""

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ENDPOINT = os.environ.get("OPENAI_BASE_URL", "https://models.github.ai/inference")
MODEL = os.environ.get("TRANSLATE_MODEL", "meta/llama-3.3-70b-instruct")
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("OPENAI_API_KEY") or "ollama"
MAX_CHARS = 40_000
MAX_FILES = 20

GLOSSARY = (
    "ланжевен = Langevin transducer; свип-карта = sweep map; АЧХ = frequency response; "
    "гребёнка толщинных резонансов = comb of thickness resonances; ионистор = supercapacitor; "
    "мост Гретца/Шоттки = full-wave/Schottky bridge; нагрузочная модуляция = load modulation; "
    "обвязка = support passives; мёртвое время = dead time; струбцина = clamp; "
    "смазка = grease couplant; заваренная коробка = welded-shut box; врезка = penetration; "
    "истёкшие патенты = expired patents; стенд = test rig; макет = breadboard prototype"
)

SYSTEM_MD = f"""You are the translation-sync bot of an open-hardware repository
(ultrasonic power/data through steel walls). English files are canonical; Russian
twins live next to them as *.ru.md. Terminology (ru = en): {GLOSSARY}.

Rules:
- Update the target file so it exactly mirrors the meaning and structure of the
  new source content. Keep the lively engineering tone.
- Preserve markdown structure, tables, code blocks (do not translate commands),
  numbers, part numbers, file paths.
- Keep the language-switcher line right after the H1:
  in English files "> [Русская версия](<basename>.ru.md)",
  in Russian files "> [English (primary)](<basename>.md)".
- In Russian files internal links to translated .md files point to their .ru.md
  twins, and generated images use the .ru.png / .ru.svg suffix. In English files
  links stay canonical (no suffix).
- The user message includes the diff of what changed in the source: EVERY added,
  removed or reworded fragment there must be reflected in the target. Do not
  make unrelated edits. If the target already reflects all the changes, return
  it exactly as it is.
- Return ONLY the full content of the target file. No code fences, no comments."""

SYSTEM_JSON = f"""You translate UI label strings for an open-hardware project
(ultrasonic power through steel). Terminology (ru = en): {GLOSSARY}.
Input: a JSON object with strings in the source language. Return ONLY a JSON
object with the same keys and translated values. Keep placeholders like {{d}},
{{r}}, {{q}}, {{tau}}, units and part numbers intact. No code fences."""


def sh(*args) -> str:
    return subprocess.run(args, capture_output=True, text=True, cwd=ROOT).stdout


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


def sync_markdown(changed: list[str], base: str, dry: bool) -> int:
    n = 0
    pairs: dict[str, set[str]] = {}
    for f in changed:
        if not f.endswith(".md"):
            continue
        canon = f[:-6] + ".md" if f.endswith(".ru.md") else f
        pairs.setdefault(canon, set()).add(f)

    for canon, touched in sorted(pairs.items()):
        ru = canon[:-3] + ".ru.md"
        if canon in touched and ru in touched:
            print(f"  = {canon}: both versions changed, skipping")
            continue
        src, dst = (canon, ru) if canon in touched else (ru, canon)
        src_p, dst_p = ROOT / src, ROOT / dst
        if not src_p.exists():
            continue  # file deleted — a human removes the twin
        text = src_p.read_text(encoding="utf-8")
        if len(text) > MAX_CHARS:
            print(f"  ! {src}: too large ({len(text)} chars), skipping")
            continue
        old_dst = dst_p.read_text(encoding="utf-8") if dst_p.exists() else "(missing)"
        src_diff = sh("git", "diff", f"{base}..HEAD", "--", src)[:8000]
        print(f"  -> {src} -> {dst}")
        if dry:
            n += 1
            continue
        out = chat(SYSTEM_MD, (
            f"Source file `{src}` — NEW content:\n<<<\n{text}\n>>>\n\n"
            f"What changed in the source (unified diff):\n<<<\n{src_diff}\n>>>\n\n"
            f"Target file `{dst}` — CURRENT (possibly outdated) content:\n<<<\n{old_dst}\n>>>\n\n"
            "Produce the full updated target file, reflecting every change from the diff."))
        dst_p.write_text(out.rstrip() + "\n", encoding="utf-8")
        n += 1
    return n


def sync_labels(changed: list[str], base: str, dry: bool) -> int:
    n = 0
    for f in [c for c in changed if c.endswith("labels.json")]:
        cur = json.loads((ROOT / f).read_text(encoding="utf-8"))
        old_raw = sh("git", "show", f"{base}:{f}")
        old = json.loads(old_raw) if old_raw.strip() else {"en": {}, "ru": {}}
        for a, b in (("ru", "en"), ("en", "ru")):
            delta = {k: v for k, v in cur.get(a, {}).items()
                     if old.get(a, {}).get(k) != v
                     and old.get(b, {}).get(k) == cur.get(b, {}).get(k)}
            if not delta:
                continue
            print(f"  -> {f}: {a} -> {b}, keys: {', '.join(delta)}")
            if dry:
                n += 1
                continue
            out = json.loads(chat(SYSTEM_JSON, json.dumps(
                {"source_language": a, "target_language": b, "strings": delta},
                ensure_ascii=False)))
            cur[b].update(out.get("strings", out))
            n += 1
        if not dry and n:
            (ROOT / f).write_text(
                json.dumps(cur, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
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
    changed = [f for f in changed if not f.startswith("LICENSES/")]
    if len(changed) > MAX_FILES * 2:
        print(f"{len(changed)} files changed — looks like a bulk edit, sync skipped")
        sys.exit(0)
    print(f"Base: {base}; model: {MODEL} @ {ENDPOINT}")
    total = sync_markdown(changed, base, a.dry_run) + sync_labels(changed, base, a.dry_run)
    print(f"Synced: {total}")

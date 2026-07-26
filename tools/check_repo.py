#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
check_repo.py — the guard rail the translation bot writes against.

Everything here is a class of breakage that the LLM sync pipeline has actually
produced or can produce, and that nothing else in CI would notice:

  links   — every relative markdown/HTML link resolves. Catches the model
            translating a file name inside a link target, miscounting `../`
            on the way out of translations/<lang>/, or dropping a fragment.
  labels  — labels.json sections match i18n.json, every section carries the
            same keys as the primary one, and placeholders agree key by key.
            The figure renderers call str.format() on these values, so a
            renamed placeholder is a crash, not a typo.
  mirror  — every canonical doc has a twin in every language, and every
            markdown file carries a language bar under its H1.

Usage: python tools/check_repo.py [--only links|labels|mirror]
Exit code 1 if anything failed.
"""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CFG = json.loads((ROOT / "i18n.json").read_text(encoding="utf-8"))
PRIMARY = CFG["primary"]
LANGS = list(CFG["names"])
TR_DIR = "translations"
DOC_EXTS = (".md", ".csv")

# same shape as tools/translate_sync.py, deliberately: the checker must see a
# destination exactly the way the repair pass sees it
LINK_RE = re.compile(r'\]\(([^)]*)\)|src="([^"]*)"')
# .github/ holds GitHub UI text and is English-only by design
SKIP_PREFIXES = (".git", "LICENSES/", ".github/")


def split_dest(raw: str) -> str:
    m = re.search(r'(\s+"[^"]*")\s*$', raw)
    if m:
        raw = raw[:m.start()]
    raw = raw.strip()
    if raw.startswith("<") and raw.endswith(">"):
        raw = raw[1:-1]
    return raw.partition("#")[0]


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md")
                  if ".git" not in p.parts
                  and not p.relative_to(ROOT).as_posix().startswith("LICENSES/"))


def canonical_docs() -> list[str]:
    docs = []
    for ext in DOC_EXTS:
        for p in ROOT.rglob(f"*{ext}"):
            rel = p.relative_to(ROOT).as_posix()
            if not rel.startswith(SKIP_PREFIXES) and not rel.startswith(TR_DIR + "/"):
                docs.append(rel)
    return sorted(docs)


def check_links() -> list[str]:
    bad = []
    for md in markdown_files():
        rel_md = md.relative_to(ROOT).as_posix()
        text = md.read_text(encoding="utf-8")
        for i, line in enumerate(text.splitlines(), 1):
            for m in LINK_RE.finditer(line):
                dest = split_dest(m.group(1) if m.group(1) is not None else m.group(2))
                if not dest or dest.startswith(("http", "mailto:", "/")):
                    continue
                if not (md.parent / dest).exists():
                    bad.append(f"{rel_md}:{i}: broken link -> {dest}")
    return bad


def placeholders(s: str) -> set[str]:
    return set(re.findall(r"\{([^{}]*)\}", s))


def check_labels() -> list[str]:
    bad = []
    for lf in sorted(ROOT.rglob("labels.json")):
        rel = lf.relative_to(ROOT).as_posix()
        if TR_DIR + "/" in rel or ".git" in lf.parts:
            continue
        data = json.loads(lf.read_text(encoding="utf-8"))
        for missing in sorted(set(LANGS) - set(data)):
            bad.append(f"{rel}: no section for '{missing}' (declared in i18n.json)")
        for extra in sorted(set(data) - set(LANGS)):
            bad.append(f"{rel}: section '{extra}' is not in i18n.json")
        if PRIMARY not in data:
            bad.append(f"{rel}: no primary section '{PRIMARY}' — cannot compare")
            continue
        base = data[PRIMARY]
        for lang, section in data.items():
            if lang == PRIMARY:
                continue
            for k in sorted(set(base) - set(section)):
                bad.append(f"{rel}: {lang} is missing key '{k}'")
            for k in sorted(set(section) - set(base)):
                bad.append(f"{rel}: {lang} has key '{k}' that '{PRIMARY}' does not")
            for k in sorted(set(base) & set(section)):
                if placeholders(base[k]) != placeholders(section[k]):
                    bad.append(
                        f"{rel}: {lang}/{k} placeholders {sorted(placeholders(base[k]))}"
                        f" != {sorted(placeholders(section[k]))} — str.format() would fail")
    return bad


def check_mirror() -> list[str]:
    bad = []
    for c in canonical_docs():
        for lang in LANGS:
            if lang == PRIMARY:
                continue
            if not (ROOT / TR_DIR / lang / c).exists():
                bad.append(f"{TR_DIR}/{lang}/{c}: missing mirror of {c}")
    for md in markdown_files():
        rel = md.relative_to(ROOT).as_posix()
        if rel.startswith(SKIP_PREFIXES):
            continue
        lines = md.read_text(encoding="utf-8").splitlines()
        h1 = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
        if h1 is None:
            bad.append(f"{rel}: no H1 — the language bar cannot be placed")
            continue
        j = h1 + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        if not (j < len(lines) and lines[j].startswith("> ") and "·" in lines[j]):
            bad.append(f"{rel}: no language bar under the H1")
    return bad


CHECKS = {"links": check_links, "labels": check_labels, "mirror": check_mirror}

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--only", choices=sorted(CHECKS), action="append")
    a = p.parse_args()
    failures = 0
    for name in (a.only or sorted(CHECKS)):
        problems = CHECKS[name]()
        if problems:
            failures += len(problems)
            print(f"FAIL {name} ({len(problems)}):")
            for x in problems:
                print(f"  ::error::{x}")
        else:
            print(f"ok   {name}")
    if failures:
        print(f"\n{failures} problem(s)")
    sys.exit(1 if failures else 0)

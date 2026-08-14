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
  github  — no relative links in .github/. They resolve on disk, so the link
            check passes, and still break where those files are actually
            shown: the community-health tabs render them as if they sat at the
            repository root, and PR/issue bodies do not resolve repo-relative
            links at all.
  mirror  — every canonical doc has a twin in every language, and every
            markdown file carries a language bar under its H1. A twin the
            sync has never recorded in translations/.sync-state.json is a
            bootstrap still in flight (a freshly declared language), not
            breakage — the nightly sync drains it.

Usage: python tools/check_repo.py [--only links|labels|mirror|github]
Exit code 1 if anything failed.
"""

import argparse
import json
import re
import sys
from pathlib import Path

import i18n_render  # sibling module in tools/; its script half needs no deps

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


def langbar_lineno(lines: list[str]) -> int | None:
    """1-based line number of the language bar under the H1, if present."""
    for i, l in enumerate(lines):
        if l.startswith("# "):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j < len(lines) and lines[j].startswith("> ") and "·" in lines[j]:
                return j + 1
            return None
    return None


def check_links() -> list[str]:
    bad = []
    for md in markdown_files():
        rel_md = md.relative_to(ROOT).as_posix()
        text = md.read_text(encoding="utf-8")
        lines = text.splitlines()
        # the bar is machine-generated every sync and may legitimately point
        # at a mirror the bootstrap has not written yet; mirror completeness
        # (with its pending-bootstrap tolerance) governs those targets
        bar = langbar_lineno(lines)
        for i, line in enumerate(lines, 1):
            if i == bar:
                continue
            for m in LINK_RE.finditer(line):
                dest = split_dest(m.group(1) if m.group(1) is not None else m.group(2))
                if not dest or dest.startswith(("http", "mailto:", "/")):
                    continue
                if not (md.parent / dest).exists():
                    bad.append(f"{rel_md}:{i}: broken link -> {dest}")
    return bad


def check_anchors() -> list[str]:
    """Every `file.md#anchor` link must hit a heading that exists there.

    check_links() only asks whether the file exists, so a link copied verbatim
    into a mirror passes while pointing at a heading that was translated out of
    existence: every mirror of 04-hybrid-channels and 05-applications-map aimed
    at #effect-on-the-wall-and-the-media-behind-it inside a document whose
    heading now reads "Einfluss auf die Wand...". Twenty-eight dead anchors,
    invisible to every check in this file.
    """
    bad = []
    for md in markdown_files():
        rel = md.relative_to(ROOT).as_posix()
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for m in LINK_RE.finditer(line):
                raw = m.group(1) if m.group(1) is not None else m.group(2)
                dest = split_dest(raw)
                frag = raw.partition("#")[2].split(" ")[0].strip().rstrip('"')
                if not frag or dest.startswith(("http", "mailto:", "/")):
                    continue
                tgt = (md.parent / dest) if dest else md
                if not tgt.exists() or tgt.suffix != ".md":
                    continue
                if frag not in i18n_render.heading_slugs(
                        tgt.read_text(encoding="utf-8")):
                    bad.append(f"{rel}:{i}: '#{frag}' is not a heading in "
                               f"{dest or tgt.name}")
    return bad


def check_github_links() -> list[str]:
    """No relative links in .github/ — GitHub renders those files out of place.

    A relative link there resolves on disk, so check_links() is happy, and is
    still broken in the two contexts these files actually appear in:

      - the community-health tabs (?tab=security-ov-file and friends) resolve
        relative to the repository root, not to .github/, so `../docs/x.md`
        climbs one level too far and eats the branch segment:
        /blob/docs/02-safety.md instead of /blob/master/docs/02-safety.md;
      - PULL_REQUEST_TEMPLATE.md is injected into a pull request body, and
        issue and PR bodies do not resolve repo-relative links at all.

    Both were live: the security policy's link to the safety document, and
    three links in the PR template every contributor is shown.
    """
    bad = []
    for md in sorted((ROOT / ".github").rglob("*.md")):
        rel = md.relative_to(ROOT).as_posix()
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            for m in LINK_RE.finditer(line):
                dest = split_dest(m.group(1) if m.group(1) is not None else m.group(2))
                if not dest or dest.startswith(("http", "mailto:", "#")):
                    continue
                bad.append(f"{rel}:{i}: relative link '{dest}' — .github/ files are "
                           "rendered outside their directory; use the full "
                           "https://github.com/... URL")
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
        synced = synced_langs()
        for missing in sorted(set(LANGS) - set(data)):
            # same tolerance as check_mirror: a language the sync has never
            # written is a bootstrap still in flight, not breakage
            if missing not in synced:
                continue
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
            # a section can be perfectly well-formed and still be the wrong
            # language: ja shipped filled with Russian
            off = i18n_render.wrong_script(lang, " ".join(map(str, section.values())))
            if off:
                bad.append(f"{rel}: section '{lang}' {off}")
    return bad


def synced_pairs() -> set[str]:
    """'<canon>|<lang>' pairs the sync bot has actually written at least once."""
    try:
        state = json.loads(
            (ROOT / TR_DIR / ".sync-state.json").read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return set()
    return set(state.get("docs", {}))


def synced_langs() -> set[str]:
    """Languages the sync bot has written at least one file for."""
    return {p.split("|", 1)[1] for p in synced_pairs() if "|" in p}


def check_mirror() -> list[str]:
    bad = []
    synced = synced_pairs()
    for c in canonical_docs():
        for lang in LANGS:
            if lang == PRIMARY:
                continue
            if not (ROOT / TR_DIR / lang / c).exists():
                if f"{c}|{lang}" not in synced:
                    continue  # bootstrap in flight — the nightly sync drains it
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
            continue
        # An existing bar is not a current bar. When the commit step's pathspec
        # dropped the primary tree, README.md and 19 other canonical docs kept
        # a six-language bar while the mirrors had fifteen — every check passed
        # because each file did have *a* bar. Compare against i18n.json.
        absent = [CFG["names"][l] for l in LANGS if CFG["names"][l] not in lines[j]]
        if absent:
            bad.append(f"{rel}: language bar is missing {', '.join(absent)} "
                       f"({len(LANGS) - len(absent)} of {len(LANGS)} languages)")
    return bad


CHECKS = {"links": check_links, "labels": check_labels, "mirror": check_mirror,
          "github": check_github_links, "anchors": check_anchors}

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

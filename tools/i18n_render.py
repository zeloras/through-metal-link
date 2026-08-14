#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
i18n_render.py — font handling shared by the two figure renderers.

matplotlib resolves one font family and then silently draws a .notdef box for
every glyph that family lacks. It emits a warning, nothing reads it, and the
render "succeeds". That is exactly how translations/zh/docs/img/* came to be a
grid of tofu boxes: DejaVu Sans has no Han glyphs, CI was green, and the
unreadable figures were committed. No test in this repository looks at pixels,
so the only place to catch it is before anything is drawn.

Hence two jobs here:
  - build the font stack from i18n.json, keeping only families actually
    installed, so the same config works on a runner and on a laptop;
  - report which characters of a language's label set no installed font can
    draw, so the caller can skip that language instead of emitting tofu.

Scripts that need contextual shaping — Arabic and Persian (RTL, joined forms),
Devanagari and Bengali (conjuncts) — are a separate problem: matplotlib has no
complex-text-shaping engine, so even with a perfect font the glyphs come out
unjoined and in visual disorder. Those languages are listed in
i18n.json render.skip_figures and reuse the primary figures; their prose is
unaffected, and the link repair in tools/translate_sync.py already points a
mirror at the primary figure when its own copy is absent.

Also home to the script table, because the other way a localized figure comes
out useless has nothing to do with fonts: the ja section of both labels.json
files shipped filled with Russian. Placeholders matched, lengths were sane, so
the only remaining tell is which script the text is written in.

matplotlib is imported lazily so tools/check_repo.py can use the script half
of this module without any third-party dependency.
"""

from __future__ import annotations

import re
import unicodedata

# Noto covers nearly every living script and is what CI installs
# (fonts-noto-core + fonts-noto-cjk). The rest are the macOS equivalents, so a
# contributor regenerating figures locally is not stuck without CJK.
DEFAULT_STACK = [
    "DejaVu Sans",              # base: Latin, Cyrillic, Greek — matches existing figures
    "Noto Sans",
    "Noto Sans CJK JP", "Noto Sans CJK SC", "Noto Sans CJK KR",
    "Noto Sans Devanagari", "Noto Sans Bengali", "Noto Sans Arabic",
    "Noto Sans Hebrew", "Noto Sans Thai",
    "Hiragino Sans", "Apple SD Gothic Neo", "Arial Unicode MS",  # macOS
]


def configured_stack(i18n: dict) -> list[str]:
    return list(i18n.get("render", {}).get("fonts") or DEFAULT_STACK)


def skip_figures(i18n: dict) -> set[str]:
    """Languages whose figures stay in the primary language on purpose."""
    return set(i18n.get("render", {}).get("skip_figures") or ())


def _installed(families: list[str]) -> list[str]:
    from matplotlib import font_manager

    have = {f.name for f in font_manager.fontManager.ttflist}
    return [f for f in families if f in have]


def apply(i18n: dict) -> list[str]:
    """Install the font stack into rcParams; return the families actually present.

    matplotlib walks the family list per character, so listing a script-specific
    Noto face after the base font is what makes mixed "40 kHz · 钢板" labels come
    out whole.
    """
    import matplotlib

    stack = _installed(configured_stack(i18n))
    if not stack:  # nothing configured is installed — leave matplotlib's default
        return []
    matplotlib.rcParams["font.family"] = stack
    return stack


def _font_paths(families: list[str]) -> list[str]:
    from matplotlib import font_manager
    from matplotlib.font_manager import FontProperties

    paths = []
    for name in families:
        try:
            paths.append(font_manager.findfont(FontProperties(family=name),
                                               fallback_to_default=False))
        except Exception:
            continue
    return paths


def uncovered(text: str, families: list[str]) -> set[str]:
    """Characters in `text` that no font in `families` can draw.

    Asks FreeType for a glyph index the same way the renderer will, so this
    agrees with what would actually be painted rather than guessing from
    Unicode ranges.
    """
    from matplotlib.ft2font import FT2Font

    interesting = {ch for ch in text if ch.isprintable() and not ch.isspace()}
    if not interesting:
        return set()
    missing = set(interesting)
    for path in _font_paths(families):
        if not missing:
            break
        try:
            face = FT2Font(path)
        except Exception:
            continue
        missing = {ch for ch in missing if face.get_char_index(ord(ch)) == 0}
    return missing


# ---------- markdown anchors ----------

# Shared with tools/check_repo.py and the link repair in tools/translate_sync.py
# so all three agree on what a heading anchor is.
_HEADING = re.compile(r"(?m)^#{1,6}\s+(.*?)\s*$")


def slugify(heading: str) -> str:
    """GitHub's heading anchor: lowercase, punctuation dropped, spaces hyphenated.

    Combining marks are kept. Python's word-character class excludes them (a Devanagari matra is
    category Mn and not alphanumeric), which silently mangled Hindi anchors —
    "दीवार" came out "दवर" — while GitHub keeps them.
    """
    kept = [ch for ch in heading.strip().lower()
            if ch.isalnum() or ch.isspace() or ch in "-_"
            or unicodedata.category(ch).startswith("M")]
    return re.sub(r"\s+", "-", "".join(kept)).strip("-")


def heading_slugs(markdown: str) -> list[str]:
    """Anchors of a document, in document order."""
    return [slugify(h) for h in _HEADING.findall(markdown)]


# ---------- script identity ----------

# The script a language's text must predominantly be written in. A language
# absent from here is simply not checked, so adding one to i18n.json never
# breaks — it just gets no script guard until it is listed.
SCRIPTS: dict[str, set[str]] = {
    "en": {"LATIN"}, "de": {"LATIN"}, "pt": {"LATIN"}, "es": {"LATIN"},
    "fr": {"LATIN"}, "it": {"LATIN"}, "nl": {"LATIN"}, "pl": {"LATIN"},
    "tr": {"LATIN"}, "id": {"LATIN"}, "vi": {"LATIN"},
    "ru": {"CYRILLIC"}, "uk": {"CYRILLIC"},
    "zh": {"CJK"}, "ja": {"CJK", "HIRAGANA", "KATAKANA"}, "ko": {"HANGUL"},
    "hi": {"DEVANAGARI"}, "bn": {"BENGALI"},
    "ar": {"ARABIC"}, "fa": {"ARABIC"},
}

_SCRIPT_TAGS = ("CYRILLIC", "CJK", "HIRAGANA", "KATAKANA", "HANGUL", "ARABIC",
                "DEVANAGARI", "BENGALI", "HEBREW", "THAI", "GREEK", "LATIN")
# below this there is not enough alphabetic text to judge — a batch of
# "OOK {r} kbit/s"-style strings is legitimately almost all Latin
MIN_ALPHA = 24


def _script_counts(text: str) -> dict[str, int]:
    """How many alphabetic characters belong to each script."""
    counts: dict[str, int] = {}
    for ch in text:
        if not ch.isalpha():
            continue
        name = unicodedata.name(ch, "")
        for tag in _SCRIPT_TAGS:
            if name.startswith(tag):
                counts[tag] = counts.get(tag, 0) + 1
                break
    return counts


def wrong_script(lang: str, text: str) -> str | None:
    """Reason the text is not in `lang`'s script, or None if it is fine.

    Dominance alone is the wrong test: the schematics labels are part numbers
    and units — "10 µF", "I2C SDA", "SMBJ5.0A" — so a perfectly good Japanese
    section is majority Latin. Latin is the neutral script here and never
    counts against a language. What does:

      - the expected script is entirely absent, with enough text to say so.
        The Russian-filled ja section had zero kana and zero kanji;
      - some other non-Latin script dominates, which is how a Cyrillic answer
        to a "translate into Spanish" prompt would look.
    """
    expected = SCRIPTS.get(lang)
    if not expected:
        return None
    counts = _script_counts(text)
    total = sum(counts.values())
    if total < MIN_ALPHA:
        return None
    if not any(counts.get(tag) for tag in expected):
        return f"contains no {'/'.join(sorted(expected))} at all"
    got = max(counts, key=counts.get)
    if got not in expected and got != "LATIN":
        return f"dominated by {got}, expected {'/'.join(sorted(expected))}"
    return None


def report_uncovered(lang: str, missing: set[str]) -> str:
    sample = "".join(sorted(missing)[:12])
    return (f"{lang}: {len(missing)} character(s) no installed font can draw "
            f"({sample!r}) — install the Noto face for this script "
            "(CI: fonts-noto-core, fonts-noto-cjk) or add the language to "
            "render.skip_figures in i18n.json")

# How to Contribute

> English (primary) · [Русский](translations/ru/CONTRIBUTING.md) · [Deutsch](translations/de/CONTRIBUTING.md) · [Português](translations/pt/CONTRIBUTING.md) · [中文](translations/zh/CONTRIBUTING.md) · [日本語](translations/ja/CONTRIBUTING.md)

Thank you for wanting to advance the open through-steel channel. The three rules below are not bureaucracy — they are the project's patent armor (see [LICENSES.md](LICENSES.md) for why).

## 1. Contribution licenses (inbound = outbound)

By submitting a contribution, you agree that it is licensed the same way as the rest of the material in its directory:

- `software/`, `firmware/` → Apache-2.0;
- `hardware/` → CERN-OHL-W v2;
- `docs/`, `experiments/` → CC-BY-4.0.

**Patent grant.** In addition — since CC-BY-4.0 does not license patents — you grant the project and all recipients of its materials a perpetual, irrevocable, worldwide, royalty-free, non-exclusive patent license to make, have made, use, offer for sale, sell, import, and otherwise transfer your contribution, both on its own and as part of the project — to the extent of those of your patent claims that are necessarily infringed by the contribution by itself or by its combination with the project it was submitted to. The terms follow §3 of Apache-2.0, regardless of which directory the contribution landed in. If you institute patent litigation against anyone (including a counterclaim) alleging that the project's materials infringe your patent, then all **patent** licenses granted to you by the project and its contributors under this clause and under the project's licenses terminate as of the date such litigation is filed.

## 2. DCO: a signature on provenance

Every commit carries a sign-off (`git commit -s`), signifying agreement with the [Developer Certificate of Origin 1.1](https://developercertificate.org/): you confirm that you have the right to submit this contribution under the project's license.

```
Signed-off-by: Firstname Lastname <email@example.com>
```

PRs without a sign-off do not get merged; the check is automatic — the CI job [.github/workflows/dco.yml](.github/workflows/dco.yml) fails the PR if even a single commit lacks a sign-off. The patent protection of the docs layer rests on exactly this chain — no exceptions.

**Moving material between layers.** Material lives in the layer it landed in (and under that layer's license). Moving text/code between layers with different licenses is allowed only if it is your own material, or with an explicit note of the fragment's original license.

## 3. Patent hygiene and experiment protocol

- Every technical decision must trace back to a free source — an expired patent or a paper from [docs/01-prior-art.md](docs/01-prior-art.md). Implementations of live claims (listed there as well) are not accepted until those claims expire.
- Experimental results — only via the [experiments/TEMPLATE.md](experiments/TEMPLATE.md) template: a dated, reproducible protocol is precisely what constitutes our prior art.
- Architecture decisions go through ADRs in [docs/decisions/](docs/decisions/).
- Code comments, docstrings, identifiers, and commit messages are English-only. Docs are multilingual (see below); user-visible figure labels live in `labels.json`.

## 4. Multilingual docs: edit one language, CI syncs the rest

English is primary and owns the canonical paths. Every other language is a mirror tree under [translations/](translations/) with identical file names — markdown, the BOM CSV and generated figures included; figure text is driven by `labels.json`. You do **not** have to maintain the mirrors by hand:

- Edit whichever language is comfortable. On push, the [Translation sync](.github/workflows/translate.yml) workflow translates the counterparts with an open-weights LLM (`glm-5.2` on Ollama Cloud), regenerates figures when the sync updates `labels.json`, and commits the result back with the `[translate-sync]` marker. Any OpenAI-compatible endpoint works — set `OPENAI_BASE_URL` and `TRANSLATE_MODEL`.
- What still owes work is tracked in `translations/.sync-state.json`, which records the primary content every translation was made from. A run cut short by a quota or a timeout therefore loses nothing: the unfinished pairs stay marked stale and are picked up by the next push or by the nightly run. Do not hand-edit that file.
- If you edited **several** languages of a doc yourself, every version you touched is kept as you wrote it; the bot only fills in the languages you did not touch.
- **`labels.json` is the exception to "edit any language".** Figure labels flow primary → mirrors only. Editing a translated label fixes that language and stops there; it does not travel back into English. To change what a label *says*, edit the primary section. The reason is asymmetry: a label edit is nearly always someone correcting the machine's wording, and letting that rewrite the primary would redefine the source all fourteen mirrors are generated from. Keys the bot has never produced still propagate back, so a hand-authored label is not stuck in one language.
- Machine translation gets committed — skim the bot's commit and touch up wording if it misses the tone; your fix won't be overwritten (the bot records your version as the current one).
- A reply that came back truncated or with mangled `labels.json` placeholders is discarded rather than committed, and the pair is retried — so an odd-looking gap in a mirror is a stale pair, not a decision.
- **External PRs:** the bot runs on `master`, so a PR may change just one language — the mirrors (including English) catch up automatically right after the merge. You do not need to know English to contribute docs.
- **Adding a language:** add its code and name to [i18n.json](i18n.json) (e.g. `"fr": "Français"`) and push — the pipeline builds the whole `translations/fr/` mirror: every doc, a `fr` section in each `labels.json`, the figure set, and the language switchers everywhere.
- **Non-Latin scripts:** CI installs the Noto families (`fonts-noto-core`, `fonts-noto-cjk`) and the renderers walk the font stack in `i18n.json` → `render.fonts`, so Cyrillic, Han, kana and Hangul come out properly. A renderer now checks glyph coverage before drawing and **fails rather than painting `.notdef` boxes** — that check exists because the Chinese figures shipped as a grid of tofu and nothing in CI looks at pixels. If it fires, add the Noto face for that script to the stack.
- **Scripts needing contextual shaping** — Arabic and Persian (RTL, joined forms), Devanagari and Bengali (conjuncts) — cannot be drawn correctly by matplotlib, which has no shaping engine: even with the right font the glyphs come out unjoined and misordered. List those languages in `i18n.json` → `render.skip_figures`. Their prose is unaffected; their docs simply link to the primary figures, which the link repair in [tools/translate_sync.py](tools/translate_sync.py) points at automatically. `hi` is set up this way.
- **Script guard:** `SCRIPTS` in [tools/i18n_render.py](tools/i18n_render.py) records which script each language's labels must contain. A reply that has none of it — the `ja` sections once shipped filled with Russian — is rejected and retried instead of committed. A language missing from that table simply gets no guard, so adding one to `i18n.json` never breaks; add the entry to get the check.

## 5. Checks you can run before pushing

```bash
python tools/check_repo.py
```

Verifies what the translation bot is capable of breaking and nothing else would catch: every relative link resolves, every `labels.json` section matches `i18n.json` and carries the same keys and the same `str.format` placeholders as the primary one, every canonical doc has a mirror in every language, and every markdown file has its language bar. CI runs it on both workflows; it needs no dependencies.

The rest of CI ([ci.yml](.github/workflows/ci.yml)) compiles the scripts and runs the whole figure pipeline. To reproduce it exactly — including the committed figures — install the pinned toolchain, not the loose one:

```bash
python -m pip install -r tools/requirements-ci.txt
```

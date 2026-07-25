# How to Contribute

> English (primary) · [Русский](translations/ru/CONTRIBUTING.md) · [Deutsch](translations/de/CONTRIBUTING.md) · [Português](translations/pt/CONTRIBUTING.md)

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

- Edit whichever language is comfortable. On push, the [Translation sync](.github/workflows/translate.yml) workflow finds docs where only one language changed, translates the counterparts with GitHub Models (`meta/llama-3.3-70b-instruct`, no API keys needed), regenerates figures when the sync updates `labels.json`, and commits the result back with the `[translate-sync]` marker.
- If you edited **several** languages of a doc yourself, the bot leaves that doc alone.
- Machine translation gets committed — skim the bot's commit and touch up wording if it misses the tone; your fix won't be overwritten (the bot only reacts to new changes).
- **External PRs:** the bot runs on `master`, so a PR may change just one language — the mirrors (including English) catch up automatically right after the merge. You do not need to know English to contribute docs.
- **Adding a language:** add its code and name to [i18n.json](i18n.json) (e.g. `"fr": "Français"`) and push — the pipeline builds the whole `translations/fr/` mirror: every doc, a `fr` section in each `labels.json`, the figure set, and the language switchers everywhere.
- **Non-Latin scripts (CJK etc.):** figure rendering currently ships Latin + Cyrillic fonts only; before adding e.g. Japanese to i18n.json, a CJK font has to be wired into the render scripts — open an issue first.

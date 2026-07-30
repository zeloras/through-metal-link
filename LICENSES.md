# Licensing and patent protection

> English (primary) · [Русский](translations/ru/LICENSES.md) · [Deutsch](translations/de/LICENSES.md) · [Português](translations/pt/LICENSES.md) · [中文](translations/zh/LICENSES.md) · [日本語](translations/ja/LICENSES.md)

The goal of this scheme: the project is fully open, anyone can fork it and build on it (commercially included), while the patent-litigation risk is cut down to the bare minimum achievable by legal and procedural means at all.

## The scheme (three layers; full texts in [LICENSES/](LICENSES/))

| Area | License | Text | Patent provisions |
|---|---|---|---|
| `software/`, `firmware/` | Apache-2.0 | [LICENSES/Apache-2.0.txt](LICENSES/Apache-2.0.txt) | §3: every contributor automatically grants a patent license for their contribution; file a patent suit and you lose the **patent** license (retaliation; the copyright license in §2 is irrevocable and survives the suit) |
| `hardware/` | CERN-OHL-W v2 | [LICENSES/CERN-OHL-W-2.0.txt](LICENSES/CERN-OHL-W-2.0.txt) | §7.1: a patent license (Make / have Made / use / sell / import…) from every licensor — but only for claims necessarily infringed by the given Covered Source; §7.2: a patent suit (including an attempt to invalidate someone else's patent) terminates **all** rights under the license |
| `docs/`, `experiments/` | CC-BY-4.0 | [LICENSES/CC-BY-4.0.txt](LICENSES/CC-BY-4.0.txt) | grants **no** patent rights (§2(b)(2)) — the gap is closed by the explicit patent grant in [CONTRIBUTING.md](CONTRIBUTING.md) |
| everything else (root `README.md`, `QUICKSTART.md`, this file, `data/`, etc.) | CC-BY-4.0 | — | fallback: no file in the repository is left "all rights reserved" |

Code files carry SPDX headers (Apache-2.0); the machine-readable coverage map is [REUSE.toml](REUSE.toml). The copyright line lives in [NOTICE](NOTICE); the root [LICENSE](LICENSE) is a pointer to this scheme.

**Why CERN-OHL-W, not S or P.** W is the middle ground: the design and its modifications must stay open on any distribution, but the product the design is built into may be commercial and proprietary — which keeps open the niches from docs/05 (labs, breweries, battery packs). S (strong copyleft) would shut the door on embedding; P (permissive) would allow closed forks. Tightening toward S is baked into the license itself: §8.3 lets anyone treat W-licensed material as S-licensed (provided the Available Components condition is met) — no permission required. Loosening (toward P or another license), by contrast, is possible only while all the material belongs to a single author; after the first external contribution — only with the consent of every contributor.

**Project name.** "through-metal-link" is not a registered trademark; the licenses themselves grant no rights to the name (Apache §6, CC-BY §2(b)(2), CERN-OHL-W §8.2). Referring to the project factually ("based on through-metal-link") is free for anyone; forks with incompatible changes are asked to ship under their own name.

## What this protects against — and what it doesn't (honestly)

**It protects against:**
1. **Suits from contributors.** Anyone who contributed has automatically licensed their patent rights on that contribution (Apache §3, CERN-OHL §7.1, and CONTRIBUTING for docs). A suit costs the plaintiff dearly: under Apache-2.0 they lose the patent licenses to the code; under CERN-OHL-W they lose all rights to the hardware layer outright (§7.2 — triggered even by an attempt to challenge someone else's patent).
2. **Privatization of hardware forks.** CERN-OHL-W obliges anyone who distributes (Conveyance of a product or of sources) to publish their design modifications — improvements flow back into the open layer and themselves become prior art. (A drawer fork, never conveyed to third parties, has no publishing obligation — same as under any copyleft.)
3. **Other people's *future* patents.** Everything published with a date destroys novelty for later applications: for a solution described here before their filing date, a valid patent can no longer be granted. Against applications filed *before* our publication this does not work — for those, the only shield is the expired-patents layer (see below).

**It does not protect against:**
- **Third-party patents that already exist.** No license can do that. What works against them is the engineering discipline of docs/01-prior-art.md: build only from the expired layer (public domain), do not implement live claims (RPI OFDM/full-duplex, Drexel — until ~2032, US-only), and trace every design decision back to a free source. That is no guarantee, but it is exactly the practice that makes a lawsuit futile.
- A fork headed for commercial production does its own FTO (freedom to operate) analysis for its own jurisdiction and design — the repository makes no patent representations (disclaimers in all three licenses).

## Defensive publication protocol (execute when the repo goes public)

Every published result is dated prior art that blocks all later third-party applications for the same solution:

1. Open the repository with its full git history (commits = timestamps).
2. Snapshot to **Zenodo** → DOI: an independent archive with a legally meaningful date, citable in papers.
3. Pin it in **Software Heritage** (archive.softwareheritage.org — a perpetual mirror).
4. Every completed experiment `experiments/NNN` — with a date, numbers, and plots: that is the publication of a specific technical solution.
5. Major milestones (first watts, first node) — a writeup out in the world (Hackaday.io / arXiv / blog): the wider the spread, the stronger the prior-art status.

## For contributors

The rules live in [CONTRIBUTING.md](CONTRIBUTING.md): DCO sign-off, inbound=outbound, an explicit patent grant on every contribution regardless of directory, traceability of design decisions to free prior art.

Until it opens, the repository stays private — publishing before the first reproducible results would weaken both the scientific and the patent position.

# THE FORGOTTEN SUMMONER
## Setting Book Preview Package v0

## Package Purpose

이 문서는 현재 설정집을
reader-facing preview 형태로 보여주기 위한 조립 지시서다.

본문과 부록 원고를 한 파일에 무리하게 복제하지 않고,
어떤 순서로 읽고 어떤 기준으로 검증해야 하는지를 고정한다.

현재 대표 단일본은 `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`이고,
이 preview package는 release 후보를 만들 때의 읽기 순서와 포함 범위를 정한다.

현재 공유용 대표본은 `Setting_Book_Preview_Readable_v0.md`다.

Current naming decision:

- Keep `Setting_Book_Preview_Readable_v0.md` as the shareable preview file for now.
- Do not rename it into a release-candidate file until row-level evidence notes and final layout direction are decided.
- Use `A Living World Companion` as the v0 subtitle and keep the current cover-tone sentence aligned with the readable preview opening.

Release-candidate trigger:

- Create a separate RC package only when the checklist says packaging is the next preserved artifact, not just the next draft pass.
- Until then, keep preview and prototype as two different jobs: one shareable, one compressed reference.

## Preview Reading Order

| Order | Section | Source File | Include Mode |
| --- | --- | --- | --- |
| 1 | Shareable readable preview | `Setting_Book_Preview_Readable_v0.md` | primary shareable manuscript |
| 2 | Core profile companion set | `Setting_Book_Faction_Core_Profiles_v0.md`, `Setting_Book_People_Core_Profiles_v0.md`, `Setting_Book_Places_Core_Profiles_v0.md`, `Setting_Book_Items_Core_Profiles_v0.md`, `Setting_Book_Species_Core_Profiles_v0.md` | optional bridge set between readable preview and technical drafts |
| 3 | Cover direction and reading promise source | `Setting_Book_Front_Matter_Draft.md` | source support for preview opening |
| 4 | Reader-facing table of contents | `Setting_Book_Reader_Facing_TOC_Draft.md` | navigation map and future expansion guide |
| 5 | Public body manuscript source | `Setting_Book_Public_Assembly_Manuscript_Draft.md` | source support for preview body |
| 6 | Technical appendix manuscript | `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` | include after body when verification context is needed |
| 7 | Release readiness check | `Setting_Book_Release_Readiness_Checklist.md` | conductor-only gate before wider sharing |
| 8 | Single prototype reference | `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | compressed reference and sync check |

## Included Body Spine

The preview body currently covers:

1. How to Read This World
2. Ether Continent
3. Crossroad Cities
4. People Worth Seeking
5. Relics and Desired Objects
6. Peoples, Bloodlines, and Changed States

The preview body does not yet try to replace the full 0-8 technical chapter package.
It demonstrates the readable shape of the setting book.

## Core Profile Companion Set

The core profile set currently covers:

1. Factions
2. People
3. Places
4. Items
5. Species

These files are not the main shareable manuscript.
They are bridge documents for collaborators or for the conductor when the readable preview is too broad
and the technical drafts are too deep.

## Included Appendix Spine

The preview appendix currently covers:

1. Appendix A. 14 / 15 Boundary Candidates
2. Appendix B. Item Promotion Candidates
3. Appendix C. Place and Travel Functions
4. Appendix D. Name Collision Control
5. Appendix E. Species Classification Guard

Appendix A-E are enough for preview v0 because they cover the major risks introduced by the current body:

- hero / notable boundary drift
- item promotion drift
- place and route flattening
- name collision collapse
- species / bloodline / state overpromotion

## What Preview v0 Is Allowed To Claim

Preview v0 may claim:

- the setting book has a readable public voice
- the body and appendix are separated
- the current prototype has a stable A-E appendix flow
- major uncertainty areas are controlled rather than hidden
- `main push gate` has been added as a standing preservation rule

Preview v0 should not claim:

- every continent has a full public chapter
- every appendix table has final source citations
- every named figure, item, species, or place is promoted to body-final status
- the current package is a finished commercial layout

## Shareable Version Rule

If this package is shared with a collaborator:

1. Share `Setting_Book_Preview_Readable_v0.md` first.
2. Share the relevant `Core Profiles` file next if they need one axis in a denser form.
3. Share `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` only if they need verification context.
4. Keep `Setting_Book_Release_Readiness_Checklist.md`, `Setting_Book_Assembly_Index.md`, and `Setting_Book_Preview_Package_v0.md` as conductor documents unless the collaborator is helping with structure.

## Next Preview Build

The next preview build should do one of two things:

| Build | Purpose | Next Action |
| --- | --- | --- |
| `preview_v0_readable` | Let a reader understand the world tone quickly | polish front matter and public assembly into one smooth read |
| `preview_v0_production` | Let a collaborator understand structure and risks | add source notes and body links to Appendix A-E |

Current conductor choice:

Treat `preview_v0_readable` as the current shareable package.

The package already has enough verification structure.
The next gain is not another broad content pass.
It comes from either adding targeted evidence notes for v1
or deciding whether the package should be copied into a separate release-candidate file after v1 gates are tighter.

# THE FORGOTTEN SUMMONER
## Setting Book Preview Package v0

## Package Purpose

이 문서는 현재 설정집을
reader-facing preview 형태로 보여주기 위한 조립 지시서다.

본문과 부록 원고를 한 파일에 무리하게 복제하지 않고,
어떤 순서로 읽고 어떤 기준으로 검증해야 하는지를 고정한다.

현재 대표 단일본은 `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`이고,
이 preview package는 release 후보를 만들 때의 읽기 순서와 포함 범위를 정한다.

## Preview Reading Order

| Order | Section | Source File | Include Mode |
| --- | --- | --- | --- |
| 1 | Cover direction and reading promise | `Setting_Book_Front_Matter_Draft.md` | include before body |
| 2 | Reader-facing table of contents | `Setting_Book_Reader_Facing_TOC_Draft.md` | include as navigation map |
| 3 | Public body manuscript | `Setting_Book_Public_Assembly_Manuscript_Draft.md` | include as main reading flow |
| 4 | Technical appendix manuscript | `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` | include after body |
| 5 | Release readiness check | `Setting_Book_Release_Readiness_Checklist.md` | keep as conductor-only note unless sharing with collaborators |
| 6 | Single prototype reference | `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | use as compressed reference and sync check |

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

1. Share `Setting_Book_Front_Matter_Draft.md` first.
2. Share `Setting_Book_Public_Assembly_Manuscript_Draft.md` second.
3. Share `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` only if they need verification context.
4. Keep `Setting_Book_Release_Readiness_Checklist.md` and `Setting_Book_Assembly_Index.md` as conductor documents unless the collaborator is helping with structure.

## Next Preview Build

The next preview build should do one of two things:

| Build | Purpose | Next Action |
| --- | --- | --- |
| `preview_v0_readable` | Let a reader understand the world tone quickly | polish front matter and public assembly into one smooth read |
| `preview_v0_production` | Let a collaborator understand structure and risks | add source notes and body links to Appendix A-E |

Current conductor choice:

Proceed toward `preview_v0_readable` first.

The package already has enough verification structure.
The next gain comes from making the public body read like one intentional book rather than a bundle of samples.

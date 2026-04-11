# Setting Book Assembly Index

## Purpose

This index tracks the current setting-book recomposition package.

It is not the final setting book. It is the conductor sheet for turning the chapter drafts into a cleaner, reader-facing setting book while preserving source discipline, canon tiers, and unresolved questions.

## Current Package State

| Chapter | Draft File | Current State | Assembly Role |
| --- | --- | --- | --- |
| 0. Canon Policy | `Setting_Book_Chapter_0_Canon_Policy_Draft.md` | first draft complete | Defines source priority, canon tier, archive routing, and story-first expansion control. |
| 1. Five Continents | `Setting_Book_Chapter_1_Five_Continents_Draft.md` | first draft complete | Establishes continent identity, social spine, missing layers, and emotional tone. |
| 2. Faction Archive Structure | `Setting_Book_Chapter_2_Faction_Archive_Structure_Draft.md` | first draft complete | Separates root state, continent spine, structure label, place pressure, and 8-to-15 handoff. |
| 3. Named Notables and Operational Lines | `Setting_Book_Chapter_3_Named_Notables_Operational_Lines_Draft.md` | first draft complete | Separates 14 hero axis from 15 named figures and organization operating layers. |
| 4. Naming Normalization | `Setting_Book_Chapter_4_Naming_Normalization_Draft.md` | first draft complete | Defines display names, tone policy, faction replacements, and protected name collisions. |
| 5. Items and Relics | `Setting_Book_Chapter_5_Item_Desire_Structure_Draft.md` | first draft complete | Turns item candidates into desire-first relic, gear, trade good, and collection structures. |
| 6. Species Framework | `Setting_Book_Chapter_6_Species_Framework_Draft.md` | first draft complete | Separates species, bloodline, state, monster, and unclear evidence. |
| 7. Spatial Map | `Setting_Book_Chapter_7_Spatial_Map_Draft.md` | first draft complete | Builds map logic through place function, travel route, and layer progression. |
| 8. Register Appendix | `Setting_Book_Chapter_8_Register_Appendix_Draft.md` | first draft complete | Defines how registers, manifests, queues, conflicts, secrets, and appendices support the body. |

## Support Files

| File | Use |
| --- | --- |
| `Setting_Book_Reassembly_Source_Map.md` | Locks primary and secondary sources per chapter. |
| `Setting_Book_Skeleton.md` | Holds the original chapter build plan and required sections. |
| `Setting_Book_Public_Assembly_Manuscript_Draft.md` | Bundles the current public-facing samples into one readable manuscript flow. |
| `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` | Bundles the current appendix samples into one technical appendix flow. |
| `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | Holds the current single-file prototype with expanded body sections and A-E appendix flow. |
| `Setting_Book_Release_Readiness_Checklist.md` | Cross-checks front matter, TOC, body, appendix, prototype, and main push gate before release packaging. |
| `Setting_Book_Preview_Package_v0.md` | Defines the reader-facing preview package order and what v0 may safely claim. |
| `Setting_Book_Preview_Readable_v0.md` | Serves as the current shareable readable preview manuscript. |
| `Setting_Book_Faction_Core_Profiles_v0.md` | Serves as the faction-first bridge between the readable preview and the technical continent/faction drafts. |
| `Setting_Book_People_Core_Profiles_v0.md` | Serves as the people-first bridge between the readable preview and the 14/15 technical drafts. |
| `Setting_Book_Places_Core_Profiles_v0.md` | Serves as the places-first bridge between the readable preview and the spatial/travel technical drafts. |
| `Setting_Book_Items_Core_Profiles_v0.md` | Serves as the items-first bridge between the readable preview and the item/relic promotion drafts. |
| `Setting_Book_Species_Core_Profiles_v0.md` | Serves as the species-first bridge between the readable preview and the species classification drafts. |

## Assembly Principle

The final setting book should not expose the whole audit engine to the reader.

Use this split:

| Layer | What It Should Do |
| --- | --- |
| Reader-facing body | Explain the world clearly, with clean names and strong narrative function. |
| Technical appendix | Preserve evidence, labels, unresolved questions, and promotion gates. |
| Audit archive | Keep historical reasoning, old routes, and rejected or deferred materials. |

## Body-to-Appendix Routing

Move material into the body when it answers:

- What is this part of the world?
- Why does it matter to characters?
- What conflict, desire, memory, or movement does it create?
- What can be safely stated without overcommitting?

Move material into the appendix when it answers:

- What evidence supports this?
- What status label applies?
- What still needs verification?
- What names or variants are protected?
- What future work should not be forgotten?

Keep material in audit-only history when it answers:

- Why did an old batch make a temporary decision?
- Which route was deprecated?
- Which prior wording should not return to display canon?
- Which exploration branch is useful but not reader-facing?

## Current Cleanliness Checks

Completed checks:

- 0-8 chapter draft files exist.
- public manuscript assembly draft exists.
- appendix manuscript assembly draft exists.
- single prototype v0 exists and currently carries the expanded body spine.
- Current setting-book files do not contain the older stable-triad label.
- Current setting-book files do not use the old watch/reference phrasing.
- Current setting-book files do not use the old watch-keep display state in tables.
- `working/crosswalks/Extracted_Item_Candidates.md` remains untouched by this assembly pass.

## Next Assembly Queue

Recommended next sequence:

1. Run a style-unification pass over the public assembly manuscript.
2. Run a rhythm-and-density pass over the readable preview now that the core profile companion set is in place.
3. Expand the appendix assembly manuscript with one real embedded table per section.
4. Use the release readiness checklist before packaging a preview manuscript.
5. Use the preview package to choose readable preview or production preview.
6. Extend the strongest mid-layer sheets into small reusable profile families before widening the surface area.
7. Prepare a short checkpoint summary for thread handoff if context gets too long.
8. At stable milestones, run the `Main Push Gate` before pushing to `main`.

## Main Push Gate

`main` push는 자동으로 매번 하지 않는다.

아래 조건을 만족하는 적정 시점에만 `main`으로 올린다.

1. 현재 작업 브랜치가 원격에 푸시되어 있다.
2. 단일 prototype 파일이 최신 흐름을 대표한다.
3. 설정집 계열 파일에서 금지 표현과 미완료 표식 스캔이 깨끗하다.
4. 사용자 또는 별도 작업 파일이 섞여 있지 않다.
5. 다음 단계가 실험 확장이 아니라 안정본 보존일 때다.

현재 main push 후보 시점:

- prototype v0 1차 확장 완료 후
- public manuscript와 appendix가 서로 같은 목차를 가리킨 뒤
- 사용자가 명시적으로 main 반영을 원하거나, 오케스트라가 안정 마일스톤으로 판정한 뒤

최근 gate 통과:

- 허브 사용성 마감 패스까지 `main`에 fast-forward push 완료.

## Conductor Decision

The setting-book recomposition has moved from source-map setup and sample generation into prototype manuscript state.

The next meaningful work is controlled refinement: keep the readable manuscript stable, let the core profile companion set function as the bridge layer between body and technical drafts, and deepen the appendix with selected real tables.

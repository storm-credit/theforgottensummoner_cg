# Setting Book Thread Checkpoint

## Purpose

이 문서는 현재 설정집 재조합 작업을
새 대화창으로 넘겨야 할 때 빠르게 이어갈 수 있도록 만든 checkpoint 요약이다.

## Branch

- `codex/species-framework-side-track`

## Current Stage

설정집 작업은 이제 `prototype manuscript stage`다.

이미 끝난 축:

- 0-8장 기술 초안 작성
- source map / skeleton / assembly index 작성
- reader-facing TOC 작성
- body / appendix separation plan 작성
- public voice sample 작성
- appendix sample 작성
- public manuscript assembly draft 작성
- appendix manuscript assembly draft 작성
- single prototype v0 작성
- prototype 본문 1차 확장: Ether, Crossroad Cities, People, Relics, Species/Bloodlines/States
- `main push gate` 고정점 추가

## Core Files

기술 초안:

- `working/drafts/Setting_Book_Chapter_0_Canon_Policy_Draft.md`
- `working/drafts/Setting_Book_Chapter_1_Five_Continents_Draft.md`
- `working/drafts/Setting_Book_Chapter_2_Faction_Archive_Structure_Draft.md`
- `working/drafts/Setting_Book_Chapter_3_Named_Notables_Operational_Lines_Draft.md`
- `working/drafts/Setting_Book_Chapter_4_Naming_Normalization_Draft.md`
- `working/drafts/Setting_Book_Chapter_5_Item_Desire_Structure_Draft.md`
- `working/drafts/Setting_Book_Chapter_6_Species_Framework_Draft.md`
- `working/drafts/Setting_Book_Chapter_7_Spatial_Map_Draft.md`
- `working/drafts/Setting_Book_Chapter_8_Register_Appendix_Draft.md`

조립 제어 문서:

- `working/drafts/Setting_Book_Reassembly_Source_Map.md`
- `working/drafts/Setting_Book_Skeleton.md`
- `working/drafts/Setting_Book_Assembly_Index.md`
- `working/drafts/Setting_Book_Body_Appendix_Separation_Plan.md`
- `working/drafts/Setting_Book_Reader_Facing_TOC_Draft.md`

본문 샘플:

- `working/drafts/Setting_Book_Public_Voice_Sample_Opening_Ether.md`
- `working/drafts/Setting_Book_Public_Voice_Sample_Crossroad_Cities.md`
- `working/drafts/Setting_Book_Public_Voice_Sample_Named_Notables.md`
- `working/drafts/Setting_Book_Public_Voice_Sample_Relics.md`
- `working/drafts/Setting_Book_Public_Voice_Sample_Species_Bloodlines.md`

부록 샘플:

- `working/drafts/Setting_Book_Appendix_Sample_14_15_Boundary.md`
- `working/drafts/Setting_Book_Appendix_Sample_Item_Promotion.md`
- `working/drafts/Setting_Book_Appendix_Sample_Place_Travel.md`
- `working/drafts/Setting_Book_Appendix_Sample_Name_Collision.md`

현재 조립본:

- `working/drafts/Setting_Book_Public_Assembly_Manuscript_Draft.md`
- `working/drafts/Setting_Book_Appendix_Assembly_Manuscript_Draft.md`
- `working/drafts/The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`
- `working/drafts/Setting_Book_Release_Readiness_Checklist.md`
- `working/drafts/Setting_Book_Preview_Package_v0.md`

## Recent Commit Line

- `a64059a Align setting book appendix TOC`
- `b846eb6 Expand public setting book assembly`
- `a476683 Record main push gate pass`
- `a7709ad Add species classification appendix`
- `a563e75 Expand prototype species framework`
- `a133956 Expand prototype and add main push gate`
- `f5672b3 Expand prototype ether and crossroad sections`
- `25d9ff3 Add single setting book prototype`

그 직전 주요 축:

- `2b6fd6f Refine setting book manuscript assemblies`
- `332f72b Add setting book front matter draft`
- `b1d3d77 Refresh setting book index and checkpoint`
- `357f909 Add assembled setting book manuscript drafts`
- `db56fb8 Add species and naming collision samples`
- `34382f3 Add public samples for notables and relics`
- `5e64043 Add crossroad cities and place travel samples`

## Safety Note

이 작업 패스에서 건드리지 않은 사용자 변경 파일:

- `working/crosswalks/Extracted_Item_Candidates.md`

이 파일은 계속 untouched 상태로 두어야 한다.

## Recommended Next Queue

1. preview package 기준으로 `preview_v0_readable` 방향 진행
2. public manuscript style-unification pass
3. appendix manuscript와 prototype appendix를 A-E 흐름으로 유지
4. 최종 단일 prototype 파일 이름 정리 또는 release/bible 방향 선택
5. 안정 마일스톤마다 `main push gate` 확인

## Main Push Gate

적정 시점에는 `main`에도 푸시한다.

단, 아래 조건을 만족할 때만 진행한다.

1. 현재 작업 브랜치가 원격에 푸시되어 있다.
2. prototype 파일이 최신 대표본이다.
3. 설정집 계열 파일 스캔에서 금지 표현과 미완료 표식이 나오지 않는다.
4. 사용자 변경 파일이 커밋에 섞이지 않는다.
5. 지금 작업이 실험 중간 상태가 아니라 보존 가능한 안정 지점이다.

현재 계속 분리해서 보존해야 하는 사용자 변경 파일:

- `working/crosswalks/Extracted_Item_Candidates.md`

최근 gate 통과:

- `a64059a`까지의 prototype v0, public assembly 확장, A-E appendix flow, front matter / TOC 정합화를 `main`에 fast-forward push 완료.

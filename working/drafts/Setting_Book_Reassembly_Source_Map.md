# Setting Book Reassembly Source Map

이 문서는 `THE FORGOTTEN SUMMONER` 설정집을 다시 조립하기 전에,
어떤 working / audit / reference 문서를 어느 장의 기준으로 삼을지 잠그는 소스맵이다.

목적은 새 설정을 발명하는 것이 아니라,
이미 정리된 `cg` 기준 문서들을 설정집 목차로 안전하게 재배열하는 것이다.

현재 기준에서 이 문서는 `직접 공유 원고`가 아니라
장별 재조립을 다시 열 때 참조하는 source discipline map으로 둔다.
안정 공유본은 계속 `Setting_Book_Preview_Readable_v0.md`다.
최종 public Part naming authority는 `Setting_Book_Reader_Facing_TOC_Draft.md`에 둔다.
이 문서는 장별 source routing만 잠그며, public TOC title을 직접 바꾸지 않는다.

## Source Priority

설정집 재조합은 아래 순서로 읽는다.

1. `workflow` 정책 문서: 작품 철학, canon policy, lore engine, story engine.
2. `audit` lock / register 문서: canon tier, source priority, state label, mainline sync, missing-layer lock.
3. `working/drafts` synthesis 문서: 대륙 framework, 5대륙 synthesis, adequacy map.
4. `working/crosswalks` 문서: 이름, 아이템, 종족, faction link, normalization draft.
5. `working/imports` 원본 복사본: 근거 확인용 snapshot. 직접 수정하지 않는다.
6. `reference/manifests` 문서: 원본 inventory와 누락 확인용 manifest.

충돌이 생기면 `audit/FS_Source_Priority_Register.md`와
`audit/FS_Canon_Tier_Register.md`를 먼저 본다.

## Reassembly Chapters

| Setting Book Chapter | Primary Sources | Secondary Sources | Reassembly Rule |
|---|---|---|---|
| `0. 운영 원칙 / Canon Policy` | `workflow/00_Astralis_Vision.md`, `workflow/01_Canon_Policy.md`, `workflow/11_FS_Engine.md`, `workflow/15_FS_Lore_Engine.md`, `workflow/16_FS_Story_Engine.md` | `audit/FS_Source_Priority_Register.md`, `audit/FS_Canon_Tier_Register.md`, `audit/FS_State_Label_Register.md` | 세계관 판단 순서와 canon tier를 먼저 제시한다. |
| `1. 5대륙 개요` | `working/drafts/Continents_Framework.md`, `working/drafts/Five_Continent_Synthesis.md` | `working/drafts/Continental_Adequacy_Map.md`, `audit/Five_Continent_Missing_Layer_Master_Lock.md` | 대륙별 정체성과 인간 군상은 synthesis/framework로 재배열하되, 결손층 thin/support 판단은 `audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry authority로 따른다. |
| `2. 세력 아카이브 구조` | `audit/Section_8_Mainline_Sync_Register.md`, `audit/Section_8_Normalization_Status_Compass.md`, `audit/Section_8_Status_Vocabulary_Guard.md` | `working/crosswalks/Section_8_vs_14_Decision_Guide.md`, `working/crosswalks/Section_14_to_8_Faction_Link_Map.md` | `Section 8`은 구조 라벨과 place pressure를 섞지 않는다. |
| `3. People Worth Seeking` | `audit/Section_15_Named_Notables_Status_Compass.md`, `audit/Section_15_Named_Notables_Register.md`, `audit/Section_15_State_Vocabulary_Guard.md` | `audit/Section_15_Folder_Draft_Routing_Plan.md`, `audit/Section_15_Named_Notables_Coverage_Matrix.md` | `14` 영웅축과 `15` People Worth Seeking / operational lines handoff를 분리한다. |
| `4. 이름 / 명칭 정규화` | `workflow/05_Naming_Normalization_Map.md`, `workflow/12_Naming_Tone_Guide.md`, `working/crosswalks/Name_Normalization_Draft.md`, `working/crosswalks/Faction_Naming_Replacement_Register.md` | `audit/Section_15_Named_Notables_Name_Collision_Register.md` | 표면명, 작업명, legacy name을 같은 칸에 섞지 않는다. |
| `5. 아이템 / 유물 / 욕망 구조` | `workflow/07_Item_Canon_Schema.md`, `workflow/08_Item_Desire_Design.md`, `working/crosswalks/Item_Candidate_Register.md`, `working/crosswalks/Item_Longterm_Taxonomy.md` | `working/drafts/Item_Collection_Findings.md`, `working/crosswalks/Item_Name_Collision_Register.md` | item은 후보표에서 evidence와 desire function이 안정된 뒤에만 백과 항목으로 올린다. |
| `6. 종족 / 영물 / species framework` | `working/crosswalks/Race_Species_Term_Crosswalk.md`, `working/drafts/Race_Species_Evidence_Log.md`, `audit/Species_Framework_Risk_Register.md` | `workflow/15_FS_Lore_Engine.md` | 종족명은 tone, canon tier, overread risk를 함께 표시한다. |
| `7. 공간 / 지도 / 이동감` | `workflow/10_Spatial_Map_Progression.md`, `working/drafts/Spatial_Backlog.md`, `working/drafts/Crossroad_Cities_Map_Seed.md`, `working/drafts/Crossroad_Cities_Ops_Matrix.md` | `audit/FS_Place_Function_Register.md`, `audit/FS_Travel_Logistics_Register.md` | 세계 -> 대륙 -> 도시 -> 건물 순서로만 확장한다. |
| `8. Register Appendix` | `audit/FS_*_Register.md`, `audit/Section_14_15_Boundary_Verification_Queue.md`, `audit/Section_15_Candidate_Register.md` | `reference/manifests/factions_manifest.md`, `reference/manifests/heroes_manifest.md` | 본문에 다 넣지 않고 검증용 appendix로 둔다. |

## Current Mainline Locks

- `Section 8 -> 15` 본선은 `mainline reference carryover` 상태로 유지한다.
- `stable_15_workset`은 닫힌 reference set으로만 사용한다.
- `source_check_hold / hold reference split`와 `deferred_expansion_hold / hold reference split`는 hold reference split 안에서만 읽는다.
- `working/imports`는 원본 snapshot이므로 직접 고치지 않는다.
- `working/crosswalks/Extracted_Item_Candidates.md`는 별도 추적 아티팩트로 보고, 이 소스맵에서는 참조만 한다.

## Reassembly Guard

설정집 본문을 만들 때 아래 순서를 지킨다.

1. 각 장마다 primary source를 먼저 요약한다.
2. secondary source는 누락/충돌/보류 항목 보강에만 쓴다.
3. `Hard Canon`, `Soft Canon`, `Open Question`, `Deprecated / Legacy`를 본문 안에서 구분한다.
4. 새 명칭을 만들 때는 naming guide와 collision register를 먼저 확인한다.
5. 원본 복사본의 멋진 표현이 있어도 audit lock과 충돌하면 본문으로 올리지 않는다.

## Next Assembly Queue

1. 장별 재조립을 다시 열어야 할 때 `8. Register Appendix` source lane부터 재개.
2. 재개 시 설정집 0-8장 상호 용어 점검.
3. 재개 시 장별 appendix 후보와 본문 후보 분리.
4. 재개 시 최종 설정집 조립용 index와 연결.

## Conductor Decision

현재 이 문서는 `재조립을 다시 시작할 때의 source 순서`를 잠가 두는 용도다.

지금 실제 공유 기준은 `Setting_Book_Preview_Readable_v0.md`를 안정 공유본으로 유지하는 쪽이고,
넓은 재조립이나 장별 확장은 다시 열릴 때만 이 source map을 따라간다.

그 재조립이 다시 열리면
가장 안전한 다음 출발점은
`working/drafts/Setting_Book_Chapter_8_Register_Appendix_Draft.md`이며,
그 전까지는 source map의 primary / secondary source 순서를 넘지 않는다.

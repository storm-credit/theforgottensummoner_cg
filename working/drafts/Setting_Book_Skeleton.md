# Setting Book Skeleton

이 문서는 `Setting_Book_Reassembly_Source_Map.md`를 바탕으로 만든
설정집 본문 작성용 skeleton이다.

아직 완성 원고가 아니라,
각 장에서 어떤 내용을 어떤 순서로 채울지 잠그는 작업용 뼈대다.
최종 public Part naming authority는 `Setting_Book_Reader_Facing_TOC_Draft.md`에 두고,
이 skeleton은 chapter fill order와 content routing만 잠근다.

## Global Rules

- 새 설정을 발명하지 않는다.
- primary source를 먼저 요약하고, secondary source는 보강과 충돌 확인에만 쓴다.
- `Hard Canon`, `Soft Canon`, `Open Question`, `Deprecated / Legacy`를 섞지 않는다.
- 원본 import 문서는 근거 확인용 snapshot으로만 읽고 직접 수정하지 않는다.
- `mainline reference carryover` 상태인 항목은 확장보다 일관성 유지가 우선이다.

## 0. 운영 원칙 / Canon Policy

작성 목표:

- 이 설정집이 어떤 기준으로 세계관을 읽는지 먼저 고정한다.
- 원본보다 `cg` 기준 문서가 언제 실행 판단에서 우선하는지 설명한다.
- `Hard Canon / Soft Canon / Open Question / Deprecated / Legacy`의 사용법을 짧게 둔다.

Primary source:

- `workflow/00_Astralis_Vision.md`
- `workflow/01_Canon_Policy.md`
- `workflow/11_FS_Engine.md`
- `workflow/15_FS_Lore_Engine.md`
- `workflow/16_FS_Story_Engine.md`

Required sections:

1. 작품 철학.
2. canon tier.
3. source priority.
4. legacy quarantine.
5. story-first expansion rule.

## 1. 5대륙 개요

작성 목표:

- 5대륙이 서로 같은 방식으로 서지 않는다는 점을 설정집의 중심 축으로 둔다.
- 각 대륙을 `정체성 / 인간 군상 / 대표 갈등 / 강한 사회층 / 결손층 / 감정 톤`으로 정리한다.

Primary source:

- `working/drafts/Continents_Framework.md`
- `working/drafts/Five_Continent_Synthesis.md`

Secondary source:

- `working/drafts/Continental_Adequacy_Map.md`
- `audit/Five_Continent_Missing_Layer_Master_Lock.md`

Required sections:

1. 에테르: 중심 문명, 가문/길드 강세, 정령연합 내부 부족축.
2. 크림슨: 사막 생존, 씨족 정치, 부족/길드 강세.
3. 프로스트: 혹한 생존, 클랜 정치, 보급 경제.
4. 오벨리스크: 붕괴 이후 기억, 봉인, 보급, 망명 네트워크.
5. 해양: 항로, 함대, 해상 귀족, 해적 질서, 교단 권위.

Guard:

- 결손층은 새 설정 발명으로 채우지 않는다.
- `thin/support` 범위는 `Five_Continent_Missing_Layer_Master_Lock.md`를 따른다.

## 2. 세력 아카이브 구조

작성 목표:

- `Section 8` 세력 구조를 설정집에서 읽는 기준을 정리한다.
- 구조 라벨, place pressure, mismatch, root corruption을 서로 다른 층으로 둔다.

Primary source:

- `audit/Section_8_Mainline_Sync_Register.md`
- `audit/Section_8_Normalization_Status_Compass.md`
- `audit/Section_8_Status_Vocabulary_Guard.md`

Required sections:

1. status vocabulary.
2. structure label과 place pressure 분리.
3. root corruption / quarantine / legacy 처리.
4. 5대륙 missing layer entry.
5. Section 8 -> 15 handoff.

Guard:

- `Section 8` 구조 라벨을 `Section 15` 인물 상태 라벨처럼 쓰지 않는다.
- place pressure는 sidecar/register owner를 따른다.

## 3. People Worth Seeking

작성 목표:

- `14` 영웅 백과와 `15` People Worth Seeking / operational lines handoff를 분리한다.
- 이름 있는 명사형 인물과 조직 작동층을 설정집에서 어떤 표로 보여줄지 정한다.

Primary source:

- `audit/Section_15_Named_Notables_Status_Compass.md`
- `audit/Section_15_Named_Notables_Register.md`
- `audit/Section_15_State_Vocabulary_Guard.md`

Secondary source:

- `audit/Section_15_Folder_Draft_Routing_Plan.md`
- `audit/Section_15_Named_Notables_Coverage_Matrix.md`

Required sections:

1. `stable_15_workset`.
2. `source_check_hold / hold reference split`.
3. `deferred_expansion_hold / hold reference split`.
4. 14/15 boundary review.
5. operational profile lower-card authority.

Guard:

- `stable_15_workset`은 닫힌 reference set으로만 둔다.
- `source_check_hold` 후보를 본문에서 확정 인물처럼 쓰지 않는다.
- operational profile의 `3-1. Policy Guard`는 상위 summary가 덮어쓰지 않는다.

## 4. 이름 / 명칭 정규화

작성 목표:

- 표면명, 작업명, legacy name, collision name을 분리한다.
- 최종 설정집에 들어갈 이름과 보류 이름을 구분한다.

Primary source:

- `workflow/05_Naming_Normalization_Map.md`
- `workflow/12_Naming_Tone_Guide.md`
- `working/crosswalks/Name_Normalization_Draft.md`
- `working/crosswalks/Faction_Naming_Replacement_Register.md`

Secondary source:

- `audit/Section_15_Named_Notables_Name_Collision_Register.md`

Required sections:

1. naming policy.
2. collision handling.
3. faction display name.
4. legacy name quarantine.

## 5. 아이템 / 유물 / 욕망 구조

작성 목표:

- item 후보를 단순 목록이 아니라 욕망, 기능, canon tier, collision risk로 정리한다.
- item은 후보표가 안정된 뒤 백과 항목으로 승격한다.

Primary source:

- `workflow/07_Item_Canon_Schema.md`
- `workflow/08_Item_Desire_Design.md`
- `working/crosswalks/Item_Candidate_Register.md`
- `working/crosswalks/Item_Longterm_Taxonomy.md`

Secondary source:

- `working/drafts/Item_Collection_Findings.md`
- `working/crosswalks/Item_Name_Collision_Register.md`

Guard:

- `working/crosswalks/Extracted_Item_Candidates.md`는 현재 별도 작업 파일이므로, 직접 편집하지 않고 참조만 한다.

## 6. 종족 / 영물 / Species Framework

작성 목표:

- 종족과 영물 항목을 tone, canon tier, overread risk로 분리한다.
- 종족명은 멋진 이름보다 작품 톤과 서사 기능을 우선한다.

Primary source:

- `working/crosswalks/Race_Species_Term_Crosswalk.md`
- `working/drafts/Race_Species_Evidence_Log.md`
- `audit/Species_Framework_Risk_Register.md`

Required sections:

1. race/species term policy.
2. evidence log.
3. overread risk.
4. future canon promotion path.

## 7. 공간 / 지도 / 이동감

작성 목표:

- 지도 작업을 세계 -> 대륙 -> 도시 -> 건물 순으로 붙인다.
- 이동감, 항로, 도시 기능, 장소 기능을 설정집 appendix로 정리한다.

Primary source:

- `workflow/10_Spatial_Map_Progression.md`
- `working/drafts/Spatial_Backlog.md`
- `working/drafts/Crossroad_Cities_Map_Seed.md`
- `working/drafts/Crossroad_Cities_Ops_Matrix.md`

Secondary source:

- `audit/FS_Place_Function_Register.md`
- `audit/FS_Travel_Logistics_Register.md`

## 8. Register Appendix

작성 목표:

- 본문에서 길어지는 검증표를 appendix로 빼서 유지한다.
- register는 본문 authority를 보강하지만, 독자용 본문처럼 풀어쓰지 않는다.

Primary source:

- `audit/FS_*_Register.md`
- `audit/Section_14_15_Boundary_Verification_Queue.md`
- `audit/Section_15_Candidate_Register.md`
- `reference/manifests/factions_manifest.md`
- `reference/manifests/heroes_manifest.md`

## Next Fill Order

1. `0. 운영 원칙 / Canon Policy` 본문 1차 작성.
2. `1. 5대륙 개요` 본문 1차 작성.
3. `2. 세력 아카이브 구조` 본문 1차 작성.
4. `3. People Worth Seeking` 본문 1차 작성.
5. `4~8`은 위 네 장의 terminology가 안정된 뒤 채운다.

## Conductor Decision

이 skeleton은 설정집 재조합의 실제 작업 시작점이다.

다음 배치에서는 `0. 운영 원칙 / Canon Policy`를
짧은 본문 초안으로 채우되,
새 canon을 만들지 않고 source priority와 canon tier만 설명한다.

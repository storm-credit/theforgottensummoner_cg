# Section 15 Index Draft

이 문서는 `15. 인물백과`의 열람용 인덱스 초안이다.

이 단계에서는 live 폴더나 원본 문서를 바꾸지 않는다.
이 문서는 `cg` 안에서 라우팅과 열람 순서를 점검하기 위한 설계도다.

index draft reading은
`Section_15_Named_Notables_Status_Compass.md`,
`Section_15_Named_Notables_Register.md`,
`Section_15_Group_Index.md`,
`Section_15_Profile_Draft_Index.md`,
`Section_15_Subline_Register.md`,
`Section_15_Folder_Structure_Draft.md`,
`Section_15_Folder_Draft_Routing_Plan.md`,
`Section_15_Folder_Revision_Gate.md`,
`Section_15_Named_Notables_Name_Collision_Register.md`,
`Section_14_15_Boundary_Verification_Queue.md`,
`Continuous_Workstream.md`
기준으로 읽는다.

## Top-Level Reading Order

1. `15-A. People Worth Seeking`
2. `15-B. Operational Lines`
3. `15-C. Need Named Candidate Slots`
4. `14/15 Boundary Holds`
5. `Name Collision Watch`

## 15-A. People Worth Seeking

안정 후보:

| Name | Route | State |
|---|---|---|
| `울프가르 드래곤포지` | `크림슨 / 용의 후예 / 드래곤포지 공방` | `named_notable_candidate / stable_15_workset / route_hierarchy_locked / grade_caution` |
| `에리온 드라코비스` | `크림슨 / 엘드라칸 / 학술-전승층` | `named_notable_candidate / stable_15_workset / route_hierarchy_locked / grade_caution / name_collision_watch` |
| `오그마` | `크림슨 / 엘드라칸 / 전승 보관층` | `named_notable_candidate / stable_15_workset / route_hierarchy_locked / act_watch` |
| `엘다라` | `에테르 / 정령연합 / 루미라` | `source_check_hold / hold reference split` |
| `실비아` | `범대륙 후기 확장 / 키르케 영약회` | `deferred_expansion_hold / hold reference split / name_collision_watch` |

People Worth Seeking guard:

- `크림슨` 대표 카드군은 씨족 중심 질서와 현자/장인/전승 thin-support만 보강하며, 전통 귀족국가형 `state_house strong` 근거로 올리지 않는다.
- `엘다라`는 정령연합 내부 예외축 hold reference split 안의 `source_check_hold / hold reference split`로만 유지하고 에테르 전체 부족층 일반화 근거로 쓰지 않는다.
- `실비아`는 5대륙 본선이 아니라 `범대륙 후기 확장 / deferred_expansion_hold / hold reference split`로만 유지한다.

## 15-B. Operational Lines

이 축은 유명 NPC 개인이 아니라,
도시와 조직의 실무층을 보여주는 보조 색인이다.

현재 주요 묶음:

- `Hidden Exchange`
- `Ironblood`
- `Black Skull`
- `Shadow Field Network`
- `Iron Finance Field`
- `Trade Broker Ring`
- `Mercenary Operations`
- `Silent Market Undercurrent`

운영 원칙:

- 이름은 판타지 표면명 후보로 계속 낮춘다.
- 현대 범죄/기업물 어휘는 정본명으로 쓰지 않는다.
- 개별 named holder가 확인되기 전까지는 `People Worth Seeking`이 아니라 Operational Lines reference로만 둔다.
- `Operational_Display_Guard_Audit.md` 기준으로 현재 표면명 후보는 대체로 reference 유지 가능하다.
- reference backlog 후보는 `밤그물 첩보망`, `회랑 운반자`, `환영 집행관` 계열이다.

Operational Lines guard:

- 자유도시 shadow-market cluster는 `urban_market / shadow_port / debt-enforcement` 축으로만 읽고, 해양 `토착 공동체층` 근거와 섞지 않는다.
- `철의 금융 연맹`, `그림자 첩보망`, `침묵의 상회`, `거울방` 계열은 `nontraditional elite thin-support` 또는 `dark institution` 범위에서만 읽는다.
- 이 operational guard 문장은 lower-card authority를 따르며,
`People Worth Seeking` 승인 논리로 역수입하지 않는다.
- 이 인덱스는 cluster type을 분류만 하고,
  정확한 operational guard 문구 권한은 각 `Section_15_Profile_*` 카드의 `3-1. Policy Guard`에 남긴다.
- 다시 말해 exact operational guard wording authority는 하위 profile 카드에 있고,
  이 인덱스는 그 wording source를 reference로만 읽는다.
- subline 확장까지 내려간 경우에도
  exact operational guard wording authority는 각 `Section_15_Subline_Profile_*` 카드의
  `3-1. Policy Guard`에 남고, 이 인덱스는 그 wording source를 reference로만 읽는다.
- representative `Port Authority / Black Auction / Gravewell / Counterfeit Workshop` pair는
  닫힌 subline 교차감사 샘플로 유지하고,
  이 인덱스는 그 closure 상태를 상위 열람층에서만 참조한다.

## 15-C. Need Named Candidate Slots

개인명이 아직 없는 유명 NPC 슬롯:

| Area | Slot Index |
|---|---|
| `에테르` | `Section_15_Ether_Need_Named_Candidate_Index.md` |
| `프로스트` | `Section_15_Frost_Need_Named_Candidate_Index.md` |
| `해양` | `Section_15_Oceanic_Need_Named_Candidate_Index.md` |
| `오벨리스크` | `Section_15_Obelisk_Need_Named_Candidate_Index.md` |


현재 Ether 메모:

- `Section_15_Ether_Place_Institution_Sidecar.md` 기준 표면명 기본값은 잠겼다.
- `탑서기`, `왕실 의전서기`, `성벽 설계서기`, `상단 조율관`, `항만 인장관`, `탐사 기록관`, `연구소 보존관`은 read-only pass에서 direct holder를 못 찾아 role slot 유지로 잠갔다.
- `대현자 보좌 기록관`은 direct holder를 못 찾았고, `엘다라`나 `엘라라 문힘`에 덮어씌우지 않기로 잠갔다.
- `침묵의 감시자`는 개인명 아니라 `Silent Watchers` 집단 직함으로만 확인돼 role slot 유지로 잠갔다.
- 따라서 Ether low-priority auxiliary slot 9개 read-only closure는 완료됐다.
- 세부 확인 큐는 `Section_15_Ether_Need_Named_Candidate_Index.md`, `Section_15_Ether_Named_Candidate_Search_Queue.md`를 따른다.
원칙:

- 이름을 발명하지 않는다.
- 장소-기관 앵커를 먼저 보존한다.
- 14 신호를 확인하기 전에는 15 후보로 올리지 않는다.

## 14/15 Boundary Holds

현재 보류 후보는 아래 문서들을 우선 본다.

- `Section_15_Five_Continent_Closure_Table.md`
- `Section_15_Named_Notables_Status_Compass.md`
- `Section_14_15_Boundary_Verification_Queue.md`
- `Section_8_to_15_Notable_Anchor_Bridge.md`

판정 원칙:

- SS/S/A급, Act 중심성, 제독/단장/탑주/원로단 지도부 신호가 있으면 15 확정 금지.
- 전설 영웅록 출처는 무조건 `verify_before_15`.
- 이미 14 독립 파일이 확인되면 `keep_14`.

## Name Collision Watch

현재 병합 금지 클러스터:

- `실비아`
- `Aegis / 아이기스`
- `Mera / 메라`
- `Ravenfell`
- `Sylas / 실라스`
- `Selena / 셀레나`
- `Valerius`
- `Drake Ruga / Rawson`

기준 문서:

- `Section_15_Named_Notables_Name_Collision_Register.md`
- `workflow/05_Naming_Normalization_Map.md`

## Conductor Decision

15번은 지금 `read-only closure sync / watch-reference` 단계로 유지한다.

현재 메인 본선은 `8번 세력 아카이브` 재점검이나
stable triad package 재가동이 아니라,
이 인덱스 초안과 상태 나침반이 이미 닫힌 closure sync / carryover wording을
같은 authority 분리 문장으로 mirror하는 것이다.

People Worth Seeking index는 상위 요약층으로만 읽고,
operational profile의 `3-1. Policy Guard`는 하위 카드층에 그대로 남겨 둔다.
따라서 People Worth Seeking summary는 operational profile guard 문장을 다시 써서 대체하지 않는다.
exact operational guard wording authority 역시 상위 index 문서가 아니라
각 `Section_15_Profile_*` 카드의 `3-1. Policy Guard`에 남는다.
subline 확장까지 내려간 경우에도
exact operational guard wording authority는 각 `Section_15_Subline_Profile_*` 카드의
`3-1. Policy Guard`에 남는다.

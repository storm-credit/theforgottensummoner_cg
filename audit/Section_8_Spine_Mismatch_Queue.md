# Section 8 Spine Mismatch Queue

이 문서는 `Section 8` 루트 정규화에서
대륙 spine과 구조 해석이 어긋날 위험이 큰 후보를 먼저 모으는 큐다.

## Input Locks

- `audit/Section_8_Root_Findings.md`
- `audit/Section_8_Root_Normalization_Plan.md`
- `audit/Section_8_Standard_Spine.md`
- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Section_8_Status_Vocabulary_Guard.md`
- `audit/Ether_Core_Faction_Layers.md`
- `audit/Section_8_Crimson_Notable_Anchor_Audit.md`
- `audit/Frost_Core_Faction_Layers.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Obelisk_Core_Faction_Layers.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_A.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_B.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_C.md`
- `audit/Section_8_Root_Corruption_First_Pass_A.md`
- `audit/Section_8_Place_Network_P2_Queue.md`

## Mismatch Categories

1. `clan_as_state_house`
2. `port_power_as_tribe_clan`
3. `nontraditional_elite_as_state_house`
4. `place_style_flattened_to_section_style`
5. `section_style_forced_on_place_network`

## Watch Queue

| Priority | Candidate / Family | Risk Category | State Snapshot | Closure Source | Reference Owner |
|---|---|---|---|---|---|
| `P0` | `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))` | `root_corruption` | `mismatch_keep` | `Section_8_Root_Corruption_First_Pass_A.md` | `canonical_root / quarantine_root / legacy_root` 분리 유지, 원본 접근 시 subtree sampling으로 실제 비교 |
| `P2` | `바다의 교단`, `오로라 평원`, `빙하의 성소`, `본 마켓` 계열, `잊힌 자들의 연합` pressure family | `section_style_forced_on_place_network` | `watch_keep` | `Section_8_Spine_Mismatch_First_Pass_C.md`, `Section_8_Place_Network_P2_Queue.md` | structure label과 place pressure를 분리한 채 sidecar/register handoff drift만 감시 |

## Round 1 Locked Snapshot

| Priority | Candidate | Risk Category | State Snapshot | Closure Source | Lock Note |
|---|---|---|---|---|---|
| `P1` | `용의 후예` | `clan_as_state_house` | `mismatch_keep` | `Section_8_Spine_Mismatch_First_Pass_B.md` | 씨족 상층을 국가형 가문층으로 과승격하지 않는다 |
| `P1` | `붉은 사막 부족 연합` | `clan_as_state_house` | `mismatch_keep` | `Section_8_Spine_Mismatch_First_Pass_B.md` | 부족장 상층을 곧바로 `state_house strong`으로 올리지 않는다 |
| `P1` | `프로스트본 연합` | `clan_as_state_house` | `mismatch_keep` | `Section_8_Spine_Mismatch_First_Pass_A.md` | 클랜 정치와 정주 귀족 질서를 분리해 읽는다 |
| `P1` | `해적 연합` | `port_power_as_tribe_clan` | `mismatch_keep` | `Section_8_Spine_Mismatch_First_Pass_A.md` | 항만 권력과 토착 공동체를 분리해 읽는다 |
| `P1` | `바다의 교단` | `port_power_as_tribe_clan` | `mismatch_keep` | `Section_8_Spine_Mismatch_First_Pass_B.md` | 성지/신앙 압력과 `tribe_clan` 증거를 분리한다 |
| `P1` | `망자의 왕국` | `nontraditional_elite_as_state_house` | `mismatch_keep` | `Section_8_Spine_Mismatch_First_Pass_B.md` | 비정통 엘리트 구조를 전통 귀족국가로 과승격하지 않는다 |
| `P1` | `잊힌 자들의 연합` | `nontraditional_elite_as_state_house` | `mismatch_keep` | `Section_8_Spine_Mismatch_First_Pass_A.md` | 가문 폴더와 귀족국가 해석을 분리한다 |
| `P1` | `봉인 수호단` | `place_style_flattened_to_section_style` | `mismatch_clear` | `Section_8_Spine_Mismatch_First_Pass_B.md` | mismatch mainline에서는 내리고 `place_pressure_strong` 메모만 유지한다 |

## Conductor Rules

- `씨족`, `부족장`, `클랜 상층`은 자동으로 `state_house strong`으로 올리지 않는다.
- `항만`, `함대`, `해상 귀족`, `해적 가문`, `교단 권위`는 자동으로 `tribe_clan` 근거로 올리지 않는다.
- `가문`, `귀족`, `왕국` 표현이 보여도 오벨리스크에서는 먼저 `nontraditional elite`인지 본다.
- `place pressure strong` 후보는 구조 라벨을 바꾸기 전에 sidecar/register handoff를 먼저 본다.

## Follow-up Pass Snapshot

1. `P1` 후보의 1차 closure는 완료했고, 이 문서에서는 watch queue와 locked snapshot을 분리해 유지한다.
2. 현재 watch mainline은 `P0 root_corruption`과 `P2 section_style_forced_on_place_network` family만 남긴다.
3. `P0`는 `Section_8_Root_Corruption_First_Pass_A.md`와 `Section_8_Root_Subtree_Sampling_Queue.md` 기준으로 이어간다.
4. `P2`는 `Section_8_Place_Network_P2_Queue.md`, `Section_8_Place_Network_Handoff_Map.md` 기준으로 sidecar/register drift만 본다.
5. 새 `P1` 후보를 늘리기 전에는 `Section_8_Normalization_Status_Compass.md`와 status vocabulary를 먼저 동기화한다.
6. missing-layer component set은 `Five_Continent_Missing_Layer_Master_Lock.md` 아래 closeout reference로 보고,
   이 queue는 새 evidence 전까지 `P0 / P2` watch만 우선한다.

## Conductor Decision

이 문서는 `Section 8` 구조 정규화에서
잘못된 평탄화와 성급한 해석 승격을 막는 mismatch 장부다.

이 기준에서는 `새 P1 후보 발굴`보다
이미 잠근 `P1 closure`와 남은 `P0 / P2 watch queue`를
명확히 분리해서 유지하는 데 사용한다.

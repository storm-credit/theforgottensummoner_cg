# Section 8 Normalization Status Compass

이 문서는 현재 `Section 8` closure sync / watch-reference 본선이
어디까지 잠겼는지 한 장으로 보는 상태표다.

## Input

- `audit/Section_8_Root_Findings.md`
- `audit/Section_8_Root_Label_Map.md`
- `audit/Section_8_Root_Normalization_Plan.md`
- `audit/Section_8_Standard_Spine.md`
- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Mixed_Exception_Review_Queue.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_A.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_B.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_C.md`
- `audit/Section_8_Root_Corruption_First_Pass_A.md`
- `audit/Section_8_Root_Subtree_Sampling_Queue.md`
- `audit/Section_8_Place_Network_P2_Queue.md`
- `audit/Section_8_Place_Network_Handoff_Map.md`
- `audit/Section_8_Frost_Notable_Anchor_Audit.md`
- `audit/Section_8_Status_Vocabulary_Guard.md`
- `audit/Section_8_Mainline_Sync_Register.md`
- `audit/Section_8_15_Closure_Sync_Carryover_Watch.md`
- `audit/Five_Continent_Missing_Layer_Master_Lock.md`
- `audit/Section_15_Profile_Draft_Index.md`
- `audit/Section_15_Subline_Register.md`
- `audit/Section_15_Oceanic_Place_Institution_Sidecar.md`
- `audit/Section_15_Frost_Place_Institution_Sidecar.md`
- `audit/Section_15_Obelisk_Place_Institution_Sidecar.md`
- `audit/FS_Place_Function_Register.md`

## Stage Snapshot

- `5대륙 Section 8 spine sample`: `closed_round1`
- `root label map`: `locked`
- `structure label first pass`: `locked_for_mainline`
- `mixed review round1`: `closed_round1`
- `spine mismatch round1`: `closed_round1`
- `root corruption first pass`: `locked`
- `subtree sampling prep`: `ready_when_source_available`
- `place-pressure P2 queue`: `locked` (`section_style_forced_on_place_network` legacy risk key)
- `place-pressure handoff`: `applied_round1` (`section_style_forced_on_place_network` legacy risk key)
- `section8_to_15 closure sync watch`: `watch_mainline`
- `five_continent_missing_layer_master_lock`: `closed_component_set`

## Root Status

| Root | State | Note |
|---|---|---|
| `01-8. 세력 아카이브 (국가·조직 정리).md` | `canonical_root` | 본문 인덱스 |
| `1~5 대륙` | `canonical_root` | 대륙 본체 루트 |
| `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)` | `canonical_root` | 범대륙 활성 입력 |
| `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))` | `quarantine_root` | 손상/중복 경로 |
| `_Legacy_중립세력 (Backup)` | `legacy_root / reference-only` | 비교/참고 전용 |

## Structure Label Snapshot

| Candidate | Current Structure Label | Status |
|---|---|---|
| `성국` | `section_style` | `stable_sample` |
| `왕국연합` | `section_style` | `stable_sample` |
| `정령연합` | `mixed_keep` | `exception_locked` |
| `용의 후예` | `section_style` | `watch_keep` |
| `붉은 사막 부족 연합` | `mixed_keep` | `exception_locked` |
| `프로스트본 연합` | `mixed_keep` | `exception_locked` |
| `황금 함대` | `section_style` | `stable_sample` |
| `해적 연합` | `mixed_keep` | `exception_locked` |
| `바다의 교단` | `section_style_reclassify` | `place_pressure_strong` |
| `망자의 왕국` | `section_style_reclassify` | `place_pressure_strong` |
| `잊힌 자들의 연합` | `section_style_reclassify` | `watch_keep` |
| `봉인 수호단` | `section_style_reclassify` | `place_pressure_strong` |

## Mixed Review Snapshot

| Candidate | Round 1 Result | Note |
|---|---|---|
| `정령연합` | `mixed_keep` | 에테르 특수축 |
| `붉은 사막 부족 연합` | `mixed_keep` | 부족 연합 + 생존 시장 병행 |
| `프로스트본 연합` | `mixed_keep` | 클랜 정치 + 장소 네트워크 병행 |
| `해적 연합` | `mixed_keep` | 파벌 구조 + 항만/섬/암시장 네트워크 병행 |
| `잊힌 자들의 연합` | `section_style_reclassify` | 구조는 section형, 내용은 생존 연합 축 |

## Mismatch Snapshot

| Candidate / Family | Risk | Round 1 Result | Note |
|---|---|---|---|
| `용의 후예` | `clan_as_state_house` | `mismatch_keep` | 씨족 상층 과승격 금지 |
| `붉은 사막 부족 연합` | `clan_as_state_house` | `mismatch_keep` | 부족 상층 과승격 금지 |
| `프로스트본 연합` | `clan_as_state_house` | `mismatch_keep` | 클랜 상층 과승격 금지 |
| `해적 연합` | `port_power_as_tribe_clan` | `mismatch_keep` | 항만 권력과 토착 공동체 분리 |
| `바다의 교단` | `port_power_as_tribe_clan` | `mismatch_keep` | 성지/신앙과 tribe 근거 분리 |
| `망자의 왕국` | `nontraditional_elite_as_state_house` | `mismatch_keep` | 기억 귀족 과승격 금지 |
| `잊힌 자들의 연합` | `nontraditional_elite_as_state_house` | `mismatch_keep` | 가문 폴더와 귀족국가 분리 |
| `봉인 수호단` | `place_style_flattened_to_section_style` | `mismatch_clear` | flattening 증거 없음 |
| `Supranational & 마립` broken root | `root_corruption` | `mismatch_keep` | 손상 루트 격리 유지 |
| `place-pressure family` | `section_style_forced_on_place_network` | `watch_keep` | place pressure와 구조 라벨 분리 |

## Place Pressure Handoff Snapshot

| Candidate / Family | Current Structure Read | Pressure State | Handoff State | Current Target |
|---|---|---|---|---|
| `바다의 교단` | `section_style_reclassify` | `place_pressure_strong` | `handoff_applied` | `Section_15_Oceanic_Place_Institution_Sidecar.md` |
| `오로라 평원` | `anchor-led place pressure` | `place_pressure_strong` | `handoff_applied` | `Section_15_Frost_Place_Institution_Sidecar.md`, `Section_8_Frost_Notable_Anchor_Audit.md` |
| `빙하의 성소` | `anchor-led place pressure` | `place_pressure_strong` | `handoff_applied` | `Section_15_Frost_Place_Institution_Sidecar.md`, `Section_8_Frost_Notable_Anchor_Audit.md` |
| `본 마켓` 계열 | `section-linked place pressure` | `place_pressure_strong` | `handoff_applied` | `Section_15_Obelisk_Place_Institution_Sidecar.md` |
| `잊힌 자들의 연합` | `section_style_reclassify` | `place_pressure_strong + exile_network_pressure` | `handoff_applied` | `FS_Place_Function_Register.md` |

## Conductor Lock

현재 이 본선에서 유지할 lock:

1. 새 후보를 늘리기보다 지금 잠근 결과를 충돌 없이 유지한다.
2. `canonical_root / quarantine_root / legacy_root`를 활성 판단에서 섞지 않는다.
3. `place pressure strong`과 `structure label`을 같은 것으로 취급하지 않는다.
4. 원본 경로 접근이 가능해지면 `Section_8_Root_Subtree_Sampling_Queue.md` 기준으로 `S1 -> S2 -> S3` reference sampling 필요 여부만 판단한다.
5. 그 전까지는 `P2` 후보를 새로 늘리지 않고 현재 handoff가 sidecar/register에서 drift 없이 유지되는지 본다.
6. `Section 8 -> 15`는 새 후보를 늘리기보다 `closure sync / watch-reference`가 summary, bridge, queue에서 같은 현재 시점을 가리키는지 먼저 본다.
7. `1~5 대륙 결손층 5개`는 `Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 따라,
   thin/support 범위와 evidence/firewall 순서를 넘겨 읽지 않는다.
   이 compass의 stage label은 component shorthand일 뿐,
   결손층 authority를 master lock 밖으로 옮기지 않는다.
8. `Section_15_Subline_Profile_*` 카드의 `3-1. Policy Guard`는 exact wording source로 유지하고,
   상위 summary / bridge / watch 문서가 이를 재정의하지 않는지 함께 본다.
9. representative `Port Authority / Black Auction / Gravewell / Counterfeit Workshop` pair는
   닫힌 subline 교차감사 샘플로 유지하고,
   새 drift가 생길 때만 국소 재대조한다.

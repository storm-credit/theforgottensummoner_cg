# Section 8 / 15 Closure Sync Watch-Reference

이 문서는 오케스트라 메인 본선 reference인
`5대륙 closure sync / Section 8 -> 15 watch-reference`를
한 장으로 잠그는 감시 문서다.

목적:

- 이미 닫힌 판정을 다시 열지 않고, summary / bridge / queue / package 문서가 같은 기준 시점을 가리키게 한다.
- `stable triad package freeze`, `source_check_hold / hold reference split`, `deferred_expansion_hold / hold reference split`, Ether hold cluster, P2 place-pressure handoff를 서로 다른 층으로 유지한다.
- `Section 8` 구조 라벨과 `Section 15` 후보 상태가 서로를 덮어쓰지 않게 한다.

## Input

- `audit/Section_8_Normalization_Status_Compass.md`
- `audit/Section_8_15_Spine_Compatibility_Audit.md`
- `audit/Section_8_Mainline_Sync_Register.md`
- `audit/Section_8_to_15_Notable_Anchor_Bridge.md`
- `audit/Section_15_Stable_Candidate_8_Anchor_Index.md`
- `audit/Section_15_Named_Notables_Status_Compass.md`
- `audit/Section_15_Five_Continent_Closure_Table.md`
- `audit/Section_15_Actual_Draft_Package_Freeze.md`
- `audit/Section_15_Ether_Hold_Cluster_Continuation.md`
- `audit/Section_15_Ether_Tower_Saint_Hold_Continuation.md`
- `audit/Section_15_Ether_Spirit_Union_Hold_Continuation.md`
- `audit/Next_Sequential_Workstream.md`
- `audit/Audit_Queue.md`

## Mainline Lock Snapshot

1. `stable triad actual draft package freeze`는 닫힌 상태로 유지한다.
2. `엘다라 [source_check_hold / hold reference split]`, `실비아 [deferred_expansion_hold / hold reference split]`는 triad package 밖 hold reference split으로만 유지한다.
3. Ether hold cluster는 `library_core_hold / archive_admin_hold / tower_seer_hold / bardic_archive_hold`, `white_tower_barrier_hold / abyss_blood_taboo_hold / shadow_intelligence_hold / holy_barrier_hold`, `great_druid_hold / spirit_envoy_hold / shadow_crow_hold`까지 한 번 closure 상태로 본다.
4. `P2 place-pressure handoff`는 candidate index가 아니라 sidecar/register를 주 기록처로 유지한다.
5. 메인 본선 reference는 새 후보 창출이 아니라 `5대륙 closure sync / Section 8 -> 15 watch-reference`다.
6. 카드층 `Policy Guard`는 summary / bridge / index / folder / routing 문서까지 반영하되,
   exact wording source로 승격하지 않는다.
7. canonical state drift와 policy carryover drift는 서로 다른 층으로 점검한다.
8. People Worth Seeking 카드와 operational profile card의 lower-card authority는 분리 유지한다.
9. operational middle-layer는 family-level carryover만 요약하고,
   exact wording source는 실제 profile/subline profile 카드의 `3-1. Policy Guard`에 남긴다.
10. 대표 `subline draft / subline profile` 교차감사
    (`Black Auction / Port Authority / Gravewell / Counterfeit Workshop`)는
    closure 상태로 유지하고, 새 drift가 생길 때만 국소 재개한다.
11. stable candidate / package freeze / compatibility audit도
    각 `Section_15_Profile_*` 카드의 `3-1. Policy Guard`를
    exact wording source로 읽고,
    subline 확장까지 내려간 경우에는 각 `Section_15_Subline_Profile_*` 카드의
    `3-1. Policy Guard`를 exact wording source로 읽으며,
`People Worth Seeking` 승인 논리로 역수입하지 않는다.
12. `결손층 5개`의 thin/support 판정은 이 watch 문서가 새로 확정하지 않고,
    `audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 참조한다.
13. `Five_Continent_Missing_Layer_Master_Lock.md` 아래 component set은
    closeout 완료 상태로 보고,
    새 evidence가 들어오기 전까지는 root / structure / mismatch / P2 handoff watch를 우선한다.

## Watch Table

| Watch Family | Snapshot State | Primary Source | Drift Risk | Rule |
|---|---|---|---|---|
| `stable triad package` | `closed_and_frozen` | `Section_15_Actual_Draft_Package_Freeze.md` | freeze를 다시 본선처럼 여는 것 | wording 정리 외 재개 금지 |
| `source_check_hold / hold reference split`, `deferred_expansion_hold / hold reference split` | `separated_from_triad` | `Section_15_Stable_Candidate_8_Anchor_Index.md` | triad package와 hold reference split 혼용 | `source_check_hold / hold reference split`, `deferred_expansion_hold / hold reference split`만 사용 |
| `Ether hold clusters` | `closed_round1_for_watch` | `Section_15_Ether_Hold_Cluster_Continuation.md`, `Section_15_Ether_Tower_Saint_Hold_Continuation.md`, `Section_15_Ether_Spirit_Union_Hold_Continuation.md` | 이미 닫힌 hold를 계속 next batch처럼 적는 것 | 새 증거 전까지 closure 상태 유지 |
| `Section 8 carryover` | `bridge_locked` | `Section_8_to_15_Notable_Anchor_Bridge.md`, `Section_8_15_Spine_Compatibility_Audit.md` | 구조 라벨과 후보 상태 혼용 | structure label과 place pressure 분리 |
| `lower-card authority` | `separated_and_respected` | `Section_15_Named_Notables_Register.md`, `Section_15_Profile_Draft_Index.md`, `Section_15_Profile_*`, `Section_15_Subline_Profile_*` | 상위 summary가 하위 `3-1. Policy Guard`를 재정의하는 것 | register/index는 비교 문서로만 쓰고, exact wording source는 각 profile/subline profile 카드에 남긴다 |
| `P2 place-pressure` | `handoff_applied` | `Section_8_Place_Network_Handoff_Map.md` | candidate index나 summary에 place owner를 재정의하는 것 | owner는 sidecar/register만 가진다 |
| `root / deferred axis` | `guarded` | `Section_8_Normalization_Status_Compass.md` | 범대륙 후기 확장을 메인 본선처럼 재상승 | deferred routing만 유지 |
| `missing-layer master lock` | `closed_component_set` | `Five_Continent_Missing_Layer_Master_Lock.md` | component shorthand가 단일 entry authority처럼 재상승하는 것 | master lock 아래 component set으로만 유지 |

## Immediate Drift Triggers

아래 경우에는 이 watch 문서를 기준으로 closure sync를 다시 돈다.

1. stable triad package가 다시 `next batch`나 `active build`처럼 적힐 때
2. `source_check_hold / hold reference split`나 `deferred_expansion_hold / hold reference split`가 triad package 안으로 다시 섞일 때
3. Ether hold cluster가 closure 상태가 아니라 active discovery처럼 적힐 때
4. `Section 8` 구조 라벨이 `Section 15` 상태 라벨처럼 오독될 때
5. `P2 place-pressure` 기록처가 sidecar/register 밖에서 다시 재정의될 때
6. `Audit_Queue.md`, `Next_Sequential_Workstream.md`, `Status Compass`가 서로 다른 본선 reference를 가리킬 때
7. 카드층 `Policy Guard`와 `Section 15` index/folder/routing 문서의 carryover 문장이 다시 어긋날 때
8. canonical state가 prose guard 문장으로 대체되거나, 반대로 prose guard가 state label처럼 오기입될 때
9. operational profile guard 문장이 `People Worth Seeking` 승인 논리로 역수입될 때
10. subline draft와 각 `Section_15_Subline_Profile_*` 카드의 `3-1. Policy Guard` 문장이 서로 어긋날 때

## Ordered Cycle

오케스트라는 아래 순서로 같은 점검 사이클을 반복한다.

1. `Section_8_Normalization_Status_Compass.md`에서 `root / structure / mismatch / P2 handoff` snapshot 상태를 먼저 확인한다.
2. `Section_15_Named_Notables_Status_Compass.md`, `Section_15_Five_Continent_Closure_Table.md`, `Section_15_Named_Notables_Coverage_Matrix.md`에서 summary wording drift를 확인한다.
3. `Section_8_to_15_Notable_Anchor_Bridge.md`, `Section_8_15_Spine_Compatibility_Audit.md`, `Section_15_Stable_Candidate_8_Anchor_Index.md`에서 carryover wording drift를 확인한다.
4. `Section_15_Index_Draft.md`, `Section_15_Folder_Structure_Draft.md`, `Section_15_Folder_Draft_Routing_Plan.md`, `Section_15_Folder_Revision_Gate.md`, `Section_15_Named_Notables_Anchor_Map.md`, `Section_15_Stable_Candidate_Profile_QA.md`에서 policy carryover drift를 확인한다.
5. `Section_15_Profile_Draft_Index.md`, `Section_15_Operational_Lines_Track.md`, `Section_15_Operational_Display_Canon_Candidates.md`, `Section_15_Intake_Structure.md`에서 operational profile layer의 `3-1. Policy Guard` 형식 drift를 확인한다.
6. `Section_15_Ether_Hold_Cluster_Continuation.md`, `Section_15_Ether_Tower_Saint_Hold_Continuation.md`, `Section_15_Ether_Spirit_Union_Hold_Continuation.md`에서 hold cluster가 closure 상태로 유지되는지 확인한다.
7. `Section_8_Place_Network_Handoff_Map.md`와 sidecar/register owner를 대조해 `P2 place-pressure` owner drift가 없는지 확인한다.
8. `Audit_Queue.md`, `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`에서 본선 reference가 같은 순서로 적혀 있는지 확인한다.
9. `Section_15_Named_Notables_Register.md`와 `Section_15_Profile_Draft_Index.md`를 대조해 lower-card authority가 summary에 재정의되지 않는지 확인한다.
10. `Section_15_Subline_Draft_*`와 `Section_15_Subline_Profile_*`는
    대표 짝 교차감사가 이미 닫힌 상태로 읽고,
    wording-source drift가 생길 때만 국소 대조한다.
11. 위 1~10이 모두 잠긴 뒤에만 신규 closure batch 후보나 subtree sampling 재개 필요 여부를 판단한다.
12. missing-layer component set은 closeout reference로만 보고,
    새 evidence 전까지는 `root / structure / mismatch / P2 handoff` snapshot을 먼저 본다.

## Conductor Checklist

변경 후 최소 확인 문서:

1. `Section_8_Normalization_Status_Compass.md`
2. `Section_8_15_Spine_Compatibility_Audit.md`
3. `Section_8_Mainline_Sync_Register.md`
4. `Section_8_to_15_Notable_Anchor_Bridge.md`
5. `Section_15_Stable_Candidate_8_Anchor_Index.md`
6. `Section_15_Named_Notables_Status_Compass.md`
7. `Section_15_Five_Continent_Closure_Table.md`
8. `Next_Sequential_Workstream.md`
9. `Audit_Queue.md`
10. `Section_8_Place_Network_Handoff_Map.md`
11. `Section_15_Profile_Draft_Index.md`
12. `Section_15_Operational_Lines_Track.md`
13. `Section_15_Named_Notables_Register.md`

## Conductor Decision

오케스트라는
`새 후보 발굴`보다
`이미 잠근 판정이 같은 authority 분리 문장으로 유지되는가`를 먼저 본다.

즉 메인선 reference는
`5대륙 closure sync / Section 8 -> 15 watch-reference`
유지다.

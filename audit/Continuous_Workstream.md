# Continuous Workstream

이 문서는 오케스트라가
무엇을 메인 본선 reference로 유지하는지와
어떤 순서로 drift를 점검하는지 보여주는 연속 진행 기준서다.

## Mainline Reference

메인 본선 reference는
`5대륙 closure sync / Section 8 -> 15 watch-reference`
유지다.

즉 새 후보 발굴이나 triad package 재개방보다
이미 잠근 구조 라벨, hold state, carryover wording,
P2 owner가 같은 기준 시점을 가리키는지를 먼저 본다.

## Mainline Lock

총괄 기준은 아래처럼 잠근다.

1. `Section 8`의 `canonical_root / quarantine_root / legacy_root` 경계를 유지한다.
2. `Section 8`의 `section_style / mixed_keep / section_style_reclassify` 구조 라벨을 유지한다.
3. `Section_8_Spine_Mismatch_Queue.md`의 `P1 locked snapshot`과 `P0 / P2 watch queue` 분리를 유지한다.
4. `Section 8 -> 15` carryover는 `structure label`, `hold state`, `place pressure`를 서로 덮어쓰지 않게 유지한다.
5. `P2 place-pressure handoff` owner는 candidate index가 아니라 sidecar/register에만 둔다.
6. `stable triad package`, `source_check_hold / hold reference split`, `deferred_expansion_hold / hold reference split`, Ether hold cluster는 서로 다른 층으로 유지한다.
7. 카드층 `Policy Guard`와 `Section 15` status/index/folder/routing/anchor-map/stable-candidate-QA 문서의 family-level carryover 문장을 같은 해석선으로 유지한다.
8. canonical state와 prose carryover guard는 같은 것이 아니며, 둘을 서로 대체하지 않는다.
9. operational profile layer는 `Section_15_Profile_Template.md`의 `3-1. Policy Guard` 형식을 유지한 채 상위 watch 문서와 연결한다.
10. 상위 summary / bridge / queue는 lower-card authority를 요약만 하고,
   operational profile 카드의 `3-1. Policy Guard`를 재정의하지 않는다.
11. operational middle-layer (`Group Index / Group Draft / Subline Register / Subline Draft`)는
   family-level carryover만 요약하고 exact wording source는 카드 본문에 남긴다.
12. representative `Subline Draft / Subline Profile` pair
    (`Black Auction / Port Authority / Gravewell / Counterfeit Workshop`)는
    wording-source 교차감사가 닫힌 상태로 유지되며, 새 drift가 생길 때만 국소 재개한다.
13. `Section_15_Subline_Profile_*` 카드의 `3-1. Policy Guard`는
    exact wording source로 유지되고,
    상위 summary / bridge / watch 문서는 그 wording source를 참조만 한다.
14. `Five_Continent_Missing_Layer_Master_Lock.md` 아래 component set은
    closeout reference로 유지하고,
    새 evidence 전까지는 `root / structure / mismatch / P2 handoff` watch를 우선한다.
15. named-notables mainline은
    `core hub / live card-template / frozen snapshot-sample` 3층 분리를
    닫힌 기준선으로 유지하고,
    새 local drift가 생길 때만 해당 family를 국소 재개한다.
16. bridge-anchor 인접층과 spine-index 층도
    같은 authority split / master-lock carryover / stable-vs-hold separation 아래
    닫힌 reference 상태로 유지한다.

## Ordered Cycle

오케스트라는 아래 순서를 반복한다.

1. `Section_8_Normalization_Status_Compass.md`에서 `root / structure / mismatch / P2 handoff` 상태를 먼저 확인한다.
2. `Section_15_Named_Notables_Status_Compass.md`, `Section_15_Five_Continent_Closure_Table.md`, `Section_15_Named_Notables_Coverage_Matrix.md`의 summary wording drift를 점검한다.
3. `Section_8_to_15_Notable_Anchor_Bridge.md`, `Section_8_15_Spine_Compatibility_Audit.md`, `Section_15_Stable_Candidate_8_Anchor_Index.md`의 carryover wording drift를 점검한다.
4. `Section_15_Index_Draft.md`, `Section_15_Folder_Structure_Draft.md`, `Section_15_Folder_Draft_Routing_Plan.md`, `Section_15_Folder_Revision_Gate.md`, `Section_15_Named_Notables_Anchor_Map.md`, `Section_15_Stable_Candidate_Profile_QA.md`의 policy carryover drift를 점검한다.
5. `Section_15_Profile_Draft_Index.md`, `Section_15_Operational_Lines_Track.md`, `Section_15_Operational_Display_Canon_Candidates.md`, `Section_15_Intake_Structure.md`의 operational profile `3-1. Policy Guard` drift는 2026-04-13 KST spot-check closed 상태를 유지하는지 점검한다.
6. `Section_15_Ether_Hold_Cluster_Continuation.md`, `Section_15_Ether_Tower_Saint_Hold_Continuation.md`, `Section_15_Ether_Spirit_Union_Hold_Continuation.md`의 closure 상태를 점검한다.
7. `Section_8_Place_Network_Handoff_Map.md`와 sidecar/register를 대조해 `P2 place-pressure` owner drift를 점검한다.
8. `Audit_Queue.md`, `Next_Sequential_Workstream.md`, `Section_8_15_Closure_Sync_Carryover_Watch.md`가 같은 본선 reference를 가리키는지 확인한다.
9. `People Worth Seeking` 승인 논리와 operational profile guard 문장이 서로 역수입되지 않는지 확인한다.
10. representative subline draft/profile pair는 닫힌 교차감사 결과를 유지하고,
    새 wording-source drift가 생길 때만 해당 pair를 국소 교차감사한다.
11. `subline_profile_authority` sync group이
    `Section_15_State_Vocabulary_Guard.md`, `Section_8_Mainline_Sync_Register.md`,
    summary / bridge / watch 문서에 같은 문장으로 유지되는지 확인한다.
12. missing-layer master lock component set은 닫힌 reference로 보고,
    새 evidence가 생기기 전에는 `root / structure / mismatch / P2 handoff` snapshot 점검을 우선한다.
13. named-notables mainline umbrella는
    `core hub -> card/template -> search-batch/frozen sample`
    3층 분리가 유지되는지 확인하고,
    새 drift가 없으면 no-change watch로만 둔다.
14. bridge-anchor와 spine-index 인접층은
    같은 authority split과 master-lock carryover를 유지하는지만 확인하고,
    새 drift가 없으면 no-change watch로만 둔다.

## Input Reference Set

직접 참조하는 문서는 아래다.

1. `audit/Section_8_15_Closure_Sync_Carryover_Watch.md`
2. `audit/Section_8_Mainline_Sync_Register.md`
3. `audit/Section_8_Normalization_Status_Compass.md`
4. `audit/Section_8_Place_Network_Handoff_Map.md`
5. `audit/Section_8_Root_Corruption_First_Pass_A.md`
6. `audit/Section_8_Root_Subtree_Sampling_Queue.md`
7. `audit/Section_8_Frost_Notable_Anchor_Audit.md`
8. `audit/Section_8_15_Spine_Compatibility_Audit.md`
9. `audit/Section_8_to_15_Notable_Anchor_Bridge.md`
10. `audit/Section_15_Stable_Candidate_8_Anchor_Index.md`
11. `audit/Section_15_Named_Notables_Status_Compass.md`
12. `audit/Section_15_Five_Continent_Closure_Table.md`
13. `audit/Section_15_Named_Notables_Coverage_Matrix.md`
14. `audit/Section_15_Index_Draft.md`
15. `audit/Section_15_Folder_Structure_Draft.md`
16. `audit/Section_15_Folder_Draft_Routing_Plan.md`
17. `audit/Section_15_Folder_Revision_Gate.md`
18. `audit/Section_15_Named_Notables_Anchor_Map.md`
19. `audit/Section_15_Stable_Candidate_Profile_QA.md`
20. `audit/Section_15_Profile_Draft_Index.md`
21. `audit/Section_15_Operational_Lines_Track.md`
22. `audit/Section_15_Operational_Display_Canon_Candidates.md`
23. `audit/Section_15_Intake_Structure.md`
24. `audit/Section_15_Oceanic_Place_Institution_Sidecar.md`
25. `audit/Section_15_Frost_Place_Institution_Sidecar.md`
26. `audit/Section_15_Obelisk_Place_Institution_Sidecar.md`
27. `audit/FS_Place_Function_Register.md`
28. `audit/Section_15_Named_Notables_Register.md`
29. `audit/Section_15_Group_Index.md`
30. `audit/Section_15_Subline_Register.md`
31. `audit/Audit_Queue.md`
32. `audit/Next_Sequential_Workstream.md`
33. `audit/Historical_Batch_Reading_Guard.md`
34. `audit/Five_Continent_Missing_Layer_Master_Lock.md`

## Reference Backlog

아래는 메인 본선 reference가 아니라,
watch cycle이 안정된 뒤 조건부로 검토할 reference backlog다.

1. 원본 접근 가능 시 `Section_8_Root_Subtree_Sampling_Queue.md` 기준 subtree reference sampling 필요 여부 판단
2. 신규 closure batch 후보 검토 여부 판단
3. `14` 인물 백과 구조 감사와 `8 ↔ 14` 링크맵 심화
4. 후기 범대륙 / deferred routing 재확장 여부 판단
5. 실제 원고 입력 발생 시 live handoff case 승격

## Archive Note

이전 문서에 길게 남아 있던 `Tier 1 intake`, `대륙별 narrowing batch`,
`stable triad hardening`, `hold continuation`, `species side track`의
세부 이력은 이미 잠긴 참고 기록으로 본다.

`1~5 대륙 결손층 5개`는
`audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 따라
정책, evidence, firewall까지 묶어 읽는다.

실제 증거 intake 기준은
`audit/Five_Continent_Missing_Layer_Evidence_Register.md`에서
함께 잠근 상태로 읽는다.

1차 샘플 본문 기준은
`audit/Five_Continent_Missing_Layer_Evidence_First_Pass_A.md`에서
함께 유지한다.

반복 증거 안정화 기준은
`audit/Five_Continent_Missing_Layer_Evidence_Second_Pass_A.md`에서
함께 유지한다.

overread 차단 기준은
`audit/Five_Continent_Missing_Layer_Overread_Firewall.md`에서
함께 유지한다.

결손층 5개 전체 묶음의 단일 entry는
`audit/Five_Continent_Missing_Layer_Master_Lock.md`에서
함께 유지한다.

이 문서는 그 이력을 다시 순차 실행하는 문서가 아니라,
그 결과가 본선 reference와 충돌하지 않게 유지하는 문서로 읽는다.

historical batch/findings/search 문서의 읽기 규칙은
`audit/Historical_Batch_Reading_Guard.md`를 따른다.

## Conductor Rule

- 끊어서 오늘치만 끝내지 않는다.
- 새 후보를 늘리기 전에 lock과 wording drift를 먼저 잠근다.
- 실제 원고 입력이 생기면 summary drift보다 live handoff가 우선한다.
- watch cycle이 흔들리지 않는 한, 메인 본선 reference는 `closure sync / watch-reference 유지`다.

# Next Sequential Workstream

이 문서는 오케스트라가
무엇을 다음 확인 순서로 두는지를
reference 순서표로 보여주는 진행표다.

## Mainline Reference

메인 본선 reference는
`5대륙 closure sync / Section 8 -> 15 carryover watch`
유지다.

즉 새 후보 발굴, triad package 재개방,
새 hold batch 확장이 아니라
이미 잠근 구조/상태/소유권이 같은 문장으로 유지되는지를 본다.

## Locked State Snapshot

잠긴 상태 snapshot은 아래와 같다.

1. `Section 8`의 `canonical_root / quarantine_root / legacy_root`는 고정 상태다.
2. `Section 8`의 `section_style / mixed_keep / section_style_reclassify`는 고정 상태다.
3. `Section_8_Spine_Mismatch_Queue.md`는 `P1 locked snapshot`과 `P0 / P2 active queue`를 분리한 상태로 유지한다.
4. stable triad package는 닫힌 상태로 유지하고, `support_hold`, `deferred_expansion_hold`, Ether hold cluster는 triad package 밖에서만 유지한다.
5. `P2 place-pressure handoff` owner는 candidate index가 아니라 sidecar/register에서만 유지한다.
6. 카드층 `Policy Guard`는 `Section 15` summary/index/folder/routing 문서에 이미 흡수된 상태로 유지한다.

## Ordered Watch Sequence

오케스트라는 아래 순서로 점검한다.

1. `Section_8_Normalization_Status_Compass.md`
2. `Section_15_Named_Notables_Status_Compass.md`
3. `Section_15_Five_Continent_Closure_Table.md`
4. `Section_15_Named_Notables_Coverage_Matrix.md`
5. `Section_8_to_15_Notable_Anchor_Bridge.md`
6. `Section_8_15_Spine_Compatibility_Audit.md`
7. `Section_15_Stable_Candidate_8_Anchor_Index.md`
8. `Section_15_Index_Draft.md`
9. `Section_15_Folder_Structure_Draft.md`
10. `Section_15_Folder_Draft_Routing_Plan.md`
11. `Section_15_Folder_Revision_Gate.md`
12. `Section_15_Named_Notables_Anchor_Map.md`
13. `Section_15_Stable_Candidate_Profile_QA.md`
14. `Section_15_Ether_Hold_Cluster_Continuation.md`
15. `Section_15_Ether_Tower_Saint_Hold_Continuation.md`
16. `Section_15_Ether_Spirit_Union_Hold_Continuation.md`
17. `Section_8_Place_Network_Handoff_Map.md`
18. `Audit_Queue.md`
19. `Continuous_Workstream.md`

## What Stays Closed

아래는 watch 대상으로만 유지하고,
다시 active build처럼 열지 않는다.

1. stable triad actual draft package freeze
2. Crimson / Ether / Frost / Oceanic / Obelisk narrowing batch
3. Ether hold continuation 3종
4. `Section 8 -> 15` carryover wording sync가 끝난 closure 항목
5. `1~5 대륙 결손층 5개` 정책 lock

## Conditional Backlog

아래는 조건이 충족될 때만 다시 올린다.

1. 원본 접근이 가능해지면 `Section_8_Root_Subtree_Sampling_Queue.md` 기준 subtree 샘플링 진행 여부를 다시 연다.
2. 실제 원고 입력이나 새 증거 drift가 생기면 live handoff case를 우선 승격한다.
3. carryover watch가 흔들리면 해당 계층만 국소 재점검한다.
4. watch cycle이 안정된 뒤에만 다음 신규 closure batch 진행 여부를 판단한다.

## Conductor Decision

이 문서의 역할은
`다음 대륙`, `다음 배치`, `다음 확장`
목록을 계속 늘리는 것이 아니다.

이 기준에서는
`closure sync / carryover watch`
순서를 고정하고,
문서군이 같은 기준 시점을 가리키게 유지하는 단계다.

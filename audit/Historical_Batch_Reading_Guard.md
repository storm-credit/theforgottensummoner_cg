# Historical Batch Reading Guard

이 문서는 `batch`, `findings`, `search`, `scout`, `queue` 이름을 가진
과거 감사 문서들을 현재 본선 문서와 어떻게 구분해서 읽을지 고정하는 가드다.

## Purpose

- 과거 배치 기록이 현재 활성 workstream처럼 오독되는 일을 막는다.
- historical evidence와 current mainline control 문서를 같은 강도로 읽지 않게 한다.
- `closure sync / watch-reference` 단계에서 reference backlog를 안전하게 유지한다.

## Mainline Source of Truth Reference

현재 active mainline은 아래 문서만 source-of-truth로 읽는다.

1. `audit/Continuous_Workstream.md`
2. `audit/Next_Sequential_Workstream.md`
3. `audit/Audit_Queue.md`
4. `audit/Section_8_Normalization_Status_Compass.md`
5. `audit/Section_8_Mainline_Sync_Register.md`
6. `audit/Section_8_15_Closure_Sync_Carryover_Watch.md`
7. `audit/Section_15_Named_Notables_Status_Compass.md`
8. `audit/Section_15_Five_Continent_Closure_Table.md`
9. `audit/Section_15_Named_Notables_Coverage_Matrix.md`
10. `audit/Section_8_to_15_Notable_Anchor_Bridge.md`
11. `audit/Section_15_Named_Notables_Anchor_Map.md`
12. `audit/Section_15_Named_Notables_Continent_Synthesis.md`
13. `audit/Section_8_15_Spine_Compatibility_Audit.md`
14. `audit/Section_15_Stable_Candidate_8_Anchor_Index.md`
15. `audit/Five_Continent_Missing_Layer_Master_Lock.md`

위 문서에 직접 올라오지 않은 historical batch 문서는
현재 active step이 아니라 reference evidence로 읽는다.

## Historical Families

아래 이름 패턴은 기본적으로 historical/reference family로 읽는다.

1. `*_Search_Findings_Batch_*.md`
2. `*_Recovery_Batch_*.md`
3. `*_Scout*.md`
4. `*_Search_Synthesis.md`
5. `*_Named_Candidate_Search_Queue.md`
6. `*_Need_Named_Candidate_Index.md`
7. `*_Conflict_Register.md`
8. `*_Root_Findings.md`

## Reading Rule

historical family 문서는 아래 순서로만 읽는다.

1. 당시 무엇이 확인됐는지 본다.
2. 그 결과가 현재 watch 문서에 반영됐는지 본다.
3. 반영이 끝났다면 reference evidence로만 유지한다.
4. live handoff, 새 source access, 새 evidence drift가 생길 때만 다시 연다.

## Wording Rule

historical family 문서에서 아래 표현은
`당시 배치 기록`으로만 읽고 현재 실행 명령으로 읽지 않는다.

- `다음 배치`
- `다음 실제 배치`
- `다음 메인 본선`
- `Immediate Actions`
- `Next Action`
- `1차 마감`
- `2차 narrowing`
- `post-push`

현재형으로 다시 써야 할 경우에는 아래 표현을 우선한다.

- `Current Reference State`
- `Locked Action Reading`
- `reference backlog`
- `historical batch log`
- `closure state`
- `watch-reference input`

## Reopen Trigger

historical family 문서를 다시 active하게 읽는 조건은 아래뿐이다.

1. current mainline 문서가 그 문서를 직접 source-of-truth로 승격할 때
2. 원본 접근 가능 상태가 새로 생길 때
3. live handoff나 새 evidence drift가 발생할 때
4. 기존 closure wording과 충돌하는 새 source가 나올 때

## Conductor Decision

과거 batch/findings 문서는 지우지 않는다.
다만 현재는 `실행 큐`가 아니라 `증거 archive`로 유지한다.

즉 오케스트라는
historical batch를 계속 다시 밟는 방식이 아니라,
current mainline 문서가 필요하다고 선언한 경우에만
그 archive를 다시 연다.

# Setting Book Current Status Dashboard

## 목적

이 문서는 설정집 작업의 현재 위치를 한 화면에서 보기 위한 상태판이다.

진행률을 감으로 올리지 않고,
각 구간을 아래 네 상태로 나눠 본다.

| Status | Meaning |
| --- | --- |
| done | 현재 단계에서 마감으로 봐도 되는 상태 |
| shareable | 외부/협업자에게 보여 줄 수 있는 preview 상태 |
| controlled hold | 위험을 알고 통제 중이지만 v1 이름을 붙이기 전 남은 결정이 있는 상태 |
| not next | 지금 당장 할 일이 아닌 후순위 상태 |

## 현재 한 줄 결론

설정집은 지금 `shareable preview v0` 단계까지 정리됐다.

허브와 진입 동선은 마감에 가깝고,
별도 release-candidate 파일은 아직 만들지 않는다.

## 구간별 판정

| Area | Current Status | Why |
| --- | --- | --- |
| Hub navigation | done | 00-08 허브에 재진입 순서가 있고, 역할 지도 / preview / process hub로 복귀 가능하다. |
| Document role clarity | done | `Setting_Book_Document_Roles_Map.md`가 reader / reference / appendix / conductor 문서를 구분한다. |
| Shareable preview | shareable | `Setting_Book_Preview_Readable_v0.md`가 현재 가장 책처럼 읽히는 공유용 preview다. |
| Core profile bridge | shareable | 세력, 인물, 장소, 유물, 종족 5축 core profile이 preview와 기술 초안 사이를 잇는다. |
| Appendix A-E control | shareable | A-E 부록 흐름이 있고, high-risk row evidence note와 B/C sample evidence check가 들어갔다. |
| Compressed reference | shareable | `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`는 전체 구조 확인용 reference로 유지한다. |
| Release-candidate file | controlled hold | RC 파일명/상업용 layout/production bible 방향이 아직 다음 보존 산출물로 확정되지 않았다. |
| Full v1 release | controlled hold | preview v0는 공유 가능하지만, v1은 최종 이름, layout 방향, 필요한 row-level evidence만 더 좁힌 뒤 판단한다. |

## 지금 열어볼 순서

처음 보는 사람:

1. `Setting_Book_Preview_Readable_v0.md`
2. `Setting_Book_Document_Roles_Map.md`
3. 필요한 축의 core profile

세력별로 보고 싶은 사람:

1. `01_Setting_Book_Faction_Hub.md`
2. `Setting_Book_Faction_Core_Profiles_v0.md`
3. `Setting_Book_Chapter_2_Faction_Archive_Structure_Draft.md`

작업 상태를 확인하는 사람:

1. `Setting_Book_Current_Status_Dashboard.md`
2. `Setting_Book_Release_Readiness_Checklist.md`
3. `Setting_Book_Assembly_Index.md`
4. `Setting_Book_Thread_Checkpoint.md`

## 남은 일

현재 남은 일은 broad redraft가 아니다.

남은 것은 아래 세 가지 판단이다.

1. RC 파일명을 지금 만들지, preview 이름을 더 유지할지 판단
2. 상업용 layout과 production bible 중 어느 방향을 먼저 보존 산출물로 삼을지 결정
3. Appendix B/C에서 정말 필요한 행에만 row-level evidence note를 추가

세부 hold 기준은 `Setting_Book_Release_Readiness_Checklist.md`의 `V1 Hold Breakdown`에서 관리한다.

Appendix B/C 추가 근거 작업은 같은 문서의 `Appendix B/C Evidence Queue`에서 필요한 행만 고른다.

## 하지 말아야 할 일

- 허브를 다시 크게 갈아엎지 않는다.
- 공유용 preview와 compressed reference를 한 역할로 섞지 않는다.
- raw extraction 파일을 그대로 본문 canon으로 승격하지 않는다.
- 사용자 변경 파일을 release 커밋에 섞지 않는다.

## 오케스트라 다음 순서

1. 상태 대시보드와 허브 링크를 고정한다.
2. 필요할 때만 Appendix B/C evidence queue에서 행 단위 evidence note를 추가한다.
3. filename / layout 방향이 결정되면 RC 파일 생성 여부를 다시 판정한다.
4. 안정 마일스톤마다 branch와 main에 push한다.

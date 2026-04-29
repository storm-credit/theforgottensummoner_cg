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

설정집은 지금 `shareable preview v0` 단계까지 정리됐고,
설정집 cleanup loop는 `closed_for_current_cleanup / watch-reference mode`로 닫혔다.
직접 공유 원고는 내부 초안/작업 용어 스캔을 통과한 상태다.

허브와 진입 동선은 마감에 가깝고,
별도 release-candidate 파일은 아직 만들지 않는다.

## 지금 고정된 것

- 직접 공유 원고는 `Setting_Book_Preview_Readable_v0.md`로 유지한다.
- `Prototype_v0`는 압축 reference 역할로 유지한다.
- `Setting_Book_Preview_Package_v0.md`는 현재 reader-facing package의 적용 조립 지시서로 유지한다.
- `audit/Setting_Book_Cleanup_Closeout.md`는 cleanup 종료 boundary로 유지한다.
- `Setting_Book_Post_Closeout_Assembly_Gate.md`는 다음 reader-facing layout gate로 유지한다.
- Appendix B/C는 현재 anchored row만 유지하고, 최신 preview 기준으로 새 row를 추가하지 않는다.
- 허브 단계는 사실상 마감 상태로 보고, 필요하면 질문 문장만 미세 수정한다.
- 00-09 허브 위키링크 무결성 스캔은 통과했다.

## 아직 안 닫힌 것

- 별도 RC 파일명을 만들지, 현재 preview 이름을 더 오래 유지할지
- production bible 전환 신호가 실제로 생겼는지
- Appendix B/C에서 나중에 정말 body-final entry가 생길 때 추가 evidence row가 필요한지

## 구간별 판정

| Area | Current Status | Why |
| --- | --- | --- |
| Hub navigation | done | 00-08 허브에 재진입 순서가 있고, 메인 허브에서 세력/인물/유물/장소/종족 축으로도 바로 갈 수 있다. |
| Hub quick indexes | done | 01-08 허브가 질문 기준 첫 클릭 표를 갖고 있어 축/검증/원재료 진입이 짧아졌다. |
| Document role clarity | done | `Setting_Book_Document_Roles_Map.md`와 관련 support/source 문서가 reader / reference / appendix / conductor 경계를 같은 기준으로 구분한다. |
| Shareable preview | shareable | `Setting_Book_Preview_Readable_v0.md`가 현재 가장 책처럼 읽히는 공유용 preview이며, 내부 작업어 스캔을 통과했다. |
| Reader-facing package scope | shareable | `Setting_Book_Preview_Package_v0.md`가 core package / optional bridge / verification-only lane을 실제 적용 기준으로 분리한다. |
| Core profile bridge | shareable | 세력, 인물, 장소, 유물, 종족 5축 core profile이 preview와 더 깊은 기록 사이를 잇는다. |
| Appendix A-E control | shareable | A-E 부록 흐름이 있고, high-risk row evidence note와 B/C sample evidence check가 들어갔다. |
| Compressed reference | shareable | `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`는 전체 구조 확인용 reference로 유지한다. |
| Release-candidate file | controlled hold | RC 파일명/상업용 layout/production bible 방향이 아직 다음 보존 산출물로 확정되지 않았다. |
| Full v1 release | controlled hold | preview v0는 공유 가능하지만, v1은 최종 이름, layout 방향, 필요한 row-level evidence만 더 좁힌 뒤 판단한다. |

Post-closeout preview note:

- `Setting_Book_Preview_Readable_v0.md`는 out-of-order Part numbering, raw support-doc filenames, and backstage support wording을 제거한 상태다.
- preview package, front matter, reader-facing TOC support docs도 같은 post-closeout reader-facing order를 가리킨다.
- public assembly, prototype, release readiness, and post-closeout gate도 같은 reader-facing label baseline을 따른다.
- people/items/places/species/appendix hubs도 같은 reader-facing label baseline을 따른다.
- appendix assembly, public voice samples, named-notables chapter draft도 같은 reader-facing label baseline을 따른다.
- direct-share preview headings, reader-facing TOC section notes, post-closeout gate order table도 같은 Korean reader-facing label baseline을 따른다.
- preview package는 이제 core package / optional bridge / verification-reference only lane을 실제 적용 상태로 분리한다.
- direct-share preview flow list now includes its appendix boundary section instead of implying the appendix is outside the current preview.
- preview package direct-share flow summary now also includes the appendix boundary section from the direct-share preview.
- preview package flow language now describes the direct-share preview rather than a body-only slice.
- preview package next-build gate now keeps `preview_v0_readable` active and treats `preview_v0_production` as a held watchpoint, not a parallel active build.
- direct-share preview now describes axis companion material as reader-facing `동행 안내` rather than exposing support-doc/profiling language.
- preview package latest-QA line now records both the internal draft/work-term scan and the optional companion support-term scan.
- preview package now clarifies that its seven-part direct-share flow is a compact path inside the broader post-closeout reader-facing assembly order, with `힘과 질서, 숨은 체계` and `이름, 언어, 세계의 톤` reserved for fuller assembly.
- release readiness checklist now mirrors the same compact-preview / fuller-assembly split and keeps production bible as a held watchpoint.

## 지금 열어볼 순서

처음 보는 사람:

1. `Setting_Book_Preview_Readable_v0.md`
2. `Setting_Book_Document_Roles_Map.md`
3. 필요한 축의 core profile

세력별로 보고 싶은 사람:

1. `01_Setting_Book_Faction_Hub.md`
2. `Setting_Book_Faction_Core_Profiles_v0.md`
3. `Setting_Book_Chapter_2_Faction_Archive_Structure_Draft.md`

축별로 빠르게 보고 싶은 사람:

1. `02_Setting_Book_People_Hub.md` 또는 `03_Setting_Book_Items_Hub.md`
2. `04_Setting_Book_Places_Hub.md` 또는 `05_Setting_Book_Species_Hub.md`
3. 각 허브의 `빠른 인덱스` 표에서 바로 갈 문서 선택

검증이나 원재료로 바로 가고 싶은 사람:

1. `06_Setting_Book_Appendix_Hub.md`
2. `08_Setting_Book_Source_Hub.md`
3. 각 허브의 `빠른 인덱스` 표에서 질문에 맞는 문서 선택

작업 상태를 확인하는 사람:

1. `Setting_Book_Current_Status_Dashboard.md`
2. `Setting_Book_Post_Closeout_Assembly_Gate.md`
3. `Setting_Book_Release_Readiness_Checklist.md`
4. `Setting_Book_Filename_Decision_Matrix.md`
5. `Setting_Book_Next_Preserved_Artifact_Scope.md`
6. `Setting_Book_Assembly_Index.md`
7. `Setting_Book_Thread_Checkpoint.md`

## 남은 일

현재 남은 일은 broad redraft가 아니다.

남은 것은 아래 네 가지 판단이다.

1. post-closeout gate 기준으로 reader-facing layout 기본값을 유지할지 확인
2. `Setting_Book_Packaging_Direction_Matrix.md`의 switch test 기준으로 production bible 전환 신호가 실제로 생겼는지 계속 판정
3. Appendix B/C에서 정말 필요한 행에만 row-level evidence note를 추가
4. RC 이름 재개 여부는 `패키징이 다음 보존 산출물`로 바뀔 때만 다시 판정

세부 hold 기준은 `Setting_Book_Release_Readiness_Checklist.md`의 `V1 Hold Breakdown`에서 관리한다.
`filename / RC naming` 판단은 `Setting_Book_Filename_Decision_Matrix.md`에서 따로 관리한다.
`layout vs production bible` 방향은 `Setting_Book_Packaging_Direction_Matrix.md`에서 따로 관리한다.
실제 다음 보존 묶음 범위는 `Setting_Book_Next_Preserved_Artifact_Scope.md`에서 따로 관리한다.

Appendix B/C 추가 근거 작업은 같은 문서의 `Appendix B/C Evidence Queue`에서 필요한 행만 고른다.
최신 readable preview polish 이후에는 새 B/C row를 추가하지 않는 것으로 판정했다.

## 하지 말아야 할 일

- 허브를 다시 크게 갈아엎지 않는다.
- 공유용 preview와 compressed reference를 한 역할로 섞지 않는다.
- raw extraction 파일을 그대로 본문 canon으로 승격하지 않는다.
- 사용자 변경 파일을 release 커밋에 섞지 않는다.

## 오케스트라 다음 순서

1. 공유용 preview는 현재 안정본으로 두고, 대규모 문장 재작성은 다시 열지 않는다.
2. `Setting_Book_Post_Closeout_Assembly_Gate.md`를 먼저 읽고 reader-facing layout 범위 안에서만 다음 배치를 연다.
3. 허브 인덱스는 현재 완료 상태로 보고, 필요하면 질문 문장만 미세 수정한다.
4. filename hold는 matrix 기준으로 유지하고, 조기 RC rename은 다시 열지 않는다.
5. packaging direction matrix의 switch test를 기준으로 layout vs production bible 방향을 계속 선명하게 유지한다.
6. 필요할 때만 Appendix B/C evidence queue에서 행 단위 evidence note를 추가한다.

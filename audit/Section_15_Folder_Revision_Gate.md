# Section 15 Folder Revision Gate

이 문서는 `Section_15_Folder_Structure_Draft.md`와
actual draft package freeze 단계의
안전 점검표다.

목표:

- actual draft package freeze 단계에서 위험을 먼저 확인한다.
- 실제 폴더 생성/이동 전에 마지막 안전 조건을 잠근다.
- 14번 영웅과 15번 명사형 인물을 섞지 않는다.
- 이름 충돌과 후기 확장 구역을 과확정하지 않는다.

## Gate Checklist

| Gate | Question | Current Result |
|---|---|---|
| `G1. Archive Split` | 14 중심 영웅과 15 명사형 인물이 분리되어 있는가? | `pass_with_holds` |
| `G2. Folder Basis` | 직업별이 아니라 대륙 -> 세력/도시/조직 기준인가? | `pass` |
| `G3. Boundary Safety` | `verify_before_15` 후보를 실제 15 확정자로 다루지 않았는가? | `pass` |
| `G4. Name Collision Safety` | 실비아, 아이기스, 메라, Ravenfell, 실라스 등 충돌을 병합하지 않았는가? | `pass` |
| `G5. Need Named Candidate Safety` | 개인명 없는 슬롯에 새 이름을 만들지 않았는가? | `pass` |
| `G6. Original Repo Safety` | 원본 저장소를 건드리지 않았는가? | `pass` |
| `G7. Late Expansion Safety` | 범대륙 후기 확장을 메인 정본처럼 과확정하지 않았는가? | `pass_with_deferred_expansion_hold` |
| `G8. Stable Triad Route Safety` | `울프가르 / 에리온 / 오그마`가 `드래곤포지 공방 / 학술-전승층 / 전승 보관층` actual draft 기준으로 분리되어 있는가? | `pass_with_actual_draft_lock` |
| `G9. support_hold Separation` | `엘다라`가 stable triad actual draft에 섞이지 않고 `support_hold`로 분리되어 있는가? | `pass_with_support_hold` |
| `G10. Move Freeze Safety` | bridge / routing consistency 점검 단계에서도 실제 파일 이동은 여전히 금지되어 있는가? | `pass` |
| `G11. Route Hierarchy Consistency` | 상위 route anchor와 보조 place lock이 같은 계층처럼 혼용되지 않는가? | `pass_with_hierarchy_lock` |
| `G12. Package Freeze Completeness` | stable triad actual draft package와 hold queue separation이 별도 freeze 시트까지 포함해 잠겨 있는가? | `pass_with_package_freeze` |

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| `에테르 후보 과밀` | `medium` | 마법협회/성국/정령연합 경계 후보는 전원 `verify_before_15` 또는 `keep_14` 유지. |
| `해양 역할 슬롯 과다` | `medium` | 포트 아우렐리온/크로스윈드 포트 중심으로 장소 기능을 먼저 보존. |
| `오벨리스크 초월 서사 과열` | `medium` | 사람보다 기록/기억/거래/죄책감/망명 기능으로 낮춰 읽음. |
| `범대륙 후기 확장 과확정` | `medium` | 키르케는 강한 후보만 보존하고 전체 범대륙은 후순위 유지. |
| `실제 폴더 이동 시 충돌` | `high` | 아직 이동하지 않는다. 다음 단계도 `cg` 설계문서로만 진행. |
| `stable triad route drift` | `medium` | `울프가르 = 드래곤포지 공방`, `에리온 = 학술-전승층`, `오그마 = 전승 보관층` 기준을 bridge/routing docs에 고정 유지. |
| `엘다라 premature promotion` | `medium` | `support_hold`, `verify_source_before_profile`, `정령연합 전체 14 확인 전 Hard Canon 금지`를 동시에 유지. |
| `route/place 계층 혼용` | `medium` | 상위 route는 `공방 / 층 / 보관층`, 보조 place는 `도서관 / 샘 / 재료지`로 분리 표기한다. |
| `package scope blur` | `medium` | stable triad와 hold queue를 `Section_15_Actual_Draft_Package_Freeze.md`에서 분리 유지한다. |
| `policy overread recurrence` | `medium` | 카드층의 `Policy Guard`와 summary/folder carryover 문장을 같이 유지해 `state_house strong`, `토착 공동체층`, `전통 국가기관` 과독해를 막는다. |

## Profile Format Gate

- operational profile card는 `Section_15_Profile_Template.md`의 `3-1. Policy Guard` 형식을 유지해야 한다.
- 폴더/route/revision gate 문서는 이 하위 profile 형식을 덮어쓰지 않고,
  같은 carryover rule이 유지되는지만 검사한다.

## Gate Decision

`Section_15_Folder_Structure_Draft.md`는
stable triad actual draft 단계의 설계 문서로 사용 가능하다.

하지만 실제 폴더 이동 또는 문서 이동은 아직 금지한다.

현재는 아래 두 가지를 `설계 문서 기준`으로만 유지한다.

1. stable triad actual draft package freeze 상태 유지와 closure sync / carryover watch 점검
2. `15번 실제 폴더 생성/이동 계획`은 계속 보류

추가 기준:

- `크림슨` route는 씨족 중심 질서와 thin-support까지만 반영한다.
- `해양` route는 자유도시 shadow-market cluster를 `urban_market` 범위에서만 반영한다.
- `오벨리스크` route는 `nontraditional elite thin-support / dark institution` 범위에서만 반영한다.

## Conductor Decision

현재 `Section 15` 내부 기준은
stable triad actual draft package freeze를 닫힌 상태로 두고,
hold queue 쪽 경계 보류군 유지 점검과
carryover wording consistency를 함께 유지하는 것이다.

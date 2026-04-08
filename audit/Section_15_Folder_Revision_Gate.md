# Section 15 Folder Revision Gate

이 문서는 `Section_15_Folder_Structure_Draft.md`의 안전 점검표다.

목표:

- 실제 폴더 생성/이동 전에 위험을 확인한다.
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
| `G7. Late Expansion Safety` | 범대륙 후기 확장을 메인 정본처럼 과확정하지 않았는가? | `pass_with_deferred_zone` |

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| `에테르 후보 과밀` | `medium` | 마법협회/성국/정령연합 경계 후보는 전원 `verify_before_15` 또는 `keep_14` 유지. |
| `해양 역할 슬롯 과다` | `medium` | 포트 아우렐리온/크로스윈드 포트 중심으로 장소 기능을 먼저 보존. |
| `오벨리스크 초월 서사 과열` | `medium` | 사람보다 기록/기억/거래/죄책감/망명 기능으로 낮춰 읽음. |
| `범대륙 후기 확장 과확정` | `medium` | 키르케는 강한 후보만 보존하고 전체 범대륙은 후순위 유지. |
| `실제 폴더 이동 시 충돌` | `high` | 아직 이동하지 않는다. 다음 단계도 `cg` 설계문서로만 진행. |

## Gate Decision

`Section_15_Folder_Structure_Draft.md`는 설계 문서로는 사용 가능하다.

하지만 실제 폴더 이동 또는 문서 이동은 아직 금지한다.

다음 단계는 아래 두 가지 중 `설계 문서`만 허용한다.

1. `Section_15_Index_Draft.md` 작성
2. `15번 실제 폴더 생성/이동 계획`은 보류

## Conductor Decision

다음 작업은 `Section_15_Index_Draft.md`를 작성해
15번을 열람할 때 어떤 순서로 볼지 정리하는 것이다.

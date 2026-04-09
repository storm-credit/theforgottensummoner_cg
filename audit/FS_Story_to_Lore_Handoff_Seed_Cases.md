# FS Story-to-Lore Handoff Seed Cases

이 문서는 `FS_Story_to_Lore_Handoff_Gate.md`가
실제로 어떤 route와 register write로 이어지는지 시험하는 seed 장부다.

원칙:

- seed case는 정본 선언이 아니다.
- 새 고유명, 새 아이템명, 새 세력명을 발명하지 않는다.
- 실제 원고에서 같은 압력이 다시 나오면 이 장부를 보고 handoff packet을 보강한다.

## Seed Case 001

| Field | Value |
|---|---|
| `case_id` | `FS-HANDOFF-SEED-001` |
| `story_source` | `FS_Story_Act_Question_Register.md / FS-AQ-004` |
| `scene_or_act` | `전설 무구는 누구를 영웅으로 만들고 누구를 망가뜨리는가?` |
| `proposed_new_element` | 전설 무구의 구체 후보가 필요해지는 압력 |
| `proposal_type` | `item` |
| `working_name` | `unnamed legendary armament pressure` |
| `why_now` | 울프가르 / 드락사르 제작축이 장면 목표와 감정 비용을 요구한다 |
| `expected_reader_effect` | 무구 자체보다 제작 책임과 사용자 손상을 먼저 읽게 한다 |
| `lore_risk` | 새 무구명을 바로 만들면 아이템 정본과 14/15 영웅축이 동시에 과열된다 |
| `suggested_route` | `item_hold -> FS_Asset_Secret_Register -> FS_Foreshadow_Payoff_Register` |

## Lore Intake Result

| Check | Result |
|---|---|
| Existing source conflict | 없음. 아직 새 아이템명이 없으므로 충돌 없음 |
| State label | `handoff_test / no_canon_name` |
| Route | `item_hold` |
| Naming tone | 이름 생성 금지. 실제 장면 필요 시 `display_canon_candidate` 이전에 다시 검토 |
| Relation/time impact | 울프가르 / 드락사르 제작축과 `FS-AQ-004` 감정 비용에 연결 |
| Required register write | `FS_Asset_Secret_Register`, `FS_Foreshadow_Payoff_Register` |

## Decision

`FS-HANDOFF-SEED-001`은
새 전설 무구를 만드는 케이스가 아니다.

현재 판정은
`hold_for_evidence / item_pressure_only`다.

따라서 다음 실제 원고에서 무구의 이름, 제작자, 사용자, 대가가 함께 나오기 전까지
정본 아이템으로 승격하지 않는다.

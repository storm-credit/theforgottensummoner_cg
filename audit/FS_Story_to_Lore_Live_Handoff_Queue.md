# FS Story-to-Lore Live Handoff Intake Template

이 문서는 실제 원고나 장면 입력에서 나온 새 설정을
Story Engine에서 Lore Engine으로 넘길 때 쓰는 intake template이다.

`seed case`와 `live case`를 섞지 않기 위해
실제 입력이 없는 동안에는 watch-ready template로 비워 둔다.

handoff active state는
`Continuous_Workstream.md`,
`Next_Sequential_Workstream.md`,
`FS_Story_to_Lore_Handoff_Gate.md`
기준으로 읽는다.

## Intake Reference Rules

- live case는 실제 원고 / 장면 입력이 있을 때만 생성 대상으로 읽는다.
- 새 고유명, 새 아이템명, 새 세력명은 이 문서에서 발명 대상으로 다루지 않는다.
- live case가 생기면 `FS_Story_to_Lore_Handoff_Gate.md`의 packet fields를 채운 뒤 Lore route로 넘기는 기준으로 읽는다.
- seed case는 `FS_Story_to_Lore_Handoff_Seed_Cases.md`에만 남기는 기준으로 분리한다.
- table이 비어 있다는 사실은 `작업 없음`이 아니라 `실제 입력 대기` 상태를 뜻한다.

## Intake Schema Reference

| Field | Required | Note |
|---|---|---|
| `case_id` | yes | `FS-LIVE-HANDOFF-###` 형식 |
| `source_excerpt_or_summary` | yes | 원고 전체가 아니라 필요한 짧은 요약만 |
| `story_source` | yes | 장면, 액트, 질문, 초안 파일 |
| `scene_or_act` | yes | 어느 장면/액트에서 발생했는가 |
| `trigger_type` | yes | 새 지명, 세력, 기관, 유명인, 아이템, route, rumor_to_fact 등 |
| `proposed_new_element` | yes | 무엇이 새로 들어오려 하는가 |
| `proposal_type` | yes | place / faction / institution / named_person / operational_line / item / lineage / route / rumor_to_fact |
| `working_name` | optional | 원고에 이미 있는 경우만 적는다 |
| `why_now` | yes | 장면상 왜 필요한가 |
| `expected_reader_effect` | yes | 독자가 무엇을 느끼거나 알게 되는가 |
| `lore_risk` | yes | 이름 충돌, 등급 과열, route 흔들림, 톤 충돌 |
| `suggested_route` | yes | 14 / 15 / 8 / Place / Item / Hold 등 |
| `intake_status` | yes | 아래 Status Labels 기준 |
| `next_register` | yes | 다음에 써야 할 장부 |

## Intake Table Template

| Case ID | Story Source | Trigger Type | Proposed Element | Suggested Route | Intake Status | Next Register |
|---|---|---|---|---|---|---|

## Reference Status Labels

| Label | Meaning |
|---|---|
| `new` | 실제 원고 입력에서 막 들어온 상태로 기록한다 |
| `needs_lore_review` | Lore Engine 검토가 필요한 상태로 읽는다 |
| `routed_to_register` | 다음 장부가 정해진 상태로 읽는다 |
| `hold_for_evidence` | 근거가 약해 보류한 상태로 읽는다 |
| `rejected_or_reframed` | 정본 구조와 충돌해 장면 해법을 바꾼 상태로 읽는다 |
| `closed` | 필요한 장부 반영과 change log가 끝난 상태로 읽는다 |

## Closure Reference Checklist

live case를 닫을 때는 아래 기준을 확인한다.

- `FS_Story_to_Lore_Handoff_Gate.md` packet fields가 채워졌는가
- route가 14 / 15 / 8 / Place / Item / Hold 중 하나로 정리됐는가
- 필요한 register write가 정해졌는가
- 정본 선언이 필요한 경우 `FS_Revision_Gate_Checklist.md`를 통과했는가
- 상태 이동이 있으면 `FS_Canon_Change_Log.md`에 남겼는가

## Conductor Note

이 intake template은 상상 장면을 만들기 위한 곳이 아니다.

실제 원고 입력이 없으면 template를 비워 둔다.
실제 입력이 오면 그때 seed가 아니라 live case로 승격하는 기준으로 쓴다.

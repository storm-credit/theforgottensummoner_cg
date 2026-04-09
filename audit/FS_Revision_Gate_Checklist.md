# FS Revision Gate Checklist

이 문서는 FS Lore Engine이
설정집을 실제로 수정하거나
정본 후보를 올리기 전에 통과해야 하는 검수 게이트다.

현재 원칙:

- 원본 저장소는 수정하지 않는다.
- 모든 실작업은 `theforgottensummoner_cg`에서만 한다.
- 이름, 소속, 폴더링, 정본 판정은 장부를 거쳐야 한다.

## Gate 1. Source Priority

수정 전 확인:

- 어떤 출처에서 온 정보인가?
- 더 높은 우선순위의 문서와 충돌하지 않는가?
- `FS_Source_Priority_Register.md` 기준으로 설명 가능한가?

통과 조건:

- 출처 계층이 적혀 있다.
- 낮은 우선순위 문서를 높은 우선순위 문서처럼 쓰지 않는다.

## Gate 2. State Label

수정 전 확인:

- 이 항목의 상태는 무엇인가?
- `hard_canon`, `soft_canon`, `active_working`, `conflict`, `legacy_hold`, `open_question` 중 무엇인가?

통과 조건:

- 상태 라벨이 붙어 있다.
- `conflict`나 `legacy_hold`를 바로 정본화하지 않는다.

## Gate 3. Archive Routing

수정 전 확인:

- 이 항목은 어디에 들어가야 하는가?
- `14`, `15 Named Notables`, `15 Operational Lines`, `8`, `지도`, `아이템`, `hold` 중 어디인가?

통과 조건:

- 폴더 기준은 `대륙 -> 세력/도시/조직`이 우선이다.
- 직업/기능은 보조 인덱스로 둔다.

## Gate 4. Naming Tone

수정 전 확인:

- 표면명이 서양 정통 에픽 판타지 톤에 맞는가?
- 현대 범죄물, 기업물, 무협/동양풍 어휘가 섞이지 않았는가?
- 작업용 구조 라벨과 세계 안 이름을 분리했는가?

통과 조건:

- `workflow/12_Naming_Tone_Guide.md`와 충돌하지 않는다.
- 필요하면 `display_canon_candidate`로 보류한다.

## Gate 5. Relationship / Causality

수정 전 확인:

- 이 항목이 관계망이나 시간축을 바꾸는가?
- 누가 누구를 실제로 아는지, 소문만 들었는지, 과거/미래 인연인지 분리했는가?
- 액트 결과나 복선 회수에 영향을 주는가?

통과 조건:

- 관계 변화는 `FS_Relationship_Ledger.md`와 연결한다.
- 액트 결과는 `FS_Act_Outcome_Ledger.md`와 연결한다.
- 복선은 `FS_Foreshadow_Payoff_Register.md`와 연결한다.

## Gate 6. Original Repository Safety

수정 전 확인:

- 작업 대상이 `theforgottensummoner_cg` 안인가?
- 원본 저장소나 로컬 원본 클론을 수정하지 않는가?

통과 조건:

- 원본은 읽기 전용이다.
- 복사본, 분석표, 장부만 `cg`에서 수정한다.

## Gate 7. Story-to-Lore Handoff

수정 전 확인:

- 이 요소가 Story Engine에서 새로 제안된 것인가?
- 새 지명, 새 세력, 새 아이템, 새 유명인, 새 소속, 소문의 사실화가 걸려 있는가?
- `audit/FS_Story_to_Lore_Handoff_Gate.md` 기준으로 되돌려 보냈는가?

통과 조건:

- `story_source`, `trigger_type`, `proposed_element`, `expected_lore_target`가 적혀 있다.
- Lore Engine route와 필요한 register write가 정해져 있다.
- Story Engine의 장면 제안이 정본 선언보다 먼저 가지 않는다.

## Required Audit Trace

정본 선언, 라우팅 변경, 이름 변경 후보에는 아래 흔적을 남긴다.

| Field | Meaning |
|---|---|
| `source_tier` | 어느 출처 우선순위를 근거로 삼았는가 |
| `state_label` | 현재 상태 라벨은 무엇인가 |
| `route` | 14, 15 Named Notables, 15 Operational Lines, 8, 지도, 아이템, hold 중 어디인가 |
| `naming_state` | 표면명 확정인지 display canon 후보인지 |
| `relation_time_impact` | 관계, 액트, 연표, 복선에 영향을 주는가 |
| `story_source` | 어떤 장면/액트/스토리 초안에서 이 요소가 나왔는가 |
| `handoff_trigger` | 왜 Story-to-Lore handoff를 걸었는가 |

## Fast Decision Table

| Situation | Required Gate |
|---|---|
| 이름만 바꾸고 싶다 | Gate 1, 2, 4 |
| 14에서 15로 보낼지 고민된다 | Gate 1, 2, 3, 5 |
| 레거시 루트를 정리하고 싶다 | Gate 1, 2, 3, 6 |
| 아이템을 백과로 회수하고 싶다 | Gate 1, 2, 3, 5 |
| 지도/도시/건물 내부 맵 후보를 추가한다 | Gate 1, 2, 3, 5 |
| 범대륙 후기 확장을 올린다 | Gate 1, 2, 3, 4, 5 |
| 원고에서 새 설정이 바로 튀어나왔다 | Gate 1, 2, 3, 5, 7 |

## Conductor Note

수정은 빠르게 해도 된다.
하지만 정본 선언은 천천히 한다.

FS Lore Engine의 목표는
많이 고치는 것이 아니라
나중에 고쳐도 무너지지 않는 구조를 만드는 것이다.

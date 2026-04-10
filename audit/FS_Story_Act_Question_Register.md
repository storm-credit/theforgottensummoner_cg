# FS Story Act Question Register

이 문서는 FS Story Engine이
각 액트의 감정적 질문을 관리하기 위한 장부다.

액트는 사건 목록이 아니라
하나의 질문을 던지고,
끝에서 그 질문의 답을 바꾸는 단위로 본다.

## Fields

| Act ID | Act Question | Primary Human Axis | External Conflict | Emotional Cost | Outcome Link | Status |
|---|---|---|---|---|---|---|

## Question Types

### `trust_question`

누구를 믿을 수 있는가.

사용:

- 동료였던 인물이 적대자로 바뀔 때
- 소문만 들은 인물을 실제로 만날 때
- 조직의 공식 기록과 개인 증언이 다를 때

### `belonging_question`

어디에 속하는가.

사용:

- 가문, 길드, 부족, 용병단, 교단 사이 소속이 흔들릴 때
- 14번 영웅과 15번 명사형 인물이 다른 층에서 만날 때

### `truth_question`

무엇이 사실인가.

사용:

- 진품/가품
- 소문/정본
- 금서/공식 연대기
- 숨은 소속

### `cost_question`

무엇을 얻기 위해 무엇을 잃는가.

사용:

- 전설 무구
- 영약
- 금지 지식
- 봉인 해제
- 위험한 동맹

## Seed Questions

| Act ID | Act Question | Primary Human Axis | External Conflict | Emotional Cost | Outcome Link | Status |
|---|---|---|---|---|---|---|
| `FS-AQ-001` | `세실리아는 자유도시의 그림자 경제를 어디까지 인정할 수 있는가?` | `세실리아 / 벤투라 / 도미닉 / 로렌조` | `합법 상업권 vs 음지 유통망` | `공적 질서의 균열` | `FS-ACT-SEED-01` | `seed` |
| `FS-AQ-002` | `키르케 영약회는 치료를 위해 어디까지 의존할 수 있는가?` | `멜리산드르 / 실비아 / 외부 개입자` | `임상 교착 vs 위험한 돌파` | `맹목적 의존과 윤리 손상` | `FS-ACT-SEED-02` | `seed` |
| `FS-AQ-003` | `금서의 해독은 누구에게 맡겨도 되는가?` | `에리온 / 오그마 / 엘드라칸 지식축` | `지식 접근 제한 vs 위기 해결` | `금지 지식 노출` | `FS-ACT-SEED-03` | `seed` |
| `FS-AQ-004` | `전설 무구는 누구를 영웅으로 만들고 누구를 망가뜨리는가?` | `울프가르 / 드락사르 / 제작축` | `제작 욕망 vs 무구의 대가` | `장인의 책임과 사용자 손상` | `FS-ACT-SEED-04` | `seed` |

## Conductor Reading Rule

액트가 막히면 사건을 더 추가하지 말고
먼저 질문을 선명하게 만든다.

질문이 선명하지 않은 액트는
인물과 설정이 많아도 독자에게 흐릿하게 느껴진다.

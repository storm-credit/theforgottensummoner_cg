# Surface Naming Audit Findings

이 문서는 현재 import된 작업본 기준으로
`정통 판타지 톤을 해칠 수 있는 표면 명칭`을 추려서
`유지`, `영문만 완화`, `한국어와 영문 모두 교체 후보`, `내부 분류 전용`으로 나눈 감사서다.

## Conductor Summary

현재까지 확인한 결과,

- 문제의 핵심은 한국어 명칭보다 영문 suffix에 더 자주 있다.
- `Syndicate`, `Cartel`, `Industry`, `Megacorp` 같은 영어 꼬리표가 장르 톤을 흔든다.
- 한국어가 이미 `-단`, `-회`, `-연맹`, `-상회` 계열이면 한국어는 유지하고 영문만 완화하는 쪽이 가장 안전하다.
- 한국어에 `카르텔`이 직접 들어간 둘은 우선 교체 대상으로 본다.

## 1. Keep Korean, Soften English

아래는 한국어 표면명은 비교적 자연스럽고,
영문 suffix만 정통 판타지 쪽으로 낮추는 편이 좋은 후보들이다.

| Current Form | Preferred Display Candidate | Reason |
|---|---|---|
| `검은 파도단 (Black Tide Syndicate)` | `검은 파도단 (Black Tide League)` | 한국어 `파도단`은 충분히 판타지스럽고 영문 `Syndicate`만 과현대적이다. |
| `고대 유산단 (Ancient Legacy Syndicate)` | `고대 유산단 (Ancient Legacy League)` | 한국어는 유지 가능하고 영문만 완화하면 된다. |
| `모래늑대단 (Sand Wolf Cartel)` | `모래늑대단 (Sand Wolf League)` | 크림슨 계열 분위기는 유지하면서 범죄물 느낌을 줄인다. |
| `황금 손아귀 (Golden Claw Syndicate)` | `황금 손아귀 (Golden Claw League)` | 첩보/비공식 권력 느낌은 남기되 현대 범죄조직 뉘앙스를 뺀다. |
| `검은 발톱단 (Black Talon Cartel)` | `검은 발톱단 (Black Talon League)` | 한국어는 살아 있고 영문만 다듬으면 된다. |
| `검은 왕관단 (Black Crown Syndicate)` | `검은 왕관단 (Black Crown League)` | 궁정 암투/비밀결사 느낌으로 더 안정적이다. |
| `검은 해골단 (Black Skull Cartel)` | `검은 해골단 (Black Skull League)` | 폭력조직 결은 남기되 현대 범죄물 느낌을 줄인다. |
| `붉은 칼날단 (Red Blade Syndicate)` | `붉은 칼날단 (Red Blade League)` | 전투조직/용병조직 느낌은 유지된다. |
| `신성 거래회 (Holy Trade Syndicate)` | `신성 거래회 (Holy Trade League)` | 성역권 교역 네트워크 같은 결로 낮추는 편이 자연스럽다. |
| `얼음 독점단 (Frozen Trade Syndicate)` | `얼음 독점단 (Frozen Trade League)` | 프로스트 생존경제 문법에 더 맞는다. |

## 2. Replace Korean and English

아래는 한국어 자체에도 현대 조직물 느낌이 강해서
한국어와 영문 모두 재검토하는 편이 좋다.

| Current Form | Preferred Display Candidate | Reason |
|---|---|---|
| `철의 금융 카르텔` | `철의 금융 연맹` | 한국어 `카르텔`이 너무 직접적이다. |
| `침묵의 카르텔` | `침묵의 상회` | 비공식 교역권 느낌은 유지하면서 정통 판타지 어휘로 낮춘다. |

## 3. Internal Classification Only

아래는 표면 세력명이라기보다 분류명, umbrella label, 기능 설명어에 가깝다.
정본 표면명으로는 그대로 쓰지 않는 편이 좋다.

| Current Form | Suggested Handling | Reason |
|---|---|---|
| `Megacorps` | `Grand Trade Houses` 같은 표면 분류로 대체 검토 | 메타 분류명으로는 가능하지만 판타지 표면 분류명으론 거칠다. |
| `Syndicates` | `Trade Leagues`, `Merchant Leagues`, `교역 연맹` 계열 검토 | 분류어로는 편하지만 표면 문서명으론 현대 범죄경제 느낌이 강하다. |
| `Aether Gear Industry` | `Aether Gear Foundry` 검토 | 제작소/공방/조병소 느낌이 더 판타지 톤에 맞다. |

## 4. Keep As-Is For Now

아래는 지금 단계에서 굳이 손대지 않아도 되는 이름들이다.

- `키르케 영약회`
- `황금 닻 조합`
- `거상 연합`
- `Twilight Merchants Guild`
- `Grey Market Guild`
- `Hidden Exchange Guild`
- `성혈단`
- `서리 맹약단`

## Working Rule

앞으로 이름을 볼 때는 아래 순서로 처리한다.

1. 한국어 표면명이 이미 장르 톤에 맞는지 본다.
2. 맞으면 영문 suffix만 완화한다.
3. 한국어까지 현대적이면 양쪽 모두 교체 후보로 올린다.
4. 분류명이라면 표면명으로 쓰지 말고 내부 분류로만 유지한다.

## Next Action

다음 단계에서는

1. `범대륙 조직` 분류명 자체를 `Guilds / Syndicates / Megacorps`에서 더 판타지 톤의 분류명으로 바꿀지 검토
2. `철의 금융 카르텔`, `침묵의 카르텔`에 걸린 인물/관계 표기를 새 display 후보와 연결
3. 대륙별 어계 규칙이 생기면 영문 display 후보를 다시 다듬기

로 이어간다.

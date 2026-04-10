# Oceanic Core Faction Layers

## Scope

- 현재 문서는 `working/imports/phase4_section8_oceanic_*` 작업본과
  해양 관련 `Section 8` / `15` 감사 메모를 함께 본 1차 통합 메모다.
- 원본은 수정하지 않았다.

## Main Read

해양 대륙은 현재 기준으로 `가문층`과 `길드/경제층`이 이미 충분히 서 있다.
반면 독립 `부족층`은 해상 귀족, 해적 가문, 항만 권력, 교단 권위에 비해 아직 약하다.

## Spine Lock

해양의 현재 표준 읽기는 아래처럼 잠근다.

- 주 spine: `state_house`
- 보조 spine: `guild_market`
- 얇은 층: `tribe_clan`

즉 해양은 `항만 권력과 해상 경제, 해상 귀족 정치가 중심인 대륙`이고,
토착 공동체층은 아직 본선 구조로 확인되지 않았다.

## 1. Golden Armada

- 중간 사회층 성격:
  - `state_house strong`
  - `guild/economy enough`
  - `tribe_clan weak`
- 핵심 근거:
  - `3. 가문 (Noble Houses)` 폴더와 해상 귀족 연합 구조가 직접 확인된다.
  - 함대, 무역 의회, 조선, 재정, 해군식 운영이 함께 선다.
  - 해양 대륙의 정통 권력 구조를 대표하는 중심 샘플이다.
- 대표 파일:
  - `working/imports/phase4_section8_oceanic_golden_armada/황금 함대 (Golden Armada).md`
  - `working/imports/phase4_section8_oceanic_golden_armada/3. 가문 (Noble Houses)`

## 2. Pirate Confederacy

- 중간 사회층 성격:
  - `state_house thin-support`
  - `guild/economy enough`
  - `tribe_clan weak`
- 핵심 근거:
  - 해적 가문, 파벌, 선장 정치가 반복된다.
  - 암시장, 밀무역, 해상 거래망이 실질 경제층으로 기능한다.
  - 혈연과 파벌은 강하지만 토착 공동체보다는 범죄-교역 질서에 가깝다.
- 대표 파일:
  - `working/imports/phase4_section8_oceanic_pirate_confederacy/해적 연합 (Pirate Confederacy).md`

## 3. Church of the Sea

- 중간 사회층 성격:
  - `state_house adjacent`
  - `guild/economy medium-support`
  - `tribe_clan weak`
- 핵심 근거:
  - 성지, 심연 감시, 해상 요새, 교단 권위가 직접 보인다.
  - 교역과 항로 통제에 간접적으로 관여하지만, 본체는 종교-감시 기관이다.
  - 토착 신앙 공동체보다는 제도권 해양 종교 질서에 가깝다.
- 대표 파일:
  - `working/imports/phase4_section8_oceanic_church_of_sea/바다의 교단 (Church of the Sea).md`

## Closure Table

| Target | state_house | guild_market | tribe_clan | Conductor Note |
|---|---|---|---|---|
| `황금 함대` | `strong` | `enough` | `weak` | 해양의 정통 해상 귀족 질서를 대표한다. |
| `해적 연합` | `thin-support` | `enough` | `weak` | 가문과 파벌은 있으나 토착 부족 질서가 아니라 해상 범죄-교역 질서다. |
| `바다의 교단` | `adjacent` | `medium-support` | `weak` | 교단 권위와 심연 감시가 중심이다. |
| `항구 / 해협 / 해상 요새 / 성지` | `support` | `strong-support` | `weak` | 도시망과 항로 기능은 강하지만, 원주민 공동체 근거는 아직 약하다. |

## Separation Rule

앞으로 해양 `Section 8`을 읽을 때는 아래를 분리한다.

1. `해상 귀족 / 함대 정치`
2. `항만 경제 / 조선 / 거래 / 암시장`
3. `토착 공동체 / 원주민 해양 씨족`

현재 확보 근거로는
1과 2는 이미 충분하지만,
3은 아직 `thin`이다.

따라서 해양에서 `선장`, `가문`, `섬`, `성지`, `파도 신앙`, `해녀형 삶`, `혈연` 같은 말이 나와도
곧바로 `tribe_clan enough`로 올리지 않는다.

먼저 아래 질문을 통과해야 한다.

- 함대와 해적 양쪽에 속하지 않는 토착 공동체가 있는가
- 항만 국가나 교단 바깥에서 독립된 섬 씨족 질서가 반복되는가
- 바다에 원래부터 뿌리내린 비국가 공동체가 생활 단위로 보이는가

셋 중 다수가 없으면
`해상 권력 / 항만 경제`로만 기록하고 `tribe_clan thin`을 유지한다.

## Conductor Reading

해양의 인간 서사는 아래처럼 읽는 것이 가장 강하다.

- 항로 상속과 해상 귀족 경쟁
- 함대 질서와 해적 무법의 충돌
- 교역 욕망과 교단 통제의 줄다리기
- 항만, 보험, 조선, 암시장을 둘러싼 해상 경제

즉 해양은 `해상 문명 정치 + 항만 경제`가 함께 선다.

## Conductor Decision

- 이 문서는 `해양 spine sample`로 유지한다.
- 해양은 `가문 enough / 길드 enough / 부족 thin` 대륙으로 잠근다.
- 다음 실제 감사는 `오벨리스크 / 망자의 왕국 / 잊힌 자들의 연합 / 봉인 수호단`을 같은 형식으로 닫는 것이다.

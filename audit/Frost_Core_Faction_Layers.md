# Frost Core Faction Layers

## Scope

- 현재 문서는 `working/imports/phase3_section8_frost_frostborn_tribes` 작업본과
  프로스트 관련 `Section 8` / `15` 감사 메모를 함께 본 1차 통합 메모다.
- 원본은 수정하지 않았다.

## Main Read

프로스트 대륙은 현재 기준으로 `부족층`과 `길드/경제층`이 이미 충분히 서 있다.
반면 독립 `가문층`은 클랜 상층과 부족장 가문 구조로는 확인되지만,
에테르식 왕가 / 문장가문 질서로 보긴 어렵다.

## Spine Lock

프로스트의 현재 표준 읽기는 아래처럼 잠근다.

- 주 spine: `tribe_clan`
- 보조 spine: `guild_market`
- 얇은 층: `state_house`

즉 프로스트는 `혹한 속 부족 정치와 생존 경제가 중심인 대륙`이고,
클랜 상층은 분명하지만 전통 귀족국가 질서는 아직 약하다.

## 1. Frostborn Tribes

- 중간 사회층 성격:
  - `state_house thin`
  - `guild/economy enough`
  - `tribe_clan strong`
- 핵심 근거:
  - `아이스블러드`, `울프스피릿`, `스톰베인`, `프리즌윈드` 같은 클랜 단위가 곧 상층 정치다.
  - 생활 문서에서도 `귀족과 평민` 구도가 반복되어 상층/하층 분화는 확인된다.
  - 상인 협회, 방어 협회, 독점단, 주요 교역로가 실제 생존 경제를 받친다.
- 대표 파일:
  - `working/imports/phase3_section8_frost_frostborn_tribes/프로스트본 연합 (Frostborn Tribes).md`
  - `working/imports/phase3_section8_frost_frostborn_tribes/3. 부족 (Tribes)/0. 프로스트본 연합 관계도.md`
  - `working/imports/phase3_section8_frost_frostborn_tribes/8. 경제 및 상업 (Economy & Commerce)/0. 프로스트본 연합 상인 협회 및 경제 관계도.md`

## Closure Table

| Target | state_house | guild_market | tribe_clan | Conductor Note |
|---|---|---|---|---|
| `프로스트본 연합` | `thin` | `enough` | `strong` | 프로스트 전체 spine을 대표하는 핵심 샘플이다. |
| `오로라 평원` | `adjacent` | `adjacent` | `strong-support` | 부족 전승과 징조 해석이 강한 기억/의식 공간이다. |
| `얼음무덤 언덕` | `adjacent` | `adjacent` | `strong-support` | 혈통과 죽은 자의 이름을 기억하는 공동체 축이다. |
| `푸른 폭풍 요새 / 퍼마프로스트 요새` | `thin-support` | `strong-support` | `adjacent` | 귀족 궁정보다 방어선과 보급, 공방 기능이 먼저 선다. |
| `아이스포지 병기소` | `adjacent` | `strong-support` | `adjacent` | 병기 전승과 장인 기능을 대표하는 workshop 축이다. |

## Separation Rule

앞으로 프로스트 `Section 8`을 읽을 때는 아래를 분리한다.

1. `클랜 상층 / 부족장 가문`
2. `혹한 생존 경제`
3. `국가형 귀족 질서`

현재 확보 근거로는
1과 2는 이미 충분하지만,
3은 아직 `thin`이다.

따라서 프로스트에서 `장로`, `족장`, `귀족`, `가문`, `상층` 같은 말이 나와도
곧바로 `state_house strong`으로 올리지 않는다.

먼저 아래 질문을 통과해야 한다.

- 왕가 / 귀족가 / 문장가문 같은 독립 가문 질서가 있는가
- 클랜 정치와 별개인 정주 궁정 구조가 있는가
- 도시 운영이 혈통 귀족 네트워크로 굴러가는가

셋 중 다수가 없으면
`클랜 상층`으로만 기록하고 `state_house thin`을 유지한다.

## Conductor Reading

프로스트의 인간 서사는 아래처럼 읽는 것이 가장 강하다.

- 혹한 속 생존 계급
- 부족장과 클랜 상층의 책임과 폭력
- 정착보다 이동이 우선인 삶
- 열량, 장비, 보급, 운송을 둘러싼 잔혹한 경제

즉 프로스트는 `북방 부족 서사 + 생존 경제`가 함께 선다.

## Conductor Decision

- 이 문서는 `프로스트 spine sample`로 유지한다.
- 프로스트는 `부족만 강한 대륙`이 아니라 `tribe_clan + guild_market` 대륙으로 잠근다.
- 다음 실제 감사는 `해양 / 황금 함대 / 해적 연합 / 바다의 교단`을 같은 형식으로 닫는 것이다.

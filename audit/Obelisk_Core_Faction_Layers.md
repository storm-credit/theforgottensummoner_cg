# Obelisk Core Faction Layers

## Scope

- 현재 문서는 `working/imports/phase5_section8_obelisk_*` 작업본과
  오벨리스크 관련 `Phase 5` 감사 메모를 함께 본 1차 통합 메모다.
- 원본은 수정하지 않았다.

## Main Read

오벨리스크 대륙은 현재 기준으로 `길드/경제층`이 충분히 서 있고,
`frontier_survival` 구조가 대륙 정체성의 중심이다.
반면 전통 `가문층`은 약하고, `부족층`은 사실상 보이지 않는다.

## Spine Lock

오벨리스크의 현재 표준 읽기는 아래처럼 잠근다.

- 주 spine: `frontier_survival`
- 보조 spine: `guild_market`
- 얇은 지원층: `state_house` only as `nontraditional elite`

즉 오벨리스크는 `붕괴 후에도 생존 조직과 거래 질서가 남아 있는 대륙`이고,
가문 신호가 보이더라도 먼저 `기억 귀족 / 파벌 대표 / 망명 지배층`으로 읽는다.

## 1. Kingdom of the Dead

- 중간 사회층 성격:
  - `state_house thin-support`
  - `guild/economy enough`
  - `frontier_survival strong`
- 핵심 근거:
  - 기억 귀족, 죽은 자의 통치 구조, 폐허 위 질서 유지 비용이 직접 보인다.
  - 거래와 통행, 기억 저당, 생존 비용이 실제로 경제를 이룬다.
  - 전통 왕가라기보다 `죽은 문명 위의 통치 잔존물`에 가깝다.
- 대표 파일:
  - `working/imports/phase5_section8_obelisk_kingdom_of_dead/망자의 왕국 (Kingdom of the Dead).md`

## 2. Forgotten Alliance

- 중간 사회층 성격:
  - `state_house thin-support`
  - `guild/economy enough`
  - `frontier_survival strong`
- 핵심 근거:
  - `3. 가문 (Noble Houses)` 폴더가 있지만, 전체 톤은 생존 연합과 망명 네트워크다.
  - 가문은 정통 귀족 질서라기보다 생존 조직 내부의 실권 엘리트층으로 보인다.
  - 시장, 거래, 보급이 실제 생존 기반으로 기능한다.
- 대표 파일:
  - `working/imports/phase5_section8_obelisk_forgotten_alliance/잊힌 자들의 연합 (Forgotten Alliance).md`
  - `working/imports/phase5_section8_obelisk_forgotten_alliance/3. 가문 (Noble Houses)`

## 3. Seal Wardens

- 중간 사회층 성격:
  - `state_house adjacent`
  - `guild/economy medium-support`
  - `frontier_survival strong`
- 핵심 근거:
  - 봉인 유지, 방어선, 보루, 전선 운영이 중심이다.
  - 정치 귀족보다 기능 조직과 임무 체계가 먼저 선다.
  - 생존과 봉인 유지 비용이 대륙 정체성과 직접 연결된다.
- 대표 파일:
  - `working/imports/phase5_section8_obelisk_seal_wardens/봉인 수호단 (Seal Wardens).md`

## Closure Table

| Target | state_house | guild_market | frontier_survival | Conductor Note |
|---|---|---|---|---|
| `망자의 왕국` | `thin-support` | `enough` | `strong` | 기억 귀족은 보이지만 전통 귀족국가로 읽지 않는다. |
| `잊힌 자들의 연합` | `thin-support` | `enough` | `strong` | 가문 폴더가 있어도 망명-생존 연합이 본체다. |
| `봉인 수호단` | `adjacent` | `medium-support` | `strong` | 기능 조직과 방어선 운영이 핵심이다. |
| `본 마켓 / 잊힌 시장 / 서플라이 포트 알파` | `adjacent` | `strong-support` | `strong-support` | 기억 거래와 보급 경제가 대륙 질서를 떠받친다. |

## Separation Rule

앞으로 오벨리스크 `Section 8`을 읽을 때는 아래를 분리한다.

1. `붕괴 후 생존 조직`
2. `기억 / 유물 / 보급 경제`
3. `전통 귀족 질서`

현재 확보 근거로는
1과 2는 이미 충분하지만,
3은 아직 `thin-support`다.

따라서 오벨리스크에서 `가문`, `귀족`, `왕국`, `통치자`, `원로`, `대표` 같은 말이 나와도
곧바로 `state_house` 대륙으로 올리지 않는다.

먼저 아래 질문을 통과해야 한다.

- 혈통 귀족이 대륙 공통 상층 질서로 반복되는가
- 망명 네트워크나 생존 조직과 별개인 정통 궁정 구조가 있는가
- 경제와 방어선이 아니라 귀족 네트워크가 사회 운영의 중심인가

셋 중 다수가 없으면
`nontraditional elite`로만 기록하고
`frontier_survival + guild_market` 잠금을 유지한다.

## Conductor Reading

오벨리스크의 인간 서사는 아래처럼 읽는 것이 가장 강하다.

- 기억을 버리거나 붙드는 생존 선택
- 버려진 병사와 망명자의 책임
- 봉인 유지 비용과 인간 비용의 충돌
- 무너진 세계에서도 계속 돌아가는 거래와 보급

즉 오벨리스크는 `붕괴 후 생존 질서 + 기억 경제`가 함께 선다.

## Conductor Decision

- 이 문서는 `오벨리스크 spine sample`로 유지한다.
- 오벨리스크는 `frontier_survival + guild_market`, `state_house thin-support` 대륙으로 잠근다.
- 이로써 `1~5 대륙 Section 8 spine sample`이 모두 닫혔다.
- 다음 실제 감사는 `Section 8` 대륙 샘플을 바탕으로 `루트 구조 / 표준 spine / 레거시 분리`를 재정렬하는 것이다.

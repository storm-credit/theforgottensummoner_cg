# Ether Core Faction Layers

## Scope

- 현재 문서는 `working/imports/phase3_section8_ether_*` 작업본과
  `phase2_section14_current_ether` 인물 작업본을 함께 본 1차 통합 메모다.
- 원본은 수정하지 않았다.

## Main Read

에테르 대륙은 현재 기준으로 `가문층`과 `길드/경제층`이 이미 충분히 서 있다.
반면 독립 `부족층`은 정령연합 쪽에서만 부분적으로 강하게 보이고,
대륙 전체 공통 축으로는 아직 약하다.

## Spine Lock

에테르의 현재 표준 읽기는 아래처럼 잠근다.

- 주 spine: `state_house`
- 보조 spine: `guild_market`
- 특수 예외 spine: `tribe_clan` only inside `Spirit Union`

즉 에테르는 `가문과 도시 질서가 중심인 대륙`이고,
정령연합만 그 안에서 별도의 부족 질서를 강하게 보존하는 예외 축이다.

## 1. Saint Haven

- 중간 사회층 성격:
  - `가문 strong`
  - `길드 medium`
  - `부족 weak`
- 핵심 근거:
  - `3. 가문 (Noble Houses)` 하위에 왕가, 교황가, 유력 가문이 분리돼 있음
  - 정치 구조도 성직 지배 + 왕가 예외 + 귀족 가문 교육 네트워크로 정리됨
  - 수도, 주요 도시, 종교 구역이 선명해 공간축도 좋음
- 대표 파일:
  - `working/imports/phase3_section8_ether_sainthaven/성국 (Saint Haven).md`
  - `working/imports/phase3_section8_ether_sainthaven/3. 가문 (Noble Houses)`

## 2. Allied Kingdoms

- 중간 사회층 성격:
  - `가문 strong`
  - `길드/economy medium-strong`
  - `부족 weak`
- 핵심 근거:
  - `3. 가문 (Noble Houses)`가 분리돼 있고 봉건 귀족 체계가 매우 선명함
  - 상단 대표, 연합 상무회, 상업 귀족, 금융 가문이 직접 서술됨
  - 도시, 요새, 국경 방어선이 명확해서 세력-공간 연결도 좋음
- 대표 파일:
  - `working/imports/phase3_section8_ether_allied_kingdoms/왕국연합 (Allied Kingdoms).md`
  - `working/imports/phase3_section8_ether_allied_kingdoms/3. 가문 (Noble Houses)`

## 3. Crossroad Cities

- 중간 사회층 성격:
  - `가문 weak-traditional`
  - `길드/economy very strong`
  - `부족 weak`
- 핵심 근거:
  - 전통 세습 귀족은 약하고 대신 상업 귀족, 금융 귀족, 길드마스터가 핵심
  - 도시 평의회, 상업회의, 용병 연맹, 상단, 은행, 항만 경비 구조가 선명함
  - 자유도시연합은 에테르의 길드/상단/도시경제 허브로 기능
- 대표 파일:
  - `working/imports/phase3_section8_ether_crossroad_cities/자유도시연합 (Crossroad Cities).md`
  - `working/imports/phase3_section8_ether_crossroad_cities/8. 경제 및 상업 (Economy & Commerce)`

## 4. Arcane Society

- 중간 사회층 성격:
  - `가문 weak`
  - `guild/research order strong`
  - `부족 absent`
- 핵심 근거:
  - 세습 귀족이 아니라 실력과 연구 성과가 계급을 결정
  - 초국가 학술 기관 + 지부 + 연구소 + 내부 암약 조직이 뚜렷함
  - 상단/귀족 후원 + 기술 라이선스 구조로 경제 연결도 분명함
- 대표 파일:
  - `working/imports/phase3_section8_ether_arcane_society/마법협회 (Arcane Society).md`
  - `working/imports/phase3_section8_ether_arcane_society/9. 내부 암약 조직 (Clandestine Organizations)`

## 5. Spirit Union

- 중간 사회층 성격:
  - `가문 weak`
  - `부족 strong`
  - `guild/economy thin-medium`
- 핵심 근거:
  - 세습 귀족 부재가 명시됨
  - 수인 부족, 숲 수호자, 샤먼, 부족 영역, 부족장 구조가 직접 등장
  - 희귀 재료 공급과 교역은 보이지만 자유도시처럼 길드 기반이 강하지는 않음
- 대표 파일:
  - `working/imports/phase3_section8_ether_spirit_union/정령연합 (Spirit Union).md`
  - `working/imports/phase3_section8_ether_spirit_union/8. 경제 및 상업 (Economy & Commerce)`

## Closure Table

| Target | state_house | guild_market | tribe_clan | Conductor Note |
|---|---|---|---|---|
| `성국` | `strong` | `medium` | `weak` | 성직 지배와 귀족 가문 질서가 core다. |
| `왕국연합` | `strong` | `medium-strong` | `weak` | 봉건 귀족, 상업 귀족, 금융 가문이 동시에 선다. |
| `자유도시연합` | `weak-traditional` | `very strong` | `weak` | 전통 귀족보다 도시 금융과 길드마스터가 상층이다. |
| `마법협회` | `weak` | `strong` | `absent` | 귀족 질서보다 연구 질서와 후원 구조가 우세하다. |
| `정령연합` | `weak` | `thin-medium` | `strong` | 에테르의 일반 규칙이 아니라 예외적 부족축으로 읽는다. |

## Separation Rule

앞으로 에테르 `Section 8`을 읽을 때는 아래를 분리한다.

1. `대륙 공통 규칙`
2. `정령연합 특수축`

현재 확보 근거로는
에테르 전체를 `state_house + guild_market` 대륙으로 읽는 것이 맞고,
정령연합만 `tribe_clan strong` 예외로 둔다.

따라서 숲, 정령, 수인족, 부족장, 자치 구역 신호가 보여도
곧바로 에테르 전체의 부족층을 `enough`로 올리지 않는다.

먼저 아래 질문을 통과해야 한다.

- 그 신호가 정령연합 바깥에서도 반복되는가
- 왕국연합 변방이나 국경 공동체에도 같은 생활 단위가 보이는가
- 대륙 공통 중간 사회층으로 재등장하는가

셋 중 다수가 없으면
`정령연합 특수축`으로만 기록하고
에테르 전체 부족층은 `thin`을 유지한다.

## Conductor Reading

에테르 대륙은 한 대륙 안에서도 중간 사회층의 결이 다르다.

- 성국 / 왕국연합: 가문 중심
- 자유도시연합: 길드와 금융 중심
- 마법협회: 연구 질서와 후원 구조 중심
- 정령연합: 부족과 자연 계약 중심

즉 에테르는 `부족층이 얇다`기보다,
`정령연합을 제외하면 대륙 공통 중간층이 가문/길드 쪽으로 치우친다`가 더 정확하다.

## Conductor Decision

- 이 문서는 `에테르 spine sample`로 유지한다.
- `정령연합 = 에테르 전체 부족층의 증거`가 아니라 `에테르 내부 특수축`이라는 판정을 잠근다.
- 다음 실제 감사는 `프로스트 / 프로스트본 연합`을 같은 형식으로 닫아 비교 기준을 늘리는 것이다.

# Phase 3 Findings

## What Was Imported

- `phase3_section8_ether_sainthaven`
- `phase3_section8_ether_allied_kingdoms`
- `phase3_section8_ether_crossroad_cities`
- `phase3_section8_ether_arcane_society`
- `phase3_section8_ether_spirit_union`
- `phase3_section8_crimson_dragon_descendants`
- `phase3_section8_crimson_red_desert_tribes`
- `phase3_section8_frost_frostborn_tribes`

## Structural Read

이번 배치로 처음 확인된 중요한 점은,
`가문 / 부족 / 길드`가 단순 추정이 아니라 실제 `8번` 구조의 하위 축으로 존재한다는 것이다.

### Ether

- 에테르 대륙 핵심 세력 5개는 실제로 `3. 가문`, `8. 경제 및 상업`, `9. 내부 암약 조직` 같은 중간 사회층 슬롯을 가진다.
- 즉 에테르의 `가문층 enough / 길드층 enough / 부족층 thin` 판정은 현재 기준으로 방어 가능하다.

대표 근거:

- `working/imports/phase3_section8_ether_sainthaven/3. 가문 (Noble Houses)`
- `working/imports/phase3_section8_ether_allied_kingdoms/3. 가문 (Noble Houses)`
- `working/imports/phase3_section8_ether_crossroad_cities/8. 경제 및 상업 (Economy & Commerce)`
- `working/imports/phase3_section8_ether_arcane_society/9. 내부 암약 조직 (Clandestine Organizations)`

### Crimson

- `붉은 사막 부족`은 부족 연합, 부족장 회의, 상업 부족장, 샤먼, 유목민 계층까지 보여 준다.
- 즉 크림슨은 현재 import 기준으로 `부족층 enough`까지는 올릴 수 있다.
- 다만 대륙 전체 가문층과 독립 길드층은 아직 더 봐야 한다.

대표 근거:

- `working/imports/phase3_section8_crimson_red_desert_tribes/붉은 사막 부족.md`
- `working/imports/phase3_section8_crimson_red_desert_tribes/3. 부족 (Tribes)`

### Frost

- `프로스트본 연합`은 유목·수렵 부족 연합, 대부족장 평의회, 전사 부족장, 사냥 부족장 구조가 분명하다.
- 즉 프로스트도 현재 import 기준으로 `부족층 enough`까지는 올릴 수 있다.
- 가문층과 도시 기반 길드층은 아직 불명확하다.

대표 근거:

- `working/imports/phase3_section8_frost_frostborn_tribes/프로스트본 연합 (Frostborn Tribes).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/3. 부족 (Tribes)`

## Conductor Decision

이제 다음 질문은 `있느냐 없느냐`가 아니라 아래로 바뀐다.

1. 에테르에서 부족층을 별도 보강해야 하는가
2. 크림슨에서 부족층 외 가문/길드층이 얼마나 필요한가
3. 프로스트에서 부족층 외 도시/가문 기반이 얼마나 필요한가
4. 해양과 오벨리스크는 어떤 중간 사회층이 핵심인가

## Rational Next Move

1. `Continental_Adequacy_Map.md`를 이번 배치 기준으로 갱신
2. 에테르 핵심 세력 5개 안에서 가문/길드 구조를 더 읽어 `house / guild` 기준을 고정
3. 크림슨과 프로스트는 부족층이 충분한 대신 어떤 층이 비는지 다음 표로 분리
4. 다음 import는 해양 또는 오벨리스크 중 하나를 골라 균형을 맞춘다

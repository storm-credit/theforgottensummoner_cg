# Phase 1 Findings

## What Was Imported

- `phase1_section8_corrupted_root`
- `phase1_section8_canonical_kirke`
- `phase1_section14_growth_aether`
- `phase1_orphans`

## Section 8 Finding

손상 루트는 `dir=3`, `file=1` 규모의 파편이다.
반면 정식 `키르케 영약회` 대응 구역은 `dir=11`, `file=39` 규모다.

이 비교로 볼 때 합리적인 판단은 다음과 같다.

- 손상 루트는 병렬 정본 후보가 아니다.
- 손상 루트는 `정식 루트에서 빠진 파편 1개를 가진 손상 복제본`으로 보는 것이 가장 자연스럽다.
- 따라서 이후 정리에서도 `마립` 루트는 구조 후보가 아니라 `corrupted fragment`로 다룬다.

## Section 14 Finding

`Aether Continent` 하위는 작은 묶음이다.

- `마법협회 (Arcane Society)`
- `성국 (Saint Haven)`
- `왕국연합 (Allians)`
- `자유도시연합 (Crossroad Cities)`
- `정령 연합 (Spirit Union)`

즉 지금 필요한 것은 대규모 인물 개정이 아니라 아래 두 가지다.

1. `Aether`와 `Ether`의 표기 정규화
2. `Allians`를 오탈자 또는 구버전 표기로 분류

## Orphan Finding

고아 파일 2개는 작업본으로 분리해 두었으므로,
이제 세력 앵커와 현재 분류만 판단하면 된다.

- `[현존] 정보단 여왕 이리나 폰 루즈.md`
- `[현존] 카르텔 수장 칼리크 디트리히.md`

## Conductor Decision

가장 합리적인 다음 순서는 이렇다.

1. `8번`의 손상 루트는 파편으로 분류
2. `14번`의 `Aether`와 `Allians`를 명칭 충돌로 고정
3. 고아 파일 2개의 소속 후보만 먼저 정리
4. 그 다음에만 `_Legacy_` 하위의 실제 충돌 구역을 선별 import

# Section 14 Normalization Plan

## Canonical Root Set

정본 루트 후보는 아래 3개 축으로 잠정 고정한다.

1. `01-14-1. 성장 영웅`
2. `01-14-2. 현존 영웅`
3. `01-14-3. 소환 영웅`

## Known Conflict Points

- `Aether Continent` vs `Ether Continent`
- `Allians` 철자
- `_Legacy_중립세력 (Backup)`
- `01-14-2. 현존 영웅` 루트의 고아 파일 2개

## Orphan Files

- `[현존] 정보단 여왕 이리나 폰 루즈.md`
- `[현존] 카르텔 수장 칼리크 디트리히.md`

## Phase Order

1. 영웅 스키마 확정
2. 관계 타입 어휘 고정
3. 세력명과 대륙명 표기 연결
4. 고아 파일의 정식 소속 경로 결정
5. 그 뒤에만 개별 인물 개정

## First Concrete Operations

- `Aether Continent` 계열 경로를 `Conflict`로 등록
- `Allians`는 오탈자 후보로 등록
- `_Legacy_`는 정본 판단에서 제외
- 고아 파일 2개는 이동 금지 상태로 목록화만 유지

## Stop Rules

- 관계가 자유서술에만 있고 구조화되지 않았으면 문체 수정 금지
- 세력 앵커가 없으면 인물 파일 승격 금지

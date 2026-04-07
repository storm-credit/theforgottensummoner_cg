# Item Canon Schema

## Role

아이템 백과는 흩어진 장비명, 유물명, 악세서리명, 소지 아티팩트를 모으는 정식 편입 축이다.

## Collection Principle

- 인물 문서에 적힌 전용 장비는 즉시 정본으로 고정하지 않는다.
- 세력 문서의 교역품과 실전 장비는 구분한다.
- 마법, 기술, 교리, 몬스터 명칭은 아이템 후보에서 제외한다.
- 아이템 도감 경로 링크가 이미 있으면 `정본 후보 경로 힌트`로만 쓴다.

## Required Fields

- 아이템명
- 분류
  - `weapon`
  - `armor`
  - `accessory`
  - `relic`
  - `unknown`
- 소유자 또는 대표 사용자
- 관련 세력
- 최초 발견 문서
- 변형 표기
- 상태
  - `candidate`
  - `duplicate_candidate`
  - `needs_merge`
  - `ready_for_encyclopedia`

## Promotion Rules

`ready_for_encyclopedia`로 올리려면 아래 3개를 충족해야 한다.

1. 이름이 실제 아이템인지 확인
2. 같은 물건의 변형명 여부 확인
3. 소유자 또는 사용 맥락이 최소 1회 이상 확인

## Do Not Merge Blindly

- 같은 계열 무기라고 해서 같은 아이템으로 합치지 않는다.
- 별칭과 상위 분류명은 같은 열에 두지 않는다.
- 경로명과 실제 아이템명을 혼동하지 않는다.

## Current Reality

- 현재 문서에는 `아이템 도감` 링크와 실제 아이템명이 섞여 있다.
- `14번` 영웅 문서에서 아이템 후보가 많이 나온다.
- `8번` 세력 문서에서는 교역품, 약품, 군수품 후보가 나올 가능성이 높다.

## Longterm Expansion Buckets

나중에 아이템 백과가 커지면 아래 축으로 확장한다.

- 성장형 아이템
- 에고형 아이템
- 설정집 산재 아이템 흡수층
- 계보형 전설 아이템군
- 세트형 장비군
- 컬렉션형 보물군

장기 분류 초안은 `working/crosswalks/Item_Longterm_Taxonomy.md`를 따른다.
수집 욕구 설계 원칙은 `workflow/08_Item_Desire_Design.md`를 따른다.

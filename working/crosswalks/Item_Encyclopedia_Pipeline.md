# Item Encyclopedia Pipeline

## Goal

문서마다 흩어진 아이템을 모아 나중에 아이템 백과로 편입한다.

## Flow

1. 인물 문서, 세력 문서, 지역 문서에서 아이템 후보를 찾는다.
2. 후보를 임시 수집표에 등록한다.
3. 같은 아이템의 변형명과 중복명을 식별한다.
4. 소유자, 관련 세력, 첫 등장 문서를 기록한다.
5. 그 뒤에만 아이템 백과 정식 문서로 승격한다.

## Current Outputs

- 1차 추출 리포트: `working/crosswalks/Extracted_Item_Candidates.md`
- 임시 등록부: `working/crosswalks/Item_Candidate_Register.md`
- 기준 문서: `workflow/07_Item_Canon_Schema.md`
- 수집 욕구 설계: `workflow/08_Item_Desire_Design.md`
- 장기 분류 초안: `working/crosswalks/Item_Longterm_Taxonomy.md`

## First Pass Status

- 현재 작업본 import 기준으로 아이템 후보 `206`개를 수집했다.
- 중복 hotspot은 `황금 (Gold)`, `보석 (Gems)`, `흑요석 (Obsidian)`, `흑철 (Iron)` 같은 재료/공용 항목 쪽에 몰려 있다.
- `14번` 영웅 문서의 `전용 무기 및 아티팩트` 구간이 가장 신뢰도 높은 공급원이다.
- 아직 탈것, 재료, 통신 장치, 생체 장치가 일부 섞여 있어 2차 정제가 필요하다.

## Do Not Do

- 문서 하나만 보고 바로 정본 아이템으로 확정
- 장비명과 유물명을 구분하지 않은 채 일괄 편입
- 서사 장치와 실제 아이템을 같은 기준으로 처리
- 성장형, 에고형, 계보형 전설군, 세트형 장비군, 컬렉션형 보물군을 지금 일반 장비 수집표에 바로 섞지 않는다

## Minimum Fields

- 아이템명
- 변형 표기
- 분류
- 소유자 또는 관련 인물
- 관련 세력
- 최초 발견 문서
- 상태
  - `candidate`
  - `duplicate_candidate`
  - `needs_merge`
  - `ready_for_encyclopedia`

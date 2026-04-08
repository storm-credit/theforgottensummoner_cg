# FS Place Function Register

이 문서는 장소를 단순 배경이 아니라
장면을 여는 기능 단위로 관리하기 위한 장부다.

FS Lore Engine에서 장소는
`어디인가`보다
`무슨 장면을 가능하게 하는가`가 먼저다.

## Place Function Types

### `threshold`

경계와 통과의 장소.

사용:

- 항구
- 성문
- 감시탑
- 검문소
- 경계 요새
- 차원 균열 지대

장면 기능:

- 첫 만남
- 추적
- 검문
- 탈출
- 신분 노출

### `market`

거래와 소문의 장소.

사용:

- 경매장
- 상단 거리
- 암시장
- 자유항
- 환전소
- 보물 감정소

장면 기능:

- 정보 거래
- 위조품 판정
- 아이템 소문
- 빚과 계약
- 세력 간 간접 충돌

### `memory_site`

기억과 기록의 장소.

사용:

- 서고
- 비문
- 묘지
- 봉인 제단
- 오래된 공방
- 몰락 왕가 유적

장면 기능:

- 과거 폭로
- 복선 회수
- 이름의 진짜 의미 확인
- 잊힌 인물 재발견

### `workshop`

제작, 연구, 변형의 장소.

사용:

- 연금술 공방
- 마법 연구소
- 위조 공방
- 대장간
- 마도공학 대공방

장면 기능:

- 아이템 제작
- 실패한 실험
- 장인의 선택
- 진품/가품 대비

### `sanctuary`

보호와 치유, 신뢰 회복의 장소.

사용:

- 성소
- 치유원
- 정령 숲
- 은신처
- 피난 항구

장면 기능:

- 상처 회복
- 관계 회복
- 신뢰 고백
- 다음 액트 전 숨 고르기

### `underworld_node`

음지 조직의 실무 거점.

사용:

- 비밀 거래장
- 채무자 감금 시설
- 땅굴쥐 통로
- 검은 경매소
- 침묵의 상회 연락점

장면 기능:

- 협박
- 암거래
- 밀수
- 청부
- 조직망 노출

## Current Seed Places

| Place | Function | Related Track | Route Link | Resource Link |
|---|---|---|---|---|
| 골든마르크 | `market` | 자유도시 합법 상업권 | `merchant_road` | `trade_luxury` |
| 포트 넥서스 | `threshold` | 자유도시 항만 / 밀수 | `sea_lane`, `underpath` | `food_water`, `trade_luxury` |
| 머시너리 게이트 | `threshold` | 용병 길드 / 중재 | `merchant_road` | `institutional_asset` |
| 검은 고양이 | `underworld_node` | 암시장 연락점 | `underpath` | `secret` |
| 공식 경매장 | `market` | 감정 / 거래 / 소문 | `merchant_road` | `trade_luxury`, `relic_material` |
| 네크로 우물 | `memory_site`, `underworld_node` | 사령 통신 / 묘지 연락 | `arcane_route` | `suppressed_record` |
| 아르카노스 탑 | `workshop` | 마법협회 연구축 | `arcane_route` | `knowledge_asset` |
| 봉인 제단 | `memory_site`, `sanctuary` | 오벨리스크 / 봉인 | `pilgrim_road` | `relic_material` |
| 드래곤포지 | `workshop` | 울프가르 / 용의 후예 제작축 | `mountain_forge_route` | `relic_material`, `craft_secret` |
| 프라이멀 엠버 | `workshop`, `memory_site` | 용의 불꽃 단조 / 고대 화염 기억 | `mountain_forge_route` | `relic_material`, `knowledge_asset` |
| 엘드라칸 학자 구역 | `memory_site` | 에리온 / 엘드라칸 고대어 해석 | `scholar_road` | `knowledge_asset` |
| 용언 도서관 | `memory_site` | 에리온 / 용언 기록 / 금서 해석 | `scholar_road`, `arcane_route` | `knowledge_asset`, `suppressed_record` |
| 몽상가의 바위 | `memory_site`, `sanctuary` | 오그마 / 고룡 조언 / 오래된 기억 | `pilgrim_road` | `knowledge_asset` |
| 지혜의 샘 | `memory_site`, `sanctuary` | 오그마 / 엘드라칸 전승 / 숨 고르기 | `pilgrim_road` | `knowledge_asset` |

## Routing Rule

지도 후보가 생기면 먼저 이 장부에 기능을 붙인다.

기능이 없는 장소는
지도에 그려도 서사적으로 죽은 장소가 될 수 있다.

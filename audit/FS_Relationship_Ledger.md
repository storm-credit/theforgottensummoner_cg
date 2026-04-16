# FS Relationship Ledger

이 문서는 FS 엔진의 `Relationship Ledger` 운용판이다.

핵심은
인물-인물, 인물-조직 관계를
`상태 + 방향 + 마지막 변화 원인`으로 누적하는 것이다.

## Relation Types

- `ally`
- `former_ally`
- `enemy`
- `intermittent_alignment`
- `asymmetric_awareness`
- `rumor_only`
- `crossed_paths`
- `mentor`
- `seeks`
- `fears`

## Ledger

| A | B | Type | Direction | Basis | Last Change Trigger | Recorded Status | Note |
|---|---|---|---|---|---|---|---|
| `세실리아 메르카토르` | `대륙 무역 연맹` | `ally` | `two_way` | `contact table` | `공적 상업 질서 형성` | `active` | 자유도시 낮의 질서 축 |
| `세실리아 메르카토르` | `철의 금융 연맹` | `intermittent_alignment` | `two_way` | `contact table` | `유통/금융 접점` | `unstable` | 협력과 압박이 교차 |
| `세실리아 메르카토르` | `그림자 첩보망` | `asymmetric_awareness` | `one_way_skewed` | `contact table` | `감시 구조 확대` | `active` | 첩보망이 더 많이 안다 |
| `세실리아 메르카토르` | `레이나 브라이트헤븐` | `ally` | `two_way` | `contact table` | `공식 경매 / 외교 협력` | `active` | 자유도시 공적 얼굴 축 |
| `세실리아 메르카토르` | `모이라 와일드웨이브` | `intermittent_alignment` | `two_way` | `contact table` | `항만 그림자 거래 접촉` | `unstable` | 필요할 때만 겹친다 |
| `세실리아 메르카토르` | `벤투라 모레티` | `intermittent_alignment` | `two_way` | `contact table` | `합법/비합법 거래 긴장` | `unstable` | 공존 불가 but 접점 존재 |
| `세실리아 메르카토르` | `도미닉 발사노` | `enemy` | `two_way` | `contact table` | `공적 상업 vs 폭력 회수` | `active` | 도시 경제 대립 |
| `세실리아 메르카토르` | `로렌조 카르미네` | `enemy` | `two_way` | `contact table` | `노예/생체 거래 충돌` | `active` | 윤리선 최전면 대립 |
| `에리온 드라코비스` | `오그마` | `mentor` | `two_way_reverent` | `People Worth Seeking seed` | `엘드라칸 전승 축` | `active` | 기록자와 기억 원천 |
| `울프가르 드래곤포지` | `드락사르 블레이즈포지` | `ally` | `two_way` | `People Worth Seeking seed` | `드래곤포지 제작 축` | `active` | 단조와 연금의 접점 |
| `울프가르 드래곤포지` | `에리온 드라코비스` | `ally` | `two_way` | `People Worth Seeking routing test` | `고대 기술 해석과 제작 지식 연결` | `active` | 용언/고대 기술을 제작 현장으로 옮기는 접점 |
| `오그마` | `울프가르 드래곤포지` | `asymmetric_awareness` | `one_way_reverent` | `People Worth Seeking routing test` | `전승과 장인 문화의 느슨한 접점` | `quiet` | 오그마는 기억의 원천, 울프가르는 물건으로 기억을 남기는 장인 |
| `실비아` | `멜리산드르` | `ally` | `hierarchical` | `deferred hold-split reference` | `시약 계량체계 확립` | `hold` | 상층 의지의 기록화. 범대륙 후기 확장축 안에서만 유지 |
| `그림자 정보단 현장 관리자 계열` | `이리나 폰 루즈` | `ally` | `hierarchical` | `operational lines` | `지부 운영 구조` | `active` | 정보망 실무층 |
| `철의 금융 연맹 집행관 계열` | `칼리크 디트리히` | `ally` | `hierarchical` | `operational lines` | `현장 집행 구조` | `active` | 금융 강제 실무층 |

## Conductor Reading Rule

- 관계는 자유서술보다 이 장부를 먼저 업데이트한다.
- 타입이 바뀌면 `Last Change Trigger`를 반드시 남긴다.
- `rumor_only`와 `enemy`를 섞지 않는다.

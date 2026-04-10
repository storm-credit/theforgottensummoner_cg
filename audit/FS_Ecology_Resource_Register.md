# FS Ecology / Resource Register

이 문서는 자원, 산지, 생태, 희귀 재료를 관리하는 장부다.

아이템, 연금술, 공방, 도시 경제, 세력 충돌은
물리적 근거가 있을 때 훨씬 강해진다.

## Resource Types

### `ore`

광물과 금속.

- 무기, 갑옷, 봉인구, 공방 경제에 연결한다.
- 산지와 운송로가 중요하다.

### `herb`

약초와 연금술 재료.

- 영약, 독, 치료, 환각, 기억 조작과 연결된다.
- 키르케 영약회 같은 조직에 특히 중요하다.

### `beast_part`

마수, 용, 정령, 사령의 부산물.

- 무구 제작과 의식 재료로 쓰일 수 있다.
- 남발하면 몬스터 파밍처럼 보이므로 신중히 둔다.

### `relic_material`

고대 유적, 봉인, 몰락 왕조에서 나온 재료.

- 복선과 연결하기 좋다.
- 정본과 소문을 반드시 분리한다.

### `food_water`

식량, 물, 향신료, 보존식.

- 도시와 군대의 실제 생존 기반이다.
- 사막, 설원, 해양 대륙에서 특히 중요하다.

### `trade_luxury`

사치품과 권위재.

- 귀족 가문, 상단, 경매장, 선물 외교와 연결한다.
- 수집 욕망과 아이템 백과의 도감 문화로 확장 가능하다.

## Resource Questions

새 자원을 추가할 때 묻는다.

1. 어디서 나는가?
2. 누가 통제하는가?
3. 누가 가공하는가?
4. 누가 가장 필요로 하는가?
5. 이동 경로는 어디인가?
6. 위조품이나 대체품이 있는가?
7. 소문과 정본이 갈리는가?

## Seed Resource Snapshot

| Resource | Type | Related Institution | Scarcity | Control | Conflict Use | State |
|---|---|---|---|---|---|---|
| 희귀 약초 | `herb` | 키르케 영약회 | `rare` | `guild_controlled` | 영약 의존과 윤리 갈등 | `active_working` |
| 영약 제조법 | `herb`, `knowledge_asset` | 키르케 영약회 | `restricted` | `institutional_secret` | 치료/독/실험 갈등 | `active_working` |
| 봉인 재료 | `relic_material` | 봉인 수호단 | `rare` | `order_controlled` | 봉인 유지와 금기 해제 | `soft_canon` |
| 장물 보물군 | `trade_luxury`, `relic_material` | 검은 경매소 | `variable` | `underworld_controlled` | 진품/가품/소유권 갈등 | `operational_line` |
| 위조 인장 | `relic_material`, `trade_luxury` | 위조 공방 | `restricted` | `underworld_controlled` | 잠입과 허가문 위조 | `display_canon_candidate` |
| 항만 보존식과 물 | `food_water` | 해양 무역망 | `seasonal` | `port_controlled` | 봉쇄와 항만 생존 | `open_question` |
| 드래곤포지 계열 금속 | `ore`, `beast_part` | Named Notables / 공방 계보 | `legendary` | `lineage_controlled` | 전설 무구 제작 대가 | `named_notable_candidate` |

## Link Rule

- 아이템 욕망 설계는 `workflow/08_Item_Desire_Design.md`와 연결한다.
- 자산/비밀은 `FS_Asset_Secret_Register.md`와 연결한다.
- 소문성 재료는 `FS_Rumor_Fact_Register.md`와 연결한다.

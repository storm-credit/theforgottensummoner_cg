# FS Scene Pressure Checklist

이 문서는 FS Story Engine이
장면을 정보 전달로만 흘러가지 않게 하기 위한 체크리스트다.

설정집의 정보가 장면으로 내려갈 때는
항상 압력이 필요하다.

## Pressure Types

### `time_pressure`

시간 제한.

예:

- 항만 봉쇄 전 통과해야 한다.
- 경매가 시작되기 전에 진품을 판별해야 한다.
- 봉인 의식 전 마지막 연락을 받아야 한다.

### `identity_pressure`

정체를 숨기거나 드러내야 하는 압력.

예:

- 영웅이지만 이름을 숨긴다.
- 유명 NPC형 명사가 자신의 저술을 부정한다.
- 세력 소속이 문서 경로와 실제 맥락에서 다르게 보인다.

### `debt_pressure`

빚과 계약 압력.

예:

- 채권 장부
- 용병 계약
- 항만 허가
- 과거 은혜

### `rumor_pressure`

소문 때문에 생기는 압력.

예:

- 멸실된 보물이 목격되었다.
- 누군가 배신자로 알려졌다.
- 어느 현자가 금서를 해독했다는 소문이 돈다.

### `spatial_pressure`

장소 자체가 주는 압력.

예:

- 검문소
- 항만
- 경매장
- 묘지
- 봉인 제단
- 비밀 거래장

### `moral_pressure`

선택 비용.

예:

- 치료를 위해 금지된 재료를 쓴다.
- 진실을 숨겨 누군가를 살린다.
- 위조품을 진품처럼 유통시켜 전쟁을 막는다.

## Scene Checklist

장면을 만들 때 최소 하나 이상 있어야 한다.

| Check | Question |
|---|---|
| `goal` | 이 장면에서 인물은 무엇을 얻으려 하는가? |
| `pressure` | 무엇이 그 시도를 어렵게 만드는가? |
| `cost` | 성공해도 무엇을 잃는가? |
| `turn` | 장면 끝에서 무엇이 바뀌는가? |
| `reveal` | 독자에게 새로 드러나는 것은 무엇인가? |
| `withhold` | 아직 숨겨야 할 것은 무엇인가? |
| `ledger` | 관계, 액트 결과, 복선 장부 중 어디에 연결되는가? |

## Seed Scene Pressure Links

| Axis | Likely Pressure | Linked Register |
|---|---|---|
| 자유도시 항만 | `time_pressure`, `identity_pressure`, `spatial_pressure` | `FS_Travel_Logistics_Register.md` |
| 검은 경매소 | `rumor_pressure`, `moral_pressure`, `debt_pressure` | `FS_Rumor_Fact_Register.md` |
| 키르케 영약회 | `moral_pressure`, `time_pressure` | `FS_Ecology_Resource_Register.md` |
| 봉인 제단 | `spatial_pressure`, `moral_pressure` | `FS_Place_Function_Register.md` |
| Named Notables 조언 장면 | `identity_pressure`, `truth_question` | `FS_Story_Act_Question_Register.md` |

## Conductor Reading Rule

설정 설명만 있는 장면은 보류한다.

그 설정을 말하는 순간
누군가의 선택, 관계, 시간, 비용이 달라져야 한다.

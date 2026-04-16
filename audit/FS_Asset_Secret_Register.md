# FS Asset / Secret Register

이 문서는 인물, 세력, 장소가 가진
자산과 비밀을 관리하기 위한 장부다.

자산은 반드시 보물만을 뜻하지 않는다.
영향력, 문서, 길, 기억, 계약, 혈통, 약점도 자산이다.

## Asset Types

### `material_asset`

눈에 보이는 물건.

- 무기
- 약품
- 보물
- 지도
- 증표
- 봉인구
- 원료

### `institutional_asset`

조직이 가진 권한과 인프라.

- 항만 허가권
- 무역 면허
- 경매 목록
- 용병 계약장
- 채권 장부
- 통행증 발급권

### `knowledge_asset`

지식과 기록.

- 연금술 레시피
- 고대 비문 해독법
- 보물 도감
- 위조 판별법
- 실종 영웅의 마지막 행적

### `relationship_asset`

관계 자체가 힘이 되는 경우.

- 옛 동료
- 빚진 사람
- 소문만 아는 인물
- 서로의 정체를 아는 사이
- 일방적으로 보호받는 인물

### `secret`

노출되면 관계나 세력 균형이 바뀌는 정보.

- 진짜 소속
- 위조품 진위
- 숨은 후원자
- 금지된 거래
- 사라진 혈통
- 폐기된 실험

## Seed Entry Snapshot

| Holder | Asset / Secret | Type | State |
|---|---|---|---|
| 검은 경매소 계열 | 장물 출처와 진품 목록 | `knowledge_asset` | `active_working` |
| 철의 금융 연맹 계열 | 채권 장부와 압류권 | `institutional_asset` | `display_canon_candidate` |
| 키르케 영약회 | 영약 제조법과 실험지 | `knowledge_asset` | `active_working` |
| 네크로 우물 연락망 | 죽은 자의 잔향 정보 | `secret` | `soft_canon` |
| 15 People Worth Seeking | 저술서, 감정법, 공방 계보 | `knowledge_asset` | `named_notable_candidate` |
| 자유도시 항만층 | 입항 허가와 밀수 통로 | `institutional_asset` | `operational_line` |
| 파브리스 가문 | 전비 어음과 관세율 | `institutional_asset` | `verify_before_15_context` |
| `FS-HANDOFF-SEED-001` | 전설 무구 후보가 필요해지는 압력 | `material_asset` | `handoff_test / no_canon_name` |

## Use Rule

복선으로 쓸 수 있는 자산은
`FS_Foreshadow_Payoff_Register.md`에도 연결한다.

관계를 바꾸는 비밀은
`FS_Relationship_Ledger.md`에도 연결한다.

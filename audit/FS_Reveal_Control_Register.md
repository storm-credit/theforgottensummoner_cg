# FS Reveal Control Register

이 문서는 FS Story Engine이
독자에게 언제 무엇을 보여줄지 관리하기 위한 장부다.

설정집에서는 이미 알고 있어도,
소설에서는 늦게 보여줘야 하는 정보가 있다.

## Reveal States

### `hidden`

아직 독자에게 보이지 않는다.

### `hinted`

분위기나 작은 단서만 보인다.

### `misread`

독자가 일부러 잘못 이해하게 둘 수 있다.

### `partial_reveal`

일부만 드러난다.

### `full_reveal`

정체나 사실이 완전히 드러난다.

### `recontextualized`

이미 보인 정보의 의미가 뒤집힌다.

## Reveal Categories

| Category | Examples |
|---|---|
| `identity` | 진짜 이름, 소속, 혈통 |
| `artifact` | 진품/가품, 저주, 결번 |
| `institution` | 기관의 금기 기억, 공식 서사와 실제 과거 |
| `relationship` | 한때 동료, 비대칭 인지, 과거 빚 |
| `rumor` | 소문과 사실의 차이 |
| `route` | 숨은 통로, 항로, 봉쇄 이유 |

## Seed Reveals

| Reveal ID | Hidden Information | Category | Current State | Possible Payoff | Linked Register |
|---|---|---|---|---|---|
| `FS-RV-001` | 자유도시 그림자 경제의 실제 깊이 | `institution` | `hinted` | 세실리아의 공적 질서 인식 변화 | `FS_Story_Act_Question_Register.md` |
| `FS-RV-002` | 검은 경매소 진품 목록 | `artifact` | `hidden` | 진품/가품 갈등 회수 | `FS_Foreshadow_Payoff_Register.md` |
| `FS-RV-003` | 키르케 영약회 실험의 윤리 비용 | `institution` | `hinted` | 치료와 의존의 대가 | `FS_Act_Outcome_Ledger.md` |
| `FS-RV-004` | 봉인 수호단 공식 전승과 실제 희생의 차이 | `institution` | `hidden` | 오벨리스크 축 재맥락화 | `FS_Institution_Memory_Register.md` |
| `FS-RV-005` | Named Notables가 가진 저술/감정/제작법의 진짜 출처 | `identity`, `artifact` | `partial_reveal` | 조언자가 아니라 복선 소유자로 전환 | `FS_Asset_Secret_Register.md` |

## Conductor Rule

설정집에 적혀 있다고 해서
소설 초반에 모두 공개하지 않는다.

특히 아래는 늦게 드러낼수록 좋을 수 있다.

- 기관의 금기 기억
- 아이템 진품 여부
- 소문과 사실의 차이
- 15번 명사형 영웅의 과거 역할
- 세력의 숨은 채무 관계


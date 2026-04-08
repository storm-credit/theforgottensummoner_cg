# FS Institution Memory Register

이 문서는 세력과 기관이
무엇을 기억하고,
무엇을 두려워하고,
무엇을 반복하는지 관리하는 장부다.

세력은 현재 이해관계만으로 움직이지 않는다.
오래된 패배, 배신, 조약, 금기, 영웅의 흔적이
현재 반응을 결정한다.

## Memory Types

### `founding_memory`

창립과 기원에 관한 기억.

- 왜 생겼는가
- 누구에게 빚졌는가
- 어떤 맹세를 아직 지키는가

### `wound_memory`

패배, 배신, 학살, 몰락의 기억.

- 누구를 믿지 않는가
- 어떤 이름에 과민 반응하는가
- 어떤 장소를 금지하는가

### `debt_memory`

빚과 은혜의 기억.

- 오래된 후원자
- 구명 은인
- 갚지 못한 계약
- 세대에 걸친 채무

### `forbidden_memory`

봉인하거나 지운 기억.

- 실패한 실험
- 숨겨진 혈통
- 삭제된 기록
- 금지된 영웅

### `public_legend`

세력이 밖으로 내세우는 공식 서사.

- 창립 영웅
- 승전담
- 성인전
- 공식 연대기

## Current Seed Institutions

| Institution | Memory Type | Possible Story Function |
|---|---|---|
| 성국 | `public_legend`, `forbidden_memory` | 신앙과 정치적 정본 충돌 |
| 자유도시연합 | `debt_memory`, `wound_memory` | 거래, 배신, 채무 관계 |
| 마법협회 | `forbidden_memory` | 실패한 연구와 금지 지식 |
| 정령연합 | `founding_memory` | 자연 계약과 부족 기억 |
| 황금 함대 | `public_legend`, `debt_memory` | 해상 귀족 명예와 항로 권리 |
| 침묵의 상회 | `forbidden_memory` | 지운 거래와 비밀 계약 |
| 봉인 수호단 | `founding_memory`, `wound_memory` | 경계와 희생의 기억 |

## Use Rule

세력 충돌을 볼 때
현재 이익만 보지 않는다.

항상 질문한다.

1. 이 세력은 무엇을 기억하는가?
2. 이 세력은 무엇을 숨기는가?
3. 이 세력은 어떤 이름을 들으면 반응하는가?
4. 이 기억이 인물 관계를 어떻게 바꾸는가?

## Rumor / Fact Link Rule

`public_legend`와 `forbidden_memory`는
독자와 인물에게 소문, 선전, 금서, 억압된 기록으로 드러날 수 있다.

따라서 아래 경우에는 `FS_Rumor_Fact_Register.md`에 함께 연결한다.

- 공식 서사가 실제 과거와 다를 때
- 숨겨진 실패나 배신이 현재 세력 반응을 바꿀 때
- 금기 기억이 아이템, 장소, 명사형 인물과 이어질 때
- 어떤 세력이 특정 소문으로 이익을 볼 때

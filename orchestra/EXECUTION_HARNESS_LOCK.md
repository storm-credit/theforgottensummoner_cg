# Execution Harness Lock

이 문서는 `MCP`, `Skills`, `Agents`, `Hooks`가
어떤 순서로 물리고 어디서 멈추는지 고정하는 실행 하네스 기준서다.

목적:

- 도구, 스킬, 에이전트, 장부가 뒤섞여 역할이 흔들리지 않게 한다.
- 같은 작업이 들어와도 같은 순서로 읽고, 분기하고, 기록하게 만든다.
- Conductor의 최종 반영권은 유지하면서도 병렬 운용 효율은 살린다.
- 분량 검사를 선택 규칙이 아니라 하네스 핵심 게이트로 고정한다.

## Harness Order

기본 실행 순서:

1. `MCP`
2. `Skills`
3. `Agents`
4. `Hooks`
5. `Registers`
6. `Next Workstream`

## Responsibility Lock

### 1. MCP

역할:

- 외부 맥락, 도구 응답, 검색 결과, 리스트, fetch를 가져온다.
- 현재 작업에 필요한 사실과 입력을 좁힌다.

금지:

- 정본 판정
- 최종 문서 반영
- 상태 라벨 확정

### 2. Skills

역할:

- 반복 작업의 읽기 순서와 출력 형식을 고정한다.
- 특정 감사, 분류, 라우팅 작업을 표준화한다.

금지:

- 스킬만으로 정본을 선언하지 않는다.
- 스킬이 Conductor 없이 최종 구조를 바꾸지 않는다.

### 3. Agents

역할:

- 병렬 읽기
- 축별 진단
- 수정 제안

금지:

- 최종 승인
- 단독 커밋
- 같은 파일 동시 최종 편집

### 4. Hooks

이 저장소에서 hook은 코드 이벤트가 아니라
`단계 전환 때 반드시 거는 운영 게이트`로 정의한다.

즉,
어떤 작업이 다음 단계로 넘어가기 전에
빠지면 안 되는 확인 / 기록 / 라우팅 장치다.

#### Hook Types

| Hook | Timing | Purpose |
|---|---|---|
| `pre_scope_hook` | 작업 시작 직후 | 현재 작업 단위, 대상 문서, 엔진 층을 고정 |
| `pre_dispatch_hook` | 에이전트 분할 직전 | 정말 병렬이 필요한지, 어떤 역할로 나눌지 확정 |
| `story_to_lore_handoff_hook` | Story Engine 신규 설정 제안 직후 | 장면 편의 설정을 Lore route와 register write로 되돌려 보낸다 |
| `episode_volume_gate` | 각 화 초안 완료 직후, 최종 반영 직전 | 회차 분량이 최소 기준을 넘는지 강제 검사하고, 미달이면 재작성으로 되돌린다 |
| `pre_write_hook` | 문서 반영 직전 | Source / State / Route / Naming / Register 연결 확인 |
| `post_write_hook` | 문서 반영 직후 | OPEN_INDEX, Workstream, Dispatch Log, Change Log 갱신 여부 확인 |
| `pre_close_hook` | 턴 종료 직전 | 다음 실제 작업선과 남은 보류 항목 고정 |

#### Volume Gate Rule

- 분량 검사는 하네스 구조에서 최상위 핵심 검사 중 하나다.
- 이 검사는 `1화마다` 빠짐없이 건다.
- 분량 미달은 경고가 아니라 실패로 본다.
- 분량이 기준에 못 미치면 해당 화는 `무조건 재작성`으로 되돌린다.
- 다른 장점이 있어도 분량 미달 상태로 통과시키지 않는다.

### 5. Registers

역할:

- 판정 기억
- 상태 이동
- 장소 기능
- 충돌/보류 흔적

대표 장부:

- `FS_Decision_Ruling_Register`
- `FS_Canon_Change_Log`
- `FS_Slot_Maturation_Register`
- `FS_Place_Function_Register`

### 6. Next Workstream

모든 실행은 마지막에
`다음 실제 작업이 무엇인가`
로 닫아야 한다.

즉,
하네스의 마지막 산출물은
늘 `다음 턴의 시작점`이어야 한다.

## Minimal Execution Rule

작업이 작아도 아래는 유지한다.

1. `pre_scope_hook`
2. 필요한 경우만 `Skills` 또는 `Agents`
3. 회차 작업이면 `episode_volume_gate`
4. `pre_write_hook`
5. `post_write_hook`
6. `pre_close_hook`

## Conductor Note

이 문서의 핵심은
`무엇을 쓸 것인가`보다
`무슨 순서로만 움직일 것인가`
를 잠그는 데 있다.

특히 회차 집필에서는
`분량 기준 통과 여부`
가 하네스 통과 여부 자체를 좌우한다.

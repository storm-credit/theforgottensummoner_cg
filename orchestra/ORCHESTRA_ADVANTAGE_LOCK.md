# Orchestra Advantage Lock

이 문서는 이 저장소에서 오케스트라 방식을 왜 쓰는지,
그리고 어떤 이점을 반드시 유지해야 하는지 잠그는 기준서다.

## Locked Advantages

### 1. Parallel Diagnosis

- 같은 대상을 여러 관점으로 동시에 읽어 병목을 줄인다.
- 긴 감사 문서, 엔진 장부, 대륙 압축표를 순차가 아니라 병렬로 닫는다.

### 2. Split Judgment

- 라우팅, 이름 톤, 등급, 장소 기능, 관계를 한 번에 섞어 보지 않는다.
- 각 역할은 자기 질문만 맡고, 최종 종합은 Conductor가 맡는다.

### 3. Single Writer Rule

- 서브에이전트는 읽기/진단/제안까지만 맡는다.
- 최종 문서 반영, 구조 결정, 커밋은 Conductor만 한다.

### 4. Traceable Dispatch

- 어떤 배치가 어떤 질문을 맡았는지 남겨야 다음 턴에서도 이어진다.
- 실제 배치는 항상 `AGENT_DISPATCH_LOG.md`에 기록한다.

### 5. Reusable Expansion

- 새 대륙, 새 장부, 새 파생 문서가 와도 같은 절차로 편입할 수 있어야 한다.
- 따라서 `ACTIVE_AGENT_SPLIT.md`, `RUNBOOK.md`, `AGENT_DISPATCH_LOG.md`는 함께 유지한다.

### 6. Locked Expert Memory

- 오케스트라는 매번 전문가를 다시 정하지 않는다.
- `필수 전문가 roster`를 고정해, 긴 작업이 이어져도 분배 기준을 잃지 않는다.
- 세부 기준은 `REQUIRED_EXPERT_ROSTER_LOCK.md`를 따른다.

## Lock Rules

1. 병렬 운용은 `많이 부르기`가 아니라 `먼저 분리해서 나중에 섞기`를 위한 것이다.
2. 같은 파일의 최종 편집권은 언제나 Conductor 하나로 잠근다.
3. 동일 대상에 대한 판단이 갈리면 강행하지 않고 `Open Question` 또는 보류로 분리한다.
4. 배치 목적, 역할, 범위, 상태가 없으면 오케스트라 배치로 간주하지 않는다.

## Repository-Fit Reading

이 프로젝트에서 오케스트라가 특히 유리한 구간:

- `15 People Worth Seeking`과 `Place Register`가 같이 엮일 때
- `verify_before_15`와 `display_canon_candidate`가 동시에 걸릴 때
- 대륙 압축표와 엔진 장부를 한 배치 안에 같이 갱신할 때
- 다음 작업선까지 바로 고정해야 할 때

## Conductor Note

오케스트라는 창작을 느리게 하는 절차가 아니다.

오히려
`빨리 읽고, 늦게 섞고, 한 번만 확정하기`
위한 운영 장치다.

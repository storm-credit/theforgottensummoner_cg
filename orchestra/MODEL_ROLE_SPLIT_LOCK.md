# Model Role Split Lock

이 문서는 이 저장소에서
`ChatGPT형 판단`과 `Codex형 실행`을
어떻게 나눠 쓰는지가 흔들리지 않도록 고정하는 기준서다.

핵심은 `브랜드명`이 아니라
`지금 작업이 무엇을 먼저 요구하는가`다.

## Core Rule

- `판단이 먼저인 작업`은 ChatGPT형 대화 검토가 우선이다.
- `파일 반영과 정합성이 먼저인 작업`은 Codex 오케스트라가 우선이다.
- 최종 저장소 반영, 장부 갱신, 브랜치/커밋/푸시는 Codex Conductor가 맡는다.

## Mode-Based Reading

현재 저장소 기준으로는
`FS Engine Writing Craft Map`의 세 모드를 기준으로 읽는 것이 가장 안전하다.

### 1. ChatGPT-First

아래는 `판단 우선` 작업이다.

- 서사 개연성
- 감정선
- 캐릭터 아크
- 세계관 밀도
- 톤과 철학
- 같은 설정안 여러 개 중 어떤 방향이 더 작품에 맞는지 비교
- 장면 잠재력, 여운, 상징성 판단

이때 필요한 산출물:

- 방향 메모
- 선택 기준
- 버릴 안과 남길 안
- 금지선

이 단계는 보통
`Story Craft`, `Plausibility`, `Expansion Control` 질문에 가깝다.

### 2. Codex-First

아래는 `실행 우선` 작업이다.

- 대량 검색
- 문서 간 정합성 점검
- crosswalk 작성
- register 갱신
- named candidate queue 관리
- naming normalization
- 중복명 / 충돌명 정리
- place-first slot / role slot 유지 판정의 장부 반영
- workstream 고정
- 브랜치, 커밋, 푸시
- 파이프라인, 자동화, 스크립트

이 단계는 보통
`Lore Operations`, `Archive Routing`, `Canon Tier`, `Naming Normalization` 질문에 가깝다.

### 3. Hybrid

이 저장소에서 가장 자주 써야 하는 방식이다.

#### Pattern A

1. ChatGPT형 검토로 방향을 먼저 고른다.
2. Codex가 관련 evidence를 찾는다.
3. Codex가 문서, 장부, 작업선을 잠근다.

#### Pattern B

1. Codex가 evidence bundle과 충돌 지점을 먼저 정리한다.
2. ChatGPT형 검토로 서사/철학/감정선 판정을 내린다.
3. Codex가 그 결론을 저장소 구조에 반영한다.

## Practical Trigger

아래 중 둘 이상이면 ChatGPT-first를 우선 검토한다.

- 파일보다 방향이 더 중요하다
- 여러 설정안이 모두 가능해 보인다
- 감정선, 개연성, 상징성이 핵심이다
- "무엇이 더 작품답나"가 주요 질문이다
- 아직 어느 문서에 쓸지도 명확하지 않다

아래 중 둘 이상이면 Codex-first를 우선 검토한다.

- 이미 만질 파일이 분명하다
- 여러 문서를 한꺼번에 맞춰야 한다
- queue, register, crosswalk, index를 갱신해야 한다
- 중복/충돌/표기 drift를 정리해야 한다
- 브랜치, 커밋, 푸시, 자동화가 따라온다

## Current Project Judgment

이 프로젝트의 현재 메인선은
Codex 오케스트라가 특히 강한 구간에 있다.

이유:

- `audit/` 문서군이 매우 크다
- `register`, `queue`, `crosswalk`, `index`, `workstream`이 서로 강하게 연결돼 있다
- 같은 판단을 여러 문서에 동시에 반영해야 한다
- branch/commit/push까지 같은 턴에 이어지는 경우가 많다

즉,
지금처럼 `14/15`, `Named Notables`, `slot`, `handoff`, `species side-track`을
실제 문서로 잠그는 작업은 Codex가 메인인 편이 맞다.

## Where ChatGPT Adds More Value

다만 아래는 ChatGPT형 검토를 먼저 쓰는 편이 더 효율적일 수 있다.

- 종족 체계의 철학과 세계관 톤 결정
- 특정 세력이 왜 기억되어야 하는지
- 설정이 장면으로 살아나는지
- 인물 관계의 여운과 상처 비용
- "이 설정을 넣으면 작품이 더 깊어지는가, 더 산만해지는가" 판단

즉,
`설정집 내용은 ChatGPT, 설정집 파이프라인은 Codex`
라는 말은 절반만 맞다.

이 저장소에 더 맞는 잠금은 아래다.

- `방향 판단`: ChatGPT 우세
- `증거 수집 + 저장소 반영`: Codex 우세
- `최종 캐논 잠금`: Codex Conductor

## Conductor Lock

- ChatGPT형 판단 메모만으로 저장소를 직접 바꾸지 않는다.
- Codex는 방향이 불명확한 상태에서 혼자 세계관 철학을 과도하게 확정하지 않는다.
- 불확실한 경우에는 `ChatGPT형 판단 -> Codex 반영` 순서를 우선한다.

## Current Recommendation

현재 이 저장소의 기본값은 아래로 둔다.

1. `문서 감사 / 구조 정리 / 정합성 / 자동화 / 커밋`은 Codex-first
2. `세계관 철학 / 종족 설계 / 서사 개연성 / 감정선`은 ChatGPT-first 검토 권장
3. 애매하면 Hybrid로 처리
4. 저장소 최종 반영은 언제나 Codex Conductor가 마감

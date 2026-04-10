# Writer Engine

> 이 문서는 `FS Engine`의 구버전 이름으로 본다.
> 실제 운용 기준은 `workflow/11_FS_Engine.md`를 우선한다.

## Goal

외부 작법 이론을 `읽을거리`로 두지 않고,
아스트라리스 오케스트라가 실제로 쓰는 `판단 엔진`으로 통합한다.

이 엔진은 특정 작가의 공식을 그대로 베끼지 않는다.
대신 여러 관점을 역할별로 분해해 설정집 정리 기준에 맞게 재조립한다.

## Engine Layers

### 1. Story Architecture Engine

역할:

- 대륙, 세력, 인물, 욕망, 충돌을 한 시스템으로 묶는다
- 이야기의 큰 줄기가 어디로 흐르는지 본다

오케스트라 적용:

- `세계관 -> 대륙 -> 세력 -> 인물` 순서 유지
- 각 세력이 서사의 무대인지, 장식인지 판별
- 액트마다 무엇이 정서적으로 끝나는지 점검

## 2. Conflict Engine

역할:

- 누가 왜 충돌하는지
- 같은 사실을 왜 다르게 해석하는지
- 관계가 왜 비틀리는지 본다

오케스트라 적용:

- 같은 편 / 다른 편 / former ally / rumor_only / crossed_paths 같은 관계 타입 관리
- 세력 충돌과 인물 충돌을 같은 축에서 본다
- 단순 선악이 아니라 관점 충돌로 정리

## 3. Character Arc Engine

역할:

- 인물이 무엇을 믿고, 무엇을 잃고, 무엇이 바뀌는지 본다
- 강함보다 감정 비용과 변화 방향을 본다

오케스트라 적용:

- `14번` 인물 문서에서 능력보다 관계와 비용을 우선 점검
- 성장 영웅 / 현존 영웅 / 소환 영웅 구분이 실제 아크와 맞는지 검토
- `15번` 예정 축으로 회수할 중간 인물도 서사 기능 기준으로 분류

## 4. Relationship Network Engine

역할:

- 인물들을 네트워크로 보고 중심성, 고립, 군집, 매개를 본다
- 누가 지나치게 모든 사건을 독점하는지 판별한다

오케스트라 적용:

- 주인공과 핵심 영웅에게 과도한 연결이 몰리는지 경고
- 세력과 인물 간 연결 밀도를 점검
- `스침`, `소문`, `비대칭 인지`, `과거 인연` 같은 간접 연결도 기록

## 5. Scene and Consequence Engine

역할:

- 이 설정이 실제 장면으로 이어지는지 본다
- 사건 이후 무엇이 달라지는지 본다

오케스트라 적용:

- 문서가 설명만 하고 실제 장면 잠재력이 없는 경우 경고
- 액트가 끝난 뒤 남는 정서 변화가 있는지 점검
- 장소와 세력이 실제 장면의 압력을 주는지 확인

## 5A. Episode Volume Gate

역할:

- 각 화가 최소 분량 기준을 넘는지 강제 검사한다
- 장면 수, 감정 축, 사건 압력이 있어도 분량 미달이면 통과시키지 않는다

오케스트라 적용:

- `1화마다` 반드시 분량 검사를 건다
- 분량 미달은 부분 수정이 아니라 `재작성` 트리거로 본다
- 분량 검사는 선택형 QA가 아니라 집필 통과 게이트다
- 이 게이트를 통과하지 못한 화는 다음 엔진 단계로 넘기지 않는다

## 6. Expansion Control Engine

역할:

- 설정이 넓어질 때 핵심을 해치지 않도록 제어한다
- 멋있는 설정과 필요한 설정을 구분한다

오케스트라 적용:

- `범대륙`은 후기 확장으로 미룸
- 아이템, 지도, 생활상은 메인 축을 막지 않는 소진행으로 운영
- 레거시와 확장 문서는 삭제보다 격리와 보류 우선

## Engine Routing

각 작업 단계에서 어떤 엔진을 먼저 쓰는지 고정한다.

### 세계관

1. Story Architecture Engine
2. Conflict Engine
3. Expansion Control Engine

### 대륙

1. Story Architecture Engine
2. Relationship Network Engine
3. Expansion Control Engine

### 가문 / 부족 / 길드

1. Conflict Engine
2. Character Arc Engine
3. Scene and Consequence Engine

### 세력

1. Story Architecture Engine
2. Conflict Engine
3. Scene and Consequence Engine

### 인물

1. Character Arc Engine
2. Relationship Network Engine
3. Conflict Engine

### 관계망

1. Relationship Network Engine
2. Conflict Engine
3. Scene and Consequence Engine

### 아이템 / 지도 / 확장 백과

1. Expansion Control Engine
2. Scene and Consequence Engine
3. Story Architecture Engine

### 회차 / 에피소드 초안

1. Episode Volume Gate
2. Scene and Consequence Engine
3. Character Arc Engine

## Conductor Rule

Conductor는 어떤 문서를 볼 때마다 최소한 아래를 판단한다.

1. 이 문서는 어느 엔진으로 먼저 봐야 하는가
2. 이 기준에서 필요한 건 구조인가, 갈등인가, 인물 변화인가
3. 이 문서는 메인 축인가, 소진행인가
4. 이 시점에 확정해야 하는가, 보류해야 하는가
5. 회차 초안이라면 분량 기준을 넘겼는가

## Do Not Do

- 특정 작법서를 절대 법칙처럼 쓰지 않는다
- 영웅서사 템플릿 하나로 모든 인물을 밀어 넣지 않는다
- 관계망 문제를 파워 밸런스로 덮지 않는다
- 설정 확장을 구조 안정화보다 앞세우지 않는다
- 분량 미달 회차를 다음 단계로 넘기지 않는다

## Working Use Snapshot

오케스트라는 아래 방식으로 이 엔진을 쓴다.

- `에테르 / 크림슨 / 프로스트`의 중간 사회층은 `Story Architecture + Conflict + Character Arc`로 본다
- `14번` 인물 문서는 `Character Arc + Relationship Network`로 본다
- 아이템과 지도는 `Expansion Control` 아래 소진행으로 유지한다

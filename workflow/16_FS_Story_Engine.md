# FS Story Engine

`FS Story Engine`은 실제 소설 집필과 장면 설계를 위한 엔진이다.

설정집이
`무엇이 존재하는가`를 다룬다면,
Story Engine은
`그것이 언제, 누구에게, 어떤 감정으로 드러나는가`를 다룬다.

## Scope

FS Story Engine이 담당하는 것:

- 액트별 질문
- 장면 목표
- 갈등 압력
- 캐릭터 아크
- 감정 비용
- POV
- 대화와 침묵
- 복선 배치와 회수 타이밍
- 독자가 언제 무엇을 알게 되는가
- 액트 종료 후 관계 변화

담당하지 않는 것:

- 폴더 위치
- 정본 티어
- 레거시 격리
- 이름 정규화 자체
- 설정 문서의 저장 구조

이 영역은 `FS Lore Engine`이 우선한다.

## Core Modules

### 1. Act Question

각 액트는 하나의 감정적 질문을 가져야 한다.

예:

- 이 인물은 누구를 믿을 수 있는가?
- 이 동맹은 끝까지 유지되는가?
- 이 소문은 사실인가?
- 이 영웅은 무엇을 잃고 성장하는가?

연결 장부:

- `audit/FS_Story_Act_Question_Register.md`

### 2. Character Arc

인물이 무엇을 믿고,
무엇을 잃고,
무엇을 바꾸는지 추적한다.

중심 질문:

- 이 인물은 액트 전과 후에 달라졌는가?
- 강해진 것보다 감정 비용이 남았는가?
- 관계가 바뀌었는가?

### 3. Scene Pressure

장면이 그냥 정보 전달이 되지 않도록 압력을 건다.

장면 압력 예:

- 시간 제한
- 숨겨야 하는 정체
- 빚
- 소문
- 통행 제한
- 위험한 거래
- 과거 인연

연결 장부:

- `audit/FS_Scene_Pressure_Checklist.md`

### 4. Relationship Turn

관계가 어떻게 틀어지고 바뀌는지 본다.

관계 유형:

- 같은 편
- 한때 같은 편
- 지금은 적
- 서로 모름
- 한쪽만 앎
- 소문으로만 앎
- 과거 인연
- 미래 인연

연결 장부:

- `audit/FS_Relationship_Ledger.md`

### 5. Foreshadow / Payoff Timing

복선을 언제 심고 언제 회수할지 정한다.

연결 장부:

- `audit/FS_Foreshadow_Payoff_Register.md`

### 6. Reveal Control

독자에게 보여줄 정보와 숨길 정보를 나눈다.

특히 아래는 늦게 보여줘도 된다.

- 진짜 소속
- 진품/가품
- 과거 배신
- 소문과 사실의 차이
- 기관이 숨긴 기억

연결 장부:

- `audit/FS_Reveal_Control_Register.md`

### 7. Act Outcome

액트가 끝나면 무엇이 바뀌었는지 기록한다.

연결 장부:

- `audit/FS_Act_Outcome_Ledger.md`

### 8. Story-to-Lore Handoff

장면이나 액트에서 새 설정이 튀어나오면
바로 정본처럼 쓰지 않고
Lore Engine으로 handoff를 건다.

연결 장부:

- `audit/FS_Story_to_Lore_Handoff_Gate.md`

## Live Story Registers

- `audit/FS_Story_Act_Question_Register.md`
- `audit/FS_Scene_Pressure_Checklist.md`
- `audit/FS_Reveal_Control_Register.md`
- `audit/FS_Relationship_Ledger.md`
- `audit/FS_Foreshadow_Payoff_Register.md`
- `audit/FS_Act_Outcome_Ledger.md`
- `audit/FS_Story_to_Lore_Handoff_Gate.md`

## Operating Sequence

장면이나 액트를 만들 때 기본 순서:

1. 액트 질문을 정한다.
2. 중심 인물의 감정 비용을 정한다.
3. 갈등 압력을 붙인다.
4. 관계 변화 지점을 정한다.
5. 복선과 회수 타이밍을 본다.
6. 독자에게 공개할 정보와 숨길 정보를 나눈다.
7. 액트 결과 장부에 남길 변화를 정한다.
8. story-born 신규 설정이면 handoff gate를 건다.

## Lore Engine Cross-Check

Story Engine이 장면을 제안할 때도
아래는 Lore Engine으로 되돌려 확인한다.

- 새 지명
- 새 세력명
- 새 아이템
- 새 소속
- 새 혈통
- 장거리 이동
- 세계 안 유명인 추가
- 소문을 사실로 바꾸는 순간

연결 게이트:

- `audit/FS_Story_to_Lore_Handoff_Gate.md`

## Conductor Note

현재 단계에서는 Story Engine은 보조 엔진이다.

하지만 액트 설계나 실제 원고 단계로 들어가면
Story Engine이 주 엔진이 되고,
Lore Engine은 정합성 검사 역할로 뒤에서 받친다.

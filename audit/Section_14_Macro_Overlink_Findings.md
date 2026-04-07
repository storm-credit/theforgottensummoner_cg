# Section 14 Macro Overlink Findings

이 문서는 `14번 영웅 문서`에서 반복적으로 보이는
`7축 거시 엔진 연동 대상` 블록이
실제 정본 구조인지, 자동 확장 잔재인지 구분하기 위한 중간 진단서다.

## Current Judgment

현재 단계의 판단은 아래와 같다.

- `조직망 접점` 자체는 이 세계에 실제로 필요하다.
- 하지만 `동일한 매크로 블록의 반복 삽입`은 정본 관계 서술이라기보다
  후속 자동 확장 흔적으로 보이는 비율이 높다.
- 따라서 관계표에는 조직망 접점을 남기되,
  원문 블록의 어조와 범위를 그대로 정본 취급하지 않는다.

## Evidence Set

### 1. 이리나 폰 루즈

- file:
  - `working/imports/phase1_orphans/[현존] 정보단 여왕 이리나 폰 루즈.md`
- observed:
  - 문서 서두에 `7축 거시 엔진 연동 대상 (첩보/흑막)` 블록이 단독 삽입된다.
- judgment:
  - `그림자 첩보망` 접점 자체는 정합적이다.
  - 다만 문서 본문보다 앞선 시스템 문구가 강해서,
    실제 인물 서사보다 메타 하네스 문장이 먼저 보이는 문제가 있다.

### 2. 칼리크 디트리히

- file:
  - `working/imports/phase1_orphans/[현존] 카르텔 수장 칼리크 디트리히.md`
- observed:
  - `길드/시스템`
  - `상단/자본`
  - `마탑/진리`
  - `첩보/흑막`
  - 총 4개의 거시 엔진 블록이 연속 삽입된다.
- judgment:
  - 이 인물이 여러 조직축과 닿는 것은 맞다.
  - 하지만 현재 블록은 실제 소속 설명이 아니라
    `무조건 다 걸린다`는 식의 기계적 연결문에 가깝다.

### 3. 세실리아 메르카토르

- file:
  - `working/imports/phase2_section14_current_ether/3. 자유도시연합 (Crossroad Cities)/06. 세실리아 메르카토르 (Cecilia Mercator).md`
- observed:
  - `상단/자본`
  - `마탑/진리`
  - `기업/생산`
  - `첩보/흑막`
  - 총 4개의 거시 엔진 블록이 연속 삽입된다.
- judgment:
  - 자유도시 핵심 외교 인물이 자본, 첩보, 생산축에 걸리는 건 그럴듯하다.
  - 다만 `기업/생산`까지 일괄 매핑되는 방식은 현재 아스트라리스 톤보다
    과설계된 시스템 설명처럼 읽힌다.

## Conductor Rule

이제부터 `7축 거시 엔진 연동 대상` 문구는 이렇게 다룬다.

1. `접점 존재`의 근거로는 사용 가능
2. `문장 자체`를 정본 관계 설명으로 채택하지 않음
3. 실제 관계표에는
   - `same_side_different_front`
   - `intermittent_alignment`
   - `asymmetric_awareness`
   같은 관계 타입으로 재서술
4. 같은 패턴이 3회 이상 반복되는 축은 `macro_overlink` 감시 대상으로 올림

## Immediate Use

- `Section_14_Conflict_Register.md`의 `macro_overlink` 판정 보강
- `Key_Character_Contact_Table.md`에서
  매크로 문장을 관계 타입으로 환원
- `15번` 후보 수집 시
  실제 사람 노드가 보이는 조직만 우선 회수

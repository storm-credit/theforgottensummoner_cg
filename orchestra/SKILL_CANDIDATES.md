# Skill Candidates

이 문서는 오케스트라 문서들을 별도 스킬로 분리할 때를 대비한 설계 초안이다.

이 문서는 실제 설치 상태를 선언하는 문서가 아니라,
역할과 입력/출력을 설계 메모로 정리해 두는 reference 문서다.

## 1. lore-audit

### Role

- 설정 충돌
- 중복
- 누락
- 레거시
- 구조 파손

을 표준 형식으로 점검한다.

### Inputs

- 대상 경로
- 상위 기준 문서
- 작업 단계

### Outputs

- `Gap`
- `Conflict`
- `Duplicate`
- `Structure`

형식의 이슈 목록

### Source Docs

- `workflow/02_Lore_Audit_Rules.md`
- `audit/Audit_Queue.md`
- `audit/reports/*`

## 2. relationship-mapper

### Role

- 인물 관계를 타입별로 분류
- 스침, 소문, 과거, 미래, former ally, asymmetric awareness 같은 연결을 수집

### Inputs

- 인물 문서 묶음
- 세력 문서 묶음

### Outputs

- 관계 타입 표
- 핵심 접점
- 관계 공백

### Source Docs

- `workflow/03_Relationship_Types.md`
- `workflow/04_Hero_Canon_Schema.md`

## 3. faction-adequacy

### Role

- 대륙별 `가문 / 부족 / 길드` 충분성 점검
- 세력 구조가 인간 서사를 지탱하는지 판단

### Inputs

- 대륙 프레임 문서
- 세력 작업본

### Outputs

- 충분성 판정
- 결손층 목록
- 후속 import 제안

### Source Docs

- `workflow/09_House_Clan_Guild_Adequacy.md`
- `working/drafts/Continental_Adequacy_Map.md`
- `audit/House_Clan_Guild_First_Pass.md`

## 4. canon-normalizer

### Role

- 표기 흔들림
- 명칭 충돌
- Hard/Soft/Open Question 분류

### Inputs

- 충돌 경로
- 표기 후보

### Outputs

- 정규화 표
- 보류 판정
- 우선순위

### Source Docs

- `workflow/01_Canon_Policy.md`
- `workflow/05_Naming_Normalization_Map.md`
- `audit/reports/naming_crosswalk.md`

## 5. item-desire-design

### Role

- 아이템 수집 욕구 설계
- 성장형 / 에고형 / 세트형 / 컬렉션형 분류
- 후보 수집과 장기 확장 연결

### Inputs

- 아이템 후보 등록부
- 관련 인물 / 세력 문서

### Outputs

- 분류안
- 욕망 장치 태그
- 백과 승격 후보

### Source Docs

- `workflow/07_Item_Canon_Schema.md`
- `workflow/08_Item_Desire_Design.md`
- `working/crosswalks/Item_Encyclopedia_Pipeline.md`
- `working/crosswalks/Item_Longterm_Taxonomy.md`

## 6. spatial-cartography

### Role

- 세계지도
- 대륙 지도
- 도시 지도
- 건물 내부 맵

을 점진적으로 backlog화한다.

### Inputs

- 대륙 문서
- 세력 본거지 문서
- 도시/요새/신전/연구소 후보

### Outputs

- 공간 계층 메모
- 지도 backlog
- 동선 후보

### Source Docs

- `workflow/10_Spatial_Map_Progression.md`
- `working/drafts/Spatial_Backlog.md`

## 7. writer-engine-router

### Role

- 해당 작업에 어떤 작가 엔진을 먼저 적용할지 결정
- 구조, 갈등, 아크, 관계망, 장면성 중 무엇을 우선 볼지 라우팅

### Inputs

- 작업 단계
- 대상 문서

### Outputs

- 우선 적용 엔진
- 보조 엔진
- 보류 사유

### Source Docs

- `workflow/11_Writer_Engine.md`
- `orchestra/RUNBOOK.md`

## Repository Decision

이 저장소에서는 이 후보들을 자동으로 실제 스킬로 간주하지 않는다.

이유:

- 아직 구조가 계속 바뀌는 중이다
- 현 단계에서는 Conductor가 직접 통합하는 편이 더 빠르다
- 반복 루틴이 충분히 굳은 뒤에 분리하는 편이 안전하다

## Harness Position

이 문서의 skill 후보들은
항상 아래 경계 안에서만 쓴다.

- `MCP`는 문맥 수집
- `Skill`은 반복 절차 고정
- `Agent`는 병렬 진단
- `Hook`은 전환 누락 방지
- `Register`는 장기 기억

즉 skill은
`판단 주체`가 아니라
`같은 절차를 다시 설명하지 않게 해 주는 층`
이다.

## Conversion Review Triggers

아래 중 2개 이상이 반복되면 실제 스킬화 검토:

- 같은 감사 형식을 3회 이상 반복
- 같은 분류 규칙을 수동으로 계속 재설명
- 같은 출력 형식을 여러 배치에서 재사용
- 분업이 고정돼 있고 충돌이 적음

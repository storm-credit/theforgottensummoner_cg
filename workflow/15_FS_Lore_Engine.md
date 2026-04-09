# FS Lore Engine

`FS Lore Engine`은 설정집 구성과 백과 운영을 위한 엔진이다.

목표는 멋있는 설정을 더 많이 만드는 것이 아니라,
이미 존재하는 설정을 무너지지 않게 정렬하고,
새 설정이 들어올 때 어디로 가야 하는지 판단하는 것이다.

## Scope

FS Lore Engine이 담당하는 것:

- 세계관 코어
- 대륙 프레임
- 세력, 가문, 부족, 길드 충분성
- `8. 세력 아카이브`
- `14. 영웅백과`
- `15. Named Notables`
- `15. Operational Lines`
- 아이템 후보
- 지도, 도시, 건물 내부 맵 후보
- 레거시, 소문, 보류, 충돌 판정

담당하지 않는 것:

- 실제 장면 문장 쓰기
- 대화 리듬
- 문단 호흡
- 원고 연출
- 독자에게 언제 보여줄지의 최종 장면 설계

이 영역은 `FS Story Engine`이 우선한다.

## Core Modules

### 1. Source Priority

서로 충돌하는 문서를 만났을 때
어떤 출처를 먼저 믿을지 정한다.

연결 장부:

- `audit/FS_Source_Priority_Register.md`

### 2. State Label

각 항목이 정본인지, 보류인지, 소문인지, 레거시인지 표시한다.

연결 장부:

- `audit/FS_State_Label_Register.md`

### 3. Revision Gate

실제 수정이나 정본 선언 전에 통과해야 하는 검수 게이트다.

연결 장부:

- `audit/FS_Revision_Gate_Checklist.md`
- `audit/FS_Story_to_Lore_Handoff_Gate.md`

### 4. Archive Routing

새 항목이 어디로 가야 하는지 판단한다.

우선 라우팅:

- `14 = 서사 중심 영웅`
- `15 Named Notables = 세계관 명사형 영웅 / 유명 NPC`
- `15 Operational Lines = 조직 작동을 보여주는 실무층`
- `8 = 세력 / 기관 / 집단`
- `지도 = 공간 기능`
- `아이템 = 물건, 보물, 장비, 도감성 후보`
- `hold = 판단 보류`

14/15 경계 규칙:

- `SS / S / A급`, `Act 중심성`, `전설 영웅록`, `독립 14 파일` 신호가 있으면 먼저 `verify_before_15`로 둔다.
- 유명 NPC형 가치가 있어도 14 중심 영웅 신호가 강하면 바로 15로 내리지 않는다.
- `15 Named Notables`는 `약한 영웅` 창고가 아니라 `세계 안에서 찾아갈 이유가 있는 이름 있는 명사` 축이다.
- `15 Named Notables`의 본체 라우팅은 `대륙 -> 세력 / 도시 / 조직` 기준으로 한다.
- `현자 / 장인 / 기록자 / 감정사 / 연금술사 / 공방주` 같은 기능은 보조 색인으로만 둔다.

### 5. Naming Tone

서양 정통 에픽 판타지 톤을 유지한다.

원칙:

- 동양/무협 문법 제외
- 현대 범죄물/기업물 어휘 남발 금지
- 작업용 구조 라벨과 세계 안 표면명을 분리

연결 문서:

- `workflow/12_Naming_Tone_Guide.md`
- `audit/Section_15_Operational_Display_Canon_Candidates.md`

### 6. Place / Asset / Institution

장소, 자산, 기관 기억이 실제 서사 기능을 갖도록 관리한다.

연결 장부:

- `audit/FS_Place_Function_Register.md`
- `audit/FS_Asset_Secret_Register.md`
- `audit/FS_Institution_Memory_Register.md`

### 7. Travel / Resource / Rumor

이동 개연성, 자원 경제, 소문과 사실의 분리를 관리한다.

연결 장부:

- `audit/FS_Travel_Logistics_Register.md`
- `audit/FS_Ecology_Resource_Register.md`
- `audit/FS_Rumor_Fact_Register.md`

### 8. Decision / Firewall / Slot Growth / Change Log

반복 판단과 누수 방지를 위한 보조 코어.

연결 장부:

- `audit/FS_Decision_Ruling_Register.md`
- `audit/FS_Cross_Chronicle_Firewall.md`
- `audit/FS_Slot_Maturation_Register.md`
- `audit/FS_Canon_Change_Log.md`

### 9. Story-to-Lore Intake

Story Engine에서 올라온 새 설정은
바로 정본 장부로 쓰지 않고
handoff packet으로 먼저 받는다.

연결 장부:

- `audit/FS_Story_to_Lore_Handoff_Gate.md`

## Operating Sequence

설정 항목을 볼 때 기본 순서:

1. 출처 우선순위를 확인한다.
2. 상태 라벨을 붙인다.
3. 어디로 라우팅할지 정한다.
4. 이름 톤이 맞는지 본다.
5. 관계, 시간, 장소, 자산, 소문과 연결되는지 본다.
6. 수정하려면 Revision Gate를 통과한다.
7. story-born 신규 설정이면 handoff packet과 register write를 같이 남긴다.

## Current Priority

현재 FS Lore Engine의 우선순위:

1. `14/15` 분리 기준 유지
2. Named Notables와 Operational Lines를 섞지 않기
3. 대륙 -> 세력/도시/조직 폴더링을 본체로 유지
4. 직업/기능은 보조 색인으로 관리
5. 이름은 판타지 표면명 후보로 따로 관리
6. 소문과 사실을 섞지 않기

## Live Lore Registers

FS Lore Engine이 실제로 쓰는 장부:

- `audit/FS_Canon_Tier_Register.md`
- `audit/FS_Relationship_Ledger.md`
- `audit/FS_Act_Outcome_Ledger.md`
- `audit/FS_Foreshadow_Payoff_Register.md`
- `audit/FS_Source_Priority_Register.md`
- `audit/FS_State_Label_Register.md`
- `audit/FS_Revision_Gate_Checklist.md`
- `audit/FS_Story_to_Lore_Handoff_Gate.md`
- `audit/FS_Place_Function_Register.md`
- `audit/FS_Asset_Secret_Register.md`
- `audit/FS_Institution_Memory_Register.md`
- `audit/FS_Travel_Logistics_Register.md`
- `audit/FS_Ecology_Resource_Register.md`
- `audit/FS_Rumor_Fact_Register.md`
- `audit/FS_Decision_Ruling_Register.md`
- `audit/FS_Cross_Chronicle_Firewall.md`
- `audit/FS_Slot_Maturation_Register.md`
- `audit/FS_Canon_Change_Log.md`

## Conductor Note

FS Lore Engine은 지금 단계의 주 엔진이다.

설정집이 안정될 때까지는
`Story Engine`보다 `Lore Engine`을 우선 적용한다.

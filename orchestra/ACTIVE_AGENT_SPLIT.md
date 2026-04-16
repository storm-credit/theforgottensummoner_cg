# Active Agent Split

## How Agents Operate Here

이 저장소의 에이전트는 상시 자동 프로세스가 아니라,
Conductor가 필요 배치마다 실제 서브에이전트를 호출하거나
역할 렌즈를 내부적으로 적용하는 혼합 운용 방식이다.

즉:

- 역할은 실제로 분리된다
- 판단 기준도 분리된다
- 실제 서브에이전트가 필요한 경우 배치 단위로 띄운다
- 실제 배치 기록은 `orchestra/AGENT_DISPATCH_LOG.md`에 남긴다
- 산출물도 역할별로 남긴다
- 최종 통합만 Conductor가 한다

## Locked Orchestra Advantages

오케스트라 방식의 이점은 아래처럼 고정한다.

1. `병렬 진단`
   같은 대상을 여러 관점으로 동시에 읽어, 긴 문서를 한 번에 닫는 속도를 높인다.
2. `판단과 반영의 분리`
   에이전트는 읽기/진단/제안까지만 맡고, 최종 반영은 Conductor만 한다.
3. `충돌 조기 발견`
   라우팅, 이름 톤, 서사 등급, 장소 기능 충돌을 한 문서 안에서 늦게 발견하지 않고 배치 단계에서 분리한다.
4. `전문 렌즈 고정`
   대륙, 세력, 관계, 장소, 엔진 같은 축을 한 사람이 한 번에 섞어 읽지 않게 한다.
5. `책임 추적 가능`
   어떤 배치가 어떤 판단을 냈는지 `AGENT_DISPATCH_LOG.md`와 산출물 문서로 되짚을 수 있다.

## Required Expert Startup Rule

실제 배치를 시작할 때는 항상 아래 순서를 먼저 본다.

1. 해당 배치가 어떤 작업 종류인지 고른다.
2. 그 작업 종류에 맞는 `필수 전문가 묶음`을 `orchestra/REQUIRED_EXPERT_ROSTER_LOCK.md`에서 고른다.
3. 그 뒤에만 실제 서브에이전트를 배치한다.

## Split Trigger

아래 조건이면 Conductor는 오케스트라 분할을 우선 검토한다.

- 같은 대상에 `라우팅`, `이름`, `등급`, `장소 기능`이 한꺼번에 걸려 있을 때
- 여러 대륙 또는 여러 장부를 같이 만져야 할 때
- `verify_before_15`, `need_named_candidate`, `display_canon_candidate`가 동시에 얽힐 때
- 긴 압축표를 닫으면서 다음 작업선까지 같이 정해야 할 때

## Harness Reading

오케스트라 분할은 단독으로 돌지 않는다.

항상 아래 하네스 안에서 읽는다.

1. `MCP`가 문맥을 모은다.
2. `Skills`가 반복 절차를 고정한다.
3. `Agents`가 관점별 병렬 진단을 맡는다.
4. `Hooks`가 전환 누락과 기록을 강제한다.
5. `Registers`가 상태와 판정을 기억한다.
6. `Conductor`가 최종 통합과 반영을 맡는다.

## Real Subagent Reading

실제로 띄운 배치는 `orchestra/AGENT_DISPATCH_LOG.md`와
current workstream 문서 기준으로 본다.

활성 역할은 고정 이름 배치가 아니라,
current mainline에 맞는 `closure sync / carryover / mismatch / handoff drift`
질문으로 다시 배정한다.

## Active Segmentation Reading

### 1. Conductor

- current 메인 축 결정
- 작업 순서 고정
- 충돌 판단 최종 승인

### 2. Continent Adequacy Scout

- `1~5 대륙` 프레임 점검
- 각 대륙의 `가문 / 부족 / 길드` 결손층 확인
- `audit/Five_Continent_Missing_Layer_Master_Lock.md`를 우선 기준으로 읽고,
  `working/drafts/Continental_Adequacy_Map.md`는 보조 평가 기준으로만 사용

### 3. Faction Cartographer

- `8. 세력 아카이브` 구조 점검
- 대륙 루트와 세력 루트 연결 여부 확인
- 길드, 상단, 중간 사회 단위가 실제 구조 안에 있는지 확인

### 4. House and Lineage Auditor

- 가문층 점검 전담
- 귀족권, 기사권, 장인 계보, 왕가, 몰락 가문, 방계 가문 존재 여부 확인
- 인물 출신과 계승 갈등이 실제로 서는지 확인

### 5. Clan and Tribe Auditor

- 부족층 점검 전담
- 변경, 산악, 숲, 혹한, 해양 계열 대륙에서 부족 단위가 필요한지 확인
- 생활 방식, 금기, 전승, 외부 세력 접촉 방식 확인

### 6. Guild and Economy Auditor

- 길드층 점검 전담
- 상단, 장인조합, 정보조직, 운송, 모험가, 마도 공방, 항해 조직 존재 여부 확인
- 도시와 경제 흐름을 실제로 받치는지 확인

### 7. Hero Curator

- `14. 인물 백과`에서 인물 출신 기반 확인
- 인물이 어느 사회 단위 위에 서 있는지 역추적
- `가문 / 부족 / 길드` 결손이 인물 문서에서 드러나는지 수집

### 8. Relationship Mapper

- 사회 단위가 인간 관계망에 실제 영향을 주는지 점검
- 혼인, 복수, 계승, 거래, 사제 관계, 의리 관계를 추적

### 9. Item Archivist

- 현재 mainline에서는 소진행
- 아이템 후보와 장기 분류를 유지하되 메인 축 안정화 이후 확장

### 10. Spatial Cartographer

- 현재 mainline에서는 소진행
- 세계 / 대륙 / 도시 / 건물 / 실내 맵 backlog 유지
- 메인 진행에서 나온 위치 정보를 지도 축으로 점진 축적

## Baseline Main Track

1. 세계관
2. 대륙
3. `가문 / 부족 / 길드` 충분성
4. 세력
5. 인물
6. 관계망

## Active Watch Track

1. `closure sync`
2. `Section 8 -> 15 watch-reference`
3. `structure label / mismatch / P2 handoff owner drift`
4. `summary / bridge / package / register wording consistency`

## Watch-Cycle Default Bundle

current mainline이 `closure sync / Section 8 -> 15 watch-reference`일 때
Conductor는 아래 묶음을 기본 선언으로 쓴다.

- `Canon Architect`
- `Engine Router`
- `Hook Keeper`
- `Report Clerk`
- `Faction Cartographer`
- `Hero Curator`
- `People Worth Seeking Curator`
- `Boundary Hold Scout`
- `Index Auditor`

필요 시 추가:

- `Place-Function Auditor`
- `Place-Institution Slot Scout`
- `Collision Auditor`
- `Plausibility Judge`

읽기 질문:

1. `Section 8`의 `structure label / mismatch / P2 handoff owner`가 sidecar/register와 같은 문장으로 유지되는가
2. `Section 15`의 hold cluster / `source_check_hold / hold reference split` / `deferred_expansion_hold / hold reference split`가 summary 문서에서 같은 상태어로 유지되는가
3. `summary / bridge / queue / package / register`가 같은 기준 시점을 가리키는가
4. `keep_14` 경계가 새 증거 없이 summary drift로 약화되지 않았는가

## Active Side Track

- 아이템 수집 파이프라인
- 아이템 욕망 설계
- 장기 아이템 분류
- 세계지도 / 도시 / 건물 내부 맵 backlog

## Rule

- 모든 역할이 동시에 문서를 수정하지 않는다.
- 한 번에 하나의 메인 산출물만 Conductor가 승인한다.
- 같은 대상에 대한 판단이 갈리면 `Open Question`으로 올린다.

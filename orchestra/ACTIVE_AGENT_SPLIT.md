# Active Agent Split

## How Agents Operate Here

이 저장소의 에이전트는 독립 자동 프로세스가 아니라,
Conductor가 역할을 분리해 같은 작업 흐름 안에서 세분화하여 운용하는 방식이다.

즉:

- 역할은 실제로 분리된다
- 판단 기준도 분리된다
- 산출물도 역할별로 남긴다
- 최종 통합만 Conductor가 한다

## Current Segmentation

### 1. Conductor

- 현재 메인 축 결정
- 작업 순서 고정
- 충돌 판단 최종 승인

### 2. Continent Adequacy Scout

- `1~5 대륙` 프레임 점검
- 각 대륙의 `가문 / 부족 / 길드` 결손층 확인
- `working/drafts/Continental_Adequacy_Map.md` 기준으로 평가

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

- 현재는 소진행
- 아이템 후보와 장기 분류를 유지하되 메인 축 안정화 이후 확장

### 10. Spatial Cartographer

- 현재는 소진행
- 세계 / 대륙 / 도시 / 건물 / 실내 맵 backlog 유지
- 메인 진행에서 나온 위치 정보를 지도 축으로 점진 축적

## Current Main Track

1. 세계관
2. 대륙
3. `가문 / 부족 / 길드` 충분성
4. 세력
5. 인물
6. 관계망

## Current Side Track

- 아이템 수집 파이프라인
- 아이템 욕망 설계
- 장기 아이템 분류
- 세계지도 / 도시 / 건물 내부 맵 backlog

## Rule

- 모든 역할이 동시에 문서를 수정하지 않는다.
- 한 번에 하나의 메인 산출물만 Conductor가 승인한다.
- 같은 대상에 대한 판단이 갈리면 `Open Question`으로 올린다.

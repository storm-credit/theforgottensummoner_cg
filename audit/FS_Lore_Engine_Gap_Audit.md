# FS Lore Engine Gap Audit

이 문서는 FS 엔진 코어가 잡힌 뒤,
`로어 엔진 전용`으로 아직 더 필요하거나
강화가 필요한 모듈을 점검한 결과다.

전제:

- FS 엔진 전체에는 작법 층과 운영 층이 함께 있다.
- 여기서는 그중 `설정집 구성과 백과 운영`에 필요한
  로어 엔진 쪽만 본다.

## Strength Snapshot

이미 확보된 강한 코어:

1. `Reverse Design`
2. `Canon Tier`
3. `Archive Routing`
4. `Relationship Ledger`
5. `Chronology / Causality`
6. `Act Outcome Ledger`
7. `Foreshadow / Payoff`
8. `Plausibility`
9. `Naming Normalization`
10. `Faction / House / Clan / Guild Layer`
11. `Legacy Quarantine`

이 정도면 `뼈대`는 있다.

하지만 큰 설정집을 오래 굴리려면
아래 추가 모듈이 필요하다.

## Priority A. 바로 붙이면 좋은 것

### 1. Source Priority Register

Status: `built`

역할:

- 어떤 문서가 더 상위 근거인지 고정한다.

최소 우선순위 예:

1. 세계관 헌장
2. 대륙 프레임
3. 세력 루트
4. 인물 문서
5. 소문성 기록

왜 필요한가:

- 충돌이 날 때 `무엇을 믿을지`가 빨라진다.
- 같은 내용이 여러 문서에 있을 때 정리 비용이 줄어든다.

### 2. State Label Register

Status: `built`

역할:

- 항목 상태를 표준 라벨로 관리한다.

추천 최소 라벨:

- `active`
- `hold`
- `rumor`
- `legacy`
- `duplicate_candidate`
- `needs_merge`

왜 필요한가:

- 초안, 소문, 보류, 레거시가 정본처럼 섞이는 걸 막는다.

### 3. Revision Gate Checklist

Status: `built`

역할:

- 수정 전에 반드시 통과해야 하는 게이트를 둔다.

최소 질문:

1. canon tier는?
2. 대표 표기는?
3. 어디로 라우팅되는가?
4. 기존 관계/연표와 충돌 없는가?
5. 충돌 시 hold 했는가?

왜 필요한가:

- 설정을 추가할 때마다 다시 무너지지 않게 한다.

## Priority B. 세계를 더 살아 있게 만드는 것

### 4. Place Function Register

Status: `built`

역할:

- 장소가 어떤 장면을 여는지 기록한다.

예:

- 서고: 해독, 금서 접근, 조언
- 항만: 유통, 밀수, 검문, 재회
- 공방: 제작, 개조, 수리, 시험
- 묘지: 금기 연락, 전승, 은닉, 봉인

왜 필요한가:

- 지도와 장소 문서가 죽은 설정이 되지 않는다.

### 5. Asset / Secret Register

Status: `built`

역할:

- 유물, 계약서, 비밀 문서, 혈통 정보, 금고 열쇠, 장부 같은
  `움직이는 정보/자산`을 추적한다.

왜 필요한가:

- 누가 무엇을 쥐고 있는지가 서사를 실제로 움직일 때 많다.

### 6. Institution Memory Register

Status: `built`

역할:

- 세력이나 기관이 기억하는 오래된 사건,
  금기, 복수, 부채, 치부를 누적한다.

왜 필요한가:

- 개인이 아니라 조직의 감정 기억을 관리할 수 있다.
- 같은 세력이 왜 반복적으로 특정 반응을 보이는지 설명된다.

## Priority C. 장기 확장 대비

### 7. Travel & Logistics Register

Status: `built`

역할:

- 항로, 육로, 우회로, 이동 비용, 위험 구간, 계절 영향 기록

왜 필요한가:

- 대륙이 커질수록 `왜 여기까지 왔는가`를 방어하는 데 필요하다.

### 8. Ecological / Resource Register

Status: `built`

역할:

- 희귀 약초, 광물, 용혈, 식량, 물류 핵심 자원과 산지를 추적한다.

왜 필요한가:

- 연금술, 대장간, 도시 경제, 세력 충돌이 물리적 근거를 가진다.

### 9. Rumor vs Fact Register

Status: `built`

역할:

- 작중 소문과 정본 사실을 별도로 관리한다.

왜 필요한가:

- 이 작품은 소문, 엇갈림, 비대칭 인지가 중요해서
  `rumor`를 적극 써야 하지만 곧바로 사실 취급하면 안 된다.

## Recorded Build Order Snapshot

1. `FS_Source_Priority_Register.md`
2. `FS_State_Label_Register.md`
3. `FS_Revision_Gate_Checklist.md`
4. `FS_Place_Function_Register.md`
5. `FS_Asset_Secret_Register.md`
6. `FS_Institution_Memory_Register.md`
7. `FS_Travel_Logistics_Register.md`
8. `FS_Ecology_Resource_Register.md`
9. `FS_Rumor_Fact_Register.md`

## New Upgrade Pass

장부가 충분히 생긴 뒤,
다음 단계에서 정말 필요한 업그레이드는 아래 3개로 압축된다.

1. `FS_Decision_Ruling_Register.md`
2. `FS_Cross_Chronicle_Firewall.md`
3. `FS_Slot_Maturation_Register.md`

이유:

- 큰 설정집은 `판정 기억`이 없으면 다시 흔들린다.
- 아스트라리스는 `다른 크로니클과의 경계`를 유지해야 한다.
- `need_named_candidate` 슬롯이 많아지면서
  이름 없는 구조가 실제 named notable 후보로 자라는 과정을 추적할 장부가 필요해졌다.

## Build Status

Priority A and B are represented as registered modules.

Priority C has also been opened as registered modules so that
large-scale continent, item, city, and rumor work can proceed
without waiting for a later refactor.

## Conductor Note

한 줄 결론:

FS 로어 엔진은 이미 강한 코어를 갖췄다.

이제 필요한 건
`무엇이 정본인지 더 빠르게 고르는 장치`,
`무엇이 보류인지 섞이지 않게 하는 장치`,
`장소와 자산이 실제로 서사를 움직이게 하는 장치`다.

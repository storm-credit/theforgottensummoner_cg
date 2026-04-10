# Five Continent Missing Layer Policy Lock

이 문서는 `Continents_Framework.md`의 `Conductor Lock`에 남아 있던
결손층 5개를 실제 정책 문장으로 닫기 위한 락 문서다.

목적:

- 빈칸을 새 설정 발명으로 메우지 않는다.
- 이미 확보한 `Section 8 spine sample`을 바탕으로
  각 대륙의 얇은 층을 어디까지 인정할지 고정한다.
- 이후 `인물`, `세력`, `place-pressure`, `14/15 boundary`가
  이 얇은 층을 과독해하지 못하게 한다.

## Input

- `working/drafts/Continents_Framework.md`
- `audit/Section_8_Crimson_Notable_Anchor_Audit.md`
- `audit/Ether_Core_Faction_Layers.md`
- `audit/Frost_Core_Faction_Layers.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Obelisk_Core_Faction_Layers.md`
- `audit/Section_15_Five_Continent_Closure_Table.md`
- `audit/Section_15_Named_Notables_Coverage_Matrix.md`
- `audit/Section_15_Oceanic_Place_Institution_Sidecar.md`
- `audit/Section_15_Obelisk_Place_Institution_Sidecar.md`

## Policy Table

| Continent | Missing Layer | Policy Lock | Overread Ban |
|---|---|---|---|
| `에테르` | `변방 부족층` | `정령연합 바깥 부족층은 frontier echo / border support까지만 인정` | 숲, 수인, 샤먼, 자치 구역 신호를 곧바로 에테르 대륙 공통 `tribe_clan enough`로 올리지 않는다. |
| `크림슨` | `국가형 가문층` | `씨족형 지배층 위에 얇은 국가형 가문층이 부분적으로만 존재` | 용혈 상층, 부족장 상층, 도시 거점 상층을 전통 왕가/문장가문 질서와 동일시하지 않는다. |
| `프로스트` | `정주 귀족층` | `정주 귀족층은 요새/보급 거점/병기소 운영층에서 thin-support로만 읽는다` | 클랜 상층과 장로층을 곧바로 정주 궁정 귀족 질서로 읽지 않는다. |
| `해양` | `토착 공동체층` | `토착 공동체층은 항만/교단/함대 바깥 생활 관습의 support range로만 보존` | 섬, 성지, 선장 혈연, 파도 신앙을 곧바로 해양 대륙 공통 `tribe_clan enough`로 올리지 않는다. |
| `오벨리스크` | `비정통 엘리트` | `가문/왕국/통치자 신호는 먼저 nontraditional elite로 읽는다` | 왕국, 귀족, 가문 표현을 전통 `state_house` 복구 신호로 먼저 읽지 않는다. |

## 1. Ether Frontier Tribe Policy

### Lock

에테르의 부족층은 `정령연합 inside strong`이 이미 닫힌 기준이다.
정령연합 바깥에서 보이는 변방 숲 공동체, 국경 자치 생활, 계약 해석자,
감시 공동체 같은 신호는 당분간 `frontier echo / border support`로만 받는다.

### What Counts

- 왕국연합/성국 바깥 경계 생활의 흔적
- 도시 질서에 흡수되지 않은 변방 공동체
- 정령연합과 닿는 계약/숲 경계 실무층

### What Does Not Count

- 정령연합 내부 부족 구조의 반복
- 숲, 정령, 샤먼 어휘의 분위기적 사용
- 개별 수인/자치 구역 신호만으로 대륙 공통 부족층을 승격하는 읽기

### Downstream Rule

에테르 outside `Spirit Union` 자료는
`tribe_clan thin-support outside core`로만 기록한다.
대륙 본선 spine은 계속 `state_house + guild_market`로 유지한다.

## 2. Crimson State-House Policy

### Lock

크림슨의 국가형 가문층은 `thin`이 맞다.
다만 완전히 없는 것은 아니고,
`용의 후예`의 용혈 상층, `붉은 사막 부족 연합`의 상층 부족장 질서,
`엘드라칸` 같은 핵심 거점 운영층에서
`국가형으로 기울 수 있는 얇은 상층`이 부분적으로 보인다.

### What Counts

- 씨족장과 별개로 지속되는 거점 운영 상층
- 용혈 지배층의 상속/문벌 기능
- 도시/거점 유지에 반복적으로 관여하는 상층 가계

### What Does Not Count

- 명예, 혈통, 씨족 우위 자체
- 사막 부족장의 권위 그 자체
- 장면 한 번의 귀족/명문 언급

### Downstream Rule

크림슨에서는
`씨족형 지배층`과 `국가형 가문층`을 항상 분리한다.
후자는 `state_house thin` 또는 `thin-support`까지만 허용한다.

## 3. Frost Settled Nobility Policy

### Lock

프로스트의 정주 귀족층은 대륙 중심 질서가 아니다.
있더라도 `요새`, `보급 거점`, `병기소`, `상설 저장고`,
`방한 장비/열량 배분`을 관리하는 정착 운영층에서만 `thin-support`로 읽는다.

### What Counts

- 이동 부족 질서와 별개로 남아 있는 상설 거점 운영층
- 장기 보급, 병기 생산, 요새 방어를 세대적으로 관리하는 집단
- 정주 거점에서 반복되는 관리자 혈통

### What Does Not Count

- 클랜 장로
- 부족장 가문
- 생존 공동체의 상하 위계 일반

### Downstream Rule

프로스트 자료에서 귀족/상층 신호가 보여도
우선 `클랜 상층`으로 읽고,
정착 거점 운영의 독립 상층일 때만 `state_house thin-support`를 허용한다.

## 4. Oceanic Indigenous Community Policy

### Lock

해양의 토착 공동체층은 아직 본선 spine이 아니다.
다만 완전히 공백으로 두지 않고,
항만/함대/교단 질서 바깥의 `연안 생활 관습`, `성지 주변 공동체`,
`항로를 몸으로 기억하는 현지 생활층` 정도를 `support range`로 보존한다.

### What Counts

- 항만 국가 바깥에서 반복되는 연안 공동체 생활
- 교단 성지 주변의 생활 단위 공동체
- 함대/해적과 다른 생활 논리로 항로를 유지하는 현지층

### What Does Not Count

- 선장 혈연
- 해적 가문
- 해상 귀족 가문
- 교단 권위 자체

### Downstream Rule

해양에서 `섬`, `성지`, `파도 신앙`, `혈연`이 보여도
우선 `place-pressure / seamanship culture / local support`로 기록한다.
`tribe_clan thin`은 유지하고, 증거가 반복될 때만 support에서 재검토한다.

## 5. Obelisk Nontraditional Elite Policy

### Lock

오벨리스크는 `비정통 엘리트`를 정식 정책으로 고정한다.
즉 `가문`, `왕국`, `통치자`, `원로`, `대표` 신호는
먼저 `nontraditional elite`로 읽고,
전통 귀족국가 복원 신호로 읽는 것은 후순위로 둔다.

### Allowed Classes

- 기억 귀족
- 기록/금서/묘역 관리 상층
- 망명 네트워크 실권층
- 봉인선 유지 책임자
- 빚, 통행, 보급을 쥔 계약 엘리트

### What Does Not Count

- 왕국 명칭 자체
- 가문 폴더 존재 자체
- 통치자 호칭 하나만으로 전통 귀족 질서를 복원하는 읽기

### Downstream Rule

오벨리스크에서 `state_house`는
항상 `nontraditional elite thin-support`로만 허용한다.
대륙 본체는 계속 `frontier_survival + guild_market`로 읽는다.

## Conductor Decision

`Continents_Framework.md`에 남아 있던 결손층 5개는
이제 `빈칸`이 아니라 `정책적으로 어디까지 허용하는 얇은 층인가`로 잠근다.

즉 다음 보강은
이 다섯 층을 새 설정 발명으로 키우는 일이 아니라,
이미 잠근 정책 범위 안에서 증거를 더 모으는 일로 읽는다.

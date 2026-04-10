# Five Continent Missing Layer Overread Firewall

이 문서는
`Five_Continent_Missing_Layer_Evidence_Register.md`,
`Five_Continent_Missing_Layer_Evidence_First_Pass_A.md`,
`Five_Continent_Missing_Layer_Evidence_Second_Pass_A.md`
까지 확보한 샘플을 바탕으로,
어디서 overread가 발생하는지를 대륙별 firewall 형태로 잠근 문서다.

목적:

- `얇은 층`을 `강한 본체 층`으로 오독하는 경로를 차단한다.
- tempting signal과 safe read를 분리한다.
- 이후 evidence intake가 들어와도 같은 overread를 반복하지 않게 한다.

## Input

- `audit/Five_Continent_Missing_Layer_Evidence_Register.md`
- `audit/Five_Continent_Missing_Layer_Evidence_First_Pass_A.md`
- `audit/Five_Continent_Missing_Layer_Evidence_Second_Pass_A.md`

## Firewall Table

| Continent | Tempting Overread | Why It Is Tempting | Why It Is Still Blocked | Locked Safe Read |
|---|---|---|---|---|
| `에테르` | outside core를 곧바로 부족 연합 본체로 복원 | 국경 개척민, 전진 기지, 숲 경계 실무가 반복됨 | 반복되는 것은 부족 연합 본체보다 border-support survival/function | `frontier echo / border support` |
| `크림슨` | 씨족 상층을 세습 귀족국가로 복원 | 의회, 관세, 출입 관리, 상층 lifestyle 분화가 보임 | import 본문이 직접 `세습 귀족은 없다`고 못 박음 | `tribe_clan core + state_house thin-support` |
| `프로스트` | 요새 운영층을 settled nobility enough로 승격 | 보급, 병기소, 영구 주둔, 난방/식량 유지가 반복됨 | 중심 질서는 여전히 클랜/부족, 정주 운영은 support layer에 머묾 | `settled stronghold support layer only` |
| `해양` | 토착 공동체층을 tribe_clan enough로 승격 | 원주민, 어부, 나룻배, local survival trace가 반복됨 | 교단/함대 core가 너무 강하고, 일부 문서는 fleet-core 기능일 뿐임 | `local support outside fleet/church/port core` |
| `오벨리스크` | 기억/계약 엘리트를 전통 monarchy/state-house로 복원 | 가문, 왕국, 귀족, 국왕급 같은 표면어가 보임 | 실질 구동력은 기억/기록/계약/보호증서/망명 네트워크이며, 세속 귀족 체계가 부정됨 | `state_house signal rerouted to nontraditional elite first` |

## 1. Ether Firewall

### Tempting Signal

- `변방공국`
- `국경 개척민`
- `서부 개척 전진기지`
- `정찰`, `사냥꾼 조합`, `자급자족`

### Why Not To Overread

- 이 반복은 `outside Spirit Union tribe confederation restored`
  라기보다 `경계 생존 / 완충 / 계약 실무` 반복이다.
- 즉 공동체의 존재는 받지만,
  대륙 본체급 부족층 복원으로 바로 넘기지 않는다.

### Locked Read

- `tribe_clan thin-support outside Spirit Union core`
- shorthand로는 `frontier echo / border support`

## 2. Crimson Firewall

### Tempting Signal

- `드래곤 의회`
- `외교·정찰부`
- `출입국 관리`
- `관세청`
- `지배층 / 하층민` lifestyle 분화

### Why Not To Overread

- 이 신호들은 thin state-house function을 보강하지만,
  import 본문은 `세습 귀족은 없다`고 직접 말한다.
- therefore:
  `씨족형 지배층 + thin administration`
  까지는 받되,
  `세습 귀족국가 / state_house strong`
  로는 못 올린다.

### Locked Read

- `state_house thin-support separated from tribe_clan core`

## 3. Frost Firewall

### Tempting Signal

- `연합 최전방 감시 초소`
- `보급 구역`
- `영원한 주둔지`
- `훈련소이자 물자 비축 기지`
- `아이스포지 병기소`
- `난방/방어`, `식량 공급`

### Why Not To Overread

- stronghold operation과 storage/maintenance가 반복되는 건 맞다.
- 하지만 이게 바로 궁정형 귀족제나 settled nobility enough를 뜻하지는 않는다.
- 중심 조직은 여전히 클랜/부족이며,
  정주 운영은 support layer로만 받는다.

### Locked Read

- `settled stronghold support layer only`

## 4. Oceanic Firewall

### Tempting Signal

- `원주민 착취`
- `원주민 다이버들`
- `섬세력 원주민 수만 명`
- `굶주린 어부`
- `빈민들의 나룻배`

### Why Not To Overread

- local/indigenous trace가 실제로 있는 건 맞다.
- 그러나 해양권은 fleet/church/port core가 너무 강하고,
  `해안 경비대` 같은 문서는 local layer가 아니라 fleet-core defense다.
- 또 교단 본문은 `혈통은 의미가 없다`고 하므로,
  교단 내부 위계를 혈연/부족층 근거로 읽을 수 없다.

### Locked Read

- `support range only`
- register wording으로는 `local support outside fleet/church/port core`

## 5. Obelisk Firewall

### Tempting Signal

- `가문`
- `왕국`
- `귀족`
- `국왕급`
- `기억 귀족`

### Why Not To Overread

- 표면어는 전통 귀족국가처럼 보일 수 있다.
- 그러나 반복되는 실질 기능은
  `기억 지기`, `실질 통치`, `자원 배분`, `영혼 계약서`,
  `방벽 보호 증서 및 통행권`, `부패한 발굴 브로커`,
  `세속 귀족 체계는 없다` 쪽이다.
- therefore:
  state-house signal이 보이면 먼저 전통 귀족국가가 아니라
  `memory/contract/nontraditional elite`로 우회시킨다.

### Locked Read

- `state_house signal rerouted to nontraditional elite first`
- shorthand로는 `nontraditional elite thin-support`

## Intake Firewall Rule

1. tempting signal이 보여도 먼저 `core layer`와 `thin/support layer`를 분리한다.
2. thin/support repetition은 `안정화` 근거이지 `승격` 근거가 아니다.
3. reject example이 이미 잠긴 대륙은 같은 종류의 표면어가 더 나와도 바로 승격하지 않는다.
4. `14/15`, profile layer, place-pressure, summary/bridge/watch 문서는 이 firewall을 넘어서 대륙 본체를 재정의하지 않는다.

## Conductor Decision

이제 `결손층 5개`는
`policy lock`,
`evidence register`,
`first pass sample`,
`second pass repetition`,
`overread firewall`
까지 한 세트로 잠겼다.

다음 보강은
새 층을 만드는 작업이 아니라,
새 evidence가 들어왔을 때 이 firewall 안에서만
받고 거르는 작업으로 읽는다.

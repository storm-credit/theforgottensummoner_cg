# Five Continent Missing Layer Evidence Second Pass A

이 문서는
`Five_Continent_Missing_Layer_Evidence_First_Pass_A.md` 다음 단계로,
같은 방향의 반복 증거가 실제로 다른 문서 family에서도 잡히는지를
확인하는 2차 샘플 패스다.

목적:

- `thin/support` 판정을 승격하지 않는다.
- `1차 샘플`에서 잡은 읽기 방향이 다른 문서 family에서도 반복되는지만 본다.
- 반복 신호가 있어도 `enough` 승격이 아니라
  `Five_Continent_Missing_Layer_Master_Lock.md` 아래의
  `safe read가 안정적`이라는 component 결론까지만 잠근다.

## Input

- `audit/Five_Continent_Missing_Layer_Evidence_Register.md`
- `audit/Five_Continent_Missing_Layer_Evidence_First_Pass_A.md`
- `working/imports/phase3_section8_ether_allied_kingdoms/왕국연합 (Allied Kingdoms).md`
- `working/imports/phase3_section8_ether_allied_kingdoms/1. 주요 장소 (Locations)/요새/1. 웨스트게이트 (Westgate).md`
- `working/imports/phase3_section8_ether_allied_kingdoms/1. 주요 장소 (Locations)/요새/8. 웨스트 마치 (Westmarch).md`
- `working/imports/phase3_section8_ether_allied_kingdoms/1. 주요 장소 (Locations)/도시/2. 드레이븐 (Draven).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/지역/1. 서리늑대 쉼터 (Frostwolf Haven).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/도시/1. 스노우하트 (Snowheart).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/16. 예하 부대 및 기사단 (Military Units)/03. 툰드라실드 방패단 (Tundrashield Defenders).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/16. 예하 부대 및 기사단 (Military Units)/08. 퍼마프로스트 공성단 (Permafrost Siegeforce).md`
- `working/imports/phase3_section8_crimson_dragon_descendants/용의 후예.md`
- `working/imports/phase3_section8_crimson_dragon_descendants/1. 주요 장소 (Locations)/요새/3. 스케일 게이트 (Scale Gate).md`
- `working/imports/phase4_oceanic_trade_flow.md`
- `working/imports/phase4_section8_oceanic_golden_armada/5. 역사 (History)/0. 황금 함대 역사 및 연표.md`
- `working/imports/phase4_section8_oceanic_church_of_sea/7. 법률 및 규범 (Laws & Norms)/0. 바다의 교단 법률 및 사회 규범.md`
- `working/imports/phase4_section8_oceanic_church_of_sea/바다의 교단 (Church of the Sea).md`
- `working/imports/phase4_section8_oceanic_golden_armada/16. 예하 부대 및 기사단 (Military Units)/09. 해안 경비대 (Coastal Rangers).md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/잊힌 자들의 연합 (Forgotten Alliance).md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/14. 생활양식/14-1. 귀족과 평민의 식생활 차이.md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/8. 경제 및 상업 (Economy & Commerce)/1. 잊힌 자들의 연합 주요 교역로 및 무역 거점.md`
- `working/imports/phase5_section8_obelisk_seal_wardens/봉인 수호단 (Seal Wardens).md`
- `working/imports/phase5_obelisk_trade_flow.md`

## Repetition Table

| Continent | Repeated Signal | Repeated From | Stable Safe Read | Still Blocked |
|---|---|---|---|---|
| `에테르` | 국경 개척민 + 전진 정찰 자급 구조 | polity file + frontier fortress file | `frontier echo / border support` | outside layer를 바로 부족 연합으로 승격 |
| `크림슨` | 의회/정찰/관세/출입 관리 상층 | core overview + gate fortress file | `state_house thin-support` | 세습 귀족국가 / state_house strong |
| `프로스트` | 전초 감시 + 보급창 + 정주 유지 기술 관료 | frontier outpost + city maintenance file | `settled stronghold support` | 정주 귀족층 enough |
| `해양` | 현지 생계층 착취 + 교단 외곽 생활 압박 | trade flow + church law file | `support range only` | 토착 공동체 enough / fleet-core를 토착층으로 오독 |
| `오벨리스크` | 망명 네트워크 실권 + 계약/보호 증서 경제 | faction overview + trade flow file | `nontraditional elite thin-support` | 전통 monarchy / state_house 복원 |

## 1. Ether Repetition Check

### Repeated Evidence

- [왕국연합 (Allied Kingdoms).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_ether_allied_kingdoms\왕국연합%20%28Allied%20Kingdoms%29.md)
  - `변방공국`, `국경 개척민`이 polity-level 계층표에 직접 들어 있다.
- [웨스트게이트 (Westgate).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_ether_allied_kingdoms\1.%20주요%20장소%20%28Locations%29\요새\1.%20웨스트게이트%20%28Westgate%29.md)
  - `서부 개척 전진기지`, `서부 개척단`이 outside core 개척-완충 실무를 frontier fortress 층에서 반복한다.
- [웨스트 마치 (Westmarch).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_ether_allied_kingdoms\1.%20주요%20장소%20%28Locations%29\요새\8.%20웨스트%20마치%20%28Westmarch%29.md)
  - `전진 정찰 기지`, `사냥꾼 조합`, `자급자족`이 frontier support를 place file에서도 반복한다.
- [드레이븐 (Draven).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_ether_allied_kingdoms\1.%20주요%20장소%20%28Locations%29\도시\2.%20드레이븐%20%28Draven%29.md)
  - `통역사 길드`, `삼국 조율 위원회`가 경계 계약 해석·조율 인터페이스라는 support 실무층을 city file에서 반복한다.

### Conductor Read

- Ether thin layer는 여전히 `Spirit Union outside core frontier echo`다.
- repetition은 늘었지만, 부족 연합 enough가 아니라 `border-support stability`만 보강한다.

## 2. Crimson Repetition Check

### Repeated Evidence

- [용의 후예.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\용의%20후예.md)
  - `드래곤 의회`, `외교·정찰부`가 씨족 core 위 얇은 통치/대외 접속 기능을 보여준다.
- [스케일 게이트 (Scale Gate).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\1.%20주요%20장소%20%28Locations%29\요새\3.%20스케일%20게이트%20%28Scale%20Gate%29.md)
  - `출입국 관리`, `관세청`, `통행세`가 gate-administration 층을 place file에서 반복한다.

### Reject Reminder

- [용의 후예.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\용의%20후예.md)
  - `세습 귀족은 없다`가 직접 있어 `state_house strong` 복원은 여전히 금지다.

### Conductor Read

- Crimson은 `tribe_clan core + state_house thin-support`가 더 안정적으로 읽힌다.
- 하지만 repetition은 `세습 귀족국가` 복원이 아니라 `thin state-house` 분리만 강화한다.

## 3. Frost Repetition Check

### Repeated Evidence

- [서리늑대 쉼터 (Frostwolf Haven).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\1.%20주요%20장소%20%28Locations%29\지역\1.%20서리늑대%20쉼터%20%28Frostwolf%20Haven%29.md)
  - `연합 최전방 감시 초소`, `보급 구역`, `식량과 탄약 비축`이 stronghold support를 frontier node에서 반복한다.
- [스노우하트 (Snowheart).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\1.%20주요%20장소%20%28Locations%29\도시\1.%20스노우하트%20%28Snowheart%29.md)
  - `난방/방어` 기술 관료화와 `식량 공급` 유지가 정주 운영 층을 city file에서 반복한다.
- [툰드라실드 방패단 (Tundrashield Defenders).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\16.%20예하%20부대%20및%20기사단%20%28Military%20Units%29\03.%20툰드라실드%20방패단%20%28Tundrashield%20Defenders%29.md)
  - `영원한 주둔지`, `훈련소이자 물자 비축 기지`가 상설 거점 운영층을 military-unit file에서도 반복한다.
- [퍼마프로스트 공성단 (Permafrost Siegeforce).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\16.%20예하%20부대%20및%20기사단%20%28Military%20Units%29\08.%20퍼마프로스트%20공성단%20%28Permafrost%20Siegeforce%29.md)
  - `아이스포지 병기소`, `영구적인 방어 시설들`이 병기소/시설 관리형 정착 운영을 다시 보강한다.

### Conductor Read

- Frost는 `settled stronghold support`가 1차보다 더 안정적으로 보인다.
- 그래도 중심은 클랜/부족 질서이므로 `settled nobility enough`로는 올리지 않는다.

## 4. Oceanic Repetition Check

### Repeated Evidence

- [phase4_oceanic_trade_flow.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_oceanic_trade_flow.md)
  - `원주민 착취`, `원주민 다이버들`이 trade-flow 층에서 local support 존재를 반복한다.
- [황금 함대 역사 및 연표.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_golden_armada\5.%20역사%20%28History%29\0.%20황금%20함대%20역사%20및%20연표.md)
  - `섬세력 원주민 수만 명`, `노예로 갈아 넣어`가 토착 섬 공동체가 실제로 있었음을 history 층에서 반복한다.
- [바다의 교단 법률 및 사회 규범.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_church_of_sea\7.%20법률%20및%20규범%20%28Laws%20%26%20Norms%29\0.%20바다의%20교단%20법률%20및%20사회%20규범.md)
  - `굶주린 어부`, `빈민들의 나룻배`가 church-law 층에서도 local survival range를 반복한다.
- [바다의 교단 (Church of the Sea).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_church_of_sea\바다의%20교단%20%28Church%20of%20the%20Sea%29.md)
  - `혈통은 의미가 없다`, `신앙의 깊이와 심연에 대한 헌신이 서열을 결정`이 교단 위계를 혈연/씨족층 근거로 못 쓰게 막는다.

### Reject Reminder

- [해안 경비대 (Coastal Rangers).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_golden_armada\16.%20예하%20부대%20및%20기사단%20%28Military%20Units%29\09.%20해안%20경비대%20%28Coastal%20Rangers%29.md)
  - `연안 순찰`은 fleet-core 방어 기능이라 local/indigenous support 증거로 받지 않는다.

### Conductor Read

- Oceanic은 local support signal이 반복되지만, 여전히 `support range only`다.
- local support repetition이 곧 토착 공동체 enough는 아니다.

## 5. Obelisk Repetition Check

### Repeated Evidence

- [잊힌 자들의 연합 (Forgotten Alliance).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_forgotten_alliance\잊힌%20자들의%20연합%20%28Forgotten%20Alliance%29.md)
  - `망명 네트워크`, `계약`, `기억 지기`, `각 구역 실질 통치`, `자원 배분`이 faction overview 층에서 반복된다.
- [귀족과 평민의 식생활 차이.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_forgotten_alliance\14.%20생활양식\14-1.%20귀족과%20평민의%20식생활%20차이.md)
  - `혈통이 아니라 정화 자원의 독점력`, `자유도시연합에서 몰래 들여온`이 상층 기능의 근거가 세습 혈통이 아니라 resource chokehold라는 점을 반복한다.
- [잊힌 자들의 연합 주요 교역로 및 무역 거점.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_forgotten_alliance\8.%20경제%20및%20상업%20%28Economy%20%26%20Commerce%29\1.%20잊힌%20자들의%20연합%20주요%20교역로%20및%20무역%20거점.md)
  - `부패한 발굴 브로커`, `자유도시에 납품`, `국가의 자금지원을 빨아먹지만`이 브로커/유통망 실권을 더 강하게 보여준다.
- [phase5_obelisk_trade_flow.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_obelisk_trade_flow.md)
  - `영혼 계약서`, `방벽 보호 증서 및 통행권`, `지식 브로커질`, `봉인 카르텔`이 contract-elite mechanism을 대륙-wide로 반복한다.
- [봉인 수호단 (Seal Wardens).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_seal_wardens\봉인%20수호단%20%28Seal%20Wardens%29.md)
  - `세속 귀족 체계는 없다`, `본국 수입 95% 이상 의존`이 비세속 엘리트 구조와 얇은 support dependency를 반복한다.

### Conductor Read

- Obelisk는 `state_house signal rerouted to nontraditional elite first`가 더 강해졌다.
- repetition이 늘수록 전통 monarchy가 아니라 `memory/contract elite` reading이 더 안전해진다.

## Conductor Decision

`Second Pass A` 기준으로도
`Five_Continent_Missing_Layer_Master_Lock.md` 아래에서
다섯 대륙 모두 `thin/support` 판정이 맞다는 component read를 유지하고,
반복 증거는 `승격 근거`가 아니라 `안정화 근거`로만 읽는다.

즉 다음 패스는
새 층을 세우는 일이 아니라,
이 방향을 거스르는 overread를 더 잘 막는 쪽으로 이어진다.

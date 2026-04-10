# Five Continent Missing Layer Evidence First Pass A

이 문서는
`Five_Continent_Missing_Layer_Evidence_Register.md`를
실제 import 본문에 대조한 1차 샘플 패스다.

목적:

- 얇은 층 5개를 `파일명 추정`이 아니라 `본문 근거` 위에서 읽는다.
- 각 대륙마다 `admissible`, `still not enough`, `safe read`를
  샘플 anchor로 한 번 실제 고정한다.
- 다음 패스부터는 이 샘플과 같은 방향의 반복 증거만 추가한다.

## Input

- `audit/Five_Continent_Missing_Layer_Evidence_Register.md`
- `audit/Five_Continent_Missing_Layer_Master_Lock.md`
- `working/imports/phase3_section8_ether_allied_kingdoms/왕국연합 (Allied Kingdoms).md`
- `working/imports/phase3_section8_ether_allied_kingdoms/1. 주요 장소 (Locations)/요새/8. 웨스트 마치 (Westmarch).md`
- `working/imports/phase3_section8_ether_allied_kingdoms/1. 주요 장소 (Locations)/요새/5. 그레이리지 방어선 (Grayridge Line).md`
- `working/imports/phase3_section8_crimson_dragon_descendants/용의 후예.md`
- `working/imports/phase3_section8_crimson_dragon_descendants/6. 사회 및 정치 (Society & Politics)/0. 용의 후예 사회 구조 및 정치 체계.md`
- `working/imports/phase3_section8_crimson_dragon_descendants/1. 주요 장소 (Locations)/요새/3. 스케일 게이트 (Scale Gate).md`
- `working/imports/phase3_section8_crimson_dragon_descendants/14. 생활양식/14-1. 귀족과 평민의 식생활 차이.md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/요새/1. 푸른 폭풍 요새 (Blue Storm Citadel).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/지역/1. 서리늑대 쉼터 (Frostwolf Haven).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/도시/1. 스노우하트 (Snowheart).md`
- `working/imports/phase4_oceanic_trade_flow.md`
- `working/imports/phase4_section8_oceanic_church_of_sea/1. 주요 장소 (Locations)/금단구역/고래의 길 (Path of Whales).md`
- `working/imports/phase4_section8_oceanic_church_of_sea/1. 주요 장소 (Locations)/도시/포트 오브 프레이어 (Port of Prayer).md`
- `working/imports/phase4_section8_oceanic_church_of_sea/1. 주요 장소 (Locations)/성지/트렌치사이드 슈라인 (Trenchside Shrine).md`
- `working/imports/phase4_section8_oceanic_church_of_sea/7. 법률 및 규범 (Laws & Norms)/0. 바다의 교단 법률 및 사회 규범.md`
- `working/imports/phase4_section8_oceanic_golden_armada/16. 예하 부대 및 기사단 (Military Units)/09. 해안 경비대 (Coastal Rangers).md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/잊힌 자들의 연합 (Forgotten Alliance).md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/1. 주요 장소 (Locations)/거래소/기억 경매장 (Memory Auction House).md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/3. 가문 (Noble Houses)/0. 잊힌 자들의 연합 가문 관계도.md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/3. 가문 (Noble Houses)/1. 에라툼 가문 (Eratum Family).md`
- `working/imports/phase5_section8_obelisk_kingdom_of_dead/망자의 왕국 (Kingdom of the Dead).md`
- `working/imports/phase5_obelisk_trade_flow.md`

## Sample Table

| Continent | Sample Anchor | Safe Read | Why Admissible | Why Still Limited |
|---|---|---|---|---|
| `에테르` | `왕국연합`, `웨스트 마치`, `그레이리지 방어선` | `frontier echo / border support` | 국경 개척민, 숲 경계 정찰 기지, 드루이드 협력, 사냥꾼 조합, 물자 리프트 같은 경계 생존 실무가 반복된다 | `정령연합 outside core` 부족층이라기보다 border-support layer에 가깝다 |
| `크림슨` | `용의 후예 사회 구조`, `귀족과 평민의 식생활 차이` | `state_house thin-support` | `대용왕`, `용기병단 & 부족장`, 혈통 기반 지배층, 지배층/하층민 분화가 씨족 core 위의 얇은 상속-지배 기능을 보강한다 | 여전히 중심은 씨족/용혈 지배층이며, 전통 `state_house strong`까지는 아니다 |
| `프로스트` | `푸른 폭풍 요새`, `서리늑대 쉼터`, `스노우하트` | `settled stronghold support` | 사령부, 보급청, 생산 구역, 저장/보급 거점, 정주 도시 열원과 식량 유지가 반복된다 | 중심 질서는 여전히 클랜/부족이며, 정주 귀족층은 stronghold support에 머문다 |
| `해양` | `고래의 길`, `포트 오브 프레이어`, `트렌치사이드 슈라인` | `support range only` | 해류 기억, 순례 기착지, 성지 주변 격리 노동, 심해 감시 생활이 `현지/성지 주변 생활 단위`를 얇게 보여준다 | 여전히 교단 질서 의존도가 크고, 독립 토착 공동체/원주민 연맹까지는 아니다 |
| `오벨리스크` | `잊힌 자들의 연합`, `기억 경매장`, `내부 정치망`, `에라툼`, `망자의 왕국`, `phase5_obelisk_trade_flow` | `nontraditional elite thin-support` | 기억/기록 상층, 계약-경매-통행 보증, 망명 네트워크 실권, 기록 가문, 기억 귀족이 전통 귀족보다 더 선명하다 | `가문/왕국` 표면명은 있어도 중심 기능은 비정통 엘리트이며 전통 `state_house` 복구로는 읽지 않는다 |

## 1. Ether Sample Read

### Admissible

- [왕국연합 (Allied Kingdoms).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_ether_allied_kingdoms\왕국연합%20%28Allied%20Kingdoms%29.md)
  - `국경 개척민`과 gray-zone village 신호가 직접 보여 outside `Spirit Union` 경계 생활층을 받을 수 있다.
- [웨스트 마치 (Westmarch).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_ether_allied_kingdoms\1.%20주요%20장소%20%28Locations%29\요새\8.%20웨스트%20마치%20%28Westmarch%29.md)
  - 드루이드 협력자, 사냥꾼 조합, 자급자족 구조가 `forest-edge survival/watch community`를 보여준다.
- [그레이리지 방어선 (Grayridge Line).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_ether_allied_kingdoms\1.%20주요%20장소%20%28Locations%29\요새\5.%20그레이리지%20방어선%20%28Grayridge%20Line%29.md)
  - 국경 방어선, 현지 산악 가이드, 물자 리프트가 `border-support population`을 보강한다.

### Still Not Enough

- outside `Spirit Union`에서 보이는 것은 부족 연합 자체보다 국경 생활/완충 실무층이다.
- 따라서 `tribe_clan enough`로는 올리지 않고 `frontier echo / border support`로만 남긴다.

## 2. Crimson Sample Read

### Admissible

- [용의 후예.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\용의%20후예.md)
  - `드래곤 의회`, `외교·정찰부`처럼 씨족 core 위에 놓인 통치/대외 접속 기능이 실제로 보인다.
- [용의 후예 사회 구조 및 정치 체계.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\6.%20사회%20및%20정치%20%28Society%20%26%20Politics%29\0.%20용의%20후예%20사회%20구조%20및%20정치%20체계.md)
  - `대용왕`, `용기병단 & 부족장`, 혈통 기반 지배층이 씨족 core 위의 얇은 국가형 상층 기능을 보인다.
- [스케일 게이트 (Scale Gate).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\1.%20주요%20장소%20%28Locations%29\요새\3.%20스케일%20게이트%20%28Scale%20Gate%29.md)
  - `출입국 관리`, `관세청`, `통행세`가 부족-군사 질서 위에 얇은 gate-administration 층이 얹혀 있음을 보강한다.
- [귀족과 평민의 식생활 차이.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\14.%20생활양식\14-1.%20귀족과%20평민의%20식생활%20차이.md)
  - `용인 전사(지배층)`과 하층민의 분화가 상속/혈통 기반 상층 존재를 lifestyle 축에서 보강한다.

### Reject Example

- [용의 후예.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_crimson_dragon_descendants\용의%20후예.md)
  - `세습 귀족은 없다`는 문장이 직접 있기 때문에, 이를 전통 `state_house strong`이나 세습 귀족국가로 복원하면 과독해다.

### Still Not Enough

- 중심 질서는 여전히 `용혈-씨족 지배층`이다.
- 따라서 `state_house thin-support separated from tribe_clan core`까지만 허용한다.

## 3. Frost Sample Read

### Admissible

- [푸른 폭풍 요새 (Blue Storm Citadel).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\1.%20주요%20장소%20%28Locations%29\요새\1.%20푸른%20폭풍%20요새%20%28Blue%20Storm%20Citadel%29.md)
  - 사령부, 보급청, 생산 구역, 항구 구역이 함께 있어 `정주 stronghold support` 증거로 적합하다.
- [서리늑대 쉼터 (Frostwolf Haven).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\1.%20주요%20장소%20%28Locations%29\지역\1.%20서리늑대%20쉼터%20%28Frostwolf%20Haven%29.md)
  - frontier watch-and-supply node라서 저장/보급 거점형 support로 받기 좋다.
- [스노우하트 (Snowheart).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\1.%20주요%20장소%20%28Locations%29\도시\1.%20스노우하트%20%28Snowheart%29.md)
  - 영구 열원과 식량 유지가 반복되어 `settled stronghold support`를 추가 보강한다.

### Reject Example

- [귀족과 평민의 식생활 차이.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase3_section8_frost_frostborn_tribes\14.%20생활양식\14-1.%20귀족과%20평민의%20식생활%20차이.md)
  - 이 문서는 클랜 상층/하층 격차를 보여 주지만, 그 자체만으로 `정주 귀족층` 증거로 승격하면 과독해다.

## 4. Oceanic Sample Read

### Admissible

- [phase4_oceanic_trade_flow.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_oceanic_trade_flow.md)
  - `원주민 착취`, `원주민 다이버들`이 실제 trade-flow 본문에 들어 있어 현지층 존재 자체는 support range에서 받을 수 있다.
- [고래의 길 (Path of Whales).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_church_of_sea\1.%20주요%20장소%20%28Locations%29\금단구역\고래의%20길%20%28Path%20of%20Whales%29.md)
  - 특정 계절 해류와 고래 이동 경로가 `항로를 몸으로 기억하는 현지층` 가능성을 support range에서 열어 둔다.
- [포트 오브 프레이어 (Port of Prayer).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_church_of_sea\1.%20주요%20장소%20%28Locations%29\도시\포트%20오브%20프레이어%20%28Port%20of%20Prayer%29.md)
  - 순례길 중간 기착지와 평생 기도/노동 공동체는 `성지 주변 생활 단위`의 얇은 샘플로만 볼 수 있다.
- [트렌치사이드 슈라인 (Trenchside Shrine).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_church_of_sea\1.%20주요%20장소%20%28Locations%29\성지\트렌치사이드%20슈라인%20%28Trenchside%20Shrine%29.md)
  - 이름 없는 심해 감시자의 희생/봉인 유지 생활은 `현지 support unit`으로만 읽을 수 있다.
- [바다의 교단 법률 및 사회 규범.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_church_of_sea\7.%20법률%20및%20규범%20%28Laws%20%26%20Norms%29\0.%20바다의%20교단%20법률%20및%20사회%20규범.md)
  - `굶주린 어부`, `빈민들의 나룻배`가 직접 박혀 있어 성역 바깥의 얇은 생계층이 실제로 존재함을 보강한다.

### Reject Example

- [해안 경비대 (Coastal Rangers).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase4_section8_oceanic_golden_armada\16.%20예하%20부대%20및%20기사단%20%28Military%20Units%29\09.%20해안%20경비대%20%28Coastal%20Rangers%29.md)
  - 연안 순찰과 상륙 저지는 fleet-core 방어 기능이므로, 이를 곧바로 토착 공동체층 증거로 올리면 과독해다.

### Still Not Enough

- 세 샘플 모두 교단 질서의 외곽 단위에 더 가깝다.
- 따라서 `tribe_clan enough`로는 올리지 않고 `support range`까지만 유지한다.

## 5. Obelisk Sample Read

### Admissible

- [잊힌 자들의 연합 (Forgotten Alliance).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_forgotten_alliance\잊힌%20자들의%20연합%20%28Forgotten%20Alliance%29.md)
  - 망명 네트워크, 기억 지기, 자원 배분과 은밀 거래 축이 `nontraditional elite` 읽기를 지지한다.
- [기억 경매장 (Memory Auction House).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_forgotten_alliance\1.%20주요%20장소%20%28Locations%29\거래소\기억%20경매장%20%28Memory%20Auction%20House%29.md)
  - 기억/저주/계약 거래, 보증, 중립 중개가 `계약-기억 엘리트`를 직접 보여준다.
- [잊힌 자들의 연합 가문 관계도.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_forgotten_alliance\3.%20가문%20%28Noble%20Houses%29\0.%20잊힌%20자들의%20연합%20가문%20관계도.md)
  - 역사 보존, 연구, 유물 탐사 가문 경쟁은 `house-shaped nontraditional elite` 샘플로 읽는 편이 안전하다.
- [에라툼 가문 (Eratum Family).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_forgotten_alliance\3.%20가문%20%28Noble%20Houses%29\1.%20에라툼%20가문%20%28Eratum%20Family%29.md)
  - archive custody, history compilation, sealed-record access가 핵심이라 전통 귀족보다 기록 상층에 가깝다.
- [망자의 왕국 (Kingdom of the Dead).md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_section8_obelisk_kingdom_of_dead\망자의%20왕국%20%28Kingdom%20of%20the%20Dead%29.md)
  - `기억 귀족`, 기록 평의회, 기억 거래/저당 구조는 `기억 기반 상층`을 더 강하게 보여준다.
- [phase5_obelisk_trade_flow.md](C:\Users\Storm%20Credit\Desktop\Novel\The%20Forgatten%20Summoner\theforgottensummoner_cg\working\imports\phase5_obelisk_trade_flow.md)
  - 영혼 계약, 보호/통행 증서, 지식 중개, 봉인 오염 거래가 대륙-wide elite mechanism으로 반복된다.

### Reject Example

- `대봉인관 = 국왕급` 같은 단일 위계 대응만으로
  전통 monarchy를 복원하는 읽기는 과독해다.
- `가문` 폴더 존재 자체도 곧바로 `state_house strong` 증거가 되지 않는다.

## Conductor Decision

1차 샘플 기준으로는
다섯 얇은 층 모두 `정책상 허용된 thin/support 범위` 안에서만 읽는 게 맞다.

즉 다음 패스는
새 층 승격이 아니라,
이 샘플과 같은 방향의 반복 증거가 다른 문서 family에서 또 잡히는지를 보는 작업이다.

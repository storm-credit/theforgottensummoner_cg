# Section 8 Root Findings

## Scope

- Source: `X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)`
- Directories: `1474`
- Files: `3905`

## Primary Findings

1. `6. 범대륙 초국가 및 중립 세력` 루트가 중복되어 있다.
2. 깨진 이름의 변형 루트가 섞여 있다.
3. `_Legacy_중립세력 (Backup)`이 루트 레벨에 남아 있다.
4. 세력 내부 구조가 두 가지 스타일로 섞여 있다.
   - 공통 섹션형
   - 실제 장소 하위 폴더형
5. 템플릿성 반복 파일이 대량으로 존재한다.

## Spine Feedback From 5 Continents

`1~5 대륙 Section 8 spine sample` 1차 사이클을 닫은 뒤,
루트 구조에 되먹여야 하는 핵심 판정은 아래다.

1. `에테르`, `해양`은 기본적으로 `state_house + guild_market` 대륙이다.
   항만, 함대, 교단, 도시 금융, 귀족 구조는 부족층 근거로 올리지 않는다.
2. `크림슨`, `프로스트`는 기본적으로 `tribe_clan + guild_market` 대륙이다.
   클랜 상층과 부족장 가문은 바로 `state_house strong`으로 올리지 않는다.
3. `오벨리스크`는 `frontier_survival + guild_market` 대륙이다.
   가문 표현이 보여도 먼저 `nontraditional elite`인지 판별한다.
4. 따라서 루트 정규화는 `같은 폴더 모양`보다
   `대륙 spine에 맞는 구조인가`를 먼저 보는 쪽이 맞다.

## Risks

- 구조를 고치기 전에 내용 수정을 시작하면 모순이 더 늘어난다.
- 이름만 보고 중복 정리하면 정상 문서까지 잘못 합칠 수 있다.
- 레거시와 활성 경로가 섞이면 정본 판단이 계속 흔들린다.
- 대륙 spine을 무시한 채 일괄 구조화하면 `씨족 상층`, `항만 권력`, `생존 조직`이 같은 층으로 뭉개질 수 있다.

## Locked Action Reading

1. `Supranational & Neutral` 루트 충돌을 `P0`로 유지
2. `_Legacy_`와 `Backup`을 격리 대상으로 고정
3. `canonical root / quarantine root / legacy root`를 먼저 확정
4. 세력 내부 표준 뼈대를 먼저 정하고 예외를 기록
5. 각 세력을 `section_style / place_style / mixed`로 먼저 라벨링
6. 서사 개정은 루트 안정화 이후로 미룸

## New Lock After Continent Samples

이제 `1~5 대륙 Section 8 spine sample` 1차 사이클이 모두 닫혔기 때문에,
루트 감사도 아래 기준으로 다시 읽는다.

1. 에테르: `state_house + guild_market`, `tribe_clan` only inside `Spirit Union`
2. 크림슨: `tribe_clan + guild_market`, `state_house thin`
3. 프로스트: `tribe_clan + guild_market`, `state_house thin`
4. 해양: `state_house + guild_market`, `tribe_clan thin`
5. 오벨리스크: `frontier_survival + guild_market`, `state_house` only as `nontraditional elite`

즉 지금부터 `8번` 루트 문제는 단순 폴더 정리가 아니라,
`대륙별 spine 규칙과 구조가 맞는가`까지 함께 보는 단계다.

## Root-Level Reading Rule

루트 감사에서는 먼저 아래 순서로 본다.

1. 이 경로가 `canonical root`인지 `quarantine root`인지 `legacy root`인지
2. 이 세력/하위 폴더가 대륙 spine과 맞는지
3. 내부 구조가 `section_style`인지 `place_style`인지
4. 예외라면 실제 예외인지, 손상/중복/레거시 오염인지

## Conductor Decision

이 문서는
`Section 8 루트 구조 / 표준 spine / 레거시 분리`
단계에서 얻은 핵심 findings를 고정하는 reference 문서다.

현재 메인 본선은 이 findings를 바탕으로
closure sync / carryover watch를 유지하는 것이다.

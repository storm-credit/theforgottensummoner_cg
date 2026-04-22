# Section 8 Standard Spine

이 문서는 `8. 세력 아카이브`를 대륙별로 어떤 뼈대로 읽고 정리할지 정하는 표준 시트다.

핵심 원칙은 단순하다.

- 모든 대륙을 같은 구조로 억지 정렬하지 않는다.
- 대신 각 대륙의 `강한 층`과 `약한 층`을 먼저 인정한다.
- `8번` 정리는 이 대륙별 강약 구조를 기준으로 한다.

## Global Rule

각 대륙은 아래 세 층을 먼저 본다.

1. `house layer`
2. `tribe layer`
3. `guild/economy layer`

그리고 세력 문서는 아래 네 축 중 어디에 가까운지 먼저 라벨링한다.

1. `state_house`
2. `tribe_clan`
3. `guild_market`
4. `frontier_survival`

루트 정규화 closure에 되먹일 때는
세력마다 아래 구조 closure label도 같이 본다.

1. `section_style`
2. `mixed_keep`
3. `section_style_reclassify`

즉 spine 라벨과 구조 라벨은 별개다.
같은 `guild_market` 세력이라도 `section_style`일 수도 있고,
place pressure는 구조 라벨이 아니라 별도 pressure state일 수도 있다.

## 1. Ether Spine

- 우선 spine:
  - `state_house`
  - `guild_market`
- 보조 spine:
  - `tribe_clan` only inside `Spirit Union`

### Expected Core

- 왕가 / 귀족가 / 협회 / 자유도시 / 길드 / 상단 / 카르텔

### Expected Weak Point

- 부족 / 씨족 / 변방 공동체

### Normalization Rule

- 에테르 세력은 기본적으로 `가문과 도시 질서` 기준으로 읽는다.
- 부족형 구조가 나오면 `정령연합 특수축`인지 먼저 확인한다.

## 2. Crimson Spine

- 우선 spine:
  - `tribe_clan`
  - `guild_market`
- 보조 spine:
  - `state_house` only as `thin`

### Expected Core

- 부족 연합
- 씨족 상층
- 약탈 경제
- 상인 연합
- 카르텔

### Expected Weak Point

- 전통 귀족국가형 가문

### Normalization Rule

- 크림슨 세력은 `부족/씨족 + 생존 경제` 기준으로 읽는다.
- 가문형 명칭이 보여도 먼저 `씨족형 지배층`인지 확인한다.

## 3. Frost Spine

- 우선 spine:
  - `tribe_clan`
  - `guild_market`
- 보조 spine:
  - `state_house` only as `thin`

### Expected Core

- 부족장 평의회
- 클랜 상층
- 생존 경제
- 보급 / 독점 / 혹한 교역

### Expected Weak Point

- 도시 귀족
- 정주형 상업 길드

### Normalization Rule

- 프로스트 세력은 `클랜 정치 + 혹한 생존 경제` 기준으로 읽는다.
- 외부 교역 거점이 보이면 `도시 길드`가 아니라 `생존 교역 조직`인지 먼저 본다.

## 4. Obelisk Spine

- 우선 spine:
  - `frontier_survival`
  - `guild_market`
- 보조 spine:
  - `state_house` only as `nontraditional elite`

### Expected Core

- 요새
- 방어선
- 망명 네트워크
- 기억 거래
- 봉인 유지
- 전선 조직

### Expected Weak Point

- 전통 가문
- 부족 / 씨족 / 토착 공동체

### Normalization Rule

- 오벨리스크 세력은 `국가 귀족 질서`보다 `생존 조직` 기준으로 읽는다.
- 귀족 표현이 나와도 먼저 `기억 귀족 / 파벌 대표 / 비정통 지배층`인지 판별한다.

## 5. Oceanic Spine

- 우선 spine:
  - `state_house`
  - `guild_market`
- 보조 spine:
  - `tribe_clan` currently weak

### Expected Core

- 해상 귀족
- 함대
- 항구 도시
- 해적 가문
- 교단
- 보험 / 세금 / 암시장

### Expected Weak Point

- 토착 공동체
- 원주민 씨족
- 비국가 섬 연맹

### Normalization Rule

- 해양 세력은 `항만 권력 + 해상 경제 + 가문 정치` 기준으로 읽는다.
- 부족형 공동체가 보이면 후순위 특수축으로 따로 표기한다.

## Conductor Rule

앞으로 `8번` 세력 문서를 볼 때는 먼저 이 질문을 던진다.

1. 이 세력은 어느 대륙 spine에 속하는가
2. 이 세력은 `state_house / tribe_clan / guild_market / frontier_survival` 중 어디에 가까운가
3. 이 세력이 대륙의 강한 층을 대표하는가, 아니면 결손을 메워야 하는 예외인가

루트 정규화 단계에서는 여기에 아래 질문을 추가한다.

4. 이 경로는 `canonical root`, `quarantine root`, `legacy root` 중 어디에 속하는가
5. 내부 구조는 `section_style / mixed_keep / section_style_reclassify` closure 중 무엇인가
6. 예외라면 대륙 spine이 허용하는 예외인가, 아니면 구조 오염인가

이 문서는 이후

- `8번` 루트 정리
- `14번` 세력명 연결
- `15번` 중간 등장인물 회수
- 지도 축 확장

의 기준판으로 사용한다.

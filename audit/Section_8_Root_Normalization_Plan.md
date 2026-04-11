# Section 8 Root Normalization Plan

## Input Locks

이 계획은 아래 기준판을 입력으로 사용한다.

- `audit/Section_8_Root_Findings.md`
- `audit/Section_8_Root_Label_Map.md`
- `audit/Section_8_Standard_Spine.md`
- `audit/Ether_Core_Faction_Layers.md`
- `audit/Section_8_Crimson_Notable_Anchor_Audit.md`
- `audit/Frost_Core_Faction_Layers.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Obelisk_Core_Faction_Layers.md`

## Canonical Root Set

정본 루트 후보는 아래 7개로 잠정 고정한다.

1. `01-8. 세력 아카이브 (국가·조직 정리).md`
2. `1. 에테르 대륙 (Ether Continent)`
3. `2. 크림슨 대륙 (Crimson Continent)`
4. `3. 프로스트 대륙 (Frost Continent)`
5. `4. 오벨리스크 대륙 (Obelisk Continent)`
6. `5. 해양 대륙 (Oceanic Continent)`
7. `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)`

## Root Classes

- `canonical root`
  - 현재 정본 판단의 기준으로 읽는 루트
- `quarantine root`
  - 손상되었거나 중복 의심이 있어 정본 판단에서 제외하는 루트
- `legacy root`
  - 과거 작업 흔적으로 남기되, 현재 정본 판단에는 직접 쓰지 않는 루트

현재 판정:

- `canonical root`: `01-8` 본문 파일, `1~5 대륙`, 정상 `6. 범대륙 초국가 및 중립 세력`
- `quarantine root`: `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))`
- `legacy root`: `_Legacy_중립세력 (Backup)`

## Quarantine Candidates

아래는 정본 루트에서 제외하고 격리 대상으로 본다.

- `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))`
- `_Legacy_중립세력 (Backup)`

## Spine Feedback Lock

루트 정규화는 이제 아래 대륙별 판정을 전제로 한다.

1. `에테르`, `해양`: `state_house + guild_market`
2. `크림슨`, `프로스트`: `tribe_clan + guild_market`
3. `오벨리스크`: `frontier_survival + guild_market`, `state_house`는 `nontraditional elite` only

즉 같은 폴더 모양이라도
대륙 spine이 다르면 같은 정규화 규칙으로 밀어붙이지 않는다.

## Baseline Phase Order

1. 루트 이름 확정
2. 격리 대상 분리
3. `canonical / quarantine / legacy` 라벨 고정
4. 세력 내부 표준 뼈대 정의
5. 혼합형 하위 폴더 예외 목록 작성
6. 그 뒤에만 개별 세력 문서 내용 감사

## Locked Reference Operations

- `마립`이 들어간 루트는 손상 경로로 기록
- `_Legacy_` 전체는 정본 참조 대상에서 제외
- `Supranational & Neutral` 하위부터 템플릿성 반복 파일을 샘플링
- 세력별로 아래 세 패턴 중 어느 쪽인지 라벨링
  - `section_style`
  - `place_style`
  - `mixed`
- `mixed` 판정 세력은 곧바로 재배치하지 않고 예외 목록으로 먼저 올린다

## Locked Reference Outputs

1. `audit/Section_8_Structure_Labeling_Queue.md`
2. `audit/Section_8_Spine_Mismatch_Queue.md`

이 두 문서는
이전 root normalization 단계의 기준 출력으로 유지한다.
현재는 이 문서들에서 새 pass를 시작하지 않고,
closure sync / watch-reference가 흔들릴 때만 reference로 다시 연다.

## Mismatch Watch

루트 정규화에서 특히 조심할 mismatch는 아래다.

1. `씨족 상층`을 `국가형 귀족`으로 과대 해석하는 경우
2. `항만 권력 / 함대 / 교단`을 `tribe_clan` 근거로 잘못 올리는 경우
3. `기억 귀족 / 망명 지배층`을 `state_house strong`으로 과대 해석하는 경우
4. `place_style` 세력을 억지로 `section_style`로 평탄화하는 경우

## Stop Rules

- 같은 세력의 활성 경로와 레거시 경로가 둘 다 내용이 많으면 삭제하지 않는다
- 이름은 같아도 부모 경로가 다르면 자동 병합하지 않는다
- `mixed` 구조를 확인하기 전에는 폴더 이동이나 병합을 하지 않는다
- 대륙 spine과 충돌하는 해석은 `Open Question`으로 올리고 즉시 정본화하지 않는다

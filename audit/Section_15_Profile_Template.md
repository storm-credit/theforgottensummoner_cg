# Section 15 Profile Template

이 문서는 `15번 인물 백과`에 들어갈
중간 인간층 인물 시트의 공용 템플릿이다.

`14번 영웅 시트`처럼 과도하게 무겁지 않고,
관계망과 조직 기능이 잘 보이도록 설계한다.

## Template

```md
# [Name]

## 1. Core Identity

- primary anchor:
  - `세력 / 조직 / 도시`
- role:
  - `직책`
- type:
  - `Faction Embedded / Organization Mesh / Region Embedded / Event Embedded`
- status:
  - `safe_15 / verify_before_15 / hold`

## 2. World Function

- 이 인물이 세계 안에서 실제로 하는 일
- 조직이 굴러가는 감각을 어떤 방식으로 보여주는지
- 영웅이 아닌데도 왜 필요한지

## 3. Spatial Tie

- primary place:
  - `핵심 장소`
- secondary place:
  - `부차 장소`
- route value:
  - `항만 / 하수구 / 길드 본부 / 시장 / 감금 시설 / 서고` 등

## 3-1. Policy Guard

- 이 카드가 보강하는 운영층/기관층이 무엇인지 쓴다.
- 동시에 무엇으로 과독해하면 안 되는지도 쓴다.
- 상위 summary/index/folder 문서는 guard family를 참조할 수는 있어도,
  exact operational guard wording은 각 profile card가 여기서 직접 작성하고 유지한다.

예시:

- `해양` 자유도시 카드면:
  - `urban_market / shadow_port / debt-enforcement` 축을 보강하지만,
    `토착 공동체층` 본체 근거로 읽지 않는다.
- `오벨리스크` 제도 카드면:
  - `nontraditional elite thin-support` 또는 `dark institution` 축을 보강하지만,
    전통 왕국/귀족국가 복원 근거로 읽지 않는다.
- `범대륙 후기 확장` 카드면:
  - `deferred_expansion_hold` 또는 후기 확장 내부 reference로만 유지하고
    5대륙 본선 증거로 끌어오지 않는다.
- `에테르` 정령연합 예외축 카드면:
  - 정령연합 내부 예외축을 보강하지만 에테르 전체 부족층 일반화 근거로 읽지 않는다.

## 4. Relation Hooks

- `누구`와 어떤 방식으로 닿는가
- `영웅`과 직접 엮이는가, 간접적으로 구조를 떠받치는가
- `ally / intermittent_alignment / enemy / asymmetric_awareness` 등

## 5. Archive Use

- 개별 문서가 필요한 이유
- 조직 묶음 안에서 어떤 위치인지
- 액트 연결, 도시 지도, 경제 구조, 첩보 구조 중 어디에 강한지

## 6. Conductor Note

- 이 시점에 확정할 것
- 후속 보강축
- 14와 충돌 가능성이 있는지
```

## Field Rule

- `14번`처럼 능력치와 전설성을 과도하게 늘리지 않는다.
- 중간 인간층의 핵심은
  `무엇을 하는가`, `어디서 움직이는가`, `누구와 닿는가`다.
- 한 인물 시트가 길어지더라도
  `세계 기능`과 `공간 연결`은 반드시 남긴다.
- canonical 상태어와 `Policy Guard` 문장은 서로 다른 층이므로 둘을 함께 유지한다.
- 이 템플릿의 `3-1. Policy Guard`는 operational profile 카드의 exact guard wording authority다.
- 상위 track/index/display/intake 문서는 이 가드 family를 참조할 수는 있어도,
  여기 적힌 guard 문장을 대체하거나 축약 권한을 가지지 않는다.
- 위 예시는 family-level guidance일 뿐이고,
  실제 카드에서는 카드별 맥락에 맞는 exact prose를 다시 써야 한다.

## Recommended Use

아래 경우 이 템플릿을 우선 사용한다.

1. 조직 운영의 핵심 실무자
2. 도시 기능 구획과 직접 연결되는 인물
3. 영웅은 아니지만 반복 접점 가치가 높은 인물
4. `15번`으로 회수한 뒤 나중에 관계망 표에 넣을 인물

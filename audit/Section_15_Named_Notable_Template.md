# Section 15 Named Notable Template

이 문서는 `15번 Named Notables`에 들어갈
이름 있는 명사형 인물 시트의 공용 템플릿이다.

이 축은 `Operational Lines`와 다르게
개별 이름과 기억 가치를 우선한다.

## Template

```md
# [Name]

## 1. Core Identity

- reading:
  - `대표 호칭`
- anchor:
  - `도시 / 세력 / 학파 / 공방`
- type:
  - `Named Notable`
- recorded judgment:
  - `named_notable_candidate`
  - `verify_before_15`
  - `support_hold`
  - `deferred_expansion_hold`
  - `hold_for_dual_review`

## 1-1. Archive Routing

- continent_anchor:
  - `대륙`
- faction_anchor:
  - `세력 / 도시 / 조직`
- city_or_place_anchor:
  - `핵심 장소`
- secondary_index:
  - `현자 / 장인 / 기록자 / 감정사 / 연금술사 / 공방주`
- routing_state:
  - `stable_15_workset / route_hierarchy_locked`
  - `verify_before_15`
  - `support_hold`
  - `deferred_expansion_hold`
  - `hold_for_dual_review`

## 1-2. Policy Guard

- 이 카드가 보강하는 층이 무엇인지 쓴다.
- 동시에 무엇으로 과독해하면 안 되는지도 쓴다.
- 이 구간은 named-notable guard logic이며,
  operational profile 카드의 `3-1. Policy Guard`와는 parallel but non-substitutable layer다.

예시:

- `크림슨` 카드면:
  - 씨족 중심 질서와 학술/전승/공방 thin-support를 보강하지만,
    전통 귀족국가형 `state_house strong` 근거로 읽지 않는다.
- `해양` 자유도시 카드면:
  - `urban_market / shadow_port / debt-enforcement` 축을 보강하지만,
    `토착 공동체층` 본체 근거로 읽지 않는다.
- `오벨리스크` 제도 카드면:
  - `nontraditional elite thin-support` 또는 `dark institution` 축을 보강하지만,
    전통 왕국/귀족국가 복원 근거로 읽지 않는다.
- `범대륙 후기 확장` 카드면:
  - `deferred_expansion_hold` 내부 카드로만 유지하고 5대륙 본선 증거로 끌어오지 않는다.

## 2. Why Remembered

- 왜 이 인물을 사람들이 기억하는가
- 왜 찾아가야 하는가
- 세계 안에서 어떤 분야의 얼굴인가

## 3. World Function

- 지식, 제작, 기록, 치료, 감정, 전승 등
  무엇을 여는 인물인지
- 주인공이 아니어도 왜 중요한지

## 4. Spatial Tie

- primary place:
  - `핵심 장소`
- secondary place:
  - `부차 장소`
- route value:
  - `서고 / 공방 / 제단 / 탑 / 항만 / 진료실` 등

## 5. Relation Hooks

- 어떤 영웅이나 세력과 닿는가
- 조언자, 거래자, 경고자, 연구자, 복원자 같은
  관계 역할이 무엇인가

## 6. Archive Use

- `14`보다 `15 Named Notables`에 두는 이유
- 아이템, 지도, 지식, 전승, 도시 분위기 중 어디에 강한지

## 7. Conductor Note

- 이 시점에 확정할 것
- 14와 겹칠 위험
- 후속 판독축
```

## Conductor Rule

- 직업별 폴더링을 본체로 삼지 않는다.
- 본체는 항상 `대륙 -> 세력 / 도시 / 조직` 앵커다.
- `secondary_index`는 검색과 보조 색인용으로만 둔다.
- `SS / S / A급`, `Act 중심성`, `전설 영웅록`, `독립 14 파일` 신호가 있으면 `verify_before_15`로 둔다.
- 강한 명사 가치가 있어도 14 신호가 강하면 먼저 경계 큐에 보낸다.
- `stable_15_workset / route_hierarchy_locked`는 stable triad 같은 actual draft package에만 쓴다.
- `support_hold`, `deferred_expansion_hold`는 stable triad package와 섞지 않는다.
- `Policy Guard` 문장은 canonical 상태어를 대체하지 않는다.
- canonical 상태어와 policy carryover 문장을 같이 유지해야 한다.
- 이 템플릿의 `Policy Guard`는 named notable 카드용 해석 가드다.
- operational profile 카드의 `3-1. Policy Guard`와 guard family가 비슷해 보여도,
  exact wording authority는 각 카드층에 따로 남기고 서로 대체하지 않는다.
- 상위 문서가 named-notable guard family를 참조할 수는 있어도,
  operational profile guard wording authority는 오직 `Section_15_Profile_*` 카드의 `3-1. Policy Guard`에 남긴다.
- 자유도시/오벨리스크 경계 문장을 named-notable 카드에서 언급할 때도,
  그것은 named-notable routing safeguard일 뿐 operational profile guard text를 대신하지 않는다.

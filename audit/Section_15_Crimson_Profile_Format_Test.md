# Section 15 Crimson Profile Format Test

이 문서는 기존 `15 People Worth Seeking` 개별 시트가
새로 고정한 폴더링 원칙과 맞는지 확인한 결과다.

검토 대상:

- `Section_15_Named_Notable_Wolfgar_Dragonforge.md`
- `Section_15_Named_Notable_Erion_Dracovis.md`
- `Section_15_Named_Notable_Oghma.md`

## Result

기존 시트는 내용 방향이 맞다.

다만 앞으로 실제 15번 백과로 전환할 때는
아래 필드를 더 명시하는 편이 좋다.

- `continent_anchor`
- `faction_anchor`
- `city_or_place_anchor`
- `secondary_index`
- `routing_state`

## Tested Profiles

| Profile | Strength Snapshot | Missing Field | Routing Read |
|---|---|---|---|
| 울프가르 드래곤포지 | 장인형 명사 가치가 매우 선명하다. | `continent_anchor`, `faction_anchor`, `secondary_index` | `크림슨 -> 용의 후예 -> 드래곤포지 계열` |
| 에리온 드라코비스 | 대현자 / 고대어 해석가 가치가 선명하다. | `continent_anchor`, `faction_anchor`, `secondary_index` | `크림슨 -> 엘드라칸 -> 대현자층` |
| 오그마 | 살아있는 도서관 / 고룡 조언자 가치가 선명하다. | `continent_anchor`, `faction_anchor`, `secondary_index` | `크림슨 -> 엘드라칸 -> 전승 보관층` |

## Template Adjustment

다음부터 `15 People Worth Seeking` 시트는 아래 블록을 맨 위쪽에 넣는 것이 좋다.

```md
## Archive Routing

- continent_anchor:
  - `크림슨`
- faction_anchor:
  - `용의 후예`
- city_or_place_anchor:
  - `드래곤포지`
- secondary_index:
  - `장인`
  - `대장장이`
  - `공방주`
- routing_state:
  - `stable_15_workset`
  - `route_hierarchy_locked`
```

그리고 그 아래에는 짧은 `Policy Guard` 블록을 붙여,
크림슨 카드가 씨족 중심 질서와 thin-support를 보강하는 것인지,
아니면 `state_house strong` 승격 근거가 아닌지를 함께 적는 편이 좋다.

operational profile template을 쓰는 문서라면
이 블록은 `Section_15_Profile_Template.md`의 `3-1. Policy Guard` 형식을 그대로 따르는 편이 좋다.

## Profile-Specific Notes

### 울프가르 드래곤포지

- 기존 시트의 `anchor: 드래곤포지`는 좋다.
- 다만 `크림슨 / 용의 후예`가 명시되지 않아 나중에 직업별 폴더로 오해될 수 있다.
- 보조색인은 `장인 / 대장장이 / 공방주 / 무구 제작`으로 둔다.

### 에리온 드라코비스

- 기존 시트의 `anchor: 엘드라칸`은 좋다.
- 보조색인은 `현자 / 고대어 / 해석가 / 관리자`로 둔다.
- `에리온`은 직업보다 `엘드라칸`이라는 장소/세력 기억에 붙어야 한다.

### 오그마

- 기존 시트의 `anchor: 엘드라칸`은 좋다.
- 보조색인은 `고룡 / 살아있는 도서관 / 전승 보관자 / 조언자`로 둔다.
- `오그마`는 전투력보다 도시와 전승의 얼굴로 읽는 편이 맞다.

## Conductor Decision

기존 3개 시트는 유지한다.

다만 다음 업데이트 때는 개별 시트 자체에 `Archive Routing` 블록을 추가해
직업별 폴더링 오해를 줄이고,
`stable_15_workset / route_hierarchy_locked` 상태를 직접 보이게 한다.

또한 크림슨 카드들은
`tribe_clan core + 학술/전승/공방 thin-support`
범위 안에서만 읽는다는 `Policy Guard`를 같이 두는 편이 안전하다.

## Frozen Test Authority Guard

- 이 profile format test는 frozen routing/sample reference로만 읽는다.
- continent sidecar/scout/display wording umbrella는
  lower current-state watch/reference authority로만 읽고,
  이 test 문서가 place/institution owner나 candidate build queue를 새로 만들지 않는다.

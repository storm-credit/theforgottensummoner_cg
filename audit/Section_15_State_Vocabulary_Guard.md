# Section 15 State Vocabulary Guard

이 문서는 `15 Named Notables` 본선에서
상태어 drift를 막기 위한 canonical 상태어 장부다.

목적은 단순하다.

`summary`, `bridge`, `register`, `template`, `package freeze` 문서가
같은 상태어를 쓰게 한다.

## Input

- `audit/Section_15_Named_Notables_Register.md`
- `audit/Section_15_Stable_Candidate_8_Anchor_Index.md`
- `audit/Section_15_Actual_Draft_Package_Freeze.md`
- `audit/Section_15_Named_Notables_Status_Compass.md`
- `audit/Section_15_Named_Notables_Anchor_Map.md`
- `audit/Section_15_Five_Continent_Closure_Table.md`
- `audit/Section_15_Named_Notables_Continent_Synthesis.md`
- `audit/Section_8_to_15_Notable_Anchor_Bridge.md`

## Canonical State Set

### Core Routing

- `named_notable_candidate`
- `verify_before_15`
- `need_named_candidate`
- `keep_14`
- `keep_14_likely`

### Stable Package

- `stable_15_workset`
- `route_hierarchy_locked`
- `grade_caution`
- `act_watch`
- `name_collision_watch`

### Hold Family

- `support_hold`
- `deferred_expansion_hold`
- `hold_for_dual_review`

### Specialized Hold Notes

- `sage_queen_hold`
- `fire_priest_hold`
- `war_artificer_hold`
- `seer_strategy_hold`
- `library_core_hold`
- `archive_admin_hold`
- `tower_seer_hold`
- `bardic_archive_hold`
- `white_tower_barrier_hold`
- `abyss_blood_taboo_hold`
- `shadow_intelligence_hold`
- `holy_barrier_hold`
- `great_druid_hold`
- `spirit_envoy_hold`
- `shadow_crow_hold`

## Usage Rule

1. `State Label`, `Package State`, `routing_state`, `Gate Result` 칸에는 underscored 상태어만 쓴다.
2. prose에서는 자연어를 써도 되지만, state를 직접 다시 적을 때는 canonical 상태어를 그대로 쓴다.
3. `support_hold`와 `deferred_expansion_hold`는 stable triad package와 섞지 않는다.
4. `named_notable_candidate`는 후보 자격이고, `stable_15_workset`은 actual draft package 단계다.
5. `hold_for_dual_review`는 14/15 가치가 둘 다 큰 경우에만 쓴다.
6. legacy 상태어는 이 문서의 `Legacy Mapping` 표나 명시적 history note에만 남길 수 있다. 현재 state table, heading, checklist, routing line에는 다시 올리지 않는다.

## Policy Carryover Rule

이 문서는 `상태어`를 잠그는 장부이고,
카드층에 들어간 `Policy Guard` 문장을 상태어로 치환하는 문서는 아니다.

즉 아래 구분을 유지한다.

- `support_hold`, `deferred_expansion_hold`, `stable_15_workset` 같은 항목은 canonical state다.
- `urban_market`, `shadow_port`, `dark institution`, `nontraditional elite thin-support`,
  `state_house strong 금지`, `토착 공동체층 본체 아님` 같은 문장은
  상태어가 아니라 해석 가드다.

따라서:

1. 해석 가드 문장을 `State Label` 칸에 그대로 넣지 않는다.
2. 반대로 canonical state만으로 카드층 `Policy Guard`를 대체하지 않는다.
3. summary / bridge / index / folder / routing 문서는
   `canonical state`와 `policy carryover sentence`를 함께 유지해야 한다.
4. `state_house strong`, `토착 공동체층`, `전통 국가기관` 같은 표현은
   승격 선언이 아니라 금지/경계 문맥에서만 다시 등장할 수 있다.
5. operational profile card는
   `Section_15_Profile_Template.md`의 `3-1. Policy Guard` heading 형식을 유지하고,
   named notable card의 `Policy Guard / Separation Guard`와 형식층을 섞지 않는다.
6. template, track, index, display, intake 문서는
   guard family를 요약할 수는 있어도 exact guard wording authority를 가져가지 않는다.
7. exact guard wording authority는
   `Section_15_Profile_*` operational card의 `3-1. Policy Guard`와
   `Section_15_Named_Notable_*` 카드의 `Policy Guard / Separation Guard`에 남긴다.
8. 상위 template/index/folder 문서는 operational guard text를
   canonical summary 문장으로 압축해 lower card를 덮어쓰지 않는다.
9. named-notable template guard text와 operational profile `3-1. Policy Guard`는
   parallel but non-substitutable layer로 유지한다.

## Legacy Mapping

| Legacy Form | Canonical Form | Rule |
|---|---|---|
| `support hold` | `support_hold` | state label에서는 underscore로 통일 |
| `deferred expansion hold` | `deferred_expansion_hold` | state label에서는 underscore로 통일 |
| `deferred_zone` | `deferred_expansion_hold` | 범대륙 후기 확장 보류 상태는 이 라벨로 통일 |
| `strong_15` | `named_notable_candidate` | 강후보 서술을 상태 라벨로 쓰지 않는다 |
| `borderline_14_15` | `hold_for_dual_review` 또는 `verify_before_15` | 근거에 따라 둘 중 하나로 내린다 |
| `route_test_ok` | `stable_15_workset / route_hierarchy_locked` | stable triad actual draft 문맥에서만 대체 |

## Conductor Decision

앞으로 `15` 오케스트라 업데이트는
이 문서를 기준으로
stable triad, hold queue, boundary review, deferred expansion을
같은 상태어로 유지한다.

동시에 카드층 `Policy Guard`가 잠근 해석선은
summary / bridge / index / folder / routing 문서에 prose carryover로 유지한다.

# Section 15 Stable Candidate Profile QA

이 문서는 현재 안정 15 후보 시트의 frozen QA snapshot이다.

대상:

- `울프가르 드래곤포지`
- `에리온 드라코비스`
- `오그마`
- `엘다라`
- `실비아`

## QA Checklist

| Candidate | Archive Routing | Primary Route Anchor | Place Lock / Detail | 14 Boundary Note | Name Collision Note | Recorded Result |
|---|---|---|---|---|---|---|
| `울프가르 드래곤포지` | `present` | `크림슨 / 용의 후예 / 드래곤포지 공방` | `드래곤포지`, `프라이멀 엠버` | `A급/전설 영웅록 신호 확인` | `Wolfgar 다중 이름 충돌` | `pass_with_grade_caution / stable_triad_frozen_reference_set / hardening_guard_added / route_hierarchy_locked` |
| `에리온 드라코비스` | `present` | `크림슨 / 엘드라칸 / 학술-전승층` | `엘드라칸 학자 구역`, `용언 도서관` | `A급/기록관/세력 핵심표 신호 확인` | `Erion 다중 이름 충돌` | `pass_with_grade_caution / stable_triad_frozen_reference_set / hardening_guard_added / route_hierarchy_locked` |
| `오그마` | `present` | `크림슨 / 엘드라칸 / 전승 보관층` | `몽상가의 바위`, `지혜의 샘` | `낮음` | 없음 | `pass / stable_triad_frozen_reference_set / hardening_guard_added / route_hierarchy_locked` |
| `엘다라` | `present` | `에테르 / 정령연합 / 루미라` | `고대수 도서관`, `현자 의회` | `정령연합 전체 14 확인 전 Hard Canon 금지` | 없음 | `pass_with_source_check_hold / hold_reference_split` |
| `실비아` | `recorded_reference` | `범대륙 후기 확장 / 키르케 영약회` | `고통의 증류탑` | `낮음` | `실비아 다중 충돌` | `pass_with_deferred_expansion_hold / name_collision_watch` |

## Residual Watch Conditions

| Candidate | Follow-up |
|---|---|
| `울프가르` | 크림슨 8번 문서에서 A급/전설 영웅록 신호가 확인됐으므로 14 독립 파일 여부 reference check 유지. |
| `에리온` | 에테르 `에리온 베르날리스`와 병합 금지. 크림슨 `에리온 드라코비스`의 14 독립 파일 여부 reference check 유지. |
| `오그마` | 특정 Act 핵심 개입도가 강하면 14 경계 재검토. |
| `엘다라` | 정령연합 전체 14 파일 확인 전 `source_check_hold`로만 남기기. |
| `실비아` | 범대륙 후기 확장축이므로 watch-reference deferred hold 유지, 이름 충돌 계속 감시. |

## Policy QA Guard

- `울프가르 / 에리온 / 오그마`의 QA pass는 크림슨 씨족 중심 질서와 학술/전승/공방 thin-support 범위 안에서만 유효하다.
- 이 QA pass를 전통 귀족국가형 `state_house strong` 고정 근거로 사용하지 않는다.
- 이 QA 문서는 profile card의 `3-1. Policy Guard`를 참조해 판정할 뿐,
  exact guard wording authority를 대체하지 않는다.
- `엘다라`는 정령연합 내부 예외축 hold reference split 안의 `source_check_hold`로만 QA pass를 인정한다.
- `실비아`는 `deferred_expansion_hold` 내부 카드로만 QA pass를 인정하고, 5대륙 본선 대표 카드로 올리지 않는다.

## Conductor Decision

현재 안정 후보 5명의 시트는 frozen reference/watch 기준으로만 유지 가능하다.

`울프가르`, `에리온`, `오그마` 시트에는
`Hardening Guard`, `Boundary Guard`, `place_function_lock` 계열 문구가 이미 반영된 상태로 본다.

15번 폴더 기준 live 이동은 아직 scope 밖으로 둔다.
현재 메인 본선은 `울프가르`, `에리온`, `오그마` 3명의 closed reference set을 다시 여는 것이 아니라,
이미 잠근 carryover 상태와 route hierarchy lock을
closure sync / watch-reference 기준으로 유지하는 것이다.

`엘다라`는 보조 후보로 유지하되,
정령연합 전체 14 확인 전 `엘다라`는 `source_check_hold`로만 남긴다.

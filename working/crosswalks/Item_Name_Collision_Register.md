# Item Name Collision Register

이 문서는 아이템 후보와 인물명/세력명/마법명이 겹치는 경우를 따로 관리한다.

지금은 아이템 백과 본편을 확장하는 단계가 아니므로,
`Item_Candidate_Register.md`에 바로 병합하지 않고
충돌 신호만 별도로 둔다.

## Rule

- 같은 단어가 아이템, 인물, 가문명, 마법명으로 모두 쓰이면 `collision`으로 둔다.
- 아이템 백과로 올리기 전, 실제 물건인지 기능어인지 확인한다.
- 인물 백과와 아이템 백과 양쪽에서 같은 단어를 볼 수 있게 교차 참조를 남긴다.

## Current Collisions

| Term | Item / Artifact Signals | Character / Name Signals | Current Judgment | Next Action |
|---|---|---|---|---|
| `Aegis / 아이기스 / 이지스` | `Coat of the Unthinking Aegis`, `Aegis of Circulating Chlorophyll`, `Heartstone of the Aegis`, `Aegis Crystal`, 다수 방패/결계/방어구명 | `아이기스 (Aegis)`, `알렉산더 이지스`, `이지스 그림쉴드` | `item_name_collision` | 인물명, 성씨, 방패/결계/아이템명을 분리한다. |

## Aegis Working Rule

- `Aegis`는 기능어로 너무 넓게 쓰인다.
- `아이기스` 단독 인물명은 정본 승격 전 보류한다.
- `알렉산더 이지스`처럼 성씨로 쓰인 경우는 인물 앵커에 둔다.
- `Coat of the Unthinking Aegis`처럼 장비명으로 쓰인 경우는 아이템 후보로 둔다.
- `Aegis Crystal`처럼 결계/수정/방벽 구조물로 쓰인 경우는 아이템 또는 장소/장치 후보로 나눈다.

## Cross Reference

- 인물 충돌 쪽:
  - `audit/Section_15_Named_Notables_Name_Collision_Register.md`
- 아이템 분류 원칙:
  - `workflow/07_Item_Canon_Schema.md`
  - `working/crosswalks/Item_Longterm_Taxonomy.md`

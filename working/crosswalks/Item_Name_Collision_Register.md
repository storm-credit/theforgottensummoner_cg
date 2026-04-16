# Item Name Collision Register

이 문서는 아이템 후보와 인물명/세력명/마법명이 겹치는 경우를 따로 관리한다.

이 단계는 아이템 백과 본편을 확장하는 단계가 아니므로,
`Item_Candidate_Register.md`에 바로 병합하지 않고
충돌 신호만 별도로 둔다.

## Rule

- 같은 단어가 아이템, 인물, 가문명, 마법명으로 모두 쓰이면 `collision`으로 둔다.
- 아이템 백과로 올리기 전, 실제 물건인지 기능어인지 확인한다.
- 인물 백과와 아이템 백과 양쪽에서 같은 단어를 볼 수 있게 교차 참조를 남긴다.

## Collision Snapshot

| Term | Item / Artifact Signals | Character / Name Signals | Recorded Judgment | Reference Action |
|---|---|---|---|---|
| `Aegis / 아이기스 / 이지스` | `Coat of the Unthinking Aegis`, `Aegis of Circulating Chlorophyll`, `Heartstone of the Aegis`, `Aegis Crystal`, 다수 방패/결계/방어구명 | `아이기스 (Aegis)`, `알렉산더 이지스`, `이지스 그림쉴드` | `item_name_collision` | 인물명, 성씨, 방패/결계/아이템명을 분리한다. |

## Aegis Working Rule

- `Aegis`는 기능어로 너무 넓게 쓰인다.
- `아이기스` 단독 인물명은 정본 승격 전 보류한다.
- `알렉산더 이지스`처럼 성씨로 쓰인 경우는 인물 앵커에 둔다.
- `Coat of the Unthinking Aegis`처럼 장비명으로 쓰인 경우는 아이템 후보로 둔다.
- `Aegis Crystal`처럼 결계/수정/방벽 구조물로 쓰인 경우는 아이템 또는 장소/장치 후보로 나눈다.

## Living / Mount / Device Ambiguity Snapshot

이 표는 아이템 후보지만 생물, 탈것, 장치, 신체개조, 고유명 후보와 섞일 수 있는 항목을
아이템 백과 승격 전 한 번 더 막는 sidecar다.

| Term | Ambiguity Signal | Recorded Judgment | Reference Action |
|---|---|---|---|
| `은빛 그리폰 '칼리스토'` | `[성수 탑승물]`, 지능 있는 비행 마수/탑승물 | `living_mount_confirmed` | 아이템 백과 승격 금지. living / mount register 쪽으로 라우팅한다. |
| `푸른 스파크 마갑` | 전극 안장/마갑, 탈것 장비 | `mount_gear_confirmed` | 아이템 후보는 유지하되 mount gear bucket으로 분류한다. |
| `광전사의 심장 펌프` | `[아티팩트]`, 가슴판에 심어진 도핑 엔진 | `artifact_device_body_modification` | device / mechanism 후보로 유지하고 신체개조 경계 note를 남긴다. |
| `공간을 베어내는 차원의 열쇠` | `[무기]`, 큐브형 금속 매개체/공간 절단 장치 | `weapon_device_confirmed` | 무기/장치 후보로 유지하되 순수 개념 장치로 승격하지 않는다. |
| `칼리안 드라코` | 동족/교류 대상 고유명 | `proper_name_not_item` | 아이템 백과 승격 금지. proper-name collision으로 라우팅한다. |
| `테네브리움의 의안 부엉이` | `[아티팩트]`, 환영 부엉이 코어/지도 투시 장치 | `artifact_familiar_device` | artifact 후보는 유지하되 familiar / automaton / device 경계를 남긴다. |
| `천둥새의 적란운 렌즈` | `[아티팩트]`, 우안 이식 마도 렌즈 | `implanted_artifact_device` | artifact 후보는 유지하되 body-device 경계를 남긴다. |
| `심연을 가두는 유리 태풍병` | `[아티팩트]`, 물리 약병/압축 폭풍 수류탄 | `artifact_container_confirmed` | container / device 후보로 유지한다. |
| `마력 심장의 심장 엔진 귀걸이` | `[아티팩트]`, 귀걸이형 생체 출력 조작 장치 | `artifact_accessory_body_engine` | accessory 후보는 유지하되 body-engine 경계를 남긴다. |

Aegis 계열은 위 표에 중복하지 않고 `Aegis Working Rule`을 따른다.

## Cross Reference

- 인물 충돌 쪽:
  - `audit/Section_15_Named_Notables_Name_Collision_Register.md`
- 아이템 분류 원칙:
  - `workflow/07_Item_Canon_Schema.md`
  - `working/crosswalks/Item_Longterm_Taxonomy.md`

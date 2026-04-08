# Section 15 Named Notables Name Collision Register

이 문서는 `15 Named Notables` 후보 중
이름이 여러 세력/대륙에서 충돌하는 경우를 따로 관리한다.

## Rule

- 같은 이름이 여러 앵커에 있으면 바로 병합하지 않는다.
- 성/이명/세력 앵커가 다르면 별개 인물 후보로 본다.
- 아이템, 방패, 마법명으로도 쓰이는 말은 인물명 승격 전 `item_name_collision`으로 둔다.

## Sylvia Collision

현재 작업본에서 확인된 `실비아 / Sylvia` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `실비아 (Sylvia)` | `범대륙 / 키르케 영약회` | 고통의 기록자, S급, 시약 계량관, 증류탑 | `named_notable_candidate` |
| `실비아 아캄 (Sylvia Arkham)` | `에테르 / 마법협회 / 심연의 서고` | 차원 균열사, Void Caller | `separate_entity_candidate` |
| `실비아 (Sylvia)` | `해양 / 황금 함대 / 전설 마도 영웅록` | 해류의 지휘관, 파도의 여왕, 은빛 항해사 | `verify_before_15 / name_collision` |
| `실비아 팬텀 (Sylvia Phantom)` | `오벨리스크 / 망자의 왕국` | 망자의 눈, A급, 척후대장, 기억 집행관 계열 | `likely_keep_14_or_separate_entity` |

판정:

- 키르케 `실비아`와 해양 `실비아`를 병합하지 않는다.
- `실비아 아캄`, `실비아 팬텀`은 성/이명/소속이 달라 별개 후보로 둔다.
- 해양 `실비아`는 이름 충돌 때문에 `해양 실비아`라는 작업명으로 임시 구분한다.

## Aegis / 아이기스 Collision

현재 작업본에서 확인된 `Aegis / 아이기스` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `아이기스 (Aegis)` | `오벨리스크 / 봉인 수호단 / 전설 마도 영웅록` | 절대 방벽의 현자, 장벽의 수호자 | `verify_before_15 / item_name_collision` |
| `알렉산더 이지스 (Alexander Aegis)` | `에테르 / 왕국연합` | 14 현존 영웅, 성씨 또는 가문명 신호 | `keep_14` |
| `이지스 그림쉴드 (Aegis Grimshield)` | `오벨리스크 / 망자의 왕국` | A급 방패 대장, 망혼 방어선 | `verify_before_15 / separate_entity_candidate` |
| `아이기스 / Aegis` | `다수 문서` | 방패, 방벽, 결계, 방어구, 마법명으로 반복 사용 | `term_or_item_usage` |
| `Aegis of Ruin / Aegis Crystal / Heartstone of the Aegis` | `오벨리스크 / 봉인 수호단 및 심연 군단` | 방패/수정/심장석 계열 | `item_or_artifact_usage` |

판정:

- 오벨리스크 `아이기스`는 인물인지 유물/개념인지 아직 확정하지 않는다.
- 에테르 `알렉산더 이지스`와 병합하지 않는다.
- `Aegis`는 너무 넓은 기능어라, 인물 정본명으로 쓰려면 보조 이름이나 성을 붙여야 한다.

## Conductor Rule

`실비아`와 `아이기스`는 이름만 보고 15번에 넣지 않는다.

각각의 대륙/세력 앵커를 먼저 확인하고,
필요하면 표면명 또는 식별자를 추가한다.

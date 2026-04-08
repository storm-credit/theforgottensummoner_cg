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

## Ravenfell / Marcus / Maxwell Drift

현재 작업본에서 확인된 `Ravenfell / Marcus / Maxwell` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `마르쿠스 레이븐펠` | `에테르 / 마법협회 / 스카우트 기록` | 기존 스카우트 문서의 후보명 | `name_drift` |
| `맥스웰 레이븐펠 (Maxwell Ravenfell)` | `에테르 / 마법협회 / 흑색의 탑` | Top 3 흑색의 탑주, S급, Act 1~4 | `verify_before_15` |
| `마르쿠스 코르부스 (Marcus Corvus)` | `에테르 / 14 현존 영웅 / 중립세력 용병단` | 직접 14 영웅 파일, 심연/어둠의 마법사 | `keep_14 / separate_entity` |

판정:

- `마르쿠스 레이븐펠`과 `맥스웰 레이븐펠`은 우선 이름 흔들림으로 본다.
- `마르쿠스 코르부스`와 병합하지 않는다.
- 레이븐펠 계열은 15 확정 전에 원본 전체에서 실제 파일명을 다시 확인한다.

## Mera Drift

현재 작업본에서 확인된 `Mera / 메라` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `메라 라일윈드 (Mera Lylewind)` | `에테르 / 정령연합 / 외교 사절단` | 외교관, 희귀 재료 교역 조건, 정보 제공 | `verify_before_15 / name_drift` |
| `메라 실피드 (Mera Sylphid)` | `에테르 / 정령연합 / 14 현존 영웅` | 직접 14 영웅 파일, 바람의 사냥꾼 | `keep_14 / separate_or_same_unverified` |

판정:

- `메라 라일윈드`와 `메라 실피드`는 이름만 보고 병합하지 않는다.
- 둘이 같은 인물인지, 별개 인물인지, 구버전/신버전 표기인지 후속 검증이 필요하다.

## Rafferty / Raphael Arcadia Drift

현재 작업본에서 확인된 `Rafferty / Raphael Arcadia` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `래퍼티 아르카디아 (Rafferty Arcadia)` | `에테르 / 성국 / 성국 핵심 인물표` | 도서관장, A급, Act 2/3, 금서/고대 마법 연구 | `verify_before_15` |
| `라파엘 아르카디아 (Raphael Arcadia)` | `에테르 / 성국 / 아스트라르 도시 문서` | 도서관장, 에반의 이계 지식에 집착, 스승 후보 | `name_drift_or_duplicate_check` |

판정:

- `래퍼티`와 `라파엘`을 바로 병합하지 않는다.
- 둘 다 성국/아스트라르/도서관장 축에 걸려 있으므로 구버전/신버전 이름 또는 별도 인물 가능성을 모두 열어둔다.
- 15번 승격보다 먼저 14 독립 파일명과 원본 전체 표기를 확인한다.

## Valerius Collision

현재 작업본에서 확인된 `Valerius / 발레리우스` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `레오니스 발레리우스` | `에테르 / 성국 / 14 현존 영웅` | 성왕/핵심 영웅 축 | `keep_14` |
| `발레리우스 (Valerius the Lightbringer)` | `에테르 / 성국 / 루멘 성채` | 성기사단장, 루멘 성채 로컬 핵심 인물 슬롯 | `local_named_slot_needs_identity_check` |

판정:

- `발레리우스` 단독 표기는 `레오니스 발레리우스`와 바로 병합하지 않는다.
- 루멘 성채의 `Valerius the Lightbringer`가 별도 인물인지, 이명/오탈자인지, 구버전 이름인지 후속 확인한다.

## Drake Ruga / Rawson Drift

현재 작업본에서 확인된 `Drake` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `드레이크 루가 (Drake Ruga)` | `에테르 / 자유도시연합 / 14 현존 영웅` | 직접 14 파일, 포트 넥서스 제독, 해군 사령부 | `keep_14` |
| `드레이크 루가 (Drake Rawson)` | `에테르 / 자유도시연합 / 포트 넥서스 관련 문서` | 지배자/보호자 링크 표기 | `name_drift` |

판정:

- 현재 기준은 14 파일명 `드레이크 루가 (Drake Ruga)`를 우선 앵커로 둔다.
- `Rawson` 표기는 이름 드리프트 또는 링크 표기 오류로 보고 바로 별도 인물화하지 않는다.

## Selena Drift

현재 작업본에서 확인된 `Selena / 셀레나` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `셀레나 아르시엔 (Selena Arsienne)` | `에테르 / 왕국연합 / 14 현존 영웅` | 직접 14 파일, 사수/왕국연합 축 | `keep_14` |
| `셀레나 와일드웨이브 (Selena Wildwave)` | `에테르 / 자유도시연합 / 포트 넥서스` | 정보원, 그림자 조합, 뒷골목 지배자, 밀항 루트 | `verify_before_15 / separate_or_drift_check` |

판정:

- `셀레나 아르시엔`과 `셀레나 와일드웨이브`를 이름만 보고 병합하지 않는다.
- 대륙은 같지만 세력/역할이 달라, 별도 인물 또는 이름 드리프트 가능성을 모두 열어둔다.

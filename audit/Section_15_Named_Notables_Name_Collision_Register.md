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
- 아이템/유물/결계명 충돌은 `working/crosswalks/Item_Name_Collision_Register.md`를 교차 참조한다.

## Conductor Rule

`실비아`와 `아이기스`는 이름만 보고 15번에 넣지 않는다.

각각의 대륙/세력 앵커를 먼저 확인하고,
필요하면 표면명 또는 식별자를 추가한다.

Closure note:

- `Sylvia`는 `2026-04-09`에 개별 Decision / Change Log 행으로 backfill했다.
- `Aegis`는 현재 `오벨리스크 경계 후보군 / 아이기스` 대표 행으로 최소 closure 기준을 통과한다.
- `Aegis`의 인물/아이템/개념 분리는 `2026-04-09`에 `person_item_concept_split` refinement로 추가 연결했다.

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
- 현재 phase3 기준 흑색의 탑 주앵커는 `맥스웰 레이븐펠`로 읽고, `마르쿠스 레이븐펠`은 로컬/구형 표기로만 보존한다.

## Isador Tempest / Isadore Solea Split

현재 작업본에서 확인된 `Isador / Isadore` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `이사도르 템페스트 (Isador Tempest)` | `에테르 / 마법협회 / 청색의 탑 / 템페스트 학파` | Top 4 청색 탑주, S급, 번개 마법단 직할 | `verify_before_15 / separate_entity_candidate` |
| `이사도르 솔레아 (Isadore Solea)` | `에테르 / 마법협회 / phase2 직접 14 영웅 파일` | 솔레아 가문, 치유·구호 전략 장로, hero / s_rank 태그 | `keep_14 / separate_entity` |

판정:

- `이사도르 템페스트`와 `이사도르 솔레아`를 이름 유사성만으로 병합하지 않는다.
- `템페스트`는 청색 탑 / 번개·기동 / 템페스트 가문 축으로 읽고 `verify_before_15`를 유지한다.
- `솔레아`는 14 영웅 파일이 직접 확인된 별도 인물로 유지한다.
- `이사도르` 단독 표기는 반드시 `템페스트`인지 `솔레아`인지 가문/탑 앵커를 함께 적는다.

## Mera Drift

현재 작업본에서 확인된 `Mera / 메라` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `메라 라일윈드 (Mera Lylewind)` | `에테르 / 정령연합 / 외교 사절단` | 외교관, 희귀 재료 교역 조건, 정보 제공 | `verify_before_15 / name_drift` |
| `메라 실피드 (Mera Sylphid)` | `에테르 / 정령연합 / 14 현존 영웅` | 직접 14 영웅 파일, 바람의 사냥꾼 | `keep_14 / separate_or_same_unverified` |

판정:

- `메라 라일윈드`와 `메라 실피드`는 이름만 보고 병합하지 않는다.
- 둘이 같은 인물인지, 별개 인물인지, 구버전/신버전 표기인지 후속 검증이 필요하다.

## Christopher Delmar / Role Slot Distinction

현재 작업본에서 확인된 `Christopher Delmar / 크리스토퍼 델마르` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `크리스토퍼 델마르 (Christopher Delmar)` | `해양 / 황금 함대 / 거상 연합` | 검은 동전, 도난품 장물 처리, 암시장 자금 담당 | `verify_before_15 / named_boundary_candidate` |
| `대경매장 주인` | `해양 / 포트 아우렐리온` | 감정사, 정보상, 경매장 역할 슬롯 | `role_slot_confirmed / no_personal_name` |
| `항해사 길드장` | `해양 / 크로스윈드 포트` | 항해사 길드장, 해도/항로 역할 슬롯 | `role_slot_confirmed / no_named_candidate_yet` |

판정:

- `크리스토퍼 델마르`를 `대경매장 주인`이나 `항해사 길드장`의 실명으로 병합하지 않는다.
- `검은 동전`은 장물 금융 / 암시장 자금 축의 이명으로만 보존한다.
- 대경매장과 항해사 길드 역할은 개인명이 확인될 때까지 role slot으로 유지한다.

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
- `대서고 학장`, `대서고 수호장` 같은 개인명 없는 role slot을 `래퍼티`나 `라파엘`의 실명으로 확정하지 않는다.

## Valerius Collision

현재 작업본에서 확인된 `Valerius / 발레리우스` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `레오니스 발레리우스` | `에테르 / 성국 / 14 현존 영웅` | 성왕/핵심 영웅 축 | `keep_14` |
| `발레리우스 (Valerius the Lightbringer)` | `에테르 / 성국 / 루멘 성채` | 성기사단장, 루멘 성채 로컬 핵심 인물 슬롯 | `local_named_slot_needs_identity_check` |

판정:

- `발레리우스` 단독 표기는 `레오니스 발레리우스`와 바로 병합하지 않는다.
- 루멘 성채의 `Valerius the Lightbringer`가 별도 인물인지, 이명/오탈자인지, 구버전 이름인지 후속 확인한다.
- `Valerius` 단독 표기는 반드시 `레오니스`인지 `the Lightbringer`인지 출처/장소 앵커를 함께 적는다.
- `순교묘역 사제장`, `성채 봉인관` 같은 개인명 없는 role slot은 `Valerius the Lightbringer`나 `레오니스 발레리우스`의 실명으로 확정하지 않는다.

## Drake Ruga / Rawson Drift

현재 작업본에서 확인된 `Drake` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `드레이크 루가 (Drake Ruga)` | `에테르 / 자유도시연합 / 14 현존 영웅` | 직접 14 파일, 포트 넥서스 제독, 해군 사령부 | `keep_14` |
| `드레이크 루가 (Drake Rawson)` | `에테르 / 자유도시연합 / 포트 넥서스 관련 문서` | 지배자/보호자 링크 표기 | `name_drift` |

판정:

- 현재 기준은 14 파일명 `드레이크 루가 (Drake Ruga)`를 우선 앵커로 둔다.
- `Rawson` 표기는 이름 드리프트 또는 링크 표기 오류로 보고 바로 별도 인물화하지 않는다.
- `Drake` 단독 표기는 포트 넥서스 / 14 파일 앵커를 함께 확인한 뒤 사용한다.
- 오벨리스크 쪽 `need_named_candidate_or_verify_rugar` 슬롯과 `Ruga / Rawson` 계열을 혼동하지 않는다.

## Selena Drift

현재 작업본에서 확인된 `Selena / 셀레나` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `셀레나 아르시엔 (Selena Arsienne)` | `에테르 / 왕국연합 / 14 현존 영웅` | 직접 14 파일, 사수/왕국연합 축 | `keep_14` |
| `셀레나 와일드웨이브 (Selena Wildwave)` | `에테르 / 자유도시연합 / 포트 넥서스` | 정보원, 그림자 조합, 뒷골목 지배자, 밀항 루트 | `verify_before_15 / separate_or_drift_check` |

판정:

- `셀레나 아르시엔`과 `셀레나 와일드웨이브`를 이름만 보고 병합하지 않는다.
- 대륙은 같지만 세력/역할이 달라, 별도 인물 또는 이름 드리프트 가능성을 모두 열어둔다.
- `그늘항로 기록관`은 개인명 없는 role slot이므로 `셀레나 와일드웨이브`의 별칭/직함/실명으로 확정하지 않는다.

## Sylas Collision

현재 작업본에서 확인된 `Sylas / 실라스` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `실라스 블랙쏜` | `에테르 / 성국 / 옵시디안` | 감옥 관리자, 고문관, S급, 옵시디안 지하 대감옥 축 | `keep_14_likely` |
| `실라스 나이트쉐이드 (Sylas Nightshade)` | `에테르 / 정령연합 / 그늘까마귀단` | S급 암살자, 숲의 그림자, 잠든 정령의 숲 그림자 이동 시험 | `verify_before_15 / likely_keep_14` |

판정:

- 두 인물은 이름이 같지만 세력 앵커와 기능이 다르므로 바로 병합하지 않는다.
- `실라스 나이트쉐이드`는 정령연합 암살/첩보 축으로 따로 검증한다.
- `실라스 블랙쏜`은 성국 옵시디안 감옥/고문 축으로 유지한다.
- `Sylas` 단독 표기는 반드시 성국/정령연합 앵커와 함께 적는다.
- `옵시디안 무기지기` 같은 개인명 없는 role slot도 `실라스 블랙쏜`의 실명으로 확정하지 않는다.

## Wolfgar Collision

현재 작업본에서 확인된 `Wolfgar / 울프가르` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `울프가르 드래곤포지 (Wolfgar Dragonforge)` | `크림슨 / 용의 후예 / 드래곤포지 공방` | A급, 공방장, 프라이멀 엠버 대장장이, 전설 영웅록 신호 | `named_notable_candidate / grade_caution` |
| `울프가르 블레이즈프로스트 (Wulfgard Blazefrost)` | `프로스트 / role-slot scan` | 프로스트 인명 후보군, 냉염계 이름군 | `separate_entity_candidate / source_scan_only` |
| `울프가르 룬팽 (Wulfgar Runefang)` | `프로스트 / role-slot scan` | 룬/야수/전투 계열 이름군 | `separate_entity_candidate / source_scan_only` |
| `울프가르 스톰본 (Wulfgar Stormborn)` | `프로스트 / role-slot scan` | 폭풍/부족 전사 계열 이름군 | `separate_entity_candidate / source_scan_only` |

판정:

- `울프가르 드래곤포지`는 크림슨 `용의 후예 / 드래곤포지 공방` 앵커로만 읽는다.
- 프로스트의 `울프가르` 계열 이름군과 병합하지 않는다.
- `Wolfgar`는 대륙 간 이름 충돌이 이미 발생했으므로, 15번 시트 표면명만 보고 안정 후보로 올리지 않는다.
- `2026-04-09` closure pass에서 Decision / Change Log 직접 행으로 연결했다.

## Erion Collision

현재 작업본에서 확인된 `Erion / 에리온` 계열:

| Form | Anchor | Signal | Current Judgment |
|---|---|---|---|
| `에리온 드라코비스 (Erion Dracovis)` | `크림슨 / 엘드라칸 / 용언 도서관` | A급, 기록관, 용의 심장, 계약 증인, 세력 핵심표 신호 | `named_notable_candidate / grade_caution / name_collision_watch` |
| `에리온 베르날리스 (Erion Vernalis)` | `에테르 / 정령연합 / 14 현존 영웅` | 직접 14 파일, 정령연합 영웅 축 | `keep_14 / separate_entity` |

판정:

- `에리온 드라코비스`와 `에리온 베르날리스`는 병합하지 않는다.
- 크림슨 `에리온`은 15 시험 후보로 유지하되 `grade_caution`을 고정한다.
- 에테르 `에리온 베르날리스`가 존재하므로, `에리온` 단독 표기는 반드시 세력 앵커를 함께 적는다.
- `2026-04-09` closure pass에서 Decision / Change Log 직접 행으로 연결했다.

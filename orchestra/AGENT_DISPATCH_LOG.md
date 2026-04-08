# Agent Dispatch Log

이 문서는 오케스트라가 실제로 서브에이전트를 배치한 기록이다.

역할표와 실제 배치를 혼동하지 않기 위해,
앞으로 실제 에이전트를 띄운 경우 이곳에 남긴다.

## Rule

- 서브에이전트는 항상 필요한 배치마다 호출한다.
- 상시 자동 실행 프로세스로 가정하지 않는다.
- 서브에이전트는 읽기/진단/제안까지만 맡긴다.
- 최종 문서 반영, 커밋, 푸쉬는 Conductor가 한다.
- 원본 저장소는 어떤 에이전트도 수정하지 않는다.

## Active Dispatch

### 2026-04-08 KST - FS Engine Consistency Batch

목적:

- FS 엔진 분리 이후 실제 운용 문서가 서로 모순 없이 연결되는지 확인한다.
- 14/15 분리 기준이 문서 전체에 일관되게 남아 있는지 확인한다.
- Story / Media 모드가 Lore Engine과 섞이지 않았는지 확인한다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Ptolemy` | FS Lore Engine Auditor | Lore Engine 문서와 live register 점검 | `completed` |
| `Beauvoir` | FS Archive Routing Auditor | 14/15 split, Named Notables, Operational Lines 점검 | `completed` |
| `Boyle` | FS Story / Media Mode Auditor | Story Engine, Media Engine, Mode Routing 점검 | `completed` |

Conductor action:

- 에이전트 결과를 기다린 뒤 필요한 수정만 `cg` 저장소에 반영한다.
- 중복되거나 상충하는 제안은 `Open Question` 또는 후속 큐로 분리한다.

Integrated actions:

- Lore Engine에 live register 목록을 보강한다.
- 15번 색인을 Named Notables와 Operational Lines로 분리해서 보이게 한다.
- Media Engine에 Reveal Control과 Live Media Registers를 연결한다.
- Writing Craft Map을 `two-layer`가 아니라 `three-mode` 구조로 갱신한다.

Follow-up actions:

- 15번 Named Notables 등록부에 `State Label` 열을 추가한다.
- 15번 Operational Lines 색인에 `operational_line`과 `display_canon_candidate` 상태를 명시한다.
- Profile Draft Index가 Named Notables가 아니라 Operational Lines 중심임을 더 명확히 한다.
- Named Notables 2차 시드로 드락사르, 벨라나, 아리안, 엘다라를 추가한다.
- Operational Lines 상위 그룹명 후보를 더 판타지 표면명으로 정리한다.
- 14/15 경계 인물 검증 큐를 추가해 `verify_before_15` 대상의 처리 순서를 고정한다.
- 드락사르, 멜리산드르, 카사르 1차 근거를 확인하고 경계 큐 판단을 유지했다.
- 모이라, 레이나, 이사벨 1차 근거를 확인하고 `verify_before_15` 판단을 유지했다.
- 대런 크레센트, 칼레스트 나이트쉐이드 1차 근거를 확인하고 `verify_before_15` 판단을 유지했다.
- 이리나 폰 루즈, 칼리크 디트리히는 14 현존 영웅 고아 파일로 확인되어 `15 흡수`가 아니라 `14 유지 + 앵커/명칭 보정`으로 처리했다.
- Named Notables를 직업별이 아니라 `대륙 -> 세력 / 도시 / 조직` 기준으로 정렬하는 앵커 맵을 추가했다.
- 프로스트, 해양, 오벨리스크의 Named Notables 결손층을 정찰하고 다음 import 필요 범위를 기록했다.
- 프로스트, 해양, 오벨리스크의 전설 영웅록/핵심 영웅 문서에서 이름 있는 경계 후보를 추출하고 15 확정이 아니라 `verify_before_15` 배치로 분리했다.
- 새 경계 후보 중 `울프릭`, `미다스`, `해양 실비아`, `바리온`, `아이기스`, `카론`을 14/15 경계 검증 큐 Tier D로 연결했다.
- `실비아`와 `Aegis / 아이기스`의 다중 사용을 확인하고 이름 충돌 레지스터로 분리했다.
- `Aegis / 아이기스`는 아이템/방패/결계명 충돌도 커서 아이템 이름 충돌 레지스터로 추가 분리했다.
- Tier D 중 `미다스`와 `카론`은 복수 문서 신호가 확인되었지만 전설/전술 축이라 `verify_before_15`를 유지했다.
- Tier D 후보 6명을 `Section_15_Named_Notables_Register`에 `verify_before_15` 상태로 반영했다.
- Named Notables 커버리지 매트릭스를 추가해 대륙별 강약과 다음 수집 우선순위를 정리했다.
- 프로스트는 안전한 15 확정보다 역할 슬롯이 강한 대륙으로 판정하고, 시그리드/마리안은 `verify_before_15`, 원로 사냥꾼/묘지기 장로/대예언자/수석 기술자는 `need_named_candidate` 슬롯으로 분리했다.
- 해양은 이름 있는 후보가 많지만 제독/A급/히어로급 신호도 강한 대륙으로 판정하고, 이소벨/마르코/엘레오노라/골드핑거/리나/에릭/오렌/마리아/모로스는 `verify_before_15`, 수석 오라클/항로 기록관/조선소 수석 공병/장물 감정사는 `need_named_candidate` 슬롯으로 분리했다.
- 오벨리스크는 기록/봉인/망각/영혼 명사 후보가 밀집했지만 전설/히어로급/조직 핵심 신호도 강한 대륙으로 판정하고, 베스/이안/카트린/레보니아/우로스/세르반/레티시아는 `verify_before_15`, 기록의 수호자/사후 서기관/기억 경매장 중개자는 역할 슬롯으로 분리했다.
- 5대륙 Named Notables 스카우트 결과를 종합해 크림슨은 실제 15번 폴더링 시험 후보, 에테르는 다음 우선 스카우트 대상, 프로스트/해양/오벨리스크는 역할 슬롯 유지 및 14 검증 후 확정 대상으로 분리했다.
- 에테르 스카우트를 진행해 마법협회 7개 탑주, 대런 크레센트, 래퍼티 아르카디아, 대사제 요한, 정령연합 엘라라/드라이덴/메라를 `verify_before_15`로 분리하고, 서고/공방/관측소/성수/정령 계약 역할 슬롯을 `need_named_candidate`로 보존했다.
- 에테르 Tier E 후보를 1차 대조한 결과 세리오스 벤타리스는 14 현존 영웅 파일이 직접 확인되어 `keep_14_likely`로 보정하고, 나머지는 현재 import 범위에 직접 14 파일이 없으므로 `verify_before_15`를 유지했다.
- 크림슨 안정 후보를 기준으로 15번 Named Notables 폴더링 시험표를 추가하고, 직업별 폴더링이 아니라 `대륙 -> 세력 / 도시 / 조직` 앵커를 본체로 삼는 규칙을 검증했다.
- 울프가르/에리온/오그마 기존 15 시트를 점검한 결과 내용 방향은 유지하되, 다음 업데이트에서 `Archive Routing` 블록을 추가해 대륙/세력 앵커를 더 명시하기로 했다.
- 울프가르/에리온/오그마 개별 15 시트에 `Archive Routing` 블록을 추가해 `크림슨 -> 용의 후예/엘드라칸 -> 장소/조직` 앵커를 명시했다.
- 벨라나/아리안 추가 근거를 확인한 결과 각각 SS급/S급 핵심 인물 신호가 강해 안정 15 후보에서 `verify_before_15`로 보정하고, 크림슨 실제 시트 시험 후보를 울프가르/에리온/오그마 3명으로 좁혔다.
- `Section_15_Named_Notable_Template`에 `Archive Routing` 블록과 14 경계 신호 규칙을 추가해 이후 모든 Named Notables 시트가 같은 라우팅 기준을 따르게 했다.

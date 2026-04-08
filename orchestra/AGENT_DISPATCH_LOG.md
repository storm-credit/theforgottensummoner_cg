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

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

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

### 2026-04-08 KST - Orchestra Lock / Frost Register Batch

목적:

- 오케스트라 방식의 이점을 문서로 고정한다.
- 프로스트 슬롯을 코어 장부에 직접 연결한다.
- 현재 진행표와 엔진 색인을 최신 상태로 맞춘다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Carson` | Orchestra Advantage Auditor | `ACTIVE_AGENT_SPLIT`, `RUNBOOK`, `AGENT_DISPATCH_LOG`, 오케스트라 이점 잠금안 | `dispatched` |
| `Peirce` | Frost Core Register Link Auditor | 프로스트 슬롯과 `FS_Place_Function_Register`, `FS_Decision_Ruling_Register`, `FS_Slot_Maturation_Register` 정합성 점검 | `dispatched` |
| `Boyle` | Workstream Sync Auditor | `Next_Sequential_Workstream`, `Continuous_Workstream`, `Status Compass`, `OPEN_INDEX`, `FS Lore Engine` 갱신안 점검 | `completed` |

Conductor action:

- 오케스트라 이점은 별도 잠금 문서와 운용 문서에 함께 고정한다.
- 프로스트 슬롯 direct link와 Canon Change Log는 Conductor가 직접 반영한다.
- 실제 배치가 끝나면 다음 턴부터도 같은 규칙으로 재사용한다.

Integrated actions:

- `orchestra/ORCHESTRA_ADVANTAGE_LOCK.md` 작성
- `orchestra/EXECUTION_HARNESS_LOCK.md` 작성
- `ACTIVE_AGENT_SPLIT.md`, `RUNBOOK.md`에 오케스트라 이점과 분할 트리거를 고정
- `Start_Here.md`, `OPEN_INDEX.md`, `AGENT_ROSTER.md`, `SKILL_CANDIDATES.md`에 하네스 연결을 추가
- 프로스트 슬롯 6개를 `Place Function -> Decision Ruling -> Slot Maturation` 코어에 직접 연결
- `FS_Canon_Change_Log.md` 초안 작성
- `Next_Sequential_Workstream.md`를 현재 작업선 기준으로 재정리

Follow-up actions:

- `Story-to-Lore Handoff Gate` 초안 작성
- 기존 `verify_before_15` 항목 중 일부를 `Decision Ruling Register`와 더 직접 연결
- `FS_Canon_Change_Log.md`에 14/15 경계 변동분 backfill 추가

### 2026-04-08 KST - Story-to-Lore Handoff Gate Batch

목적:

- Story Engine에서 나온 새 설정 요소를 Lore Engine으로 되돌리는 게이트를 고정한다.
- Revision Gate, Change Log, Workstream이 같은 기준을 따르게 맞춘다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `McClintock` | Story-to-Lore Gate Auditor | Story / Lore / Revision / Harness 문서 기준 검토 | `completed` |
| `Wegener` | Engine Register Sync Auditor | Change Log / Workstream / Dispatch Log 연결 검토 | `completed` |

Conductor action:

- handoff gate 문서는 Conductor가 직접 작성한다.
- Story, Lore, Revision, Change Log, Workstream 연결은 같은 턴에 함께 반영한다.

Integrated actions:

- `audit/FS_Story_to_Lore_Handoff_Gate.md` 작성
- `workflow/16_FS_Story_Engine.md`, `workflow/15_FS_Lore_Engine.md`, `audit/FS_Revision_Gate_Checklist.md`에 gate 연결
- `audit/FS_Canon_Change_Log.md`, `audit/OPEN_INDEX.md`, `audit/Next_Sequential_Workstream.md`를 현재 기준으로 갱신
- `orchestra/EXECUTION_HARNESS_LOCK.md`에 `story_to_lore_handoff_hook`를 명시

Follow-up actions:

- `FS_Canon_Change_Log.md`에 14/15 경계 변동분 backfill 추가

### 2026-04-08 KST - Verify-Before-15 Decision Link Batch

목적:

- 반복되는 `verify_before_15` 판정을 `FS_Decision_Ruling_Register`에 직접 연결한다.
- Canon Change Log에 왜 보류했는지 복원 가능한 변화 기록을 남긴다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Franklin` | Crimson / Ether Boundary Ruling Scout | 크림슨 / 에테르 `verify_before_15` 대표 후보 추천 | `completed` |
| `Hegel` | Frost / Oceanic / Obelisk Boundary Ruling Scout | 프로스트 / 해양 / 오벨리스크 `verify_before_15` 대표 후보 추천 | `closed_without_merge` |

Conductor action:

- Franklin의 읽기 전용 제안 중 `벨라나`, `드락사르`, `칼리스트`만 이번 턴에 반영한다.
- Hegel은 결과가 오기 전에 종료되어 이번 반영에는 합치지 않는다.
- 최종 문서 반영은 Conductor가 직접 수행한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `story-born 신규 설정`, `벨라나`, `드락사르`, `칼리스트` 판정을 추가
- `FS_Canon_Change_Log.md`에 세 후보의 `verify_before_15` 직접 연결 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`의 다음 작업선을 handoff seed 시험 후 Canon Change backfill로 이동
- `FS_Story_to_Lore_Handoff_Seed_Cases.md`를 작성하고 `FS-HANDOFF-SEED-001`을 `item_hold`로 시험 적용
- `FS_Asset_Secret_Register.md`, `FS_Foreshadow_Payoff_Register.md`에 seed case의 register write를 남김

Follow-up actions:

- `FS_Canon_Change_Log.md`에 14/15 경계 변동분 backfill 추가
- 프로스트 / 해양 / 오벨리스크 쪽 `verify_before_15` 대표군은 다음 추가 연결 후보로 보존

### 2026-04-08 KST - Canon Change Boundary Backfill Batch

목적:

- 14/15 경계 후보의 상태 이동을 `FS_Canon_Change_Log.md`에 복원 가능하게 남긴다.
- 이미 로그에 있는 `벨라나`, `드락사르`, `칼리스트`와 중복하지 않는다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `James` | Crimson / Ether Change Backfill Scout | 크림슨 / 에테르 경계 변동 로그 후보 추천 | `completed` |
| `Kepler` | Frost / Oceanic / Obelisk Change Backfill Scout | 프로스트 / 해양 / 오벨리스크 경계 변동 로그 후보 추천 | `completed` |

Conductor action:

- James 제안 중 `카사르`, `세리오스`, `Ravenfell / Corvus drift`를 반영한다.
- Kepler 제안 중 `해양 경계 후보군`, `오벨리스크 경계 후보군 / 아이기스`를 반영한다.
- `크리스토퍼 델마르` 개별 행은 해양 경계 후보군 안에 흡수하고 다음 세부 후보로 보존한다.
- 프로스트는 이미 Change Log에 `unnamed slots 6종`과 `명사층 판정`이 있으므로 이번 backfill에서는 제외한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 5개 대표 판정 추가
- `FS_Canon_Change_Log.md`에 5개 14/15 경계 변동 backfill 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 live handoff case 대기 상태로 이동

Follow-up actions:

- 실제 원고 입력이 생기면 seed가 아니라 live handoff case로 승격
- 개별 이름 충돌 후보는 다음 세부 backfill에서 필요할 때만 추가

### 2026-04-08 KST - Live Handoff Queue Prep Batch

목적:

- 실제 원고 입력이 아직 없는 상태에서 live case를 발명하지 않는다.
- seed case와 live case가 섞이지 않도록 빈 intake queue를 따로 잠근다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Feynman` | Live Handoff Intake Queue Auditor | handoff gate, seed cases, workstream, index 연결 점검 | `completed` |

Conductor action:

- Feynman의 읽기 전용 제안에 따라 `FS_Story_to_Lore_Live_Handoff_Queue.md`를 새로 만든다.
- queue는 실제 원고 입력이 없으므로 비워 둔다.
- 예시 행은 live case로 오염될 수 있어 넣지 않는다.

Integrated actions:

- `audit/FS_Story_to_Lore_Live_Handoff_Queue.md` 작성
- `FS_Story_to_Lore_Handoff_Gate.md`에 Live Queue 링크 추가
- `OPEN_INDEX.md`, `FS_Canon_Change_Log.md`, `Next_Sequential_Workstream.md`, `Continuous_Workstream.md` 연결 갱신

Follow-up actions:

- 실제 원고 입력이 들어오면 `FS-LIVE-HANDOFF-###` 형식으로 live case 생성
- 실제 입력이 없으면 개별 이름 충돌 후보 세부 backfill로 진행

### 2026-04-08 KST - Individual Name Drift Backfill Batch

목적:

- 대표군에 흡수돼 있던 개별 이름 충돌 후보를 별도 병합 금지 판정으로 남긴다.
- role slot과 named boundary candidate가 섞이지 않게 한다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Descartes` | Christopher Delmar Distinction Scout | `크리스토퍼 델마르 / 검은 동전`과 해양 role slot 오인 방지 | `completed` |
| `Hubble` | Mera Drift Scout | `메라 라일윈드 / 메라 실피드` 병합 금지 근거 점검 | `completed` |

Conductor action:

- Descartes 제안을 반영해 `크리스토퍼 델마르`를 `대경매장 주인`, `항해사 길드장`과 병합하지 않도록 고정한다.
- Hubble 제안을 반영해 `메라 라일윈드`와 `메라 실피드`를 이름만으로 병합하지 않도록 고정한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 두 개별 병합 금지 판정 추가
- `FS_Canon_Change_Log.md`에 두 개별 backfill 기록 추가
- `Section_15_Named_Notables_Name_Collision_Register.md`에 `Christopher Delmar / Role Slot Distinction` 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 이름 충돌 세부 후보로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 `Rafferty / Raphael Arcadia` 또는 `Sylas` 계열 이름 충돌 후보 세부 backfill로 진행
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-08 KST - Arcadia / Sylas Name Drift Backfill Batch

목적:

- 에테르 성국/아스트라르 도서관장 축과 정령연합/성국 `Sylas` 축을 병합하지 않게 고정한다.
- 개인명 없는 role slot을 기존 이름 있는 후보의 실명으로 확정하지 않게 한다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Parfit` | Arcadia Drift Scout | `Rafferty / Raphael Arcadia` 이름 드리프트 점검 | `completed` |
| `Zeno` | Sylas Collision Scout | `실라스 블랙쏜 / 실라스 나이트쉐이드` 앵커 분리 점검 | `completed` |

Conductor action:

- Parfit 제안을 반영해 `래퍼티`와 `라파엘`을 이름 유사성과 도서관장 역할만으로 병합하지 않도록 고정한다.
- Zeno 제안을 반영해 `실라스 블랙쏜`과 `실라스 나이트쉐이드`를 세력 앵커별로 분리한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `Rafferty / Raphael Arcadia drift`, `Sylas / 실라스 collision` 판정 추가
- `FS_Canon_Change_Log.md`에 두 이름 충돌 backfill 기록 추가
- `Section_15_Named_Notables_Name_Collision_Register.md`에 role slot 확정 금지 문구 보강
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 이름 충돌 세부 후보로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 `Valerius`, `Drake Ruga / Rawson`, `Selena` 계열 이름 충돌 후보 세부 backfill로 진행
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-08 KST - Valerius / Drake / Selena Name Drift Backfill Batch

목적:

- 에테르 성국/루멘 성채 `Valerius` 축, 자유도시 `Drake Ruga / Rawson` 축, `Selena` 축을 이름만으로 병합하지 않게 고정한다.
- 개인명 없는 role slot을 기존 이름 있는 후보의 실명으로 확정하지 않게 한다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Jason` | Valerius Collision Scout | `레오니스 발레리우스 / Valerius the Lightbringer` 앵커 분리 점검 | `completed` |
| `Dalton` | Drake Ruga / Rawson Drift Scout | `Drake Ruga / Drake Rawson` 표기 흔들림 점검 | `completed` |
| `Lovelace` | Selena Drift Scout | `셀레나 아르시엔 / 셀레나 와일드웨이브` 병합 금지 근거 점검 | `completed` |

Conductor action:

- Jason 제안을 반영해 `레오니스 발레리우스`와 `Valerius the Lightbringer`를 원본 전체 표기 확인 전 병합하지 않도록 고정한다.
- Dalton 제안을 반영해 14 파일명 `Drake Ruga`를 우선 앵커로 두고 `Rawson`은 링크 표기 흔들림으로 보존한다.
- Lovelace 제안을 반영해 `셀레나 아르시엔`과 `셀레나 와일드웨이브`를 세력/역할 앵커별로 분리한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `Valerius`, `Drake Ruga / Rawson`, `Selena` 판정 추가
- `FS_Canon_Change_Log.md`에 세 이름 충돌 backfill 기록 추가
- `Section_15_Named_Notables_Name_Collision_Register.md`에 role slot 확정 금지 문구 보강
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 `Name Collision Register closure pass`로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 `Name Collision Register closure pass`로 남은 충돌군의 직접 연결 여부를 닫는다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Name Collision Register Closure Pass Batch

목적:

- `Section_15_Named_Notables_Name_Collision_Register.md`의 충돌군이 `FS_Decision_Ruling_Register.md`와 `FS_Canon_Change_Log.md`에 직접 연결됐는지 닫는다.
- 대표군 흡수로 충분한 항목과 개별 backfill이 필요한 항목을 분리한다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Planck` | Front Collision Closure Scout | `Sylvia`, `Aegis`, `Ravenfell`, `Mera`, `Christopher Delmar` 직접 연결 점검 | `completed` |
| `Erdos` | Rear Collision Closure Scout | `Rafferty`, `Valerius`, `Drake`, `Selena`, `Sylas`, `Wolfgar`, `Erion` 직접 연결 점검 | `completed` |

Conductor action:

- Planck 제안 중 `Sylvia` 직접 행만 반영하고, `Aegis`는 대표군 행으로 최소 closure 기준을 통과한 것으로 둔다.
- Erdos 제안 중 `Wolfgar`, `Erion` 직접 collision 행을 반영한다.
- 이미 충분한 `Ravenfell`, `Mera`, `Christopher`, `Rafferty`, `Valerius`, `Drake`, `Selena`, `Sylas`는 중복 행을 추가하지 않는다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `Sylvia`, `Wolfgar`, `Erion` collision 판정 추가
- `FS_Canon_Change_Log.md`에 세 collision closure backfill 기록 추가
- `Section_15_Named_Notables_Name_Collision_Register.md`에 closure note 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 정밀화 후보로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 `Aegis person / item / concept split refinement` 필요 여부를 판단한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Aegis Person / Item / Concept Split Refinement Batch

목적:

- `Aegis / 아이기스 / 이지스`가 인물명, 성씨, 유물명, 결계 기능어로 섞이는 지점을 정밀하게 분리한다.
- 새 장부를 만들지 않고 기존 item name collision crosswalk와 직접 연결한다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Chandrasekhar` | Aegis Split Scout | `Aegis`의 인물/아이템/개념 사용 분류 | `completed` |
| `Herschel` | Aegis Crosswalk Link Scout | 기존 item name collision 장부와 누락 연결 점검 | `completed` |

Conductor action:

- Chandrasekhar 제안을 반영해 `Aegis`를 인물명, 성씨, 유물명, 기능어로 분리하는 직접 판정을 추가한다.
- Herschel 제안을 반영해 새 `FS_Item_Name_Collision_Register.md`를 만들지 않고 기존 `working/crosswalks/Item_Name_Collision_Register.md`를 교차 참조한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `Aegis / 아이기스 person-item-concept split` 판정 추가
- `FS_Canon_Change_Log.md`에 Aegis 정밀화 기록 추가
- `Section_15_Named_Notables_Name_Collision_Register.md`에 item name collision crosswalk 참조 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 `verify_before_15` 대표군 직접 연결로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 다음 `verify_before_15` 대표군 2~3건을 `Decision Ruling Register`에 추가 연결한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Verify-Before-15 Representative Direct Link Batch 02

목적:

- 아직 개별 Decision 행이 없는 `verify_before_15` 대표 후보 중 2-3건만 직접 연결한다.
- 이미 직접 연결된 후보나 대표군 행으로 충분한 후보는 중복 추가하지 않는다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Pasteur` | Crimson / Ether Verify Scout | `아리안`, `대런`, `엘라라`, `요한`, `에드가` 우선순위 점검 | `completed` |
| `Bacon` | Frost / Oceanic / Obelisk Verify Scout | `이소벨`, `카론`, `시그리드` 등 비에테르 대표 후보 점검 | `completed` |

Conductor action:

- Pasteur 제안 중 `아리안`, `대런`을 반영한다.
- Bacon 제안 중 프로스트 보강 가치가 큰 `시그리드`를 반영한다.
- 이번 사이클은 3건으로 제한하고 `이소벨`, `카론`, `엘라라`는 다음 후보로 보존한다.
- 이미 직접 연결된 `벨라나`, `드락사르`, `칼리스트`, `카사르`, `래퍼티`는 중복하지 않는다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `아리안`, `대런`, `시그리드` 판정 추가
- `FS_Canon_Change_Log.md`에 세 후보의 direct ruling backfill 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 개별 backfill 후보로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 `이소벨 골드리프`, `카론`, `엘라라 문힘` 중 필요한 개별 backfill을 검토한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Verify-Before-15 Representative Direct Link Batch 03

목적:

- Batch 02에서 보존한 `이소벨 골드리프`, `카론`, `엘라라 문힘`의 개별 backfill 필요 여부를 확인한다.
- 대표군 행에 흡수하지 않고, 기능축이 뚜렷한 후보만 직접 판정으로 남긴다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Oceanic / Obelisk Verify Scout | `이소벨 골드리프`, `카론`의 해양/오벨리스크 경계 신호 점검 | `completed` |
| `Turing` | Ether Verify Scout | `엘라라 문힘`의 에테르 기록/노래 전승 축 점검 | `completed` |

Conductor action:

- Heisenberg 제안에 따라 `이소벨 골드리프`를 `finance_power_hold`, `카론`을 `soul_guide_hold`로 직접 연결한다.
- Turing 제안에 따라 `엘라라 문힘`을 `bardic_archive_hold`로 직접 연결한다.
- 세 후보 모두 15 확정자가 아니라 `verify_before_15` 보류 후보로 유지한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `이소벨 골드리프`, `카론`, `엘라라 문힘` 판정 추가
- `FS_Canon_Change_Log.md`에 세 후보의 direct ruling backfill 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 대표 후보 판단으로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 남은 `verify_before_15` 대표 후보 중 `대사제 요한`, `에드가 룬워커`, `레온 벨가르드`의 직접 연결 필요 여부를 판단한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Verify-Before-15 Representative Direct Link Batch 04

목적:

- `MCP / Skills / Agents / Hooks / Registers` 하네스를 실제 실행 순서대로 밟으면서 남은 에테르 대표 후보 3건을 직접 판정한다.
- 대표군 상태만으로는 판정 기억이 약한 후보를 개별 Decision / Change Log 행으로 잠근다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Oceanic / Ether Verify Scout | `대사제 요한`, `레온 벨가르드`의 직접 backfill 필요 여부 점검 | `completed` |
| `Turing` | Ether Forge Verify Scout | `에드가 룬워커`의 직접 backfill 필요 여부 점검 | `completed` |

Harness execution:

- `MCP gate`: `list_mcp_resources` / `list_mcp_resource_templates` 확인, 현재 배치에 직접 쓸 프로젝트형 MCP 자원 없음으로 `skip`
- `Skills gate`: 현재 작업과 직접 맞는 로컬 스킬 없음으로 `skip`
- `pre_scope_hook`: 대상 `대사제 요한`, `에드가 룬워커`, `레온 벨가르드`와 반영 장부 범위 고정
- `pre_dispatch_hook`: `요한/레온`과 `에드가`로 분리해 병렬 scout 배치
- `pre_write_hook`: source/state/route/naming/register 연결 확인 후 direct backfill 승인
- `post_write_hook`: Decision, Change Log, Workstream, Dispatch Log 갱신 확인
- `pre_close_hook`: 다음 실제 작업선을 `리아나 실버레이크`, `드라이덴 썬더루트`, `바리온` 판단으로 고정

Conductor action:

- Heisenberg 제안에 따라 `대사제 요한`을 `holy_barrier_hold`, `레온 벨가르드`를 `mercenary_guild_hold`로 직접 연결한다.
- Turing 제안에 따라 `에드가 룬워커`를 `rune_forge_hold`로 직접 연결한다.
- 세 후보 모두 15 확정자가 아니라 `verify_before_15` 보류 후보로 유지한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `대사제 요한`, `에드가 룬워커`, `레온 벨가르드` 판정 추가
- `FS_Canon_Change_Log.md`에 세 후보의 direct ruling backfill 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 대표 후보 판단으로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 남은 `verify_before_15` 대표 후보 중 `리아나 실버레이크`, `드라이덴 썬더루트`, `바리온`의 직접 연결 필요 여부를 판단한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Verify-Before-15 Representative Direct Link Batch 05

목적:

- 하네스 순서를 유지한 채 `리아나 실버레이크`, `드라이덴 썬더루트`, `바리온`의 직접 backfill 필요 여부를 판정한다.
- 대표군 요약만으로는 약한 후보를 개별 Decision / Change Log 행으로 잠근다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Ether Verify Scout | `리아나 실버레이크`, `드라이덴 썬더루트`의 직접 backfill 필요 여부 점검 | `completed` |
| `Turing` | Obelisk Verify Scout | `바리온`의 직접 backfill 필요 여부 점검 | `completed` |

Harness execution:

- `MCP gate`: `list_mcp_resources` / `list_mcp_resource_templates` 확인, 현재 배치에 직접 쓸 프로젝트형 MCP 자원 없음으로 `skip`
- `Skills gate`: 이 저장소에 직접 맞는 로컬 스킬 없음으로 `skip`
- `pre_scope_hook`: 대상 `리아나 실버레이크`, `드라이덴 썬더루트`, `바리온`과 반영 장부 범위 고정
- `pre_dispatch_hook`: `리아나/드라이덴`과 `바리온`으로 분리해 병렬 scout 배치
- `pre_write_hook`: source/state/route/naming/register 연결 확인 후 direct backfill 승인
- `post_write_hook`: Decision, Change Log, Workstream, Dispatch Log 갱신 확인
- `pre_close_hook`: 다음 실제 작업선을 `더글라스 레가스`, `베스 스크롤`, `이안 옵저버` 판단으로 고정

Conductor action:

- Heisenberg 제안에 따라 `리아나 실버레이크`를 `banking_power_hold`, `드라이덴 썬더루트`를 `great_druid_hold`로 직접 연결한다.
- Turing 제안에 따라 `바리온`을 `rune_forbidden_text_hold`로 직접 연결한다.
- 세 후보 모두 15 확정자가 아니라 `verify_before_15` 보류 후보로 유지한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `리아나 실버레이크`, `드라이덴 썬더루트`, `바리온` 판정 추가
- `FS_Canon_Change_Log.md`에 세 후보의 direct ruling backfill 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 대표 후보 판단으로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 남은 `verify_before_15` 대표 후보 중 `더글라스 레가스`, `베스 스크롤`, `이안 옵저버`의 직접 연결 필요 여부를 판단한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Verify-Before-15 Representative Direct Link Batch 06

목적:

- `더글라스 레가스`, `베스 스크롤`, `이안 옵저버`를 같은 배치로 점검하되, 직접 backfill 필요 여부가 갈릴 경우 선별 반영한다.
- 하네스 기준상 직접 잠글 가치가 있는 후보만 Register에 남긴다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Ether Verify Scout | `더글라스 레가스`의 직접 backfill 필요 여부 점검 | `completed` |
| `Turing` | Obelisk Verify Scout | `베스 스크롤`, `이안 옵저버`의 직접 backfill 필요 여부 점검 | `completed` |

Harness execution:

- `MCP gate`: `list_mcp_resources` / `list_mcp_resource_templates` 확인, 현재 배치에 직접 쓸 프로젝트형 MCP 자원 없음으로 `skip`
- `Skills gate`: 이 저장소에 직접 맞는 로컬 스킬 없음으로 `skip`
- `pre_scope_hook`: 대상 `더글라스 레가스`, `베스 스크롤`, `이안 옵저버`와 반영 장부 범위 고정
- `pre_dispatch_hook`: `더글라스`와 `베스/이안`으로 분리해 병렬 scout 배치
- `pre_write_hook`: `더글라스 레가스`는 현 단계 유지, `베스 스크롤`, `이안 옵저버`는 direct backfill 승인
- `post_write_hook`: Decision, Change Log, Workstream, Dispatch Log 갱신 확인
- `pre_close_hook`: 다음 실제 작업선을 `카트린 라베로스`, `레보니아 셰이드`, `세르반 알테르만` 판단으로 고정

Conductor action:

- Heisenberg 제안에 따라 `더글라스 레가스`는 현재 단계에서 direct backfill하지 않고 경계 후보 보존 상태를 유지한다.
- Turing 제안에 따라 `베스 스크롤`을 `archive_notable_hold`, `이안 옵저버`를 `watcher_notable_hold`로 직접 연결한다.
- `베스`, `이안`은 15 확정자가 아니라 `verify_before_15` 보류 후보로 유지한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `베스 스크롤`, `이안 옵저버` 판정 추가
- `FS_Canon_Change_Log.md`에 두 후보의 direct ruling backfill 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`에 `더글라스 레가스` 현 단계 유지와 다음 대표 후보 판단을 반영

Follow-up actions:

- 실제 원고 입력이 없으면 남은 `verify_before_15` 대표 후보 중 `카트린 라베로스`, `레보니아 셰이드`, `세르반 알테르만`의 직접 연결 필요 여부를 판단한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Verify-Before-15 Representative Direct Link Batch 07

목적:

- 오벨리스크 중층 후보 `카트린 라베로스`, `레보니아 셰이드`, `세르반 알테르만`을 직접 판정으로 잠글지 판단한다.
- import 근거와 synthesis 근거가 함께 있는 후보를 중앙 장부까지 끌어올린다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Obelisk Archive / Language Verify Scout | `카트린 라베로스`, `레보니아 셰이드`의 직접 backfill 필요 여부 점검 | `completed` |
| `Turing` | Obelisk Deathwatch Verify Scout | `세르반 알테르만`의 직접 backfill 필요 여부 점검 | `completed` |

Harness execution:

- `MCP gate`: `list_mcp_resources` / `list_mcp_resource_templates` 확인, 현재 배치에 직접 쓸 프로젝트형 MCP 자원 없음으로 `skip`
- `Skills gate`: 이 저장소에 직접 맞는 로컬 스킬 없음으로 `skip`
- `pre_scope_hook`: 대상 `카트린 라베로스`, `레보니아 셰이드`, `세르반 알테르만`과 반영 장부 범위 고정
- `pre_dispatch_hook`: `카트린/레보니아`와 `세르반`으로 분리해 병렬 scout 배치
- `pre_write_hook`: boundary, synthesis, register, import 근거를 대조해 세 후보 모두 direct backfill 승인
- `post_write_hook`: Decision, Change Log, Workstream, Dispatch Log 갱신 확인
- `pre_close_hook`: 다음 실제 작업선을 `우로스 디 모르간`, `레티시아 모르투스`, `더글라스 레가스 재판단`으로 고정

Conductor action:

- Heisenberg 제안에 따라 `카트린 라베로스`를 `archive_cipher_hold`, `레보니아 셰이드`를 `language_memory_hold`로 직접 연결한다.
- Turing 제안에 따라 `세르반 알테르만`을 `soul_archive_watch_hold`로 직접 연결한다.
- 세 후보 모두 15 확정자가 아니라 `verify_before_15` 보류 후보로 유지한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `카트린 라베로스`, `레보니아 셰이드`, `세르반 알테르만` 판정 추가
- `FS_Canon_Change_Log.md`에 세 후보의 direct ruling backfill 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 대표 후보 판단으로 이동

Follow-up actions:

- 실제 원고 입력이 없으면 남은 `verify_before_15` 대표 후보 중 `우로스 디 모르간`, `레티시아 모르투스`, `더글라스 레가스 재판단` 필요 여부를 판단한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Verify-Before-15 Representative Direct Link Batch 08

목적:

- `우로스 디 모르간`, `레티시아 모르투스`, `더글라스 레가스 재판단`을 한 배치로 검토하되, direct backfill과 비추천 유지를 분리해 판정한다.
- 오벨리스크 쪽은 import 근거까지 반영하고, 에테르 쪽은 `likely_keep_14` 우세 여부를 분명히 남긴다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Obelisk Deep Verify Scout | `우로스 디 모르간`, `레티시아 모르투스`의 직접 backfill 필요 여부 점검 | `completed` |
| `Turing` | Ether Reconsideration Scout | `더글라스 레가스` direct backfill 비추천 유지 여부 점검 | `completed` |

Harness execution:

- `MCP gate`: `list_mcp_resources` / `list_mcp_resource_templates` 확인, 현재 배치에 직접 쓸 프로젝트형 MCP 자원 없음으로 `skip`
- `Skills gate`: 이 저장소에 직접 맞는 로컬 스킬 없음으로 `skip`
- `pre_scope_hook`: 대상 `우로스 디 모르간`, `레티시아 모르투스`, `더글라스 레가스 재판단`과 반영 장부 범위 고정
- `pre_dispatch_hook`: `우로스/레티시아`와 `더글라스 재판단`으로 분리해 병렬 scout 배치
- `pre_write_hook`: `우로스`, `레티시아`는 direct backfill 승인, `더글라스 레가스`는 `likely_keep_14` 우세로 비추천 유지 확인
- `post_write_hook`: Decision, Change Log, Workstream, Dispatch Log 갱신 확인
- `pre_close_hook`: 다음 실제 작업선을 `잔여 오벨리스크 후보`와 `에테르 보류 후보 재점검` 우선순위 재정렬로 고정

Conductor action:

- Heisenberg 제안에 따라 `우로스 디 모르간`을 `archive_infiltration_hold`, `레티시아 모르투스`를 `necromantic_bestiary_hold`로 직접 연결한다.
- Turing 제안에 따라 `더글라스 레가스`는 direct backfill 비추천을 유지하고, 이유를 `likely_keep_14` 우세로 정리한다.
- `우로스`, `레티시아`는 15 확정자가 아니라 `verify_before_15` 보류 후보로 유지한다.

Integrated actions:

- `FS_Decision_Ruling_Register.md`에 `우로스 디 모르간`, `레티시아 모르투스` 판정 추가
- `FS_Canon_Change_Log.md`에 두 후보의 direct ruling backfill 기록 추가
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`에 `더글라스 레가스` 재판단 결과와 다음 우선순위 재정렬 단계 반영

Follow-up actions:

- 실제 원고 입력이 없으면 남은 `verify_before_15` 후보를 `잔여 오벨리스크 후보`와 `에테르 보류 후보 재점검`으로 다시 정렬한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

### 2026-04-09 KST - Residual Queue Priority Reorder Batch

목적:

- direct backfill 연속 배치 이후 남은 큐를 다시 정렬한다.
- 오벨리스크는 direct backfill 큐를 닫을지 판단하고, 에테르는 다음 실제 배치 대상을 고정한다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Obelisk Residual Queue Auditor | 오벨리스크 direct backfill 잔여 핵심 대상 존재 여부 점검 | `completed` |
| `Turing` | Ether Residual Queue Auditor | 에테르 보류 후보의 다음 실제 배치 묶음 추천 | `completed` |

Harness execution:

- `MCP gate`: `list_mcp_resources` / `list_mcp_resource_templates` 확인, 현재 배치에 직접 쓸 프로젝트형 MCP 자원 없음으로 `skip`
- `Skills gate`: 이 저장소에 직접 맞는 로컬 스킬 없음으로 `skip`
- `pre_scope_hook`: 대상 `잔여 오벨리스크 후보`, `에테르 보류 후보`와 반영 장부 범위 고정
- `pre_dispatch_hook`: 오벨리스크 잔여 큐 감사와 에테르 후속 배치 추천으로 역할 분리
- `pre_write_hook`: 오벨리스크 핵심 direct queue 종료 여부와 에테르 다음 배치 우선순위 잠금 승인
- `post_write_hook`: Workstream, Dispatch Log 갱신 확인
- `pre_close_hook`: 다음 실제 작업선을 `엘다라` 근거 보강 -> 에테르 `탑주 묶음` 1차 배치로 고정

Conductor action:

- Heisenberg 제안에 따라 오벨리스크 direct backfill 핵심 큐는 사실상 종료로 본다.
- Turing 제안에 따라 에테르는 `엘다라` 근거 보강을 먼저 두고, 그 다음 배치를 `엘드린 문브링어`, `네리사 블러드위버`, `다미엔 이클립스`로 자른다.
- `마르쿠스 레이븐펠`과 `이사도르 템페스트`는 이름 드리프트/분리 확인 비용이 있어 후속 배치로 넘긴다.

Integrated actions:

- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`에 오벨리스크 direct queue 종료와 에테르 후속 우선순위 반영
- `AGENT_DISPATCH_LOG.md`에 priority reorder batch 기록 추가

Follow-up actions:

- 실제 원고 입력이 없으면 `엘다라` 근거 보강을 먼저 수행한다.
- 그 다음 에테르 `탑주 묶음` 1차 배치 `엘드린 문브링어`, `네리사 블러드위버`, `다미엔 이클립스`를 점검한다.
- 실제 원고 입력이 들어오면 live handoff case로 전환

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
- FS Lore Engine과 상위 FS Engine의 Named Notables 라우팅 규칙에도 `14 신호 우선 검증`과 `대륙 -> 세력 / 도시 / 조직` 앵커 원칙을 연결했다.
- 다음 순차 진행표를 추가해 안정 15 후보 3명, 경계 보류 후보, 다음 FS 장부 연결 순서를 명시했다.
- 울프가르/에리온/오그마 안정 후보를 FS State Label, Relationship Ledger, Place Function Register에 연결하고 장소 기능 후보를 등록했다.
- Operational Lines 표면명 후보표에 `preferred display candidate` 패스를 추가해 현대적/직역감 있는 후보를 낮추고 판타지 톤 후보를 우선순위화했다.
- 세부 직능명에도 `Functional Preferred Candidate Pass`를 추가하고, `위조 장인의 우두머리`, `하수로 짐꾼` 같은 직역 라벨을 `거울인장 장인장`, `지하 회랑 운반꾼` 등으로 보정했다.
- 이름 톤 재점검에서 `거울인장 장인장`의 말맛이 뭉치는 문제를 확인하고, 우선 후보를 `가면 공방주` / `거울인장 공방주`로 보정했다.
- 크림슨 안정 15 후보 3명(`울프가르`, `에리온`, `오그마`)을 장소 기능과 지도 후보에 연결하는 `Section_15_Crimson_Place_Sidecar`를 추가했다.
- 크림슨 경계 후보 4명(`드락사르`, `카사르`, `벨라나`, `아리안`)의 추가 근거를 묶고, 벨라나/아리안 개별 시트와 앵커맵의 상태 라벨을 `verify_before_15`로 보정했다.
- 에테르 경계 후보 2차 근거를 보강하고, `마르쿠스/맥스웰/코르부스`, `메라 라일윈드/메라 실피드` 이름 드리프트를 충돌 장부와 명칭 정규화 맵에 추가했다.
- 해양 경계 후보 7명(`미다스`, `해양 실비아`, `이소벨`, `마르코`, `엘레오노라`, `골드핑거`, `리나`)의 2차 근거를 보강하고, 전원 15 확정 대신 `verify_before_15`로 유지했다.
- 오벨리스크 경계 후보 7명(`바리온`, `아이기스`, `카론`, `베스`, `이안`, `카트린`, `레보니아`)의 2차 근거를 보강하고, 인물 확정보다 장소-기관 슬롯 보강을 다음 작업으로 돌렸다.
- 오벨리스크 장소-기관 슬롯(`템플 오브 바운더리`, `경계의 보루`, `기억 경매장`, `영원의 기록탑`, `망각의 회랑`, `그림자 도서관`)을 Place Function Register와 Spatial Backlog에 연결했다.
- 대륙별 `15 Named Notables` 상태를 `Status Compass`로 압축하고, 다음 배치를 프로스트 역할 슬롯의 장소-기관 정리로 지정했다.
- 프로스트 역할 슬롯(`오로라 평원`, `얼음무덤 언덕`, `푸른 폭풍 요새`, `퍼마프로스트 요새`, `아이스포지 병기소`, `빙하의 성소`)을 Place Function Register와 Spatial Backlog에 연결했다.
- 해양 역할 슬롯(`오라클 바지`, `골든 앵커 하버`, `크로스윈드 포트`, `왕실 조선소`, `블랙워터 항구`, `붉은 해골 섬`, `볼트 오브 아우룸`, `Abyssal Vaults`, `폭풍의 만`, `고대의 악기실`, `유령선의 안식처`)을 Place Function Register와 Spatial Backlog에 연결했다.
- 해양 역할 슬롯의 작업용 라벨을 `신탁 방주`, `파도 신탁장`, `해로 장부관`, `왕실 선공장 수석장`, `흑조 감정관`, `심연 장부관`, `진혼 악기지기` 같은 display canon 후보로 낮췄다.
- 해양 장소-기관 슬롯 상태를 Status Compass, Coverage Matrix, Continent Synthesis에 반영해 다음 후보명 탐색 큐로 이어지게 했다.
- 해양 장소-기관 슬롯별 실제 후보명 탐색 큐를 추가하고, 첫 검색 대상을 `바다의 교단 / 오라클 바지 / 수석 오라클`로 지정했다.
- 해양 후보명 1차 검색을 수행해 수석 오라클은 개인명 미확인, 세일블레스 마리아는 14 경계 유지, 항해사 길드장/대경매장 주인/늙은 감정사는 역할 슬롯 유지, 크리스토퍼 델마르는 새 경계 후보로 분리했다.
- 크리스토퍼 델마르를 해양 `황금 함대 / 거상 연합` 앵커의 `verify_before_15` 후보로 경계 큐, Named Notables 등록부, 앵커맵에 반영했다.
- 해양 후보명 2차 검색에서 크리스토퍼 델마르는 거상 연합 개요에만 직접 확인되고, 대경매장 주인과 항해사 길드장은 개인명 없는 역할 슬롯으로 유지한다고 정리했다.
- 포트 아우렐리온과 크로스윈드 포트의 unnamed role slot을 좁혀, 해양 15 Named Notables 후보명 검색 대상을 도시 기능별로 재정렬했다.
- 해양 unnamed role slot 3차 검색 결과, 마스터 쉽라이트/수석 기상관/항해사 길드장/스톰 체이서 대장/수석 무역왕/대경매장 주인/은행장/세관장은 모두 개인명 없이 역할 슬롯으로 유지한다고 정리했다.
- 에테르 장소-기관 슬롯을 `Section_15_Ether_Place_Institution_Sidecar`로 분리하고, 금서 도서관/마나 공방/아스트랄 관측소/아스트라르 중앙 도서관/루멘 성채/브룬발트 대성채/포트 넥서스/잠든 정령의 숲/루미라를 Place Function Register와 Spatial Backlog에 연결했다.
- 에테르 장소-기관 슬롯의 표면명 후보를 `봉인서고지기`, `금서 검인관`, `성좌 관측장`, `대서고 학장`, `성채 봉인관`, `서약의회 기록관`, `그늘항로 기록관`, `정령서약 해석자` 계열로 보정하고, 말맛이 뭉치는 후보는 `Needs Polish`로 분리했다.
- 에테르 `Needs Polish` 후보를 `비전로 장인장`, `성검 병장관`, `옵시디안 무기지기`, `대서고 수호장`, `정령묘 이름새김꾼`으로 보정하고, 실제 후보명 탐색 큐를 추가했다.
- 에테르 큐 1번 검색에서 금서 도서관/마법 서고단은 장소-기관 슬롯으로 확인했고, 대런 크레센트는 A+ 부탑주/행정총무/서고단 관장 신호가 강해 `verify_before_15`를 유지했다.
- 에테르 큐 2번 검색에서 마나 공방은 제작/아이템/공방 슬롯으로 확인했고, 에드가 룬워커는 A급/Act 신호 때문에 `verify_before_15`, 대장로/무기 상인/비전 제작관은 `need_named_candidate`로 유지했다.
- 에테르 큐 3번 검색에서 아스트랄 관측소와 별의 예언자단은 예언/관측 슬롯으로 확인했고, 칼리스트는 A+/Act/대예언자 신호 때문에 `verify_before_15`, 수석 점성가/관측관/점성술사/망원경 관리자/미친 예언가는 `need_named_candidate`로 유지했다.
- 에테르 큐 4번 검색에서 아스트라르 중앙 도서관은 성국 학술/금서 장소-기관 슬롯으로 확인했고, 래퍼티 아르카디아는 A급/Act/도서관장 신호 때문에 `verify_before_15`, 라파엘 아르카디아는 이름 드리프트 또는 별도 인물 확인 대상으로 분리했다.
- 대서고 학장/대서고 수호장은 별도 개인명 없이 `need_named_candidate`로 유지했고, 다음 검색은 루멘 성채/대사제 요한 축으로 넘겼다.
- 에테르 큐 5번 검색에서 루멘 성채는 성국 방어/순교/신성 결계 장소-기관 슬롯으로 확인했고, 대사제 요한은 성채 총괄/결계 공명 신호 때문에 `verify_before_15`를 유지했다.
- 발레리우스/헬렌은 루멘 성채 로컬 이름 슬롯으로만 보존하고, 성채 봉인관/순교묘역 사제장은 개인명 없는 `need_named_candidate`로 유지했다.
- 에테르 큐 6번 검색에서 옵시디안/성검의 요새는 성국 감옥/무기 제작/기사단 훈련 장소-기관 슬롯으로 확인했고, 알렉산드로 발렌티안은 `keep_14`, 실라스 블랙쏜은 `keep_14_likely`, 무기 장인/성검 병장관/옵시디안 무기지기는 `need_named_candidate`로 유지했다.
- 에테르 큐 7번 검색에서 레갈리아/아덴브루크는 왕국연합 의회/상업 장소-기관 슬롯으로 확인했고, 레온하르트/제라르드는 14 유지, 리아나는 `verify_before_15`, 의회 서기장/서약의회 기록관/전비 장부관은 `need_named_candidate`로 유지했다.
- 에테르 큐 8번 검색에서 포트 넥서스/머시너리 게이트/황금 맹약의 신전은 자유도시 항만/용병/계약 장소-기관 슬롯으로 확인했고, 드레이크는 14 유지, 셀레나 와일드웨이브와 레온 벨가르드는 `verify_before_15`, 조선소장/교관/대집행관/그늘항로 기록관/서약문 보관관은 `need_named_candidate`로 유지했다.
- 에테르 큐 9번 검색에서 루미라와 잠든 정령의 숲은 정령연합의 언어/전승/정령묘 장소-기관 슬롯으로 확인했고, 엘다라는 15 후보 유지, 실바리온은 14 유지, 엘라라/드라이덴/메라/실라스 나이트쉐이드는 `verify_before_15`로 유지했다.
- 에테르 큐 1-9번 결과를 `Section_15_Ether_Search_Synthesis`로 압축하고, 안정 15 후보는 엘다라 1명, 나머지는 14 유지/검증/이름 충돌/역할 슬롯으로 분리했다.
- 에테르 `need_named_candidate` 슬롯을 장소-기관 앵커별 색인으로 묶어, 새 이름을 만들지 않고도 후속 회수 위치를 추적할 수 있게 했다.
- Status Compass에 에테르 큐 1-9 종료 상태를 반영하고, 다음 배치는 에테르 추가 탐색이 아니라 다른 대륙 압축으로 넘기기로 했다.
- 프로스트는 안정 15 후보 없이 `verify_before_15` 후보와 장소-기관 슬롯이 중심인 대륙으로 압축했고, 이름 없는 슬롯 색인을 따로 만들었다.
- 해양은 안정 15 후보 없이 이름 있는 후보 전원을 `verify_before_15`로 유지하고, 포트 아우렐리온/크로스윈드 포트/오라클 바지 중심의 이름 없는 슬롯 색인을 따로 만들었다.
- 오벨리스크는 안정 15 후보 없이 기록/봉인/기억/망각/영혼 슬롯 중심으로 압축했고, 초월 서사로 과열되지 않도록 장소-기관 기능으로 먼저 낮춰 읽었다.
- 5대륙 `15 Named Notables` 1차 압축 종료표를 작성해 안정 후보, 경계 후보, 이름 없는 역할 슬롯을 한 문서로 묶었다.
- `8번 세력 아카이브`의 대륙별 spine과 `15 Named Notables` 후보/역할 슬롯을 연결하는 브리지를 작성했다.
- 실제 파일 이동 전, 15번 후보를 대륙/세력/도시/조직 기준으로 배치하는 가상 라우팅 계획을 작성했다.
- `15-A Named Notables / 15-B Operational Lines / 15-C Need Named Candidate Slots` 가상 폴더 구조 초안을 문서로 작성했다.
- 폴더 구조 초안에 Revision Gate를 적용해, 설계 문서로는 사용 가능하지만 실제 파일 이동은 아직 금지한다고 판정했다.
- 15번 열람용 인덱스 초안을 작성해 Named Notables, Operational Lines, Need Named Candidate Slots, 경계 후보, 이름 충돌 감시 순서를 정리했다.
- 8번 spine과 15번 가상 폴더 구조의 호환성을 감사하고, 실제 이동은 아직 보류하되 설계 문서로는 사용 가능하다고 판정했다.
- 안정 15 후보 5명을 8번 세력/도시/조직 앵커와 다시 연결하는 색인을 작성했다.
- 안정 15 후보 시트 QA를 진행하고, 키르케 `실비아` 시트에 범대륙 후기 확장 라우팅과 이름 충돌 주의사항을 보강했다.
- 범대륙/후기 확장 구역을 보존하되 메인 5대륙 spine보다 후순위로 두는 guard 문서를 작성했다.
- 범대륙 루트의 display canon / deferred expansion 판정표를 작성해 현대 조직명 후보를 후속 검토 대상으로 분리했다.
- 15-B Operational Lines의 표면명 후보를 범대륙 guard와 대조해, 현재 후보는 대체로 사용 가능하다고 판정했다.
- 15번 열람용 인덱스 초안에 Operational Display Guard 결과를 반영했다.
- 15번 1차 사이클 이후, 8번 세력 아카이브의 다음 감사 타깃을 크림슨 안정 후보 앵커로 정했다.
- 크림슨 8번 앵커를 재점검한 결과 울프가르/에리온은 A급/전설 영웅록 신호가 있어 `grade_caution`으로 낮추고, 오그마는 현재 가장 안정적인 명사형 후보로 유지했다.
- `Wolfgar / Erion` 충돌군을 이름 충돌 레지스터와 명칭 정규화 맵에 추가해, 크림슨 후보를 다른 대륙 이름군과 병합하지 않도록 가드를 세웠다.
- 프로스트는 안정 15 후보를 늘리기보다 `오로라 평원 / 얼음무덤 언덕 / 푸른 폭풍 요새 / 아이스포지 병기소 / 빙하의 성소 / 겨울회의 의장막` 슬롯을 8번 spine 기준으로 다시 묶는 편이 안전하다고 판정했다.
- 프로스트 슬롯의 작업용 라벨을 `서리길 원로 사냥꾼 / 빙묘 수호장 / 오로라 예언장 / 빙철 공방장 / 오로라 별술사 / 서리벼림 장인` 축으로 1차 보정해, 다음 배치에서 Place Function Register와 직접 연결할 준비를 마쳤다.
- FS 엔진 재점검 결과, 새 이론보다 `판정 기억`, `다른 크로니클 누수 방지`, `이름 없는 슬롯의 성장 추적`이 더 시급하다고 판단해 `Decision Ruling`, `Cross-Chronicle Firewall`, `Slot Maturation` 장부를 추가했다.

### 2026-04-08 KST - Orchestra Lock / Frost Core Link Batch

목적:

- 오케스트라 방식의 운영 이점을 문서로 고정한다.
- 프로스트 슬롯을 Place / Decision / Slot Maturation 코어에 직접 연결한다.
- 최근 상태 이동을 Canon Change Log로 남길 기반을 만든다.

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Carson` | Orchestra Operations Auditor | `ACTIVE_AGENT_SPLIT`, `RUNBOOK`, `ORCHESTRA_ADVANTAGE_LOCK`, `AGENT_DISPATCH_LOG` 정합성 점검 | `dispatched` |
| `Peirce` | Frost Core Link Auditor | 프로스트 슬롯의 Place / Decision / Slot Maturation 연결안 점검 | `dispatched` |

Conductor action:

- 실제 문서 반영은 Conductor가 단독으로 수행한다.
- 에이전트 결과는 read-only 진단으로만 사용하고, 충돌 제안은 후속 큐로 분리한다.

### 2026-04-09 KST - Ether Eldara Evidence Reinforcement Batch

목적:

- 에테르의 가장 안정적인 15 후보 `엘다라`의 근거를 `루미라` 장소 문서 기준으로 더 단단히 잠근다.
- 이번 배치를 `15 확정`이 아니라 `named_notable_candidate / verify_source_before_profile` 보강으로 한정한다.
- 다음 실제 작업선을 에테르 `탑주 묶음` 1차 배치로 넘긴다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 확인되어 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Heisenberg`, `Turing` read-only scout 배치
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Eldara Evidence Scout | `Section_15_Named_Notable_Eldara`, `Section_15_Ether_Search_Synthesis`, `Section_15_Ether_Place_Institution_Sidecar`, `루미라` import 근거 보강 포인트 추출 | `completed` |
| `Turing` | Eldara Sync Scout | `Next_Sequential_Workstream`, `Continuous_Workstream`, `AGENT_DISPATCH_LOG` 포함 동기화 포인트와 과한 확정 위험 점검 | `completed` |

Conductor action:

- `Heisenberg` 제안에 따라 `루미라`의 학술 도시성, `현자 의회`, `고대수 도서관`, `초대 정령왕의 계약서 사본` 축을 `엘다라` 시트에 직접 반영한다.
- `엘라라 문힘`, `드라이덴`, `정령서약 해석자 / 정령묘 이름새김꾼`은 분리 규칙으로 더 선명하게 잠근다.
- `Turing` 제안에 따라 이번 턴은 `Section_15_Ether_Place_Institution_Sidecar.md`를 건드리지 않고, `Eldara -> Search Synthesis -> Workstream -> Dispatch Log`만 동기화한다.
- `pre_write_hook`에서 `15 확정` 문구를 금지하고 `verify_source_before_profile` 상태 유지로 잠근다.

Integrated actions:

- `audit/Section_15_Named_Notable_Eldara.md`에 `루미라 / 현자 의회 / 고대수 도서관 / 계약서 사본` 근거와 separation guard를 추가
- `audit/Section_15_Ether_Search_Synthesis.md`의 `Stable 15 Candidate`와 `Next Action`을 이번 배치 완료 기준으로 갱신
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`를 `엘다라 보강 완료 -> 에테르 탑주 묶음 1차 배치` 순서로 갱신

Follow-up actions:

- 다음 실제 배치는 에테르 `탑주 묶음` 1차 `엘드린 문브링어`, `네리사 블러드위버`, `다미엔 이클립스` 점검
- 이후 `마르쿠스 레이븐펠`, `이사도르 템페스트`는 이름 드리프트/분리 확인을 붙여 후속 배치로 이동

### 2026-04-09 KST - Ether Tower Bundle Direct Ruling Batch

목적:

- 에테르 `탑주 묶음` 1차 `엘드린 문브링어`, `네리사 블러드위버`, `다미엔 이클립스`를 중앙 장부에 direct ruling으로 연결한다.
- 이번 배치도 `15 확정`이 아니라 `verify_before_15` 보류 잠금으로 한정한다.
- 다음 실제 작업선을 `마르쿠스 레이븐펠 / 이사도르 템페스트` 분리 검토로 넘긴다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 확인되어 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Heisenberg`, `Turing` read-only scout 배치
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Ether Tower Bundle Ruling Scout | `엘드린 문브링어`, `네리사 블러드위버`, `다미엔 이클립스`의 direct ruling 필요 여부와 short label 점검 | `completed` |
| `Turing` | Ether Tower Bundle Sync Scout | `Decision Ruling`, `Canon Change`, `Workstream`, `Dispatch Log` 동기화 범위와 과한 확정 위험 점검 | `completed` |

Conductor action:

- `Heisenberg` 제안에 따라 `엘드린 문브링어`, `네리사 블러드위버`, `다미엔 이클립스`를 모두 direct ruling 대상으로 승인한다.
- `white_tower_barrier_hold`, `abyss_blood_taboo_hold`, `shadow_intelligence_hold` 라벨을 각각 부여한다.
- `Turing` 제안에 따라 이번 턴은 `15 확정` 문구를 피하고, `Search Synthesis`는 `verify_before_15` 표와 `Next Action`만 최소 동기화한다.
- `pre_close_hook`에서 다음 실제 배치를 `마르쿠스 레이븐펠 / 이사도르 템페스트` 분리 검토로 고정한다.

Integrated actions:

- `audit/FS_Decision_Ruling_Register.md`에 세 후보의 direct ruling 추가
- `audit/FS_Canon_Change_Log.md`에 세 후보의 backfill 기록 추가
- `audit/Section_15_Ether_Search_Synthesis.md`에 세 후보를 `verify_before_15` 표로 연결하고 다음 작업선을 전진
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`를 `마르쿠스 레이븐펠 / 이사도르 템페스트` 후속 검토로 갱신

Follow-up actions:

- 다음 실제 배치는 `마르쿠스 레이븐펠`, `이사도르 템페스트`를 이름 드리프트 / 분리 확인 전제로 재검토
- 필요 시 레이븐펠 / 템페스트 축의 `keep_14`, `verify_before_15`, `name_drift` 판정을 재정렬

### 2026-04-09 KST - Ether Arcane Drift Refinement Batch

목적:

- `Ravenfell / Corvus`와 `이사도르 템페스트 / 이사도르 솔레아`를 이름 드리프트 / 분리 판정으로 더 선명하게 잠근다.
- 이번 배치도 `15 확정`이 아니라 `verify_before_15`, `name_drift`, `separate_entity` 정밀화로 한정한다.
- 다음 실제 작업선을 에테르 arcane drift 후속 동기화로 넘긴다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 확인되어 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Heisenberg`, `Turing` read-only scout 배치
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Heisenberg` | Ravenfell / Corvus Drift Scout | `마르쿠스 레이븐펠`, `맥스웰 레이븐펠`, `마르쿠스 코르부스`의 주앵커와 분리 판정 점검 | `completed` |
| `Turing` | Tempest / Solea Split Scout | `이사도르 템페스트`, `이사도르 솔레아`의 분리 판정과 문서 동기화 범위 점검 | `completed` |

Conductor action:

- `Heisenberg` 제안에 따라 `맥스웰 레이븐펠`을 phase3 흑색 탑 주앵커로 읽고, `마르쿠스 레이븐펠`은 drift 표기로만 보존한다.
- `마르쿠스 코르부스`는 phase2 직접 14 영웅 파일 기준 별도 개체로 더 선명하게 잠근다.
- `Turing` 제안에 따라 `이사도르 템페스트`와 `이사도르 솔레아`를 병합 금지하고, `템페스트`는 청색 탑 / 템페스트 가문 축의 `verify_before_15`로 유지한다.
- `pre_write_hook`에서 `템페스트 = 15 확정` 또는 `마르쿠스 레이븐펠 = 정본명 확정` 문구를 금지한다.

Integrated actions:

- `audit/FS_Decision_Ruling_Register.md`에 arcane drift refinement 판정 추가
- `audit/FS_Canon_Change_Log.md`에 `Ravenfell / Corvus`, `이사도르 템페스트 / 이사도르 솔레아` refinement 기록 추가
- `audit/Section_15_Named_Notables_Name_Collision_Register.md`에 `Isador Tempest / Isadore Solea Split` 섹션 추가 및 `Ravenfell` 판정 보강
- `audit/Section_15_Named_Notables_Register.md`, `audit/Section_15_Named_Notables_Status_Compass.md`를 최신 분리 기준으로 동기화
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`를 arcane drift 후속 동기화 기준으로 갱신

Follow-up actions:

- 다음 실제 배치는 에테르 `Named Notables Register / Status Compass`의 arcane drift 후속 동기화
- 필요 시 `맥스웰 레이븐펠`, `이사도르 템페스트` 기준 anchor 문구를 에테르 종합표와 경계 큐에 재정렬

### 2026-04-09 KST - Ether Arcane Drift Sync Batch

목적:

- 이미 잠근 `Ravenfell / Corvus`, `이사도르 템페스트 / 이사도르 솔레아` 판정을 에테르 종합표와 경계 큐 문구까지 동기화한다.
- 새 판정을 만들지 않고 `맥스웰 레이븐펠` 주앵커, `마르쿠스 레이븐펠` drift 보존, `마르쿠스 코르부스` 분리, `이사도르 템페스트 / 이사도르 솔레아` 병합 금지를 문서 전반에 같은 표현으로 맞춘다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 보여 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Lagrange`, `Fermat` read-only scout 배치
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Lagrange` | Ravenfell / Corvus Wording Sync Scout | `Ether Search Synthesis`, `Boundary Verification Queue`, `Boundary Evidence`, `Coverage Matrix`의 Marcus-only drift wording 점검 | `completed` |
| `Fermat` | Tempest / Solea Split Sync Scout | `Ether Search Synthesis`, `Boundary Verification Queue`, `Boundary Evidence`, `Continent Synthesis`의 Isador split wording 점검 | `timed_out -> conductor local evidence fallback` |

Conductor action:

- `pre_write_hook`에서 새 15 확정자 추가 없이 wording sync만 허용한다.
- `맥스웰 레이븐펠`을 phase3 흑색의 탑 주앵커로, `마르쿠스 레이븐펠`을 drift 표기로, `마르쿠스 코르부스`를 phase2 14 별도 개체로 문구 고정한다.
- `이사도르 템페스트`는 청색의 탑 / 템페스트 가문 축으로, `이사도르 솔레아`는 phase2 14 영웅 축으로 분리 고정한다.
- `Lagrange`의 read-only 제안을 반영하고, `Fermat` 범위는 timeout 이후 로컬 증거 재확인으로 마감한다.
- 두 scout 모두 write 권한 없이 문구 정렬 범위만 허용하고, 최종 write는 Conductor가 단일 책임으로 처리한다.

Integrated actions:

- `audit/Section_15_Ether_Search_Synthesis.md`의 `Name Drift / Collision Watch`, `Next Action` 동기화
- `audit/Section_14_15_Boundary_Verification_Queue.md`, `audit/Section_14_15_Ether_Boundary_Evidence.md`의 Marcus / Isador 경계 문구 동기화
- `audit/Section_15_Named_Notables_Continent_Synthesis.md`, `audit/Section_15_Named_Notables_Coverage_Matrix.md`의 에테르 요약 문구 동기화
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`를 다음 장소-기관 슬롯 표면명 정리 작업선으로 이동

Follow-up actions:

- 다음 실제 배치는 에테르 장소-기관 슬롯의 표면명 후보 정리
- 실제 원고 입력이 생기면 handoff seed가 아니라 live handoff case로 승격

### 2026-04-09 KST - Ether Surface-Name Lock Batch

목적:

- 에테르 place-institution sidecar와 operational display 표에서 이미 해결된 표면명 후보를 본표 기준으로 잠근다.
- old working label이 다시 표면명처럼 읽히지 않게 하고, 다음 작업선을 low-priority anchor wording closure pass로 넘긴다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 보여 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Mendel`, `Confucius` read-only scout 배치
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Mendel` | Ether Slot Consistency Scout | `Sidecar`, `Need Named Candidate Index`, `Search Queue`, `Slot Maturation`의 slot/display sync 점검 | `completed` |
| `Confucius` | Ether Tone Risk Scout | `Sidecar`, `Operational Display`, `Guard Audit`, `Continent Synthesis`의 naming-tone risk 점검 | `timed_out -> conductor local evidence fallback` |

Conductor action:

- `pre_write_hook`에서 새 인물 확정이나 새 실명 발명을 금지하고, 이미 `preferred_display_candidate`로 잠긴 표면명만 본표에 접어 넣는다.
- `Section_15_Ether_Place_Institution_Sidecar.md`의 place/institution slot과 display candidate pass를 최신 표면명 기준으로 갱신한다.
- `Section_15_Operational_Display_Canon_Candidates.md`의 Ether 후보표도 같은 기준으로 맞추고, `Ether Needs Polish`를 해결 완료 표로 전환한다.
- `FS_Slot_Maturation_Register.md`에는 Ether 대표 슬롯이 최신 `preferred_display_candidate`를 따른다는 메모만 최소 추가한다.
- `Mendel`의 read-only 제안을 반영하고, `Confucius` 범위는 timeout 이후 로컬 증거 재확인으로 마감한다.

Integrated actions:

- `audit/Section_15_Ether_Place_Institution_Sidecar.md`에서 resolved slot에 `slot_with_display_candidate` 상태를 병기하고 candidate slot을 최신 표면명으로 갱신
- `audit/Section_15_Operational_Display_Canon_Candidates.md`의 Ether 표면명 후보와 polish 섹션을 최신 해결분 기준으로 정렬
- `audit/Section_15_Ether_Need_Named_Candidate_Index.md`, `audit/Section_15_Ether_Named_Candidate_Search_Queue.md`를 low-priority auxiliary slot까지 확장
- `audit/FS_Slot_Maturation_Register.md`에 Ether 대표 슬롯의 name layer 기준과 display candidate row를 확장
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`를 다음 low-priority closure pass 기준으로 이동

Follow-up actions:

- 다음 실제 배치는 에테르 place-institution 축의 low-priority anchor wording closure pass
- 실제 원고 입력이 생기면 handoff seed가 아니라 live handoff case로 승격

### 2026-04-09 KST - Ether Low-Priority Closure Pass Batch

목적:

- summary-layer 문서가 아직 `표면명 후보 보정` 단계에 머물러 있는 표현을 지우고, 이미 잠긴 surface-name baseline과 low-priority auxiliary slot 확인 단계로 맞춘다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 보여 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: carry-forward scout findings + conductor local evidence
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

Conductor action:

- `pre_write_hook`에서 새 후보명이나 새 실명 발명을 금지한다.
- `Continent Synthesis`, `Coverage Matrix`의 요약 문구를 `surface-name baseline locked + low-priority auxiliary slot confirmation` 기준으로 닫는다.
- `pre_close_hook`에서 다음 실제 배치를 `Section_15_Index_Draft`류 압축표 반영으로 넘긴다.

Integrated actions:

- `audit/Section_15_Named_Notables_Continent_Synthesis.md`의 `Next Priority`, `Compressed Status` 문구 정리
- `audit/Section_15_Named_Notables_Coverage_Matrix.md`의 Ether reading / next priority 문구 정리
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`를 다음 `Index Draft` 반영 작업선으로 이동

Follow-up actions:

- 다음 실제 배치는 `Section_15_Index_Draft`류 압축표에 Ether surface-name lock 반영
- 실제 원고 입력이 생기면 handoff seed가 아니라 live handoff case로 승격

### 2026-04-09 KST - Ether Compressed Summary Reflection Batch

목적:

- 이미 잠긴 Ether surface-name baseline을 `Index Draft`, `Status Compass` 같은 압축표 문서에 반영한다.
- 다음 실제 작업선을 `low-priority auxiliary slot` 개인명 실존 여부 확인 배치로 넘긴다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 보여 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Gibbs`, `Averroes`, `Plato`, `Helmholtz` read-only scout 배치
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Gibbs` | Open Index Necessity Scout | `OPEN_INDEX` 수정 필요 여부 판단 | `completed -> no change needed` |
| `Averroes` | Summary Consistency Scout | `Index Draft`, `Status Compass`의 최소 수정 문구 제안 | `completed` |
| `Plato` | Index Draft Reflection Scout | `Section_15_Index_Draft.md`의 Ether 압축 반영 검토 | `completed -> no additional blocker surfaced` |
| `Helmholtz` | Status Compass Sync Scout | `Status Compass`, `Next/Continuous` 동기화 검토 | `errored -> usage limit, conductor local evidence fallback` |

Conductor action:

- `pre_write_hook`에서 새 후보명과 새 실명 발명을 금지한다.
- `Section_15_Index_Draft.md`에 Ether surface-name baseline lock과 low-priority auxiliary slot 대기 목록을 압축 메모로 보강한다.
- `Section_15_Named_Notables_Status_Compass.md`의 Ether row와 `Next Orchestrated Move`를 최신 작업선으로 갱신한다.
- `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`를 다음 read-only 확인 배치 기준으로 이동한다.

Integrated actions:

- `audit/Section_15_Index_Draft.md`에 Ether surface-name lock 압축 메모와 새 `Conductor Decision` 반영
- `audit/Section_15_Named_Notables_Status_Compass.md`의 Ether row / `Next Orchestrated Move` 갱신
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`를 low-priority auxiliary slot read-only 확인 작업선으로 이동

Follow-up actions:

- 다음 실제 배치는 `탑서기`, `왕실 의전서기`, `성벽 설계서기`, `상단 조율관`, `항만 인장관`, `탐사 기록관`, `연구소 보존관`, `대현자 보좌 기록관`, `침묵의 감시자`의 개인명 실존 여부 read-only 확인
- 실제 원고 입력이 생기면 handoff seed가 아니라 live handoff case로 승격

### 2026-04-09 KST - Species Framework Side-Track Opening Batch

목적:

- 메인 `14/15` workstream을 건드리지 않고, 종족 관련 공백을 병렬 감사 트랙으로 분리한다.
- `종족 / 혈통 / 상태 / 몬스터`의 기본 분류축과 위험 구간을 먼저 잠근다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 보여 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Euclid`, `Leibniz`, `Goodall`, `Ptolemy`, `Dalton` read-only scout 배치
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Euclid` | Species Intake Framework Scout | 상위 종족 분류 프레임 제안 | `timed_out -> conductor local evidence fallback` |
| `Leibniz` | Evidence and Risk Scout | 인외/혈통/변이 단서와 조기 확정 위험 점검 | `timed_out -> conductor local evidence fallback` |
| `Goodall` | Side-Track Structure Scout | 병렬 문서 구조 제안 | `timed_out -> conductor local evidence fallback` |
| `Ptolemy` | Minimal Classification Scout | `race / bloodline / state / monster` 최소 분류 검토 | `timed_out -> conductor local evidence fallback` |
| `Dalton` | Parallel Document Setup Scout | 메인선 분리 운영 구조 검토 | `timed_out -> conductor local evidence fallback` |

Conductor action:

- `pre_write_hook`에서 메인 캐논과 `14/15` workstream을 건드리지 않는다는 원칙을 먼저 잠근다.
- `Species_Framework_Audit_Sidecar.md`를 만들어 판타지 종족 수용용 상위 그릇과 `race / bloodline / state / monster` 분류축을 정리한다.
- `Species_Framework_Risk_Register.md`를 만들어 `언데드`, `정령화`, `혼혈`, `하피`, `라미아`, `해양 종`의 성급한 종족 승격을 금지선으로 기록한다.
- `OPEN_INDEX.md`, `Next_Sequential_Workstream.md`, `Continuous_Workstream.md`에는 이 작업을 `parallel side-track`으로만 연결한다.

Integrated actions:

- `audit/Species_Framework_Audit_Sidecar.md` 작성
- `audit/Species_Framework_Risk_Register.md` 작성
- `audit/OPEN_INDEX.md`에 `Species Side Track` 섹션 추가
- `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`에 병렬 트랙 연결

Follow-up actions:

- 메인선은 예정대로 Ether low-priority auxiliary slot read-only 확인을 유지
- 사이드트랙은 `하이엘프`, `드워프 장인`, `수인 부족`, `언데드`, `정령화` 1차 anchor case 정리로 이어감

### 2026-04-09 KST - Species Side-Track Evidence Hardening Batch

목적:

- 늦게 도착한 종족 전문가 scout 결과를 side-track 문서에 흡수한다.
- `용어 교차표`, `1차 판정 메모`, `layered intake card`까지 분리해 둔다.

하네스:

- `MCP gate`: `notion` 문서형 리소스만 보여 이번 배치에는 `skip`
- `Skills gate`: 현재 저장소 작업에 직접 맞는 로컬 스킬 부재로 `skip`
- `Agents`: `Euclid`, `Leibniz`, `Goodall`, `Ptolemy`, `Dalton` late-arrival read-only scout 결과 반영
- `Hooks`: `pre_scope_hook -> pre_dispatch_hook -> pre_write_hook -> post_write_hook -> pre_close_hook`

배치:

| Agent | Role | Scope | Status |
|---|---|---|---|
| `Euclid` | Species Intake Framework Scout | layered intake card와 분류축 제안 | `completed` |
| `Leibniz` | Evidence and Risk Scout | 수인, 용혈, 언데드, 해양, 하피 근거 수집 | `completed` |
| `Goodall` | Side-Track Structure Scout | sidecar 패턴과 mainline 분리 원칙 제안 | `completed` |
| `Ptolemy` | Minimal Classification Scout | `race / bloodline / state / monster` 최소 규칙 제안 | `completed` |
| `Dalton` | Parallel Document Setup Scout | crosswalk / first pass 중심의 문서 구조 제안 | `completed` |

Conductor action:

- 기존 `Species_Framework_Audit_Sidecar.md`를 layered intake card와 1차 anchor reading까지 확장한다.
- `Race_Species_Term_Crosswalk.md`를 만들어 `하이엘프`, `드워프 장인`, `수인 부족`, `Dragonborn`, `언데드`, `정령화`, `Merfolk`, `Siren Harpy` 등을 층위별로 분리한다.
- `Race_Species_First_Pass.md`를 만들어 strong / medium / thin 신호를 압축 요약한다.
- 메인 `14/15` 선은 그대로 유지하고, 사이드트랙 문서만 확장한다.

Integrated actions:

- `audit/Species_Framework_Audit_Sidecar.md`에 `Layered Intake Card`, `First Anchor Readings` 추가
- `working/crosswalks/Race_Species_Term_Crosswalk.md` 작성
- `audit/Race_Species_First_Pass.md` 작성
- `audit/OPEN_INDEX.md`, `audit/Next_Sequential_Workstream.md`, `audit/Continuous_Workstream.md`에 사이드트랙 문서 추가 연결

Follow-up actions:

- 메인선은 그대로 Ether low-priority auxiliary slot read-only 확인 유지
- 사이드트랙은 `해양 merfolk`, `하피`, `라미아`, `거인`, `요정`의 peoplehood 근거를 read-only로 더 점검

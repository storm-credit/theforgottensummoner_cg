# Setting Book Document Roles Map

## Purpose

이 문서는 설정집 관련 파일이 많아졌을 때
각 문서가 무슨 역할을 맡는지 빠르게 구분하기 위한 역할 지도다.

가장 중요한 기준은 아래 네 가지다.

1. 지금 바로 읽히는 공유용 preview인가
2. 전체 구조를 압축 확인하는 reference인가
3. 검증과 보류 판단을 위한 appendix인가
4. 오케스트라가 진행을 관리하는 conductor 문서인가

## Quick Role Table

| File | Primary Role | When To Open |
| --- | --- | --- |
| `Setting_Book_Preview_Readable_v0.md` | 현재 공유용 readable preview | 누군가에게 먼저 보여 줄 때 |
| `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | 본문+부록을 한 파일에 압축한 reference | 전체 구조를 한 번에 점검할 때 |
| `Setting_Book_Public_Assembly_Manuscript_Draft.md` | reader-facing body source manuscript | preview 본문이 어디서 조립됐는지 볼 때 |
| `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` | technical appendix source manuscript | 검증 근거와 unresolved risk를 확인할 때 |
| `Setting_Book_Front_Matter_Draft.md` | 표지 톤, subtitle, opening promise source | 설정집 첫인상과 약속 문구를 맞출 때 |
| `Setting_Book_Faction_Core_Profiles_v0.md` | faction bridge sheet | readable preview와 기술 초안 사이를 메울 때 |
| `Setting_Book_People_Core_Profiles_v0.md` | people bridge sheet | 인물 축만 더 조밀하게 볼 때 |
| `Setting_Book_Places_Core_Profiles_v0.md` | places bridge sheet | 장소 축만 더 조밀하게 볼 때 |
| `Setting_Book_Items_Core_Profiles_v0.md` | items bridge sheet | 유물/아이템 축을 빠르게 점검할 때 |
| `Setting_Book_Species_Core_Profiles_v0.md` | species bridge sheet | 종족 분류 축을 빠르게 점검할 때 |
| `Setting_Book_Release_Readiness_Checklist.md` | release gate 판단표 | 지금을 v1 또는 RC로 불러도 되는지 점검할 때 |
| `Setting_Book_Preview_Package_v0.md` | shareable preview package order guide | 어떤 파일을 어떤 순서로 공유할지 고를 때 |
| `Setting_Book_Assembly_Index.md` | 전체 조립 현황판 | next queue와 main push gate를 볼 때 |
| `Setting_Book_Thread_Checkpoint.md` | 대화창 handoff 기록 | 새 컨텍스트에서 이어받을 때 |

## Reader vs Reference vs Conductor

### 1. Reader-facing

- `Setting_Book_Preview_Readable_v0.md`

이 파일이 현재 가장 먼저 읽히는 공유용 preview다.
지금 단계에서 “설정집이 어떤 책처럼 읽히는가”를 가장 잘 보여 준다.

### 2. Compressed Reference

- `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`

이 파일은 release candidate가 아니다.
본문과 부록을 한 파일에서 같이 보며 동기화 확인을 하는 압축 reference다.
파일명 `Prototype_v0`도 그 역할을 유지하기 위해 당분간 그대로 둔다.

### 3. Appendix / Verification

- `Setting_Book_Appendix_Assembly_Manuscript_Draft.md`
- `Setting_Book_Release_Readiness_Checklist.md`

본문에서 바로 말하기 어려운 검증 정보,
근거 부족 행, naming 충돌, 분류 보류 판단은 이 축에서 본다.

### 4. Conductor / Process Control

- `Setting_Book_Assembly_Index.md`
- `Setting_Book_Thread_Checkpoint.md`
- `Setting_Book_Preview_Package_v0.md`

이 파일들은 책 원고가 아니라 진행 제어판이다.
보통 독자보다 오케스트라나 협업자가 먼저 본다.

## Safe Opening Order

목적이 분명할 때는 아래 순서가 가장 안전하다.

1. `Setting_Book_Preview_Readable_v0.md`
2. `Setting_Book_Document_Roles_Map.md`
3. `Setting_Book_Assembly_Index.md`
4. 필요한 축의 `Core Profiles`
5. 필요할 때만 `Appendix Assembly`와 `Release Readiness`

헷갈린 상태로 다시 들어올 때는 아래 순서가 더 안전하다.

1. `Setting_Book_Document_Roles_Map.md`
2. `Setting_Book_Preview_Readable_v0.md`
3. `07_Setting_Book_Process_Hub.md`

## Current Conductor Decision

- shareable manuscript는 계속 `Setting_Book_Preview_Readable_v0.md`
- compressed single-file reference는 계속 `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`
- RC 이름 논의는 나중에 packaging이 다음 보존 산출물이 될 때 다시 연다
- 지금 단계의 gain은 broad redraft보다 역할 분리와 진입 동선 선명화에서 나온다

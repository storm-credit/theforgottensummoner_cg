# Setting Book Next Preserved Artifact Scope

## Purpose

이 문서는 설정집의 다음 보존 산출물을
`reader-facing layout`로 볼지,
아니면 `production bible`로 볼지 결정했을 때
정확히 어떤 파일을 묶고 어떤 파일을 제외할지 고정하는 범위표다.

핵심은 `무엇을 더 쓰느냐`보다
`무엇을 지금 보존 대상으로 간주하느냐`를 선명하게 하는 데 있다.

## Current Orchestra Call

현재 기본값은 `reader-facing layout scope`다.

이 말은:

- 지금 당장 새 RC 파일을 만들겠다는 뜻이 아니다.
- 현재 shareable preview를 다음 보존 산출물의 중심으로 본다는 뜻이다.
- production bible 확장은 실제 필요가 생길 때만 다시 연다.

## Scope A. Reader-Facing Layout

### Core Package

이 범위가 다음 보존 산출물이 되면 아래 파일을 핵심 묶음으로 본다.

| Layer | File | Role |
| --- | --- | --- |
| main readable manuscript | `Setting_Book_Preview_Readable_v0.md` | 가장 먼저 공유되는 책형 preview |
| opening support | `Setting_Book_Front_Matter_Draft.md` | subtitle, cover tone, opening promise source; direct-share 원고가 아니라 앞부분 source |
| readable body source | `Setting_Book_Public_Assembly_Manuscript_Draft.md` | preview 본문의 조립 원고 |
| reader map support | `Setting_Book_Reader_Facing_TOC_Draft.md` | 독자용 구조 안내 source; `Internal source` 표기는 conductor용으로 유지 |
| package order guide | `Setting_Book_Preview_Package_v0.md` | 이 묶음을 어떤 순서와 범위로 공유할지 관리; direct-share 원고가 아님 |

Direct-share rule:

- 외부에 먼저 보내는 파일은 `Setting_Book_Preview_Readable_v0.md` 하나로 둔다.
- `Front_Matter`, `Reader_Facing_TOC`, `Public_Assembly`는 preview를 받치는 source/support 층으로 둔다.
- `Internal source`, `Archived`, `Production Notes` 같은 표기가 남아 있는 support 문서는 독자에게 바로 보내지 않는다.

### Optional Bridge

필수 본패키지는 아니지만,
협업자나 오케스트라가 축별 보강이 필요할 때만 붙인다.

- `Setting_Book_Faction_Core_Profiles_v0.md`
- `Setting_Book_People_Core_Profiles_v0.md`
- `Setting_Book_Places_Core_Profiles_v0.md`
- `Setting_Book_Items_Core_Profiles_v0.md`
- `Setting_Book_Species_Core_Profiles_v0.md`

### Verification Only

reader-facing layout을 보존할 때도 아래는 `원고 본체`가 아니라
검증 또는 conductor 보조축으로 남긴다.

- `Setting_Book_Appendix_Assembly_Manuscript_Draft.md`
- `Setting_Book_Release_Readiness_Checklist.md`
- `Setting_Book_Filename_Decision_Matrix.md`
- `Setting_Book_Packaging_Direction_Matrix.md`
- `Setting_Book_Document_Roles_Map.md`
- `Setting_Book_Current_Status_Dashboard.md`
- `Setting_Book_Assembly_Index.md`
- `Setting_Book_Thread_Checkpoint.md`

### Verification Depth Rule

reader-facing layout scope에서는
`모든 appendix를 본패키지에 편입`할 필요가 없다.

현재 필요한 깊이는 아래까지다.

- body가 과잉 승격되지 않도록 A-E control이 존재한다는 사실
- Appendix B/C는 현재 anchored row 기준으로만 유지해도 충분하다는 사실
- release checklist가 preview v0와 v1 hold를 구분하고 있다는 사실

반대로 아직 필요하지 않은 깊이:

- appendix 전 행의 source-note 증설
- production bible 수준의 cross-reference 밀도
- technical chapter 0-8을 본패키지 뒤에 연달아 붙이는 일

### Exclude For Now

- 별도 RC 파일 복제
- 상업용 판형 확정본
- production bible 이름의 메인 패키지
- appendix source-note 전면 확장
- `Setting_Book_Chapter_0_*`부터 `Setting_Book_Chapter_8_*`까지의 깊은 설정 초안 직결 편입

## Scope B. Production Bible

### Core Package

production bible 쪽으로 전환할 때는 아래 파일이 중심이 된다.

| Layer | File | Role |
| --- | --- | --- |
| compressed full reference | `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | body + appendix를 한 번에 보는 기준 압축본 |
| appendix manuscript | `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` | evidence / collision / classification control |
| bridge layer | core profile 5종 | 축별 운용 가이드 |
| release gate | `Setting_Book_Release_Readiness_Checklist.md` | 어떤 hold가 남았는지 판단 |
| packaging control | `Setting_Book_Packaging_Direction_Matrix.md` | production bible 전환 이유를 고정 |

### Keep Out Of The Main Production Core

- reader-facing title/cover 환상 과다 고정
- commercial layout 확정본 흉내
- preview와 reference를 한 파일명 체계로 합치기

## Switch Triggers

아래 신호가 생기면 `reader-facing layout scope`에서 `production bible scope`로 재판정한다.

1. 다음 피드백의 중심이 `읽히는가`보다 `근거와 제어가 충분한가`로 이동할 때
2. core profile과 appendix control lane을 협업자에게 본패키지로 넘겨야 할 때
3. Appendix A-E의 source note 밀도를 한 단계 더 올리는 일이 실제 다음 우선순위가 될 때
4. adaptation, art, music, follow-on creator용 기준 묶음이 먼저 필요해질 때

## Current Safe Use

지금은 아래처럼 쓰는 것이 가장 안전하다.

1. shareable artifact는 `Setting_Book_Preview_Readable_v0.md`
2. bridge artifact는 필요한 axis의 core profile
3. verification artifact는 appendix assembly와 release checklist
4. compressed full reference는 `Prototype_v0`

## Current Applied Scope Snapshot

현재 실제 적용 상태는 아래와 같다.

| Scope Layer | Current Status |
| --- | --- |
| reader-facing core package | active default |
| optional bridge | available when needed |
| verification-only docs | kept outside the main preserved package |
| production bible core | not next yet |

따라서 지금은
`preview를 중심으로 한 reader-facing 묶음`을 보존 대상으로 보고,
`prototype + appendix 중심 production 묶음`은 대기 상태로 둔다.

## Current One-Line Call

지금은 `reader-facing layout scope를 다음 보존 산출물 후보로 유지`가 맞고,
production bible scope는 `협업 요구가 실제로 앞서는 순간`에만 다시 연다.

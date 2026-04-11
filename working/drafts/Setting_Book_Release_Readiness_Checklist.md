# Setting Book Release Readiness Checklist

## Purpose

이 문서는 현재 설정집 패키지를
reader-facing release 후보로 볼 수 있는지 점검하는 관문이다.

본문을 더 쓰는 문서가 아니라,
이미 만들어진 front matter, TOC, public assembly, appendix assembly, prototype이
서로 같은 책을 가리키고 있는지 확인하는 conductor sheet다.

## Current Release Candidate Shape

현재 release 후보 묶음은 아래 파일들이 한 세트다.

| Layer | File | Current Role |
| --- | --- | --- |
| cover / opening | `Setting_Book_Front_Matter_Draft.md` | 독자에게 이 책의 목적과 읽는 법을 먼저 설명한다. |
| reader map | `Setting_Book_Reader_Facing_TOC_Draft.md` | 기술 초안 0-8장을 독자용 목차로 번역한다. |
| public body | `Setting_Book_Public_Assembly_Manuscript_Draft.md` | 실제로 읽히는 본문 흐름을 시험한다. |
| readable preview | `Setting_Book_Preview_Readable_v0.md` | front matter와 public body를 한 권처럼 읽히게 묶은 현재 공유용 시안이다. |
| core profile bridge | `Setting_Book_Faction_Core_Profiles_v0.md` 외 4종 | 허브와 기술 초안 사이를 잇는 축별 압축 가이드 세트다. |
| technical appendix | `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` | 본문 뒤의 검증표와 경계 관리를 보존한다. |
| single prototype | `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | 본문과 A-E 부록을 한 파일에 압축한 현재 대표본이다. |
| conductor index | `Setting_Book_Assembly_Index.md` | 작업 상태, main push gate, 다음 큐를 관리한다. |
| handoff checkpoint | `Setting_Book_Thread_Checkpoint.md` | 대화창이 길어질 때 이어받기 기준을 보존한다. |

## Body / Appendix Crosswalk

| Reader Body Area | What The Body Should Do | Appendix Support | Release Check |
| --- | --- | --- | --- |
| Opening: How to Read This World | 세계가 사람의 선택과 관계로 읽힌다는 약속을 세운다. | source map, canon policy notes | 내부 상태표를 노출하지 않는다. |
| Part I. Ether Continent | 중심 문명의 질서, 계승, 계약, 숲의 긴장을 보여준다. | source map, chapter 1 adequacy notes, Appendix A, Appendix C, Appendix E | Spirit Union과 종족 신호를 조심스럽게 유지하고 대륙 전체를 과잉 확정하지 않는다. |
| Part II. Crossroad Cities | 도시와 길이 물건, 소문, 배신을 움직이는 방식을 보여준다. | Appendix C. Place and Travel Functions, Appendix D. Name Collision Control, Appendix A. 14 / 15 Boundary Candidates | 장소를 배경이 아니라 장면 기능으로 설명하고 운영 인물을 자동 승격하지 않는다. |
| Part III. People Worth Seeking | 왜 사람들이 특정 장인, 현자, 기록자, 운영자를 찾아가는지 보여준다. | Appendix A. 14 / 15 Boundary Candidates, Appendix D. Name Collision Control | 영웅축과 명사층을 섞지 않는다. |
| Part IV. Relics and Desired Objects | 물건을 성능보다 욕망, 대가, 소유자, 소문으로 설명한다. | Appendix B. Item Promotion Candidates, Appendix C. Place and Travel Functions, Appendix D. Name Collision Control | 후보 물건을 자동 승격하지 않고 물건이 움직이는 장소와 이름 충돌을 확인한다. |
| Part V. Peoples, Bloodlines, and Changed States | 낯선 존재를 사람들, 혈통, 상태, 괴물, 미확정 신호로 분리한다. | Appendix E. Species Classification Guard, Appendix D. Name Collision Control, Appendix A. 14 / 15 Boundary Candidates | 이름만으로 종족 문명을 만들지 않고, 인물/혈통/상태 신호를 섞지 않는다. |

## Release Gate

release 후보로 묶기 전에 아래를 통과해야 한다.

1. `public body`가 front matter와 같은 약속을 말한다.
2. `readable preview`가 front matter와 public body의 중복 설명 없이 한 권처럼 읽힌다.
3. `appendix assembly`가 A-E 흐름을 유지한다.
4. `prototype v0`가 현재 대표본으로 최신 상태다.
5. 독자용 본문에 raw status label, 파일 경로 설명, audit jargon이 튀어나오지 않는다.
6. 부록 표는 새 lore를 발명하지 않고, 검증과 승격 기준만 보존한다.
7. 이름 충돌, 종족 승격, 아이템 승격은 각각 Appendix D, E, B를 통과한다.
8. prototype, public assembly, appendix assembly, TOC가 Appendix A-E를 같은 구조로 가리킨다.
9. 설정집 계열 파일 스캔에서 금지 표현과 미완료 표식이 나오지 않는다.
10. 사용자 변경 파일이 release 커밋에 섞이지 않는다.
11. 안정 마일스톤이면 `Main Push Gate`를 통과한 뒤 `main`에 fast-forward push한다.
12. core profile bridge 문서들이 readable preview와 기술 초안 사이의 안내선으로 일관되게 동작한다.

## Preview Packaging Gate Snapshot

현재 기준의 gate 판정은 아래와 같다.

| Gate Area | Current Result | Note |
| --- | --- | --- |
| readable preview | pass for preview v0 | `Setting_Book_Preview_Readable_v0.md`가 현재 공유용 대표본 역할을 한다. |
| public assembly tone | pass for preview v0 | public assembly와 readable preview가 같은 톤 패밀리로 정렬되어 있다. |
| core profile bridge | pass for preview v0 | 세력, 인물, 장소, 유물, 종족 중간 정리본이 본문과 기술 초안 사이를 받친다. |
| appendix A-E structure | pass for preview v0 | A-E 표는 최종 확정표가 아니라 통제표로 고정되어 있다. |
| source / evidence depth | partial pass for v1 | Appendix A, D, and E now have targeted row-level evidence notes; B/C remain source-pointer only until a specific row needs verification. |
| Opening / Part I source note | pass for preview v0 | 별도 Appendix F를 만들지 않고 Chapter 0/1과 source map으로 받치는 source note를 추가했다. |
| front matter subtitle / cover tone | pass for preview v0 | `A Living World Companion`과 현재 cover-tone sentence를 v0 선택안으로 고정했다. |
| final naming / layout | hold for v1 | 아직 release-candidate 파일명이나 상업용 판형까지 확정하지 않는다. |

따라서 현재 패키지는 `preview_v0_readable`로는 공유 가능하고,
`v1 release`로 부르기에는 아직 이르다.

## Release-Candidate File Trigger

별도 release-candidate 파일은 지금 즉시 만들지 않는다.

아래 네 조건이 함께 맞을 때만
`preview_v0_readable`을 복제하거나 새 RC 패키지 파일을 만든다.

1. Appendix B/C를 포함해 필요한 row-level evidence note가 더 이상 급한 hold가 아니라고 판단될 때
2. front matter, readable preview, public assembly, prototype의 제목/부제/표지 톤이 같은 결정을 가리킬 때
3. `Prototype_v0`라는 작업용 이름보다 reader-facing 이름이 더 도움이 될 때
4. 다음 단계가 broad drafting이 아니라 보존 가능한 packaging일 때

그 전까지는:

- `Setting_Book_Preview_Readable_v0.md`를 공유용 대표본으로 유지한다.
- `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`는 압축 대표 reference로 유지한다.
- release-candidate라는 이름은 문서 본문보다 checklist 판단에서만 사용한다.

## Current V0 Assessment

현재 패키지는 `prototype v0`와 `public assembly` 기준으로
reader-facing preview 후보를 넘어,
`preview_v0_readable` 공유 가능 상태까지 도달했다.

아직 정식 v1 release로 부르기 전 남은 작업:

1. Appendix B/C에서 특정 행 검증 요청이 생기면 그때만 row-level evidence note를 덧붙인다.
2. release-candidate file trigger 네 조건이 실제로 충족됐는지 다시 판정한다.
3. 최종 파일명을 `Prototype_v0`에서 preview 또는 release candidate 이름으로 바꿀지 결정한다.
4. 상업용 layout 또는 협업용 production bible 방향을 분리할지 결정한다.

## Conductor Decision

다음 진행은 두 갈래 중 하나다.

| Path | Use When | Next Action |
| --- | --- | --- |
| reader-facing preview | 사용자나 협업자에게 먼저 보여줄 책꼴이 필요할 때 | front matter + public assembly + appendix assembly를 하나의 preview manuscript로 묶는다. |
| production bible | 후속 창작자, 아트, 음악, adaptation 팀이 더 정확한 기준을 필요로 할 때 | appendix source notes와 cross-reference를 더 촘촘하게 만든다. |

현재 오케스트라 판단:

현재는 `reader-facing preview` 쪽이 먼저 닫혔다.
이유는 이미 prototype v0와 A-E appendix가 연결되어 있고,
readable preview, public assembly, core profiles, appendix control tables가
서로 같은 패키지 역할을 하기 때문이다.

다음 진행은 `preview_v0_readable`을 더 늘리기보다,
v1로 가기 전에 필요한 row-level evidence note와 release-candidate 파일명 결정을 좁히는 쪽이 좋다.

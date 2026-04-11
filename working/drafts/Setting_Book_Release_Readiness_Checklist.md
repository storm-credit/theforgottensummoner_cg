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
2. `appendix assembly`가 A-E 흐름을 유지한다.
3. `prototype v0`가 현재 대표본으로 최신 상태다.
4. 독자용 본문에 raw status label, 파일 경로 설명, audit jargon이 튀어나오지 않는다.
5. 부록 표는 새 lore를 발명하지 않고, 검증과 승격 기준만 보존한다.
6. 이름 충돌, 종족 승격, 아이템 승격은 각각 Appendix D, E, B를 통과한다.
7. prototype, public assembly, appendix assembly, TOC가 Appendix A-E를 같은 구조로 가리킨다.
8. 설정집 계열 파일 스캔에서 금지 표현과 미완료 표식이 나오지 않는다.
9. 사용자 변경 파일이 release 커밋에 섞이지 않는다.
10. 안정 마일스톤이면 `Main Push Gate`를 통과한 뒤 `main`에 fast-forward push한다.

## Current V0 Assessment

현재 패키지는 `prototype v0`와 `public assembly` 기준으로
reader-facing preview 후보까지는 도달했다.

아직 정식 v1 release로 부르기 전 남은 작업:

1. public body의 Part I-V를 같은 문장 밀도와 호흡으로 더 고르게 다듬는다.
2. Appendix A-E에 source pointer 또는 evidence note를 필요한 만큼만 덧붙인다.
3. Part I과 Opening을 받치는 짧은 canon/source appendix note를 추가할지 결정한다.
4. front matter의 부제와 표지 톤 문장을 하나로 좁힌다.
5. 최종 파일명을 `Prototype_v0`에서 preview 또는 release candidate 이름으로 바꿀지 결정한다.

## Conductor Decision

다음 진행은 두 갈래 중 하나다.

| Path | Use When | Next Action |
| --- | --- | --- |
| reader-facing preview | 사용자나 협업자에게 먼저 보여줄 책꼴이 필요할 때 | front matter + public assembly + appendix assembly를 하나의 preview manuscript로 묶는다. |
| production bible | 후속 창작자, 아트, 음악, adaptation 팀이 더 정확한 기준을 필요로 할 때 | appendix source notes와 cross-reference를 더 촘촘하게 만든다. |

현재 오케스트라 판단:

먼저 `reader-facing preview` 쪽으로 한 번 묶는 것이 좋다.
이유는 이미 prototype v0와 A-E appendix가 연결되어 있고,
이제 필요한 것은 더 많은 원자료 발굴보다
읽히는 책의 형태를 안정적으로 보여주는 일이기 때문이다.

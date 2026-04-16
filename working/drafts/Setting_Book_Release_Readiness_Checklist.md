# Setting Book Release Readiness Checklist

## Purpose

이 문서는 현재 설정집 패키지를
reader-facing release 후보로 볼 수 있는지,
아니면 아직 preview package로 유지해야 하는지 점검하는 관문이다.

본문을 더 쓰는 문서가 아니라,
이미 만들어진 front matter, TOC, public assembly, appendix assembly, prototype이
서로 같은 책을 가리키고 있는지 확인하는 conductor sheet다.

## Current Preview / Prototype Package Shape

현재 점검 중인 패키지 묶음은 아래 파일들이 한 세트다.

| Layer | File | Current Role |
| --- | --- | --- |
| cover / opening | `Setting_Book_Front_Matter_Draft.md` | 독자에게 이 책의 목적과 읽는 법을 먼저 설명한다. |
| reader map | `Setting_Book_Reader_Facing_TOC_Draft.md` | 깊은 설정 초안 0-8장을 독자용 목차로 번역한다. |
| public body | `Setting_Book_Public_Assembly_Manuscript_Draft.md` | 실제로 읽히는 본문 흐름을 시험한다. |
| readable preview | `Setting_Book_Preview_Readable_v0.md` | front matter와 public body를 한 권처럼 읽히게 묶은 현재 공유용 시안이다. |
| core profile bridge | `Setting_Book_Faction_Core_Profiles_v0.md` 외 4종 | 허브와 깊은 기준 기록 사이를 잇는 축별 압축 가이드 세트다. |
| technical appendix | `Setting_Book_Appendix_Assembly_Manuscript_Draft.md` | 본문 뒤의 검증표와 경계 관리를 보존한다. |
| single prototype | `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | 본문과 A-E 부록을 한 파일에 압축한 현재 compressed reference다. |
| conductor index | `Setting_Book_Assembly_Index.md` | 작업 상태, main push gate, 다음 큐를 관리한다. |
| handoff checkpoint | `Setting_Book_Thread_Checkpoint.md` | 대화창이 길어질 때 이어받기 기준을 보존한다. |

## Body / Appendix Crosswalk

Part labels in this crosswalk follow `Setting_Book_Reader_Facing_TOC_Draft.md` as the reader-facing TOC authority.

| Reader Body Area | What The Body Should Do | Appendix Support | Release Check |
| --- | --- | --- | --- |
| Opening: How to Read This World | 세계가 사람의 선택과 관계로 읽힌다는 약속을 세운다. | source map, canon policy notes | 내부 상태표를 노출하지 않는다. |
| Part I. The Five Continents | 대륙 정체성과 각 대륙의 생존/기억/거래/신앙 압력을 보여준다. | source map, chapter 1 adequacy notes, Appendix A, Appendix C, Appendix E | Spirit Union과 종족 신호를 조심스럽게 유지하고 대륙 전체를 과잉 확정하지 않는다. |
| Part II. Powers, Orders, and Hidden Systems | 왕국, 가문, 길드, 교단, 숨은 질서가 어떻게 세계를 움직이는지 보여준다. | Appendix A. 14 / 15 Boundary Candidates, Appendix C. Place and Travel Functions, Appendix D. Name Collision Control | 세력 구조와 장소 압력, 운영 인물을 자동으로 같은 층에 합치지 않는다. |
| Part III. People Worth Seeking | 왜 사람들이 특정 장인, 현자, 기록자, 운영자를 찾아가는지 보여준다. | Appendix A. 14 / 15 Boundary Candidates, Appendix D. Name Collision Control | 영웅축과 명사층을 섞지 않는다. |
| Part IV. Names, Languages, and World Tone | 이름, 언어감, 반복 이름, 미확정 표기를 독자용 톤으로 설명한다. | Appendix D. Name Collision Control, source map, canon policy notes | 이름 충돌을 본문 확정 엔트리처럼 합치지 않는다. |
| Part V. Relics, Gear, Trade Goods, and Things People Want | 물건을 성능보다 욕망, 대가, 소유자, 소문으로 설명한다. | Appendix B. Item Promotion Candidates, Appendix C. Place and Travel Functions, Appendix D. Name Collision Control | 후보 물건을 자동 승격하지 않고 물건이 움직이는 장소와 이름 충돌을 확인한다. |
| Part VI. Peoples, Bloodlines, Monsters, and Changed States | 낯선 존재를 사람들, 혈통, 상태, 괴물, 미확정 신호로 분리한다. | Appendix E. Species Classification Guard, Appendix D. Name Collision Control, Appendix A. 14 / 15 Boundary Candidates | 이름만으로 종족 문명을 만들지 않고, 인물/혈통/상태 신호를 섞지 않는다. |
| Part VII. Places, Routes, and Maps That Create Story | 도시, 항구, 시장, 성소, 길이 장면을 여는 방식을 보여준다. | Appendix C. Place and Travel Functions, Appendix D. Name Collision Control, Appendix A. 14 / 15 Boundary Candidates | 장소를 배경이 아니라 장면 기능으로 설명하고 운영 인물을 자동 승격하지 않는다. |

## Release Gate

release 후보로 묶기 전에 아래를 통과해야 한다.

1. `public body`가 front matter와 같은 약속을 말한다.
2. `readable preview`가 front matter와 public body의 중복 설명 없이 한 권처럼 읽힌다.
3. `appendix assembly`가 A-E 흐름을 유지한다.
4. `Setting_Book_Preview_Readable_v0.md`는 현재 shareable preview로, `prototype v0`는 compressed reference로 각각 최신 상태다.
5. 독자용 본문에 raw status label, 파일 경로 설명, audit jargon이 튀어나오지 않는다.
6. 부록 표는 새 lore를 발명하지 않고, 검증과 승격 기준만 보존한다.
7. 이름 충돌, 종족 승격, 아이템 승격은 각각 Appendix D, E, B를 통과한다.
8. prototype, public assembly, appendix assembly, TOC가 Appendix A-E를 같은 구조로 가리킨다.
9. 설정집 계열 파일 스캔에서 금지 표현과 미완료 표식이 나오지 않는다.
10. 사용자 변경 파일이 release 커밋에 섞이지 않는다.
11. 안정 마일스톤이면 `Main Push Gate`를 통과한 뒤 `main`에 fast-forward push한다.
12. core profile bridge 문서들이 readable preview와 깊은 기준 기록 사이의 안내선으로 일관되게 동작한다.

## Scan Interpretation Rule

스캔 히트가 모두 hold를 뜻하지는 않는다.

허용되는 히트:

- `임시 식별자`처럼 appendix/name-collision control에서 의도적으로 쓰는 관리 용어
- `미완료 표식`, `금지 표현`처럼 checklist가 스캔 기준 자체를 설명하는 문장
- `stable-triad`, `watch/reference`, `watch-keep`처럼 active display가 아니라 금지된 과거 표현으로 기록된 문장

hold로 봐야 하는 히트:

- 본문/표 안에 남은 active TODO, TBD, 미확정 메모
- 독자용 body에 노출된 raw audit label
- old display phrase가 실제 상태값처럼 쓰인 경우

## Preview Packaging Gate Snapshot

현재 기준의 gate 판정은 아래와 같다.

| Gate Area | Current Result | Note |
| --- | --- | --- |
| readable preview | pass for preview v0 | `Setting_Book_Preview_Readable_v0.md`가 현재 공유용 preview 역할을 한다. |
| public assembly tone | pass for preview v0 | public assembly와 readable preview가 같은 톤 패밀리로 정렬되어 있다. |
| core profile bridge | pass for preview v0 | 세력, 인물, 장소, 유물, 종족 중간 정리본이 본문과 깊은 기준 기록 사이를 받친다. |
| appendix A-E structure | pass for preview v0 | A-E 표는 최종 확정표가 아니라 통제표로 고정되어 있다. |
| source / evidence depth | strong partial pass for v1 | Appendix A-E now have source pointer lanes, A/B/C/D/E each carry targeted row-level evidence notes for high-risk rows, and B/C sample files carry their own evidence pointer checks. |
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
4. 다음 단계가 대규모 초안 작성이 아니라 보존 가능한 packaging일 때

현재 trigger 판정:

| Trigger | Current Status | Decision |
| --- | --- | --- |
| Evidence hold | near pass for preview, partial for v1 | A-E source lanes and high-risk row notes exist, and B/C sample evidence checks are in place. Remaining v1 work should be row-specific only. |
| Title / subtitle / cover tone | pass for preview v0 | `A Living World Companion` and the current cover-tone sentence point to the same reader promise. |
| Reader-facing filename value | hold | `Setting_Book_Preview_Readable_v0.md` is still clearer than creating an RC filename too early. |
| Packaging as preserved artifact | hold | The package is stable enough to share as preview, but commercial layout / production bible direction is not chosen yet. |

Trigger result:

- Do not create a separate RC file yet.
- Treat `Setting_Book_Preview_Readable_v0.md` as the shareable preview completion target for now.
- Re-open RC creation only after final naming/layout or production-bible direction becomes the next preserved artifact.

그 전까지는:

- `Setting_Book_Preview_Readable_v0.md`를 공유용 preview로 유지한다.
- `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`는 압축 reference로 유지한다.
- release-candidate라는 이름은 문서 본문보다 checklist 판단에서만 사용한다.
- `Prototype_v0` 파일명은 당분간 유지한다. 지금은 이름 교체보다 역할 분리가 더 중요하다.

## Current V0 Assessment

현재 패키지는 `prototype v0`와 `public assembly` 기준으로
reader-facing preview 후보를 넘어,
`preview_v0_readable` 공유 가능 상태까지 도달했다.

아직 정식 v1 release로 부르기 전 남은 작업:

1. release-candidate file trigger 네 조건이 실제로 충족됐는지 다시 판정한다.
2. 상업용 layout 또는 협업용 production bible 방향을 분리할지 결정한다.
3. 필요한 경우 Appendix B/C의 나머지 행에만 추가 evidence note를 덧붙인다. 지금은 샘플 단위 evidence pointer check까지는 내려가 있다.

## V1 Hold Breakdown

v1로 넘어가기 전 hold는 큰 원고 문제가 아니라
아래 세 결정으로 쪼개서 본다.

| Hold | Current Question | Unblock Condition |
| --- | --- | --- |
| Filename / package name | `Setting_Book_Preview_Readable_v0.md`를 유지할지, 별도 RC 파일을 만들지 | 협업자에게 넘길 보존 산출물이 preview인지 RC인지 결정됨 |
| Layout direction | 상업용 layout을 먼저 볼지, production bible을 먼저 볼지 | 다음 사용자가 reader인지 collaborator인지 결정됨 |
| Row-level evidence | Appendix B/C에서 더 필요한 행이 있는지 | 추가 행이 없거나, 필요한 행만 evidence note로 보강됨 |

`Filename / package name` 판단은 `Setting_Book_Filename_Decision_Matrix.md`에서 따로 관리한다.
`Layout direction` 판단은 `Setting_Book_Packaging_Direction_Matrix.md`에서 따로 관리한다.

현재 오케스트라 판정:

- filename hold는 유지한다. 지금은 preview 이름이 더 안전하다.
- layout hold는 유지한다. 아직 상업용 판형보다 설정 기준 보존이 먼저다.
- row-level evidence hold는 작아졌다. B/C sample evidence pointer check가 들어갔으므로, 이후는 필요한 행만 좁혀서 처리한다.

## Appendix B/C Evidence Queue

지금은 broad evidence pass를 다시 열지 않는다.

필요할 때만 아래 행을 좁혀서 보강한다.

| Appendix | Already Anchored | Add Only If |
| --- | --- | --- |
| B. Item Promotion | `Aegis` collision cluster, fully qualified Aegis item names, owner/person route separation | featured item body가 bare item name을 쓰거나, growth / legendary group item을 독립 엔트리로 올릴 때 |
| C. Place and Travel | Port Nexus, Black Cat, Mercenary Gate | Goldenmark, Dragonforge, auction house, secret warehouse, or Necro Well becomes a body-final featured place |

Current decision:

- no additional B/C row is urgent for preview v0.
- current body-facing scan across `Setting_Book_Preview_Readable_v0.md`, `Setting_Book_Public_Assembly_Manuscript_Draft.md`, core profiles, and `Prototype_v0` did not surface a new body-final B/C candidate beyond the already anchored Aegis cluster and Port Nexus / Black Cat / Mercenary Gate controls.
- latest readable-preview polish keeps Goldenmark, official auction house, secret warehouse, Dragonforge, growth items, and ego items as contextual examples or category language rather than new body-final featured entries.
- therefore, no new Appendix B/C evidence row is added in this pass.
- v1 evidence work should start from the next promoted body entry, not from the whole appendix table.

## Conductor Decision

다음 진행은 두 갈래 중 하나다.

| Path | Use When | Next Action |
| --- | --- | --- |
| reader-facing preview | 사용자나 협업자에게 먼저 보여줄 책꼴이 필요할 때 | 현재 readable preview를 안정 공유본으로 유지하고, 오탈자나 독자용 말투만 좁게 수정한다. |
| production bible | 후속 창작자, 아트, 음악, adaptation 팀이 더 정확한 기준을 필요로 할 때 | appendix source notes와 cross-reference를 더 촘촘하게 만든다. |

현재 오케스트라 판단:

현재는 `reader-facing preview` 쪽이 먼저 닫혔다.
이유는 이미 prototype v0와 A-E appendix가 연결되어 있고,
readable preview, public assembly, core profiles, appendix control tables가
서로 같은 패키지 역할을 하기 때문이다.

다음 진행은 `preview_v0_readable`을 더 늘리기보다,
v1로 가기 전에 필요한 row-level evidence note와 packaging 방향을 좁히는 쪽이 좋다.

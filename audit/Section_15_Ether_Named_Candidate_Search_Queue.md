# Section 15 Ether Named Candidate Search Queue

이 문서는 에테르 장소-기관 슬롯에 실제 개인명 후보가 있는지
이전에 어떤 순서로 확인했고 지금 무엇을 reference로 유지하는지 고정한다.

원칙:

- 새 이름을 발명하지 않는다.
- 14번 영웅 신호가 보이면 `verify_before_15`로 둔다.
- 개인명이 없으면 `need_named_candidate` 슬롯으로 유지한다.
- 표면명 후보는 정본명이 아니라 검색을 돕는 표시명이다.

## Needs Polish Resolution

| Previous Candidate | Updated Preferred Candidate | State | Reason |
|---|---|---|---|
| `마나로 장인장` | `비전로 장인장` | `preferred_display_candidate` | `마나로`보다 말맛이 안정적이고 마법협회 제작로 이미지를 준다. |
| `성검 무장장` | `성검 병장관` | `preferred_display_candidate` | 성국의 무기/병장 행정 위계를 더 잘 받는다. |
| `흑감옥 무기지기` | `옵시디안 무기지기` | `preferred_display_candidate` | 장소 앵커가 분명해진다. |
| `지식수호장` | `대서고 수호장` | `preferred_display_candidate` | 성국 중앙 도서관의 장소성이 더 살아난다. |
| `영묘 이름새김꾼` | `정령묘 이름새김꾼` | `preferred_display_candidate` | 정령연합 앵커를 분명하게 한다. |

## Search Queue

| Priority | Search Target | Anchor | Search Terms | Expected Result |
|---|---|---|---|---|
| 1 | `봉인서고지기 / 금서 검인관` | `금서 도서관`, `마법 서고단` | `금서 도서관`, `사서장`, `검열관`, `마법 서고단`, `대런 크레센트` | 개인명 확인 또는 대런 14 경계 유지 |
| 2 | `비전로 장인장 / 비전 제작관` | `마나 공방`, `마법협회 제작축` | `마나 공방`, `공방장`, `제작 감독관`, `비전 제작`, `마도 제작` | 공방장 개인명 여부 확인 |
| 3 | `성좌 관측장 / 별기록관` | `아스트랄 관측소`, `별의 예언자단` | `아스트랄 관측소`, `관측장`, `별의 예언자단`, `칼리스트`, `별기록` | 칼리스트 경계 유지 또는 별기록관 슬롯 확인 |
| 4 | `대서고 학장 / 대서고 수호장` | `아스트라르 중앙 도서관`, `성국` | `아스트라르`, `중앙 도서관`, `도서관장`, `래퍼티`, `지식의 수호자` | 래퍼티 14 경계 유지 또는 별도 학장 슬롯 확인 |
| 5 | `성채 봉인관 / 순교묘역 사제장` | `루멘 성채`, `순교자 묘역` | `루멘 성채`, `대사제 요한`, `결계`, `순교자`, `성채` | 요한 14 경계 유지 또는 성채 실무 슬롯 확인 |
| 6 | `성검 병장관 / 옵시디안 무기지기` | `옵시디안`, `성검 요새`, `감옥 무기고` | `옵시디안`, `성검 요새`, `무기 장인`, `무기고`, `감옥` | 무기/감옥 명사형 NPC 슬롯 확인 |
| 7 | `서약의회 기록관 / 전비 장부관` | `레갈리아`, `아덴브루크`, `왕국연합` | `연합 의회`, `레갈리아`, `아덴브루크`, `전비 어음`, `장부관` | 왕국연합 기록/금융 명사 슬롯 확인 |
| 8 | `그늘항로 기록관 / 서약문 보관관` | `포트 넥서스`, `머시너리 게이트`, `자유도시연합` | `포트 넥서스`, `제3 부두`, `검은 고양이`, `머시너리 게이트`, `계약문` | 자유도시 운영층 후보 확인 |
| 9 | `정령서약 해석자 / 정령묘 이름새김꾼` | `루미라`, `잠든 정령의 숲`, `정령의 무덤` | `루미라`, `엘다라`, `정령 계약`, `잠든 정령의 숲`, `정령의 무덤`, `이름 새김` | 엘다라 후보 보강 또는 이름 없는 슬롯 유지 |

## Decision Snapshot

에테르는 이번 큐에서도 새 이름을 만들지 않는다.

현재 이 문서는 새 검색 배치를 여는 기준서가 아니라,
위 검색어와 결과를 reference backlog로 유지하는 장부다.
추가 검색은 live handoff나 새 증거 drift가 있을 때만 다시 연다.

## Search Progress

| Priority | Result |
|---|---|
| 1 | `done`. `대런 크레센트`는 `verify_before_15` 유지, `봉인서고지기 / 금서 검인관`은 `need_named_candidate` 유지. |
| 2 | `done`. `에드가 룬워커`는 A급/Act 신호 때문에 `verify_before_15` 유지, `비전로 장인장 / 비전 제작관`은 `need_named_candidate` 유지. |
| 3 | `done`. `칼리스트`는 A+/Act/대예언자 신호 때문에 `verify_before_15` 유지, `성좌 관측장 / 별기록관`은 `need_named_candidate` 유지. |
| 4 | `done`. `래퍼티 아르카디아`는 A급/Act/도서관장 신호 때문에 `verify_before_15` 유지, `라파엘 아르카디아`는 이름 드리프트 확인 대상으로 분리, `대서고 학장 / 대서고 수호장`은 `need_named_candidate` 유지. |
| 5 | `done`. `대사제 요한`은 루멘 성채 총괄/결계 공명 신호 때문에 `verify_before_15` 유지, `발레리우스 / 헬렌`은 로컬 이름 슬롯 확인 대상으로 분리, `성채 봉인관 / 순교묘역 사제장`은 `need_named_candidate` 유지. |
| 6 | `done`. `알렉산드로 발렌티안`은 SS급 총단장 신호 때문에 `keep_14`, `실라스 블랙쏜`은 S급 고문관/감옥 관리자 신호 때문에 `keep_14_likely`, `성검 병장관 / 옵시디안 무기지기`는 `need_named_candidate` 유지. |
| 7 | `done`. `레온하르트 / 제라르드`는 14 유지, `리아나 실버레이크`는 왕국연합 핵심표 신호 때문에 `verify_before_15`, `서약의회 기록관 / 전비 장부관`은 `need_named_candidate` 유지. |
| 8 | `done`. `드레이크 루가`는 14 유지, `셀레나 와일드웨이브 / 레온 벨가르드`는 `verify_before_15`, `그늘항로 기록관 / 서약문 보관관`은 `need_named_candidate` 유지. |
| 9 | `done`. `엘다라`는 루미라 대현자/고대 정령어 권위자로 15 후보 유지, `실바리온`은 14 유지, `엘라라 / 드라이덴 / 메라 / 실라스 나이트쉐이드`는 `verify_before_15`, `정령서약 해석자 / 정령묘 이름새김꾼`은 `need_named_candidate` 유지. |

## Post Surface-Name Lock

- 이번 pass에서 `봉인서고지기`, `비전로 장인장`, `성좌 관측장`, `대서고 학장`, `성채 봉인관`, `성검 병장관`, `서약의회 기록관`, `그늘항로 기록관`, `정령서약 해석자` 계열을 표면 기본값으로 잠갔다.
- 이후 검색 로그와 후속 배치는 working label보다 위 표면명 후보를 우선해서 쓴다.

## Low-Priority Auxiliary Follow-Up

| Slot | Read-Only Result | Keep State |
|---|---|---|
| `탑서기` | direct holder 미확인. 탑주/협회 핵심축 실명과만 인접함. | `need_named_candidate` |
| `왕실 의전서기` | direct holder 미확인. `레온하르트` 및 익명 `의회 서기장`과 분리 유지. | `need_named_candidate` |
| `성벽 설계서기` | direct holder 미확인. `에드몬드 듀락`, `제라르드 파브리스`와 분리 유지. | `need_named_candidate` |
| `상단 조율관` | direct holder 미확인. `세실리아 메르카토르`와 분리 유지. | `need_named_candidate` |
| `항만 인장관` | direct holder 미확인. `드레이크 루가`, `셀레나 와일드웨이브`와 분리 유지. | `need_named_candidate` |
| `탐사 기록관` | direct holder 미확인. `발타자르`, `에드윈`, `에드가 룬워커`와 분리 유지. | `need_named_candidate` |
| `연구소 보존관` | direct holder 미확인. 표본/보존 책임 실명 앵커 없음. | `need_named_candidate` |
| `대현자 보좌 기록관` | direct holder 미확인. `엘다라` 및 `엘라라 문힘`과 역할 축이 다르다. | `need_named_candidate` |
| `침묵의 감시자` | 개인명 미확인. `Silent Watchers` 집단 직함으로만 확인됨. | `need_named_candidate` |

Ether low-priority auxiliary slot 9개 read-only closure가 완료됐고,
현재는 이 결과를 closure sync / carryover watch 아래 reference로 유지한다.

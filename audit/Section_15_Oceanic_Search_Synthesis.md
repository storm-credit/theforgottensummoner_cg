# Section 15 Oceanic Search Synthesis

이 문서는 해양 대륙의 `15 Named Notables` 후보와 역할 슬롯을 압축한 종합표다.

해양은 이름 있는 후보가 많지만,
대부분 제독, A/SS급, 히어로급, 단장급, 전설/신화 축과 겹친다.
따라서 15 확정보다 `verify_before_15`와 도시 기능 슬롯 보존 우선으로 정리됐다.

## Conductor Reading

해양에서는 새 15 확정자가 확인되지 않았다.

해양의 강점은 `포트 아우렐리온`, `크로스윈드 포트`, `오라클 바지`,
`블랙워터 항구`, `붉은 해골 섬`, `볼트 오브 아우룸`, `유령선의 안식처` 같은
장소-기관 슬롯이다.

`top 5 slot` read-only pass 기준으로는
`신탁 방주`, `해로 장부관`, `왕실 선공장 수석장`, `흑조 감정관`의 direct holder는 확인되지 않았고,
`심연 장부관`은 `이소벨 골드리프`라는 상위 재무 권력축만 인접하는 것으로 정리됐다.

이 `city-role batch` snapshot에서는
`항해사 길드장`, `마스터 쉽라이트`, `수석 기상관`, `대경매장 주인`, `은행장`, `세관장`도
모두 direct holder 없이 strong role slot으로만 확인됐다.

## Stable 15 Candidate

안정 15 후보 없음.

## Verify Before 15

| Candidate | Anchor | Reason | State |
|---|---|---|---|
| `미다스` | `황금 함대` | 바다의 연금술사, 침묵의 금괴, 해양 상단 신화 반복. | `verify_before_15` |
| `해양 실비아` | `황금 함대` | 해류의 지휘관, 은빛 항해사. 실비아 이름 충돌. | `verify_before_15 / name_collision` |
| `이소벨 골드리프` | `황금 함대 / 재무관실` | SS급 재무 실권자, 포탄 구매 허가권. | `verify_before_15` |
| `마르코 바르텔로` | `거상 연합` | 해운왕, 시세 조작, 히어로급 표기. | `verify_before_15` |
| `엘레오노라 라 크루즈` | `거상 연합` | 거래의 심판관, 독소조항 설계자. | `verify_before_15` |
| `골드핑거 바스` | `해적 연합 / 암시장 조합` | A급 암시장 조합장, 장물과 밀수 네트워크. | `verify_before_15` |
| `리나 웨이브서프` | `심해 탐사단` | 바다의 연금술사, 복원 학자, 히어로급 신호. | `verify_before_15` |
| `에릭 시스트롬` | `심해 탐사단` | 파도의 거래자, 금단 유물 유통, 암시장 협상가. | `verify_before_15` |
| `오렌` | `바다의 교단 / 심해 감시단` | 심연 징후 판단권, 교단 군사력 발동 트리거. | `verify_before_15` |
| `세일블레스 마리아` | `바다의 교단 / 성스러운 함대` | A급 성스러운 함대 제독, 오라클 바지 연결. | `verify_before_15` |
| `모로스` | `해적 연합 / 유령선의 안식처` | 해골 제독, 죽은 선장 항해일지 수집. | `verify_before_15` |
| `크리스토퍼 델마르` | `황금 함대 / 거상 연합` | 검은 동전, 도난품 장물 처리, 암시장 자금 담당. | `verify_before_15` |

## Need Named Candidate Slots

| Slot | Anchor | Function | State |
|---|---|---|---|
| `수석 오라클 / 파도 신탁장` | `오라클 바지 / 신탁 방주` | 이동형 예언 성소, 신탁 전달, 해상 재판과 축복. | `need_named_candidate / role_slot_confirmed` |
| `항로 기록관 / 해도 보관인` | `골든 앵커 하버 / 크로스윈드 포트` | 항로, 해도, 보험 요율, 호위 스케줄 관리. | `need_named_candidate / role_slot_confirmed` |
| `왕실 조선소 수석 공병` | `크로스윈드 포트 / 왕실 조선소` | 마도 전열함 도면, 선체 결함, 기술 유출 미스터리. | `need_named_candidate / role_slot_confirmed` |
| `장물 감정사 / 늙은 감정사` | `블랙워터 항구 / 붉은 해골 섬` | 도난품, 저주 유물, 진품/가품 감정. | `need_named_candidate / role_slot_confirmed` |
| `심해 금고 보관인` | `볼트 오브 아우룸 / Abyssal Vaults` | 이중 장부, 십일조, 영생 연구 자금 은닉. | `need_named_candidate / boundary_candidate_only` |
| `수석 무역왕` | `포트 아우렐리온 / 무역왕의 궁전` | 도시 실권, 거래 권력, 경제적 압박. | `need_named_candidate / role_slot_confirmed` |
| `스톰 체이서 대장` | `크로스윈드 포트 / 스톰 체이서` | 폭풍 항해, 위험 지역 가이드, 구조. | `need_named_candidate / role_slot_confirmed` |
| `조선공 길드 장인` | `폭풍의 만 / 검은 돛 조선소` | 납치된 기술자, 해적식 선박 개조, 반란 훅. | `need_named_candidate / role_slot_confirmed` |
| `진혼의 합창단 악기 보관인` | `고대의 악기실` | 전설 악기, 포세이돈의 소라 고둥, 음악/성물 소진행. | `need_named_candidate / role_slot_confirmed` |
| `죽은 선장의 항해일지 보관인` | `유령선의 안식처` | 망자 항해일지, 유령선 기록, 해적 전승. | `need_named_candidate / role_slot_confirmed` |

## City Slot Narrowing

| City | Slot Cluster | State |
|---|---|---|
| `크로스윈드 포트` | `마스터 쉽라이트`, `수석 기상관`, `항해사 길드장`, `스톰 체이서 대장` | 4슬롯 모두 `role_slot_confirmed / no_named_candidate_yet`로 닫혔다. |
| `포트 아우렐리온` | `수석 무역왕`, `대경매장 주인`, `은행장`, `세관장` | 4슬롯 모두 `role_slot_confirmed / no_named_candidate_yet`로 닫혔다. |
| `오라클 바지 / 볼트 오브 아우룸` | `수석 오라클`, `심해 금고 보관인` | direct holder 미확인. `마리아`, `이소벨`은 상위 boundary anchor로만 인접. |

## Read-Only Pass - Batch 04

`크로스윈드 포트`와 `포트 아우렐리온`의 2열 도시 실무층을 다시 확인한 결과는 아래와 같다.

- `항해사 길드장`, `마스터 쉽라이트`, `수석 기상관`은 `크로스윈드 포트` 핵심 인물 슬롯 표에만 보이고 실명은 없다.
- `대경매장 주인`, `은행장`, `세관장`은 `포트 아우렐리온` 핵심 인물 슬롯 표에만 보이고 실명은 없다.
- `은행장`은 무역/보험/전쟁 펀딩 문맥이 반복되지만 named holder는 확인되지 않았다.
- `대경매장 주인`은 `크리스토퍼 델마르`, `흑조 감정관`과 직접 병합하지 않는다.
- `은행장`은 `이소벨 골드리프`의 재무 권력축과 인접하지만 direct holder는 아니다.

## Read-Only Pass - Batch 05

`포트 아우렐리온`, `크로스윈드 포트`, `폭풍의 만`, `진혼의 합창단`, `유령선의 안식처`를 다시 확인한 결과는 아래와 같다.

- `수석 무역왕`, `스톰 체이서 대장`은 도시 핵심 인물 슬롯 표에만 보이고 실명은 없다.
- `조선공 길드 장인`은 `검은 돛 조선소`와 `조선공 길드` 집합만 보이며 named master는 없다.
- `진혼 악기지기`는 `고대의 악기실`과 `포세이돈의 소라 고둥` 보관/복원 의뢰만 확인되고 keeper 이름은 없다.
- `망자항해 기록관`은 `모로스`가 죽은 선장들의 항해일지를 수집한다는 직접 문장이 있으나, source상 archivist 직함 holder는 아니다.
- 따라서 `모로스`, `데드먼 콜`은 별도 boundary candidate로 두고, 해양 unnamed slot 회수는 `role slot 5`로 1차 마감한다.

## Name Collision Watch

| Cluster | Forms | Decision |
|---|---|---|
| `Sylvia` | `키르케 실비아`, `실비아 아캄`, `해양 실비아`, `실비아 팬텀` | 해양 실비아는 작업명으로만 구분하고, 기존 실비아들과 병합하지 않는다. |
| `Christopher Delmar` | `크리스토퍼 델마르`, `검은 동전` | named boundary candidate. 대경매장 주인/항해사 길드장 이름으로 오인하지 않는다. |

## Conductor Reading

해양은 reference상 “안정 15 후보”보다 “강한 도시 기능형 NPC 슬롯”이 더 중요하다.

- 이름 있는 후보들은 14 확인 전 15 확정 금지.
- 이름 없는 슬롯은 포트 아우렐리온/크로스윈드 포트/오라클 바지/볼트 오브 아우룸 중심으로 보존.
- `카르텔`, `신디케이트`, `히어로급` 같은 현대적/작업용 표현은 표면 정본명으로 고정하지 않는다.
- `세일블레스 마리아`, `이소벨 골드리프`는 slot holder가 아니라 상위 boundary candidate로만 읽는다.
- `크리스토퍼 델마르`도 `대경매장 주인`의 실명으로 읽지 않는다.
- `모로스`는 유령선 기록 축과 인접하지만 `망자항해 기록관`의 direct holder로 병합하지 않는다.

## Reference State Snapshot

해양 unnamed slot read-only pass는 1차 closure 상태로 유지한다.

이 문서는
대륙 우선순위 판단용 실행 큐가 아니라,
해양 narrowing 결과를 reference로 유지하는 종합표다.

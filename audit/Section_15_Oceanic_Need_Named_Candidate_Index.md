# Section 15 Oceanic Need Named Candidate Index

이 문서는 해양 대륙에서 개인명이 아직 확인되지 않은
유명 NPC형 역할 슬롯을 모아두는 색인이다.

## Rule

- 새 이름을 만들지 않는다.
- 항구/도시/선박/금고/경매장 기능을 먼저 보존한다.
- 이름이 확인되면 14 신호 검토 후 15 후보로 올린다.

## Slot Index

| Slot | Place / Institution Anchor | Function | State |
|---|---|---|---|
| `수석 오라클 / 파도 신탁장` | `오라클 바지 / 신탁 방주` | 해상 예언, 이동 성소, 신탁 전달 | `need_named_candidate / role_slot_confirmed` |
| `항로 기록관 / 해도 보관인` | `골든 앵커 하버 / 크로스윈드 포트` | 항로 기록, 보험 요율, 해도 보관, 호위 스케줄 | `need_named_candidate / role_slot_confirmed` |
| `왕실 조선소 수석 공병` | `크로스윈드 포트 / 왕실 조선소` | 전열함 도면, 선체 결함, 기술 유출 | `need_named_candidate / role_slot_confirmed` |
| `마스터 쉽라이트` | `크로스윈드 포트 / 제1 국영 조선소` | 배의 목소리를 듣는 노장 장인 | `need_named_candidate / role_slot_confirmed` |
| `수석 기상관` | `크로스윈드 포트 / 바람의 탑` | 기상 예보, 출항권, 폭풍 조작 | `need_named_candidate / role_slot_confirmed` |
| `항해사 길드장` | `크로스윈드 포트 / 항해사 길드 본부` | 숨겨진 섬 위치, 지도 정보, 항로 개척 | `need_named_candidate / role_slot_confirmed` |
| `스톰 체이서 대장` | `크로스윈드 포트 / 스톰 체이서` | 폭풍 항해, 위험 지역 가이드, 구조 | `need_named_candidate / role_slot_confirmed` |
| `수석 무역왕` | `포트 아우렐리온 / 무역왕의 궁전` | 도시 실권, 거래 권력, 경제적 압박 | `need_named_candidate / role_slot_confirmed` |
| `대경매장 주인` | `포트 아우렐리온 / 대경매장` | 희귀 아이템 감정, 정보상, 경매 게이트 | `need_named_candidate / role_slot_confirmed` |
| `은행장` | `포트 아우렐리온 / 세계 은행 본점` | 대륙 금융 흐름, 자금 지원, 경제적 압박 | `need_named_candidate / role_slot_confirmed` |
| `세관장` | `포트 아우렐리온 / 제1 항구 / 세관` | 입항세, 통행 편의, 밀수 단속, 뇌물 갈등 | `need_named_candidate / role_slot_confirmed` |
| `장물 감정사 / 늙은 감정사` | `블랙워터 항구 / 붉은 해골 섬` | 도난품, 저주 유물, 진품/가품 감정 | `need_named_candidate / role_slot_confirmed` |
| `심해 금고 보관인` | `볼트 오브 아우룸 / Abyssal Vaults` | 이중 장부, 금고, 십일조, 은닉 자금 | `need_named_candidate / boundary_candidate_only` |
| `조선공 길드 장인` | `폭풍의 만 / 검은 돛 조선소` | 해적식 선박 개조, 납치 기술자, 반란 훅 | `need_named_candidate / role_slot_confirmed` |
| `진혼의 합창단 악기 보관인` | `고대의 악기실` | 성물 악기, 음악/성물 소진행 연결 | `need_named_candidate / role_slot_confirmed` |
| `죽은 선장의 항해일지 보관인` | `유령선의 안식처` | 망자 항해일지, 유령선 전승, 기록 수집 | `need_named_candidate / role_slot_confirmed` |

## Read-Only Pass - Batch 03

| Slot | Direct Holder | Evidence | Hold |
|---|---|---|---|
| `수석 오라클 / 파도 신탁장` | `미확인` | `오라클 바지`에 `수석 오라클` 직함과 `12명의 타이드워커`만 보임 | `role slot 유지` |
| `항로 기록관 / 해도 보관인` | `미확인` | `골든 앵커 하버`의 항로 배치/보험 요율, `크로스윈드 포트`의 해도/항해사 길드 기능만 확인 | `role slot 유지` |
| `왕실 조선소 수석 공병` | `미확인` | `크로스윈드 포트`와 `왕실 조선소`에 조선 핵심 기능은 있으나 direct engineer 이름은 없음 | `role slot 유지` |
| `장물 감정사 / 늙은 감정사` | `미확인` | `블랙워터 항구`와 `붉은 해골 섬`에 감정/저주 판별 기능만 확인 | `role slot 유지` |
| `심해 금고 보관인` | `미확인` | `볼트 오브 아우룸`에는 금고 구조만 있고 direct keeper 없음. `이소벨 골드리프`는 SS급 상위 재무 권력축으로만 인접 | `slot 유지, boundary candidate와 분리` |

## Read-Only Pass - Batch 04

| Slot | Direct Holder | Evidence | Hold |
|---|---|---|---|
| `항해사 길드장` | `미확인` | `크로스윈드 포트` 핵심 인물 슬롯 표에 `숨겨진 섬 위치`, `지도 정보 공유`, `항로 개척` 역할로만 보임 | `role slot 유지` |
| `마스터 쉽라이트` | `미확인` | `크로스윈드 포트` 핵심 인물 슬롯 표에 `전설적인 명장`, `배의 목소리를 듣는 노인`으로만 보임 | `role slot 유지` |
| `수석 기상관` | `미확인` | `크로스윈드 포트` 핵심 인물 슬롯 표에 `바람의 탑 주인`, `정확한 기상 예보 및 출항권 획득`으로만 보임 | `role slot 유지` |
| `대경매장 주인` | `미확인` | `포트 아우렐리온` 핵심 인물 슬롯 표에 `감정사`, `정보상`으로만 보임 | `role slot 유지, 델마르와 분리` |
| `은행장` | `미확인` | `포트 아우렐리온` 핵심 인물 슬롯 표와 해양 무역 흐름 문서에 반복되지만 실명은 없음 | `role slot 유지, 이소벨과 분리` |
| `세관장` | `미확인` | `포트 아우렐리온` 핵심 인물 슬롯 표에 `뒷돈에 약한 통관 관리자`로만 보임 | `role slot 유지` |

## Read-Only Pass - Batch 05

| Slot | Direct Holder | Evidence | Hold |
|---|---|---|---|
| `수석 무역왕` | `미확인` | `포트 아우렐리온` 핵심 인물 슬롯 표에 `의회 의장이자 도시 최고의 거부`로만 보임 | `role slot 유지` |
| `스톰 체이서 대장` | `미확인` | `크로스윈드 포트` 핵심 인물 슬롯 표에 `폭풍을 즐기는 광기 어린 조타수`로만 보임 | `role slot 유지` |
| `조선공 길드 장인` | `미확인` | `폭풍의 만`에 `검은 돛 조선소`, `조선공 길드`와 `납치된 기술자와 해적 출신 장인` 집합만 보임 | `role slot 유지, 바르가스와 분리` |
| `진혼의 합창단 악기 보관인` | `미확인` | `진혼의 합창단` 문서에 `고대의 악기실` 보관소와 `포세이돈의 소라 고둥` 의뢰만 보임 | `role slot 유지` |
| `죽은 선장의 항해일지 보관인` | `미확인` | `유령선의 안식처`에 `모로스 제독이 ... 항해일지를 수집한다`는 문장이 직접 보이지만 archivist 직함 holder는 아님 | `role slot 유지, 모로스/데드먼 콜과 분리` |

## Routing Notes

해양 슬롯은 도시 기능이 강하다.

후속 작업은 다음 순서로 진행한다.

1. 포트/항구/선박/금고/경매장 장소 앵커 유지.
2. 실제 개인명 확인.
3. 제독/A급/히어로급/단장급 신호 확인.
4. 14 확인 전 `verify_before_15` 또는 `need_named_candidate`로만 유지.

# Section 15 Oceanic Role Slot Narrowing

이 문서는 `포트 아우렐리온`과 `크로스윈드 포트`의
이름 없는 유명 NPC 슬롯을 더 좁히기 위한 정리표다.

## Conductor Reading

해양 대륙은 이름 있는 후보보다
먼저 `도시 기능에 박힌 유명 NPC 슬롯`이 강하게 보인다.

따라서 새 이름을 만들지 않고,
도시별로 어떤 슬롯이 `15 Named Notables` 후보가 될 수 있는지 분리한다.

## Crosswind Port Slots

| Slot | Display Candidate Direction | Anchor | Story Function | Current State |
|---|---|---|---|---|
| `마스터 쉽라이트` | `선공장 장인장 / 배말 장인` | `크로스윈드 포트 / 제1 국영 조선소` | 선박 개조, 수리, 배의 목소리를 듣는 노인 | `need_named_candidate` |
| `수석 기상관` | `바람탑 관측장 / 풍향 예언관` | `바람의 탑` | 기상 예보, 출항권, 폭풍 조작 | `need_named_candidate` |
| `항해사 길드장` | `청해도 보관관 / 별항로 길드장` | `항해사 길드 본부 / Navigator's Quarter` | 숨겨진 섬 위치, 지도 정보, 항로 개척 | `need_named_candidate` |
| `스톰 체이서 대장` | `폭풍추적대장 / 광풍 조타장` | `스톰 체이서` | 위험 지역 가이드, 폭풍 구조, 광기 어린 조타수 | `need_named_candidate` |

## Port Aurelion Slots

| Slot | Display Candidate Direction | Anchor | Story Function | Current State |
|---|---|---|---|---|
| `수석 무역왕` | `대상왕 / 황금의 의장` | `무역왕의 궁전 / 7인의 무역왕` | 도시 실권자, 거래의 산, 넘어야 할 경제 권력 | `need_named_candidate` |
| `대경매장 주인` | `대경매장 감정관 / 황금망치 주인` | `대경매장` | 희귀 아이템 감정, 정보상, 경매 입찰 게이트 | `need_named_candidate` |
| `은행장` | `대금고장 / 황금 장부관` | `세계 은행 본점 / 금융 지구` | 자금 지원, 경제적 압박, 대륙 금융 흐름 | `need_named_candidate` |
| `세관장` | `쌍등대 세관장 / 항세 집행관` | `제1 항구 / 세관` | 통행 편의, 세금, 밀수 단속, 뇌물 갈등 | `need_named_candidate` |

## Split Rule

`대경매장 주인`과 `늙은 감정사`는 아직 같은 인물로 보지 않는다.

- `대경매장 주인`: 합법/반합법 고가 거래, 정보상, 포트 아우렐리온.
- `늙은 감정사`: 블랙워터 항구, 장물, 저주 유물, 해적 연합.

두 슬롯은 모두 감정 기능을 가지지만
무대와 사회적 계층이 다르다.

## Next Search Terms

| Slot | Search Terms |
|---|---|
| `마스터 쉽라이트` | `Master Shipwright`, `쉽라이트`, `조선소`, `배의 목소리` |
| `수석 기상관` | `수석 기상관`, `바람의 탑`, `기상관`, `풍향` |
| `항해사 길드장` | `항해사 길드장`, `Navigator's Quarter`, `해도`, `숨겨진 섬` |
| `스톰 체이서 대장` | `Storm Chaser`, `스톰 체이서`, `조타수`, `폭풍` |
| `대경매장 주인` | `대경매장 주인`, `Grand Auction House`, `감정사`, `경매장` |
| `은행장` | `은행장`, `Grand Bank`, `금융`, `장부` |
| `세관장` | `세관장`, `세관`, `Customs`, `입항세` |

## Conductor Decision

해양 15 Named Notables는
지금 당장 기존 named candidate를 확정하기보다
아래 두 도시 슬롯을 먼저 보존한다.

- `크로스윈드 포트`: 조선, 기상, 항해, 폭풍 구조.
- `포트 아우렐리온`: 경매, 금융, 세관, 무역왕.

이 방식이 해양 대륙의 도시 기능과 유명 NPC 감각을 가장 안전하게 살린다.

## Batch 03 Result

`Section_15_Oceanic_Search_Findings_Batch_03.md`에서 재검색했다.

결과:

- `마스터 쉽라이트`, `수석 기상관`, `항해사 길드장`, `스톰 체이서 대장`은 모두 개인명 없이 역할 슬롯으로 유지한다.
- `수석 무역왕`, `대경매장 주인`, `은행장`, `세관장`도 개인명 없이 역할 슬롯으로 유지한다.
- 이번 배치에서 새 named candidate는 만들지 않는다.

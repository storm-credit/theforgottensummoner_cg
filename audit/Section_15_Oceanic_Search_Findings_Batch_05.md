# Section 15 Oceanic Search Findings Batch 05

이 문서는 해양 `15 Named Notables` 후보명 탐색의
잔여 unnamed slot read-only pass 결과를 기록한다.

## Search Scope

검색 범위:

- `working/imports/phase4_section8_oceanic_golden_armada/1. 주요 장소 (Locations)/도시/포트 아우렐리온 (Port Aurelion).md`
- `working/imports/phase4_section8_oceanic_golden_armada/1. 주요 장소 (Locations)/도시/크로스윈드 포트 (Crosswind Port).md`
- `working/imports/phase4_section8_oceanic_pirate_confederacy/1. 주요 장소 (Locations)/요새/폭풍의 만 (Storm Bay).md`
- `working/imports/phase4_section8_oceanic_church_of_sea/16. 예하 부대 및 기사단 (Military Units)/09. 진혼의 합창단 (Choir of Requiems).md`
- `working/imports/phase4_section8_oceanic_pirate_confederacy/1. 주요 장소 (Locations)/요새/유령선의 안식처 (Ghost Fleet Anchorage).md`

집중 대상:

- `수석 무역왕`
- `스톰 체이서 대장`
- `조선공 길드 장인 / 검은돛 선장인`
- `진혼의 합창단 악기 보관인 / 진혼 악기지기`
- `죽은 선장의 항해일지 보관인 / 망자항해 기록관`

## Findings

| Search Slot | Best Anchor File(s) | Evidence Found | Current State | Conductor Judgment |
|---|---|---|---|---|
| `수석 무역왕` | `포트 아우렐리온 (Port Aurelion)` | `수석 무역왕`이 `의회 의장이자 도시 최고의 거부`, `사실상 도시의 지배자` 역할로만 적힌다. | `role_slot_confirmed` | `7인의 무역왕` 체계는 강하지만 direct holder 개인명은 없다. `이소벨 골드리프`, `에드워드 실버크레스트`, 거상 연합 인물군과 병합하지 않는다. |
| `스톰 체이서 대장` | `크로스윈드 포트 (Crosswind Port)` | `스톰 체이서 대장`이 `폭풍을 즐기는 광기 어린 조타수`, `위험 지역 가이드` 역할로만 적힌다. | `role_slot_confirmed` | 구조/폭풍 유인 특수부대 슬롯은 강하지만 실명은 없다. `아주라 스톰`과 병합하지 않는다. |
| `조선공 길드 장인 / 검은돛 선장인` | `폭풍의 만 (Storm Bay)` | `검은 돛 조선소`, `조선공 길드`, `납치된 기술자와 해적 출신 장인들의 기묘한 조합`만 확인된다. | `role_slot_confirmed` | 조선공 길드 기능은 강하지만 named master는 없다. `바르가스`, `파이어세일 잭`과 병합하지 않는다. |
| `진혼의 합창단 악기 보관인 / 진혼 악기지기` | `진혼의 합창단 (Choir of Requiems)` | `고대의 악기실`과 `포세이돈의 소라 고둥` 보관/복원 의뢰만 보이고 keeper 개인명은 없다. | `role_slot_confirmed` | 성물/음악 보관 기능은 선명하지만 direct holder는 없다. `레퀴엠 소나`와 병합하지 않는다. |
| `죽은 선장의 항해일지 보관인 / 망자항해 기록관` | `유령선의 안식처 (Ghost Fleet Anchorage)` | `모로스 제독이 이곳에 거주하며, 죽은 선장들의 항해일지를 수집한다`는 직접 문장이 확인된다. | `role_slot_confirmed` | 기록 수집 기능은 보이지만 source상 `모로스`의 명시 직함은 `지배자`다. direct archivist holder로 단정하지 않고 `모로스`, `데드먼 콜`과 병합하지 않는다. |

## Closure Read

- `수석 무역왕`, `스톰 체이서 대장`, `조선공 길드 장인`, `진혼 악기지기`는 원본 import 기준 direct named holder 없이 role slot으로 닫힌다.
- `망자항해 기록관`은 `모로스`의 기록 수집 축과 인접하지만, source상 direct archivist title holder는 아니다.
- 따라서 `모로스`, `데드먼 콜`은 boundary candidate로 따로 두고, 해양 unnamed slot read-only pass는 `role slot 5`로 1차 마감한다.

## Next Search

해양 unnamed slot 회수는 여기서 1차 마감한다.

다음 메인 판단은 아래 순서로 넘긴다.

1. `해양` closure 결과를 압축표와 진행표에 동기화
2. `오벨리스크`와 `프로스트` 중 다음 대륙 우선순위 재고정
3. 실제 원고 입력이 생기면 live handoff case가 우선

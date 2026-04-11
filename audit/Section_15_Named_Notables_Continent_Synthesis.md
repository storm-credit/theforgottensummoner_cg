# Section 15 Named Notables - Continent Synthesis

이 문서는 `15번 Named Notables`를 대륙별로 종합한 watch-reference synthesis다.

목적은 유명 NPC형 영웅, 현자, 장인, 기록자, 감정사, 학파 인물, 공방 인물 등을
`14번 서사 중심 영웅`과 섞지 않고,
기존 구조처럼 `대륙 -> 세력 / 도시 / 조직` 앵커로 라우팅하기 위한 것이다.

## Conductor Rule

- 원본 저장소와 원본 로컬 클론은 수정하지 않는다.
- `15번` 고정 전에는 `14번` 중복 여부를 먼저 확인한다.
- 직업별 폴더링을 본체로 삼지 않는다.
- 본체 앵커는 항상 `대륙 -> 세력 / 도시 / 조직`이다.
- 직업, 명사 유형, 기능은 보조 색인으로만 둔다.
- 빈 역할 슬롯에 새 이름을 즉시 발명하지 않는다.
- `need_named_candidate` 슬롯은 원본 문서 근거가 보일 때까지 role-slot reference로만 둔다.
- 얇은 층 정책 잠금과 evidence/firewall 묶음의 단일 entry는
  `Five_Continent_Missing_Layer_Master_Lock.md`를 우선 따른다.
- 이 synthesis는 대륙별 분포와 판정 요약을 다루는 상위 reference층이다.
- exact guard wording authority는 개별 `Section_15_Named_Notable_*` 카드의 `Policy Guard / Separation Guard`와
  `Section_15_Profile_*` 카드의 `3-1. Policy Guard`에 남기고, 여기서는 재정의하지 않는다.

## Coverage Summary

| Continent | Coverage Snapshot | Primary Reading | Reference Use |
|---|---|---|---|
| Crimson | `strongest` | 용, 대장간, 고대 현자, 부족/제국 잔재 명사층이 이미 강하다. | stable_triad_frozen_reference_set을 닫힌 상태로 유지한다. |
| Ether | `thin with strong place-institution slots` | 마법협회 탑주, 성국 도서관/성채, 정령연합 의식/계약 슬롯이 강하지만 14번 중복 위험이 크다. 장소-기관 슬롯은 먼저 보존한다. | `source_check_hold`와 hold reference split watch-reference를 유지한다. |
| Frost | `thin with strong place-institution slots` | 인물 고정보다 오로라 평원, 얼음무덤 언덕, 아이스포지 병기소, 빙하의 성소 슬롯이 강하다. unnamed slot 6개는 direct holder 없이 role slot 유지로 한 번 닫혔다. | 새 인물 회수보다 closure sync / watch-reference를 유지한다. |
| Oceanic | `thin with many boundary signals and strong place-institution slots` | 후보 이름은 많지만 제독, A급, 히어로급 신호가 많다. 신탁 방주, 해로 장부관, 흑조 감정관, 심연 장부관 슬롯은 보존한다. | 성급한 15 고정 없이 boundary watch-reference 상태를 유지한다. |
| Obelisk | `thin with dense archive slots` | 기록, 기억, 묘역, 봉인, 사후 행정 명사층이 강하다. | 기록/기관 기억 축의 closure state를 유지한다. |
| Supranational | `deferred expansion` | 후기 확장 구역이라 강한 후보도 바로 중심축으로 읽지 않는다. | `deferred expansion` 상태를 유지한다. |

## Crimson

판정: `strongest`

안정 후보:

| Candidate | State Snapshot | Note |
|---|---|---|
| 울프가르 드래곤포지 | `stable_triad_frozen_reference_set / grade_caution` | 장인/대장장이 명사층으로 강하고 `stable_triad_frozen_reference_set` 기준에서 watch-reference를 따른다. |
| 에리온 드라코비스 | `stable_triad_frozen_reference_set / grade_caution / name_collision_watch` | 현자/지식 계열 명사층으로 강하며 `엘드라칸 / 학술-전승층` stable_triad_frozen_reference_set 기준을 따른다. |
| 오그마 | `stable_triad_frozen_reference_set / act_watch` | 기록/지식/전승 계열 후보로 유지하며 `엘드라칸 / 전승 보관층` stable_triad_frozen_reference_set 기준을 따른다. |
| 벨라나 스톰브링어 | `source_check_hold` | 현자 회의 명사 가치가 있지만 SS급 폭풍의 여왕 신호가 강함. |
| 아리안 블레이즈하트 | `source_check_hold` | 현자 회의 명사 가치가 있지만 S급 불의 사제 신호가 강함. |

경계 후보:

| Candidate | State Snapshot | Note |
|---|---|---|
| 드락사르 블레이즈포지 | `source_check_hold` | 14/15 경계 검증 필요. |
| 카사르 더 시어 | `source_check_hold` | 전승/예언 축이지만 14 신호 확인 필요. |

Conductor decision:

크림슨은 `15번 Named Notables` stable_triad_frozen_reference_set 기준에 가장 가깝다.
다만 `stable_triad_frozen_reference_set` 이름은 `울프가르`, `에리온`, `오그마`로 유지하고,
벨라나, 아리안, 드락사르, 카사르는 먼저 14번 경계 검증을 통과해야 한다.
자유도시/오벨리스크 운영층 문구는 named notable 고정 논리가 아니라
lower-card carryover reference로만 유지한다.

## Ether

판정: `thin but foundational`

후보 snapshot:

| Candidate | State Snapshot | Note |
|---|---|---|
| 엘다라 | `source_check_hold / hold reference split` | 에테르 쪽 hold reference split으로 유지한다. |

검증 후보:

| Candidate | State Snapshot | Note |
|---|---|---|
| 대런 크레센트 | `source_check_hold` | 마법 서고단 대표 신호. |
| 엘드린 문브링어 | `source_check_hold` | 백색의 탑 탑주. |
| 마르쿠스 레이븐펠 | `source_check_hold / name_drift` | 흑색의 탑 주앵커는 `맥스웰 레이븐펠`로 읽고, `마르쿠스 레이븐펠`은 drift 표기로만 보존한다. |
| 이사도르 템페스트 | `source_check_hold / name_split_hold` | 청색의 탑 탑주로 보존하되 `이사도르 솔레아`와 병합하지 않는다. |
| 세리오스 벤타리스 | `source_check_hold` | 자색의 탑 탑주, 14번 신호 강함. |
| 네리사 블러드위버 | `source_check_hold` | 적색의 탑 탑주. |
| 다미엔 이클립스 | `source_check_hold` | 은색의 탑 탑주. |
| 칼리스트 | `source_check_hold` | 황금의 탑 탑주, 연금/제작 명사층 가치. |
| 래퍼티 아르카디아 | `source_check_hold` | 성국 도서관장, A급 핵심 인물표 신호. |
| 대사제 요한 | `source_check_hold` | 루멘 성채 총괄자. |
| 엘라라 문힘 | `source_check_hold` | 정령연합 노래술사, A급 영웅표 신호. |
| 드라이덴 썬더루트 | `source_check_hold / great_druid_hold` | 장로 드루이드, 자연 율법회, 생명의 의회, Top 3 대드루이드 신호. |
| 메라 라일윈드 | `source_check_hold / spirit_envoy_hold / name_collision_watch` | 정령연합 외교 사절단, 희귀 재료 교역 조건, `메라 실피드` 드리프트 신호. |
| 실라스 나이트쉐이드 | `source_check_hold / shadow_crow_hold / name_collision_watch` | 그늘까마귀단, 잠든 정령의 숲, `실라스 블랙쏜` 세력 앵커 분리 신호. |

필요 슬롯:

| Slot | State | Anchor Hint |
|---|---|---|
| 마법협회 서고 관리자 | `need_named_candidate` | 마법협회 / 아르카노스 계열 |
| 학파 원로 / 교수 | `need_named_candidate` | 마법협회 학파 구조 |
| 성국 기록 사제 | `need_named_candidate` | 성국 / 사제 기록층 |
| 정령 계약 해석자 | `need_named_candidate` | 정령연합 / 계약 기록층 |

Conductor decision:

에테르는 세계관 중심성이 높아 `source_check_hold` 중심 hold reference split cluster로 먼저 읽는다.
마법협회와 성국의 비영웅 명사층은 장소-기관 슬롯으로 먼저 받친다.
정령연합 바깥 부족층은 `frontier echo / border support` 범위를 넘겨 읽지 않는다.
`결손층 5개`의 thin/support 판정은 이 synthesis가 새로 결정하지 않고,
`audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 참조한다.
운영층 profile cluster에 걸린 guard family는 하위 `3-1. Policy Guard` authority를 따른다.

## Frost

판정: `thin with strong role slots`

경계 후보:

| Candidate | State Snapshot | Note |
|---|---|---|
| 울프릭 | `source_check_hold` | 전설/영웅 신호 확인 필요. |
| 시그리드 프로스트하트 | `source_check_hold` | 14번 신호 확인 필요. |
| 마리안 더 윈터콜러 | `source_check_hold` | 14번 신호 확인 필요. |

강한 역할 슬롯:

| Slot | State | Note |
|---|---|---|
| 전승 보존회 원로 사냥꾼 | `need_named_candidate / role_slot_confirmed` | 생존 지식과 전승 보존 기능. |
| 묘지기 장로 | `need_named_candidate / role_slot_confirmed` | 죽음/기억/공동체 의례 기능. |
| 대예언자 | `need_named_candidate / role_slot_confirmed` | 예언과 의식 권위. |
| 수석 기술자 / 드워프 장인 | `need_named_candidate / role_slot_confirmed` | 공방/기술 명사층. |
| 별의 샤먼 | `need_named_candidate / role_slot_confirmed` | 하늘/징조/부족 의식 기능. |
| 아이스포지 병기소 장인 | `need_named_candidate / role_slot_confirmed` | 무구/공방/방어선 기능. |

Conductor decision:

프로스트는 새 이름을 만들기보다 역할 슬롯을 유지하고,
unnamed slot 6개를 한 번 닫은 상태로 유지하고, 14번 후보 중복 여부는 lower-card watch에서만 더 확인한다.
정주 귀족층은 요새/보급/병기소 운영층 `thin-support` 범위를 넘겨 읽지 않는다.

## Oceanic

판정: `thin with many boundary signals`

경계 후보:

| Candidate | State Snapshot | Note |
|---|---|---|
| 미다스 | `source_check_hold` | 복수 문서 신호가 있어도 전설/전술 축 검증 필요. |
| 해양 실비아 | `source_check_hold / name_collision` | 다른 실비아와 병합 금지. |
| 이소벨 | `source_check_hold` | 제독/히어로급 신호 확인 필요. |
| 마르코 바르텔로 | `source_check_hold` | 상업/항해 명사인지 14 영웅인지 확인 필요. |
| 엘레오노라 라 크루즈 | `source_check_hold` | 귀족/해양 세력 앵커 확인 필요. |
| 골드핑거 바스 | `source_check_hold` | 장물/보물/상업 축 검증 필요. |
| 리나 웨이브서프 | `source_check_hold` | 해양 영웅 신호 확인 필요. |
| 에릭 시스트롬 | `source_check_hold` | 항해/군사 축 확인 필요. |
| 오렌 | `source_check_hold` | 역할 및 14 신호 확인 필요. |
| 세일블레스 마리아 | `source_check_hold` | 종교/항해 명사인지 확인 필요. |
| 모로스 | `source_check_hold` | 영웅/전설 신호 확인 필요. |

강한 역할 슬롯:

| Slot | State | Note |
|---|---|---|
| 신탁 방주 / 파도 신탁장 | `need_named_candidate / display_candidate` | 신탁과 항로 판단 기능. |
| 해로 장부관 / 청해도 보관관 | `need_named_candidate / display_candidate` | 지도/해도/항로 기억 기능. |
| 왕실 선공장 수석장 | `need_named_candidate / display_candidate` | 선박 기술 명사층. |
| 흑조 감정관 / 밤항 선별관 | `need_named_candidate / display_candidate` | 장물/진품/위조 판별 기능. |
| 심연 장부관 / 아우룸 장부관 | `need_named_candidate / display_candidate` | 보물/비밀/심해 자산 기능. |
| 검은돛 선장인 | `need_named_candidate / display_candidate` | 항구 장인층. |
| 진혼 악기지기 | `need_named_candidate / display_candidate` | 의례/음악/기억 기능. |

Conductor decision:

해양은 후보 이름이 많지만 경계 신호도 많다.
현재 모드에서는 `15번` 고정을 열지 않고, 이름 충돌과 14 영웅 신호만 watch 대상으로 둔다.
다만 작업용 라벨은 표면명 후보로 낮췄으므로,
관련 slot은 `신탁 방주`, `해로 장부관`, `흑조 감정관`, `심연 장부관` 기준 reference로만 유지한다.
토착 공동체층은 `support range`까지만 보존하고 대륙 본체 `tribe_clan`으로는 읽지 않는다.
이때 operational profile wording은 named notable 판정문을 대신하지 않는다.

## Obelisk

판정: `thin with dense boundary and archive slots`

경계 후보:

| Candidate | State Snapshot | Note |
|---|---|---|
| 바리온 | `source_check_hold` | 기록/전설/영웅 신호 확인 필요. |
| 아이기스 | `source_check_hold / item_name_collision` | 인물명, 방패, 결계명 충돌 분리 필요. |
| 카론 | `source_check_hold` | 전술/죽음/인도자 신호 확인 필요. |
| 베스 스크롤 | `source_check_hold` | 기록/문서 명사층 여부 확인 필요. |
| 이안 옵저버 | `source_check_hold` | 관측자/기록자 축 확인 필요. |
| 카트린 라베로스 | `source_check_hold` | 세력/기록 앵커 확인 필요. |
| 레보니아 셰이드 | `source_check_hold` | 그림자/기억/망명 축 확인 필요. |
| 우로스 디 모르간 | `source_check_hold` | 기관/가문/기억 축 확인 필요. |
| 세르반 알테르만 | `source_check_hold` | 기록/기관 앵커 확인 필요. |
| 레티시아 모르투스 | `source_check_hold` | 사후/묘역/기록 축 확인 필요. |

강한 역할 슬롯:

| Slot | State | Note |
|---|---|---|
| 기록의 수호자 | `need_named_candidate` | 기관 기억의 핵심 슬롯. |
| 오벨리스크 관측대장 | `need_named_candidate` | 관측/감시/기록 기능. |
| 대봉인관 대행 / 원로 군관 | `need_named_candidate` | 봉인과 행정 권위. |
| 신성 기록소 관리 사제 | `need_named_candidate` | 성역 기록과 사제층. |
| 기억 지기 | `need_named_candidate` | 기억 보존과 망각 관리. |
| 기억 경매장 중개자 | `need_named_candidate` | 기억 거래와 윤리 갈등. |
| 사후 서기관 | `need_named_candidate` | 사후 기록과 법적 행정. |
| 묘역 감독관 | `need_named_candidate` | 묘역 질서와 공동체 기억. |
| 심연 계약 중개자 | `need_named_candidate` | 심연 계약을 인간 제도 안에서 다루는 축. |

Conductor decision:

오벨리스크는 신, 죽음, 심연 쪽으로 과하게 밀리지 않게
`기관 기억 / 기록 / 거래 / 죄책감 / 망명자` 중심으로 읽는다.
가문/왕국/통치자 신호는 계속 `nontraditional elite thin-support` 우선으로 읽는다.
자유도시/오벨리스크 profile family는 exact guard wording authority를
하위 profile 카드에 남긴 채 여기서는 합성 요약으로만 참조한다.

## Supranational

판정: `deferred expansion`

후보:

| Candidate | State Snapshot | Note |
|---|---|---|
| 실비아 | `deferred_expansion_hold / name_collision_watch` | 키르케 영약회 계열 후보지만 범대륙 후기 확장 구역이라 deferred hold reference로만 유지한다. |
| 멜리산드르 | `source_check_hold` | 명사형 가치가 크지만 14 신호 확인 필요. |

Conductor decision:

범대륙은 후기 확장 구역이다.
강한 후보라도 메인 정리의 중심축으로 다시 읽지 않는다.

## Priority Snapshot

1. 본선 reference는 `Crimson` 안정 후보 3명의 `stable_triad_frozen_reference_set` 유지이며 `5대륙 closure sync / Section 8 -> 15 watch-reference`를 계속 읽는다.
2. `엘다라`는 hold reference split 안의 `source_check_hold`로 유지하되 정령연합 전체 14 확인 전 `source_check_hold`로만 남긴다.
3. `Frost / Oceanic / Obelisk`는 장소-기관 슬롯을 유지한 채 closure 상태를 보존하고, 14번 중복 신호 검증 뒤 상태를 다시 읽는다.
4. `Supranational`은 후기 확장 구역으로 보류한다.

## Compressed Status

압축 상태표 reference는 `Section_15_Named_Notables_Status_Compass.md`에 둔다.

최신 지휘 판단:

- 크림슨은 안정 후보 3명만 stable_triad_frozen_reference_set으로 유지한다.
- 에테르, 해양, 오벨리스크는 source_check_hold / watch-reference 상태를 유지하고 새 15 고정자는 만들지 않는다.
- 프로스트, 해양, 에테르의 역할 슬롯은 장소-기관 중심으로 정리했다.
- 이 배치 snapshot에서 프로스트 unnamed slot 6개 closure까지 반영됐고, `stable_triad_frozen_reference_set` 재개가 아니라 `closure sync / watch-reference`를 유지한다.

## Guard Authority Snapshot

- named notable synthesis는 카드층의 guard family를 요약하는 상위 reference다.
- operational lower-card carryover는 언급할 수 있지만,
  `Section_15_Profile_*` 카드의 `3-1. Policy Guard` exact wording을 대체하지 않는다.
- named notable card의 `Policy Guard / Separation Guard`와 operational profile의 `3-1. Policy Guard`는
  parallel but non-substitutable layer로 유지한다.
- subline 확장까지 내려간 경우에도
  exact operational guard wording authority는 각 `Section_15_Subline_Profile_*` 카드의
  `3-1. Policy Guard`에 남고, 이 synthesis는 그 wording source를 대체하지 않는다.
- representative `Port Authority / Black Auction / Gravewell / Counterfeit Workshop` pair는
  닫힌 subline 교차감사 샘플로 유지하고,
  이 synthesis는 그 closure 상태를 대륙 합성층에서만 참조한다.

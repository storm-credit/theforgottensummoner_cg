# Section 15 Named Notables Coverage Matrix

이 문서는 `15 Named Notables` 후보가
5대륙과 범대륙 확장축에 얼마나 분포했는지 보는 커버리지 표다.

## Coverage Table

| Area | Strong 15 Candidates | Verify Before 15 | Collision / Risk | Current Coverage |
|---|---|---|---|---|
| `에테르` | `엘다라` | `대런 크레센트`, `엘드린 문브링어`, `마르쿠스 레이븐펠 (phase3 anchor: 맥스웰 레이븐펠)`, `이사도르 템페스트`, `세리오스 벤타리스`, `네리사 블러드위버`, `다미엔 이클립스`, `칼리스트`, `래퍼티 아르카디아`, `대사제 요한`, `엘라라 문힘`, `드라이덴 썬더루트`, `메라 라일윈드` | `탑주/핵심 인물표/성국 핵심 인물표 신호`, `Ravenfell/Corvus anchor split`, `Tempest/Solea split`, `금서 도서관/마나 공방/아스트라르 중앙 도서관/루멘 성채/잠든 정령의 숲 슬롯으로 보존` | `thin with strong place-institution slots; low-priority auxiliary closure complete` |
| `크림슨` | `울프가르 드래곤포지`, `에리온 드라코비스`, `오그마` | `벨라나 스톰브링어`, `아리안 블레이즈하트`, `드락사르 블레이즈포지`, `카사르 더 시어` | `벨라나 SS급`, `아리안 S급`, `드락사르/카사르 영웅록 신호` | `strong but boundary-adjusted` |
| `프로스트` |  | `울프릭`, `시그리드 프로스트하트`, `마리안 더 윈터콜러` | `대부분 14 전설/핵심 영웅 신호`, `원로 사냥꾼/묘지기 장로/대예언자/수석 기술자/별의 샤먼/아이스포지 병기소 장인 2차 narrowing 완료`, `오로라 평원/얼음무덤 언덕/아이스포지 병기소/빙하의 성소 슬롯으로 보존` | `thin with strong place-institution slots; frost unnamed slot closure complete` |
| `오벨리스크` |  | `바리온`, `카론`, `아이기스`, `베스 스크롤`, `이안 옵저버`, `카트린 라베로스`, `레보니아 셰이드`, `우로스 디 모르간`, `세르반 알테르만`, `레티시아 모르투스`, `렌 블랭크`, `라일 템플러`, `루가르 드 바네스카` | `아이기스 item/name collision`, `전설/히어로급/조직 핵심 신호 밀집`, `기록/관측/신성 기록소/묘역/경매장/서기관 slot은 role 유지`, `기억 지기 = 렌/라일`, `심연 계약 중개자 = 루가르 strong link` | `thin with dense boundary and archive slots; second obelisk narrowing complete` |
| `해양` |  | `미다스`, `해양 실비아`, `이소벨`, `마르코 바르텔로`, `엘레오노라 라 크루즈`, `골드핑거 바스`, `리나 웨이브서프`, `에릭 시스트롬`, `오렌`, `세일블레스 마리아`, `모로스` | `해양 실비아 name collision`, `대부분 A급/히어로급/제독/단장 신호`, `top five + city-role + tail unnamed pass 완료`, `심연 장부관은 이소벨 adjacency only`, `망자항해 기록관은 모로스 merge 금지 메모` | `thin with many boundary signals and strong place-institution slots; oceanic unnamed slot pass complete` |
| `범대륙 / 후기 확장` | `실비아` | `멜리산드르` | `키르케 계열은 후기 확장이라 우선순위 낮음` | `deferred` |

## Reading

- `크림슨`은 Named Notables가 가장 잘 보인다.
- `에테르`는 정령연합의 엘다라가 15 후보로 보이고, 마법협회 탑주/성국 도서관/정령 의식 슬롯이 강하지만 14번과 겹칠 위험이 커서 `verify_before_15`가 먼저다. 장소-기관 슬롯은 `Section_15_Ether_Place_Institution_Sidecar.md`로 보존하고, 표면명 기본값은 이미 잠갔다.
- `프로스트`는 후보가 거의 14 영웅표와 겹치지만, `오로라 평원`, `얼음무덤 언덕`, `푸른 폭풍 요새`, `아이스포지 병기소`, `빙하의 성소` 쪽의 장소-기관 슬롯이 강하다. `아이스포지 병기소 장인`까지 named holder 없이 닫혀 unnamed slot 6개 closure가 한 번 완료됐다.
- `해양`은 항해/연금/항구/암시장 명사 후보가 많지만, 현재 후보 대부분은 전설 영웅록, 제독, A급, 히어로급 신호가 강해 `verify_before_15`가 먼저다. `신탁 방주`, `해로 장부관`, `왕실 선공장 수석장`, `흑조 감정관`, `심연 장부관`, `항해사 길드장`, `마스터 쉽라이트`, `수석 기상관`, `대경매장 주인`, `은행장`, `세관장`, `수석 무역왕`, `스톰 체이서 대장`, `조선공 길드 장인`, `진혼 악기지기`, `망자항해 기록관`은 새 실명 없이 role slot으로 정리됐고, `모로스`, `이소벨`, `크리스토퍼 델마르` 같은 상위 named candidate와는 병합하지 않는다.
- `오벨리스크`는 금서/봉인/영혼/기록 명사 후보가 매우 많지만, 인물/아이템/전설 영웅/조직 핵심 충돌이 커서 `verify_before_15` 중심으로 둔다. 2차 narrowing까지 반영하면 `기록의 수호자`, `오벨리스크 관측대장`, `신성 기록소 관리 사제`, `묘역 감독관`, `기억 경매장 중개자`, `사후 서기관`은 role slot 유지, `기억 지기`는 `렌/라일` existing holder, `심연 계약 중개자`는 `루가르` strong-link verify 상태다.
- `범대륙`은 후기 확장축이라 메인 정리보다 뒤로 둔다.

## Next Search Priority

1. `5대륙 closure sync`: 프로스트 2차 narrowing까지 포함한 압축표 정합성 재점검
2. `오벨리스크`: 핵심 slot narrowing은 2차까지 닫힘. `렌/라일`, `루가르` strong-link note 유지
3. `해양`: unnamed slot pass는 완료. `모로스`, `이소벨`, `크리스토퍼 델마르` boundary-only 인접 유지
4. `에테르`: low-priority auxiliary slot 9개의 read-only closure 결과 동기화 완료

## Conductor Rule

커버리지가 얇은 대륙에 후보를 억지로 만들지 않는다.

먼저 기존 작업본에서 이름 있는 후보가 실제로 있는지 찾고,
없으면 `Operational Lines` 또는 `Institution Memory` 쪽으로 임시 보강한다.

현재 다음 1순위가 `5대륙 closure sync`인 이유:

- `오벨리스크`와 `해양`은 이미 핵심 narrowing이 닫혀 있고, `에테르`도 auxiliary closure sync가 끝났다.
- `프로스트`도 `아이스포지 병기소 장인`까지 같은 결로 닫혀 unnamed slot 6개 closure가 한 번 완료됐다.
- 이제 새 slot을 더 좁히는 것보다 5대륙 closure 상태를 같은 문구로 재확인하고 다음 ROI를 고르는 편이 효율이 높다.

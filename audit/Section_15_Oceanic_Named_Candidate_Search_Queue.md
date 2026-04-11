# Section 15 Oceanic Named Candidate Search Queue

이 문서는 해양 대륙의 `15 Named Notables` 후보를
어떤 named candidate 탐색 순서로 확인했는지 남기는 reference queue다.

## Rule

- 새 이름을 즉시 발명하지 않는다.
- 먼저 원본 참조 문서에서 실제 이름이 있는지 찾는다.
- A급, SS급, 히어로급, 제독, 단장 신호가 있으면 `14` 확인 전 15로 확정하지 않는다.
- 작업용 라벨과 표면명 후보를 분리한다.

## Priority Queue

| Priority | Search Slot | Preferred Display Label | Anchor Places | Search Terms | Routing Target | State |
|---|---|---|---|---|---|---|
| 1 | `수석 오라클` | `파도 신탁장` | `오라클 바지 / 신탁 방주` | `오라클`, `신탁`, `예언`, `Oracle`, `Barge` | `해양 -> 바다의 교단 / 오라클 바지` | `read_only_pass_done` |
| 2 | `항로 기록관 / 해도 보관인` | `해로 장부관 / 청해도 보관관` | `골든 앵커 하버`, `크로스윈드 포트` | `항로`, `해도`, `기록관`, `장부`, `Harbor`, `Chart` | `해양 -> 황금 함대 / 항해사 길드` | `read_only_pass_done` |
| 3 | `왕실 조선소 수석 공병` | `왕실 선공장 수석장` | `크로스윈드 포트 / 왕실 조선소` | `조선소`, `공병`, `전열함`, `선체`, `Shipyard`, `Engineer` | `해양 -> 왕실 조선소 / 조선공 길드` | `read_only_pass_done` |
| 4 | `장물 감정사 / 늙은 감정사` | `흑조 감정관` | `블랙워터 항구`, `붉은 해골 섬` | `감정사`, `장물`, `저주`, `진품`, `Appraiser` | `해양 -> 해적 연합 / 암시장 조합` | `read_only_pass_done` |
| 5 | `심해 금고 보관인` | `심연 장부관` | `볼트 오브 아우룸`, `Abyssal Vaults` | `금고`, `장부`, `아우룸`, `Vault`, `Abyssal` | `해양 -> 황금 함대 / 바다의 교단` | `read_only_pass_done` |
| 6 | `조선공 길드 장인` | `검은돛 선장인` | `폭풍의 만 / 검은 돛 조선소` | `조선공`, `장인`, `검은 돛`, `폭풍의 만` | `해양 -> 해적 연합 / 조선공 길드` | `read_only_pass_done` |
| 7 | `진혼의 합창단 악기 보관인` | `진혼 악기지기` | `고대의 악기실` | `진혼`, `합창단`, `악기`, `소라 고둥`, `Instrument` | `해양 -> 바다의 교단 / 성물 보관층` | `read_only_pass_done` |
| 8 | `죽은 선장의 항해일지 보관인` | `망자항해 기록관` | `유령선의 안식처` | `항해일지`, `죽은 선장`, `유령선`, `Logbook` | `해양 -> 해적 연합 / 유령선의 안식처` | `read_only_pass_done` |

## Boundary Names to Keep Separate

아래 인물은 명사형 가치가 있지만, 15 확정 전에 14 신호를 확인한다.

| Name | Why Hold | Related Slot |
|---|---|---|
| `미다스` | 전설/연금술/신화 축이 강함 | `심연 장부관`, `해로 장부관` 보조 참고 |
| `해양 실비아` | 이름 충돌이 큼 | `해로 장부관`, `파도 신탁장` 보조 참고 |
| `이소벨 골드리프` | SS급 재무 실권자 | `심연 장부관`, `아우룸 장부관` |
| `마르코 바르텔로` | 히어로급 상업 축 | `해로 장부관`, `대륙 상업망` |
| `엘레오노라 라 크루즈` | 거래 심판관 / 흑막 가능성 | `닻문서 서기관`, `해로 장부관` |
| `골드핑거 바스` | A급 암시장 조합장 | `흑조 감정관`, `밤항 선별관` |
| `리나 웨이브서프` | 히어로급 복원 학자 | `심연 장부관`, `진혼 악기지기` 보조 참고 |

## Search Order Snapshot

1. 해양 unnamed slot read-only pass는 여기서 1차 마감한다.
2. `모로스`, `크리스토퍼 델마르`, `이소벨 골드리프`는 slot holder가 아니라 boundary-only 인접 후보로 유지한다.
3. 이 큐는 더 이상 대륙 메인 본선을 재고정하지 않고, watch-reference 입력으로만 유지한다.

## Batch 01 Result

1차 검색 결과는 `Section_15_Oceanic_Search_Findings_Batch_01.md`에 둔다.

요약:

- `수석 오라클`은 직함만 확인되고 개인명은 아직 없다.
- `세일블레스 마리아`는 `오라클 바지`와 연결되지만 A급 제독이라 15 확정 금지다.
- `항해사 길드장`, `대경매장 주인`, `늙은 감정사`는 역할 슬롯으로 확인되지만 개인명은 아직 없다.
- `크리스토퍼 델마르`는 장물 금융/암시장 자금 축의 새 `new_boundary_candidate`로 등록할 필요가 있다.

## Batch 03 Result

3차 `top 5 slot` read-only pass 결과는 `Section_15_Oceanic_Search_Findings_Batch_03.md`에 둔다.

요약:

- `신탁 방주 / 파도 신탁장`은 `수석 오라클` 직함만 있고 direct holder 이름은 없다.
- `해로 장부관`은 `골든 앵커 하버`와 `크로스윈드 포트`의 항로/해도/보험 기능으로 role slot이 더 선명해졌지만 개인명은 없다.
- `왕실 선공장 수석장`, `흑조 감정관`도 실명 없이 핵심 실무 슬롯으로만 확인된다.
- `심연 장부관`은 direct keeper 이름은 없고, `이소벨 골드리프`라는 SS급 상위 재무 권력축만 인접한다.

## Batch 04 Result

4차 `city-role batch` 결과는 `Section_15_Oceanic_Search_Findings_Batch_04.md`에 둔다.

요약:

- `항해사 길드장`, `마스터 쉽라이트`, `수석 기상관`은 `크로스윈드 포트` 핵심 인물 슬롯 표에만 보이고 direct holder 이름은 없다.
- `대경매장 주인`, `은행장`, `세관장`은 `포트 아우렐리온` 핵심 인물 슬롯 표에만 보이고 direct holder 이름은 없다.
- `대경매장 주인`은 `크리스토퍼 델마르`와 병합하지 않는다.
- `은행장`은 `이소벨 골드리프`와 병합하지 않는다.

## Batch 05 Result

5차 `tail unnamed slot batch` 결과는 `Section_15_Oceanic_Search_Findings_Batch_05.md`에 둔다.

요약:

- `수석 무역왕`, `스톰 체이서 대장`, `조선공 길드 장인`, `진혼 악기지기`, `망자항해 기록관`은 모두 direct holder 없이 role slot으로 닫혔다.
- `모로스`의 항해일지 수집 문장은 남기되, `망자항해 기록관` direct holder로 병합하지 않는다.
- 따라서 해양 unnamed slot 회수는 `role slot 5`로 1차 마감한다.

## Conductor Note

이 큐는 `15번` 인물 생성표가 아니라 탐색표다.

실제 이름이 나오면 먼저 `14/15 boundary check`를 거치고,
그 뒤에만 `15 Named Notables` 후보로 올린다.

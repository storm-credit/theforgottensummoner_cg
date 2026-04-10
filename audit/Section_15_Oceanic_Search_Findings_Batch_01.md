# Section 15 Oceanic Search Findings Batch 01 Snapshot

이 문서는 `Section_15_Oceanic_Named_Candidate_Search_Queue.md`의
1차 검색 결과를 기록한다.

## Search Scope

검색 범위:

- `working/imports/phase4_section8_oceanic_church_of_sea`
- `working/imports/phase4_section8_oceanic_golden_armada`
- `working/imports/phase4_section8_oceanic_pirate_confederacy`

검색어:

- `오라클`, `신탁`, `Oracle`, `Barge`, `바지`
- `항로`, `해도`, `Navigator`, `골든 앵커`, `크로스윈드 포트`
- `감정사`, `장물`, `대경매장 주인`, `Appraiser`

## Batch Findings

| Search Slot | Result | State | Recorded Judgment |
|---|---|---|---|
| `수석 오라클 / 파도 신탁장` | `오라클 바지` 문서에 `수석 오라클` 직함과 `12명의 타이드워커`가 보이나 개인명은 확인되지 않음. | `no_named_candidate_yet` | 새 이름 발명 금지. `수석 오라클` 슬롯 유지. |
| `오라클 바지 관련 인물` | `세일블레스 마리아`가 `오라클 바지`와 연결되어 있으나 `A급`, `성스러운 함대 제독` 신호가 강함. | `verify_before_15` | 15 명사형 NPC가 아니라 14 경계 후보로 유지. |
| `항로 기록관 / 해로 장부관` | `골든 앵커 하버`에 항로 배치, 호위 스케줄, 보험 요율 결정 기능이 보이나 named officer는 확인되지 않음. | `no_named_candidate_yet` | 장소/기관 슬롯 유지. |
| `해도 보관인 / 청해도 보관관` | `크로스윈드 포트`에 `항해사 길드 본부`, `Navigator's Quarter`, `항해사 길드장` 역할이 보이나 개인명은 확인되지 않음. | `role_slot_confirmed` | `항해사 길드장`은 15 후보 슬롯으로 강함. 이름은 추가 검색 필요. |
| `장물 감정사 / 흑조 감정관` | `블랙워터 항구`에 `늙은 감정사`, `장물아비`, `유물 감정` 기능이 보이나 개인명은 확인되지 않음. | `role_slot_confirmed` | 감정관 슬롯은 강하지만 named candidate는 아직 없음. |
| `대경매장 주인 / 감정사` | `포트 아우렐리온`에 `대경매장 주인`이 모든 물건의 가치를 꿰뚫는 감정사로 보이나 개인명은 확인되지 않음. | `role_slot_confirmed` | `흑조 감정관`과 별도 경매장 계열 슬롯으로 보존 가능. |
| `장물 금융 / 암시장 처리` | `크리스토퍼 델마르`가 검은 동전, 도난품 장물 처리, 암시장 자금 담당자로 보임. | `new_boundary_candidate` | 이름 있는 명사 가치가 있으나 거상 연합 / 권력축 신호가 있어 14/15 경계 확인 필요. |

## Evidence Notes

- `오라클 바지`는 `떠다니는 예언선`의 구명칭을 가진 이동형 성소다.
- `수석 오라클`은 존재하지만, 검토한 import 범위에서는 개인명이 확인되지 않는다.
- `세일블레스 마리아`는 `오라클 바지`와 연결되지만 A급 제독이라 15 확정 금지다.
- `항해사 길드장`, `대경매장 주인`, `늙은 감정사`는 유명 NPC형 슬롯으로 쓸 수 있으나 아직 이름이 없다.
- `크리스토퍼 델마르`는 새로 보이는 named boundary candidate다.

## Queue Snapshot

후속 reference는 `크리스토퍼 델마르`, `대경매장 주인`, `항해사 길드장`을 중심으로 읽는다.

목표:

- `크리스토퍼 델마르`가 14 영웅표에 있는지 확인한다.
- `대경매장 주인`과 `늙은 감정사`가 같은 인물인지 분리한다.
- `항해사 길드장`의 이름이 다른 문서에 있는지 찾는다.

2차 결과:

- `Section_15_Oceanic_Search_Findings_Batch_02.md`에 기록한다.

## Routing Record

- `크리스토퍼 델마르`를 `Section_14_15_Boundary_Verification_Queue.md`에 `verify_before_15`로 등록한다.
- `Section_15_Named_Notables_Register.md`에는 `new boundary candidate`로 등록한다.
- `Section_15_Named_Notables_Anchor_Map.md`에는 `해양 -> 황금 함대 / 거상 연합` 앵커로 연결한다.

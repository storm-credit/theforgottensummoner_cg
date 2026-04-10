# Section 15 Obelisk Need Named Candidate Index

이 문서는 오벨리스크 대륙에서 개인명이 아직 확정되지 않은
유명 NPC형 역할 슬롯을 모아두는 색인이다.

named-candidate active 판단은
`Section_15_Named_Notables_Register.md`,
`Section_15_Named_Notables_Status_Compass.md`,
`Continuous_Workstream.md`
기준으로 읽는다.

## Rule

- 새 이름을 만들지 않는다.
- 심연/망자/초월 어휘를 표면에 과하게 올리지 않는다.
- 장소-기관 기능을 먼저 보존하고, 인물 확정은 나중으로 둔다.

## Slot Index

| Slot | Place / Institution Anchor | Function | State |
|---|---|---|---|
| `기록의 수호자` | `템플 오브 바운더리 / 봉인 수호단` | 봉인 기록, 전선 기록, 기록 유출 | `need_named_candidate_or_verify_beth` |
| `오벨리스크 관측대장` | `경계의 보루` | 흑오벨리스크 계측, 경보, 관측 자료 | `need_named_candidate_or_verify_ian` |
| `대봉인관 대행 / 원로 군관` | `봉인 수호단` | 공석 대봉인관 대리, 최전선 결단 | `keep_14_or_verify` |
| `신성 기록소 관리 사제` | `봉인의 수호자 / 신성 기록소` | 봉인 해제 코드, 금단 도면, 기록 유출 | `need_named_candidate / role_slot_confirmed` |
| `기억 지기` | `망각의 회랑 / 잊힌 자들의 연합` | 기억 크레딧, 망명자 동선, 구역 통치 | `verify_existing_holders_ren_ryle` |
| `기억 경매장 중개자` | `기억 경매장` | 이름, 잔향, 사후 권리 거래 | `need_named_candidate / role_slot_confirmed` |
| `사후 서기관` | `영원의 기록탑` | 기억 기록, 이름 맡김, 사후 기록 분류 | `need_named_candidate / role_slot_confirmed` |
| `묘역 감독관` | `네크로폴리스 프라임` | 기록관/관리인 통솔, 도시 실무층 | `need_named_candidate / role_slot_confirmed` |
| `심연 계약 중개자` | `심연의 장사꾼` | 영혼 담보 계약, 금단 유물 거래, 흑마술 지식 경매 | `need_named_candidate_or_verify_rugar / strong_link` |

## Routing Notes

오벨리스크 슬롯은 `인물`보다 `장소가 여는 장면`을 먼저 본다.

후속 reference 순서:

1. 장소-기관 앵커 유지.
2. 실제 개인명 확인.
3. 전설 영웅록/히어로급/조직 핵심 신호 확인.
4. 이름/아이템/마법명 충돌 확인.
5. 필요할 때만 15 Named Notables 후보로 승격.

## Read-Only Pass - Batch 01

- `기록의 수호자`는 `베스 스크롤`과 강하게 연결되지만 전용 유닛 문서가 `지도자 미정`이라 slot을 유지한다.
- `오벨리스크 관측대장`은 `이안 옵저버`와 강하게 연결되지만 전용 유닛 문서가 `지도자 미정`이라 slot을 유지한다.
- `기억 경매장 중개자`는 role slot confirmed로 유지하고 `타르갈`과 병합하지 않는다.
- `사후 서기관`은 role slot confirmed로 유지하고 `고르고스 페일`과 병합하지 않는다.

## Read-Only Pass - Batch 02

- `신성 기록소 관리 사제`는 `기록소 관리 사제들`이라는 plural role만 보이고 single named holder가 없어 role slot 유지다.
- `기억 지기`는 `렌 블랭크`, `라일 템플러` two-holder 구조가 직접 확인돼 새 이름 탐색보다 existing holder 연동이 우선이다.
- `묘역 감독관`은 `네크로폴리스 프라임` 계층도에만 보이고 direct named holder가 없어 role slot 유지다.
- `심연 계약 중개자`는 `루가르 드 바네스카`와 강하게 연결되지만, 이번 단계에서는 strong-link verify 메모만 남기고 direct final merge는 보류한다.

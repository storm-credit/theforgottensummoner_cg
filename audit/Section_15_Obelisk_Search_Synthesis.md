# Section 15 Obelisk Search Synthesis

이 문서는 오벨리스크 대륙의 `15 Named Notables` 후보와 역할 슬롯을 압축한 종합표다.

오벨리스크는 기록, 봉인, 기억, 망각, 영혼, 금서 축이 강하지만,
이름 있는 후보 대부분이 전설 영웅록, 히어로급, 조직 핵심, 인물/아이템명 충돌과 겹친다.

## Conductor Reading

오벨리스크에서는 새 15 확정자가 확인되지 않았다.

이 대륙은 인물 확정보다 장소-기관 슬롯 우선 정리가 안전한 것으로 정리됐다.
특히 신/심연/망자 어휘가 인간 서사를 밀어내지 않도록,
`기록`, `기억`, `거래`, `죄책감`, `망명`, `학술 암투` 기능으로 낮춰 읽는다.

## Stable 15 Candidate

안정 15 후보 없음.

## Verify Before 15

| Candidate | Anchor | Reason | State |
|---|---|---|---|
| `바리온` | `봉인 수호단` | 금서의 룬마스터, 룬의 집행관, 전설 영웅록 신호. | `verify_before_15` |
| `아이기스` | `봉인 수호단` | 절대 방벽의 현자. 인물명/성씨/방패/결계/아이템명 충돌. | `verify_before_15 / item_name_collision` |
| `카론` | `망자의 왕국 / 잊힌 자들의 전술 문서` | 원혼 인도자, 영혼의 목자, 전설/전술 반복 신호. | `verify_before_15` |
| `베스 스크롤` | `봉인 수호단 / 기록의 수호자` | B급, 서고단, 기록 수호자. | `verify_before_15` |
| `이안 옵저버` | `봉인 수호단 / 오벨리스크 관측대` | B급, 관측대장, 경계의 보루. | `verify_before_15` |
| `카트린 라베로스` | `잊힌 자들의 연합 / 고대 유산단` | 잊힌 서고의 학자, 암호와 함정 해제, 히어로급 신호. | `verify_before_15` |
| `레보니아 셰이드` | `잊힌 자들의 연합 / 망각의 조율자` | 언어학자, 거짓의 직조자, 히어로급 신호. | `verify_before_15` |
| `우로스 디 모르간` | `잊힌 자들의 연합 / 망각의 조율자` | 지식 강탈자, 도서관 침투, 조직 핵심 신호 가능성. | `verify_before_15` |
| `세르반 알테르만` | `망자의 왕국 / 망령의 손길` | 망자의 감시자, 영혼 착취관, 흑막 연구 조직 신호. | `verify_before_15` |
| `레티시아 모르투스` | `망자의 왕국 / 죽음의 행진단` | 망자의 학자, 사령 괴수 도감 제작, 사령 부대 핵심 신호. | `verify_before_15` |

## Need Named Candidate Slots

| Slot | Anchor | Function | State |
|---|---|---|---|
| `기록의 수호자` | `템플 오브 바운더리 / 봉인 수호단` | 전선 기록, 봉인 기록, 기록 유출 장면. | `need_named_candidate_or_verify_beth` |
| `오벨리스크 관측대장` | `경계의 보루` | 흑오벨리스크 계측, 경보 발령, 관측 자료 관리. | `need_named_candidate_or_verify_ian` |
| `대봉인관 대행 / 원로 군관` | `봉인 수호단` | 공석인 대봉인관을 대신하는 최전선 결단자. | `keep_14_or_verify` |
| `신성 기록소 관리 사제` | `봉인의 수호자 / 신성 기록소` | 봉인 해제 코드, 금단 도면, 기록 유출 훅. | `need_named_candidate / role_slot_confirmed` |
| `기억 지기` | `잊힌 자들의 연합 / 망각의 회랑` | 구역 통치, 자원 배분, 기억 크레딧과 망명 네트워크. | `verify_existing_holders_ren_ryle` |
| `기억 경매장 중개자` | `기억 경매장` | 영혼 계약, 사후 권리 계약, 이름/잔향 거래. | `need_named_candidate / role_slot_confirmed` |
| `사후 서기관` | `영원의 기록탑` | 기억 기록, 분류, 보관, 이름 맡김 체계. | `need_named_candidate / role_slot_confirmed` |
| `묘역 감독관` | `네크로폴리스 프라임` | 하위 기록관과 관리인을 통솔하는 도시 실무층. | `need_named_candidate / role_slot_confirmed` |
| `심연 계약 중개자` | `심연의 장사꾼` | 영혼 담보 계약, 금단 유물 거래, 흑마술 지식 경매. | `need_named_candidate_or_verify_rugar / strong_link` |

## Place / Institution Anchors

| Anchor | Function | Notable Use |
|---|---|---|
| `템플 오브 바운더리` | `memory_site`, `sanctuary` | 봉인 기록 열람, 전선 기록 보관, 기록 유출. |
| `경계의 보루` | `threshold`, `memory_site` | 관측탑, 경보실, 오벨리스크 상태 계측. |
| `기억 경매장` | `market`, `underworld_node` | 이름, 잔향, 사후 권리 거래. |
| `영원의 기록탑` | `memory_site` | 이름 보관, 사후 기록 분류, 기억 제의실. |
| `망각의 회랑` | `memory_site`, `underworld_node` | 거짓 기록 편집, 망명자 동선, 잊힌 이름의 흔적. |
| `그림자 도서관` | `memory_site`, `underworld_node` | 이단 지식, 사라진 기록, 학술 암투. |
| `봉인의 제단` | `memory_site`, `sanctuary` | 룬 해석, 방벽 시험, 봉인 장면. |

## Name / Term Collision Watch

| Cluster | Forms | Decision |
|---|---|---|
| `Aegis / 아이기스` | `아이기스`, `알렉산더 이지스`, `이지스 그림쉴드`, 방패/결계/유물명 | 인물명, 성씨, 아이템명, 결계명을 분리한다. |
| `심연의 인도자들` | 여러 암약 조직의 섹션 헤더 | 실제 15 분류명이 아니라 원본 문서 라벨로 취급한다. |

## Conductor Reading

오벨리스크는 인물 확정을 보류한다.

- 이름 있는 후보는 전원 `verify_before_15` 또는 충돌 감시.
- `기록의 수호자`, `오벨리스크 관측대장`은 `베스 / 이안`과 강한 연결 신호가 있지만, 전용 유닛 문서의 `지도자 미정` 상태 때문에 unresolved slot으로 유지한다.
- `신성 기록소 관리 사제`, `묘역 감독관`은 기능은 선명하지만 single named holder가 없어 role slot으로 유지한다.
- `기억 지기`는 `렌 / 라일` 복수 holder 구조가 source에 직접 확인돼 existing holder 연동으로 읽는다.
- `심연 계약 중개자`는 `루가르`와 강하게 연결되지만, verify link까지만 유지하는 것으로 정리됐다.
- `기억 경매장 중개자`, `사후 서기관`은 direct holder 없이 장소-기관 기능 role slot으로 유지한다.
- 인물 승격 여부와 별개로 `기록 / 기억 / 거래 / 죄책감 / 망명` 기능을 먼저 통과시킨다.

## Reference State Snapshot

오벨리스크 1차 narrowing과 핵심 slot 2차 narrowing은 모두 닫힌 상태로 유지한다.

이 문서는
mainline 개방용 실행표가 아니라,
이 2차 결과를 압축표와 진행표에서 참조하기 위한 종합표다.

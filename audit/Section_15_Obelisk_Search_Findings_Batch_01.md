# Section 15 Obelisk Search Findings Batch 01 Snapshot

이 문서는 오벨리스크 `15 Named Notables` 후보명 탐색의
1차 narrowing 결과를 기록한다.

## Search Scope

검색 범위:

- `working/imports/phase5_section8_obelisk_seal_wardens/봉인 수호단 (Seal Wardens).md`
- `working/imports/phase5_section8_obelisk_seal_wardens/3. 파벌 (Factions)/4. 서고단 파벌 (Library Order Detachment).md`
- `working/imports/phase5_section8_obelisk_seal_wardens/16. 예하 부대 및 기사단 (Military Units)/05. 기록의 수호자 (Keepers of the Record).md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/1. 주요 장소 (Locations)/거래소/기억 경매장 (Memory Auction House).md`
- `working/imports/phase5_section8_obelisk_kingdom_of_dead/망자의 왕국 (Kingdom of the Dead).md`
- `working/imports/phase5_section8_obelisk_kingdom_of_dead/1. 주요 장소 (Locations)/성지/영원의 기록탑 (Tower of Eternal Records).md`

집중 대상:

- `기록의 수호자`
- `오벨리스크 관측대장`
- `기억 경매장 중개자`
- `사후 서기관`

## Findings

| Search Slot | Best Anchor File(s) | Evidence Found | Recorded State | Recorded Judgment |
|---|---|---|---|---|
| `기록의 수호자` | `봉인 수호단 (Seal Wardens)`, `서고단 파벌 (Library Order Detachment)`, `기록의 수호자 (Keepers of the Record)` | `베스`가 `기록 수호자`로 직접 적히고 조직 리더로도 연결되지만, 전용 유닛 문서는 `지도자 미정 (TBD)`를 유지한다. | `role_slot_confirmed / verify_link_beth` | `베스 스크롤`과 연결 신호는 강하지만 direct named holder로 확정하지 않는다. slot은 유지하고 `need_named_candidate_or_verify_beth` 상태를 보존한다. |
| `오벨리스크 관측대장` | `봉인 수호단 (Seal Wardens)`, `서고단 파벌 (Library Order Detachment)`, `오벨리스크 관측대 (Obelisk Observers)` | `이안`이 `관측대장`으로 직접 적히고 관측대 리더로도 연결되지만, 전용 유닛 문서는 `지도자 미정 (TBD)`를 유지한다. | `role_slot_confirmed / verify_link_ian` | `이안 옵저버`와 연결 신호는 강하지만 direct named holder로 확정하지 않는다. slot은 유지하고 `need_named_candidate_or_verify_ian` 상태를 보존한다. |
| `기억 경매장 중개자` | `기억 경매장 (Memory Auction House)` | 영혼 계약, 사후 권리 계약, 기억 거래와 중개 기능은 강하지만 direct named broker는 없다. | `role_slot_confirmed` | role slot 유지. `타르갈`은 `본 마켓 관리부` 축이라 `기억 경매장 중개자`와 병합하지 않는다. |
| `사후 서기관` | `망자의 왕국 (Kingdom of the Dead)`, `영원의 기록탑 (Tower of Eternal Records)` | `사후 서기관`은 왕국 계층표와 기사단 급 역할로 확인되지만 holder는 `다수`다. | `role_slot_confirmed` | role slot 유지. `고르고스 페일`은 `기억 제의실` 실권자이지 generic scribe holder가 아니므로 병합하지 않는다. |

## Closure Evidence Summary

- `기록의 수호자`는 `베스 스크롤`과 강하게 연결되지만 direct holder로 닫지 않고 role slot으로 유지한다.
- `오벨리스크 관측대장`은 `이안 옵저버`와 강하게 연결되지만 direct holder로 닫지 않고 role slot으로 유지한다.
- `기억 경매장 중개자`는 direct named holder 없이 role slot으로 유지된다.
- `사후 서기관`은 다수 역할군으로만 확인돼 single named holder 없이 role slot으로 유지된다.

## Queue Snapshot

오벨리스크 1차 narrowing은 여기서 닫는다.

후속 reference는 아래 순서로 읽는다.

1. `기록의 수호자`, `오벨리스크 관측대장`을 `베스 / 이안`과 강하게 연결된 unresolved slot으로 index와 synthesis에 반영
2. `신성 기록소 관리 사제`, `기억 지기`, `묘역 감독관`, `심연 계약 중개자`를 다음 read-only narrowing batch로 이동
3. 실제 원고 입력 사례가 발생한 경우 해당 사례를 우선 검토 대상으로 둔다

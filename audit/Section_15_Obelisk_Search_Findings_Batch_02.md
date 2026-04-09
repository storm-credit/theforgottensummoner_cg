# Section 15 Obelisk Search Findings Batch 02

이 문서는 오벨리스크 `15 Named Notables` 후보명 탐색의
2차 narrowing 결과를 기록한다.

## Search Scope

검색 범위:

- `working/imports/phase5_section8_obelisk_seal_wardens/8. 경제 및 상업 (Economy & Commerce)/1. 봉인의 수호자 주요 교역로 및 무역 거점.md`
- `working/imports/phase5_section8_obelisk_seal_wardens/3. 파벌 (Factions)/2. 봉인의 사제단 (Priests of the Seal).md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance/잊힌 자들의 연합 (Forgotten Alliance).md`
- `working/imports/phase5_section8_obelisk_kingdom_of_dead/1. 주요 장소 (Locations)/도시/네크로폴리스 프라임 (Necropolis Prime).md`
- `working/imports/phase5_section8_obelisk_kingdom_of_dead/망자의 왕국 (Kingdom of the Dead).md`
- `working/imports/phase5_section8_obelisk_abyssal_legion/9. 내부 암약 조직 (Clandestine Organizations)/3. 심연의 장사꾼 (Abyssal Merchants)/1. 심연의 장사꾼 개요 및 강령.md`

집중 대상:

- `신성 기록소 관리 사제`
- `기억 지기`
- `묘역 감독관`
- `심연 계약 중개자`

## Findings

| Search Slot | Best Anchor File(s) | Evidence Found | Current State | Conductor Judgment |
|---|---|---|---|---|
| `신성 기록소 관리 사제` | `봉인의 수호자 주요 교역로 및 무역 거점`, `봉인의 사제단 (Priests of the Seal)` | `기록소 관리 사제들`과 `관리 사제`는 보이지만, `신성 기록소` 전용 single named holder는 없다. | `role_slot_confirmed` | role slot 유지. `대사제 엘리나`, `사제 미리아`, `예언자 세릴`, `클레멘스 브라이트`는 사제단/정화축 핵심 인물이지 `신성 기록소 관리 사제` direct holder로 병합하지 않는다. |
| `기억 지기` | `잊힌 자들의 연합 (Forgotten Alliance)` | `기억 지기 (Keepers)`가 각 구역 실질 통치자로 직접 적히고, 현 보유자가 `렌`, `라일`로 명시된다. | `role_class_with_existing_holders` | 새 이름이 필요한 slot이 아니라 복수 existing holder가 있는 역할군으로 읽는다. 단일 인물로 닫지 않고 `렌 블랭크 / 라일 템플러` verify 연동으로 잠근다. |
| `묘역 감독관` | `네크로폴리스 프라임 (Necropolis Prime)`, `망자의 왕국 (Kingdom of the Dead)` | 도시 계층도에 `묘역 감독관 -> 하위 기록관·관리인`이 직접 나오지만 개인명은 없다. 왕국 계급표의 `묘역 영주`, `기억 귀족`과는 층위가 다르다. | `role_slot_confirmed` | role slot 유지. `칼락`, `펠릭스`, `고르고스`와 병합하지 않는다. |
| `심연 계약 중개자` | `심연의 장사꾼 개요 및 강령` | 조직 기능으로 `심연 계약 중개 및 흑색 대출업`이 직접 적히고, `루가르 드 바네스카`가 `영혼의 대가를 담보로 하는 심연 계약을 협상하는 전문 타짜`로 명시된다. | `strong_verify_link_rugar` | `루가르`가 가장 강한 existing fit이다. 다만 이번 턴은 `15 확정`이나 direct holder 완전 봉합까지는 가지 않고 `need_named_candidate_or_verify_rugar`를 유지한 채 강연결 메모만 잠근다. |

## Closure Read

- `신성 기록소 관리 사제`는 plural/functional role만 보여 single named holder 없이 role slot으로 유지된다.
- `기억 지기`는 `렌`, `라일` two-holder 구조가 source에 직접 확인돼, 새 이름 탐색보다 existing holder 연동이 우선이다.
- `묘역 감독관`은 도시 실무층 role만 보이고 direct named holder가 없다.
- `심연 계약 중개자`는 `루가르`와 강하게 연결되지만, 이번 단계에서는 verify link까지로 두고 direct final merge는 보류한다.

## Next Search

오벨리스크 2차 narrowing은 여기서 닫는다.

다음 메인 판단은 아래 순서로 넘긴다.

1. `기억 지기`, `심연 계약 중개자`의 existing holder strong-link를 index와 synthesis에 반영
2. 오벨리스크 남은 핵심 slot의 closure read를 압축표와 진행표에 동기화
3. 필요 시 `프로스트` mainline 재평가

# Section 15 Frost Search Findings Batch 01

이 문서는 프로스트 `15 Named Notables` 후보명 탐색의
1차 narrowing 결과를 기록한다.

## Search Scope

검색 범위:

- `working/imports/phase3_section8_frost_frostborn_tribes/프로스트본 연합 (Frostborn Tribes).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/성지/2. 얼음무덤 언덕 (Ice Tomb Hill).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/성지/3. 오로라 평원 (Aurora Plains).md`
- `working/imports/phase3_section8_frost_frostborn_tribes/1. 주요 장소 (Locations)/요새/1. 푸른 폭풍 요새 (Blue Storm Citadel).md`

집중 대상:

- `전승 보존회 원로 사냥꾼`
- `묘지기 장로`
- `대예언자`
- `수석 기술자 / 드워프 장인`
- `별의 샤먼`

## Findings

| Search Slot | Best Anchor File(s) | Evidence Found | Current State | Conductor Judgment |
|---|---|---|---|---|
| `전승 보존회 원로 사냥꾼` | `프로스트본 연합 (Frostborn Tribes)` | `전승 보존회` 기능표에 `원로 사냥꾼`만 적히고 개인명은 없다. | `role_slot_confirmed` | role slot 유지. `울프릭`, `하랄드`, `칼리드`와 병합하지 않는다. |
| `묘지기 장로` | `얼음무덤 언덕 (Ice Tomb Hill)` | `묘지기 장로`는 기능 설명만 있고 named holder는 없다. 바로 아래 `스카디`는 별도 named individual이다. | `role_slot_confirmed` | role slot 유지. `스카디`와 병합하지 않는다. |
| `대예언자` | `오로라 평원 (Aurora Plains)` | `눈이 멀었지만 미래를 보는 노파`로만 적히고 개인명은 없다. | `role_slot_confirmed` | role slot 유지. `프리야`, `카이라`, `마리안`과 병합하지 않는다. |
| `수석 기술자 / 드워프 장인` | `푸른 폭풍 요새 (Blue Storm Citadel)` | `드워프 장인`이라는 역할만 있고 named holder는 없다. | `role_slot_confirmed` | role slot 유지. `시그리드`나 외부 불법 장인 축과 병합하지 않는다. |
| `별의 샤먼` | `오로라 평원 (Aurora Plains)` | `예언가들`이라는 복수 역할군으로 적히며 single named holder가 없다. | `role_slot_confirmed` | role slot 유지. 집단 의식/예언 전파 축으로만 보존한다. |

## Closure Read

- `전승 보존회 원로 사냥꾼`, `묘지기 장로`, `대예언자`, `수석 기술자`, `별의 샤먼`은 모두 direct named holder 없이 role slot으로 유지된다.
- `프로스트`는 이번 배치에서도 새 이름을 발명하지 않고, place-first slot pass를 유지한다.
- named boundary candidate인 `울프릭`, `시그리드`, `마리안`, `프리야`, `카이라`와는 병합하지 않는다.

## Next Search

프로스트 1차 narrowing은 여기서 닫는다.

다음 메인 판단은 아래 순서로 넘긴다.

1. `아이스포지 병기소 장인` read-only narrowing
2. 프로스트 closure 결과를 압축표와 진행표에 동기화
3. 필요 시 그 다음 대륙 우선순위 재평가

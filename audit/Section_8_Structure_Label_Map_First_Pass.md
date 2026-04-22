# Section 8 Structure Label Map - First Pass

이 문서는 `Section 8` canonical root 안에서
우선 라벨링할 핵심 세력들의 `section_style / mixed_keep / section_style_reclassify` 1차 판정을 모아둔 장부다.

## Input

- `audit/Section_8_Root_Label_Map.md`
- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Standard_Spine.md`
- `audit/Section_8_Status_Vocabulary_Guard.md`

## First Pass Table

| Candidate | Root Label | Continent Spine | Structure Label | Pressure State | Mismatch Watch | Current Handling |
|---|---|---|---|---|---|---|
| `성국 (Saint Haven)` | `canonical_root` | `state_house + guild_market` | `section_style` | `low` | `low` | 공통 섹션형 표준 샘플로 유지 |
| `왕국연합 (Allied Kingdoms)` | `canonical_root` | `state_house + guild_market` | `section_style` | `low` | `low` | 에테르 표준 section형 샘플로 유지 |
| `정령연합 (Spirit Union)` | `canonical_root` | `tribe_clan` only inside Ether | `mixed_keep` | `watch_keep` | `special_axis_generalization` | 에테르 공통 규칙과 분리된 예외축으로 유지 |
| `용의 후예 (Dragon Descendants)` | `canonical_root` | `tribe_clan + guild_market` | `section_style` | `watch_keep` | `clan_as_state_house` | 씨족 상층을 국가형 가문으로 과대 해석하지 않기 |
| `붉은 사막 부족 연합` | `canonical_root` | `tribe_clan + guild_market` | `mixed_keep` | `watch_keep` | `clan_as_state_house` | 부족 연합 구조와 거점 구조를 함께 점검 |
| `프로스트본 연합` | `canonical_root` | `tribe_clan + guild_market` | `mixed_keep` | `watch_keep` | `clan_as_state_house` | 클랜 구조와 요새/공방/성소 축을 분리 기록 |
| `황금 함대 (Golden Armada)` | `canonical_root` | `state_house + guild_market` | `section_style` | `low` | `low` | 해양 표준 section형 샘플로 유지 |
| `해적 연합 (Pirate Confederacy)` | `canonical_root` | `guild_market + thin state_house support` | `mixed_keep` | `watch_keep` | `port_power_as_tribe_clan` | 해적 가문/암시장/섬 거점 축을 함께 본다 |
| `바다의 교단 (Church of the Sea)` | `canonical_root` | `state_house adjacent / guild_market support` | `section_style_reclassify` | `place_pressure_strong` | `port_power_as_tribe_clan` | 루트 문법은 section형으로 읽고 성지/감시 요새 압력은 내용 메모로 분리 |
| `망자의 왕국 (Kingdom of the Dead)` | `canonical_root` | `frontier_survival + guild_market` | `section_style_reclassify` | `place_pressure_strong` | `nontraditional_elite_as_state_house` | 루트 문법은 section형으로 읽고 기억 귀족 과독만 따로 감시 |
| `잊힌 자들의 연합 (Forgotten Alliance)` | `canonical_root` | `frontier_survival + guild_market` | `section_style_reclassify` | `watch_keep` | `nontraditional_elite_as_state_house` | 공통 섹션형으로 읽되 가문 폴더를 정통 귀족 질서로 승격하지 않기 |
| `봉인 수호단 (Seal Wardens)` | `canonical_root` | `frontier_survival` | `section_style_reclassify` | `place_pressure_strong` | `mismatch_clear` | 루트 문법은 section형이며 보루/전선/제단 압력은 `place pressure strong`으로만 분리 기록 |

## Reading Rule

이 표는 아직 최종 확정표가 아니다.

이 단계에서는:

1. `section_style` 표준 샘플을 먼저 잠근다.
2. 장소 기능 압력은 구조 라벨이 아니라 pressure 상태로 보존한다.
3. `mixed_keep`는 예외 목록으로 올리고 재배치하지 않는다.
4. mismatch watch가 붙은 항목은 구조 수정 전에 추가 근거를 본다.
5. 상태어는 `Section_8_Status_Vocabulary_Guard.md` 기준으로만 쓴다.

## Round 1 Closure

`정령연합`과 `붉은 사막 부족 연합` 1차 재검토 결과는 아래처럼 잠근다.

1. `정령연합`
   - `mixed_keep`
   - 이유: 에테르 공통 규칙으로 일반화하면 안 되는 특수축
2. `붉은 사막 부족 연합`
   - `mixed_keep`
   - 이유: 부족 연합 구조와 생존 시장 구조가 함께 강함

따라서 다음 실제 재검토 우선순위는
`프로스트본 연합 -> 해적 연합 -> 잊힌 자들의 연합`이다.

## Round 2 Closure

`프로스트본 연합`과 `해적 연합` 1차 재검토 결과는 아래처럼 잠근다.

1. `프로스트본 연합`
   - `mixed_keep`
   - 이유: 클랜 정치가 본체지만 성소/묘역/요새/공방 네트워크가 함께 본체로 작동함
2. `해적 연합`
   - `mixed_keep`
   - 이유: 파벌 정치가 강하지만 항만/섬/암시장 네트워크도 세력 운용의 본체임

따라서 다음 실제 재검토 우선순위는
`잊힌 자들의 연합` 단독 심층 패스다.

## Round 3 Closure

`잊힌 자들의 연합` 재판정 결과는 아래처럼 잠근다.

1. `잊힌 자들의 연합`
   - `section_style_reclassify`
   - 이유: 장소 밀도는 강하지만 루트 문법은 공통 번호 섹션 중심이며,
     내용상 생존 연합 압력은 spine 해석으로 따로 보존하는 편이 정확함

따라서 `mixed_keep` 1차 재검토 사이클은 닫힌다.

## Round 4 Closure

`바다의 교단`, `망자의 왕국`, `봉인 수호단` 재확인 결과는 아래처럼 잠근다.

1. `바다의 교단`
   - `section_style_reclassify`
   - 이유: 성지/항로/감시 요새 압력은 강하지만 실제 루트 문법은 공통 번호 섹션이 먼저 선다
2. `망자의 왕국`
   - `section_style_reclassify`
   - 이유: 성채/시장/묘역 압력은 강하지만 실제 루트 문법은 공통 번호 섹션이 먼저 선다
3. `봉인 수호단`
   - `section_style_reclassify`
   - 이유: 장소 압력은 강하지만 place-pressure flattening 근거는 현재 없고, `place pressure strong` 메모로만 관리하는 편이 맞다

## Conductor Decision

다음 실제 작업은 이 표를 기준으로
`mixed_keep` 후보와 `mismatch watch` 후보를 우선 재확인하되,
구조 라벨과 `place pressure`를 같은 항목으로 섞지 않는 것이다.

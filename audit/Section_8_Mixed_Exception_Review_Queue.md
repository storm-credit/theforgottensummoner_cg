# Section 8 Mixed_Keep Exception Review Queue

이 문서는 `Section_8_Structure_Label_Map_First_Pass.md`에서
`mixed_keep`로 잠긴 후보를 따로 모아 재검토 순서를 고정하는 큐다.

## Input

- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Standard_Spine.md`
- `audit/Section_8_Status_Vocabulary_Guard.md`

## Review Principle

`mixed_keep`는 오류 확정이 아니다.

다만 아래 둘이 동시에 걸리면 우선 review backlog로만 올린다.

1. 공통 섹션형과 장소형이 함께 강하다.
2. 대륙 spine 오독 위험까지 같이 붙어 있다.

## Review Queue

| Priority | Candidate | Continent Spine | Mixed_Keep Reason | Mismatch Watch | Review Question | Status |
|---|---|---|---|---|---|---|
| 1 | `정령연합 (Spirit Union)` | `tribe_clan` inside Ether | 에테르 공통 section형과 다르게 부족 영역/자연권 구조가 강하다. | `special_axis_generalization` | 에테르 예외축 보존과 혼합 구조 세분 기준 | `reviewed_round1 / mixed_keep` |
| 2 | `붉은 사막 부족 연합` | `tribe_clan + guild_market` | 부족 연합 구조와 생존 거점/교역축이 함께 보인다. | `clan_as_state_house` | 부족 거점이 구조 중심인가, 공통 섹션형이 본체인가 | `reviewed_round1 / mixed_keep` |
| 3 | `프로스트본 연합` | `tribe_clan + guild_market` | 클랜 구조와 요새/공방/성소 앵커가 동시에 강하다. | `clan_as_state_house` | 클랜 섹션과 장소 네트워크 분리 기준 | `reviewed_round2 / mixed_keep` |
| 4 | `해적 연합 (Pirate Confederacy)` | `guild_market + thin state_house support` | 파벌 구조와 항만/암시장/섬 거점이 함께 강하다. | `port_power_as_tribe_clan` | 항만-거점 네트워크와 세력 섹션형 본체 판정 기준 | `reviewed_round2 / mixed_keep` |
| 5 | `잊힌 자들의 연합 (Forgotten Alliance)` | `frontier_survival + guild_market` | 가문 폴더와 생존 연합/시장 구조가 함께 걸린다. | `nontraditional_elite_as_state_house` | 가문 폴더와 생존 연합 구조 본체 판정 기준 | `reviewed_round3 / section_style_reclassify` |

## Stop Rules

- `mixed_keep` 후보는 재확인 전까지 이동/병합/정리 대상이 아니다.
- `mixed_keep`라는 이유만으로 오류 후보로 강등하지 않는다.
- 먼저 `의도된 예외`, `구조 오염`, `평탄화 위험` 중 무엇인지 분리한다.

## Conductor Decision

현재 큐의 1차 mixed_keep 재검토 사이클은 닫힌 것으로 본다.

정리:

1. `정령연합`, `붉은 사막 부족 연합`, `프로스트본 연합`, `해적 연합`은 `mixed_keep`
2. `잊힌 자들의 연합`은 `section_style_reclassify`

현재는
`Section_8_Spine_Mismatch_Queue.md` 기준의 확인도 닫힌 watch-reference로 유지하며,
재분류된 구조 라벨과 대륙 spine 해석이
서로 충돌 없이 유지되는지만 재점검한다.

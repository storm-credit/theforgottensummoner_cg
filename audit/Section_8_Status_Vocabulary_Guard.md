# Section 8 Status Vocabulary Guard

이 문서는 `Section 8` closure sync / watch-reference에서
같은 판단을 서로 다른 상태어로 부르는 drift를 막기 위한 기준표다.

핵심 원칙은 하나다.

`한 번 잠근 판정은 summary, queue, map, handoff에서 같은 어휘로 부른다.`

## Input

- `audit/Section_8_Normalization_Status_Compass.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Root_Corruption_First_Pass_A.md`
- `audit/Section_8_Root_Subtree_Sampling_Queue.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_A.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_B.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_C.md`
- `audit/Section_8_Place_Network_P2_Queue.md`
- `audit/Section_8_Place_Network_Handoff_Map.md`
- `audit/Section_8_Next_Audit_Targets.md`

## Canonical Status Set

### Structure States

- `section_style`
- `mixed_keep`
- `section_style_reclassify`

### Pressure States

- `low`
- `place_pressure_strong`
- `watch_keep`
- `handoff_applied`

### Mismatch Results

- `mismatch_keep`
- `mismatch_clear`

### Root States

- `canonical_root`
- `quarantine_root`
- `legacy_root / reference-only`

## Vocabulary Mapping

| Old / Drift Form | Canonical Form | Rule |
|---|---|---|
| `legacy_mixed` after closure | `mixed_keep` | 예외 유지가 잠긴 뒤에는 단순 legacy_mixed wording 대신 `mixed_keep`를 쓴다 |
| `tribe_to_state_overread` | `clan_as_state_house` | mismatch queue 기준 용어를 우선 사용한다 |
| `port_power_to_tribe_overread` | `port_power_as_tribe_clan` | mismatch queue 기준 용어를 우선 사용한다 |
| `survival_elite_to_house_overread` | `nontraditional_elite_as_state_house` | 오벨리스크 과독 범주를 queue 기준으로 통일한다 |
| `review_clear` | `mismatch_clear` | mismatch 종료 상태는 `mismatch_clear`로 통일한다 |
| `stable_with_watch` / `watch_locked` | `watch_keep` | summary 상태어에서는 감시 유지 상태를 `watch_keep`로 통일한다 |

## Conductor Rules

- 구조 라벨 본표는 closure 결과가 반영된 상태를 우선 적는다.
- mismatch 범주명은 언제나 `Section_8_Spine_Mismatch_Queue.md` 기준을 따른다.
- `place pressure strong`은 구조 라벨이 아니라 pressure 상태다.
- 이미 handoff가 끝난 항목은 `handoff_applied`로 summary에 남긴다.

## Conductor Decision

`Section 8` 문서 drift watch에서는
새 상태어를 발명하지 않고
이 표의 canonical set 안에서만 움직인다.

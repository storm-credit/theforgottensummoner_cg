# Section 8 Mixed_Keep Exception First Pass C

이 문서는 `Section_8_Mixed_Exception_Review_Queue.md`의
우선순위 5 항목인 `잊힌 자들의 연합`을
`spine 해석`과 `구조 라벨`을 분리해서 다시 읽은 재판정 시트다.

## Input

- `audit/Section_8_Mixed_Exception_Review_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Obelisk_Core_Faction_Layers.md`
- `working/imports/phase5_section8_obelisk_forgotten_alliance`
- `audit/Section_8_Status_Vocabulary_Guard.md`

## 1. Forgotten Alliance

### Reference Labels

- continent spine: `frontier_survival + guild_market`
- structure label: `mixed_keep`
- mismatch watch: `nontraditional_elite_as_state_house`

### Re-read

`잊힌 자들의 연합`은 내용상으로는
분명 `망명 네트워크`, `기억 거래`, `생존 연합`의 압력이 강하다.

하지만 이건 `spine 해석`이고,
구조 라벨과는 분리해서 읽어야 한다.

구조 기준에서 다시 보면 핵심은 세 가지다.

1. 루트가 `1. 주요 장소`, `2. 군사`, `3. 가문`, `4. 외교`,
   `5. 역사`, `6. 사회 및 정치`, `7. 법률 및 규범`, `8. 경제 및 상업`
   같은 공통 번호 섹션으로 정리돼 있다.
2. `잊힌 시장`, `베일드 바스티온`, `망각의 회랑` 같은 장소 압력은 강하지만,
   이 장소들이 루트 구조를 대체하는 place-pressure structure로 서 있지는 않다.
3. `3. 가문` 폴더가 보여도
   이건 `state_house strong` 근거가 아니라
   오벨리스크식 `nontraditional elite` 신호로 읽는 편이 맞다.

즉 이 세력이 `mixed_keep` 후보로 보였던 이유는
실제 구조가 섞여 있어서라기보다,
`frontier_survival` 내용 해석과 `가문 폴더` 신호가
한 문서 안에서 동시에 강했기 때문이다.

### Conductor Judgment

- 최종 1차 판단: `section_style_reclassify`
- 이유:
  - 구조 문법만 보면 공통 번호 섹션이 중심이므로 `section_style`이 맞다.
  - 장소 밀도는 강하지만, 이는 place-pressure structure가 아니라 `section_style 안의 강한 location density`로 기록하는 편이 정확하다.
  - 따라서 `mixed_keep`을 유지하기보다
    `section_style`로 내리고,
    대신 `nontraditional_elite_as_state_house` 감시를 유지하는 것이 더 정밀하다.

## First Pass Result

| Candidate | Previous Label | First Pass Result | Main Risk | Conductor Note |
|---|---|---|---|---|
| `잊힌 자들의 연합 (Forgotten Alliance)` | `legacy_mixed` | `section_style_reclassify` | `nontraditional_elite_as_state_house` | 구조는 section형으로 내리되 내용 해석은 오벨리스크 생존 연합 축으로 유지 |

## Conductor Decision

이번 재판정에서 잠그는 핵심은 아래 두 줄이다.

1. `잊힌 자들의 연합`의 spine 해석은 그대로 `frontier_survival + guild_market` 유지
2. 구조 라벨만 `legacy_mixed -> section_style_reclassify`로 내린다

따라서 앞으로는
`가문 폴더가 있으니 귀족국가형이다`도 아니고,
`장소가 강하니 mixed_keep을 유지해야 한다`도 아니다.

정확한 판정은
`section_style 구조 + frontier_survival 내용 본체 + nontraditional elite 경계 감시`
이다.

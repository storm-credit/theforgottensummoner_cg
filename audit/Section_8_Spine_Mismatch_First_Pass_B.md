# Section 8 Spine Mismatch First Pass B

이 문서는 `Section_8_Spine_Mismatch_Queue.md`의
우선순위 `P1` 후보 중
`Section_8_Spine_Mismatch_First_Pass_A.md` 이후 남은 항목을 다시 읽은 시트다.

대상은 아래 다섯이다.

1. `용의 후예`
2. `붉은 사막 부족 연합`
3. `바다의 교단`
4. `망자의 왕국`
5. `봉인 수호단`

## Input

- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Section_8_Spine_Mismatch_First_Pass_A.md`
- `audit/Section_8_Crimson_Notable_Anchor_Audit.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Obelisk_Core_Faction_Layers.md`

## 1. Dragon Descendants

### Risk

- risk category: `clan_as_state_house`
- current structure label: `section_style`
- current continent spine: `tribe_clan + guild_market`

### Mismatch Re-read

`용의 후예`의 핵심 위험은
`용혈 상층`, `명문 씨족`, `상층 혈통` 같은 표면 신호를 보고
국가형 가문 질서로 과승격하는 것이다.

하지만 현재 기준에서 잠기는 건 아래다.

1. 본체는 여전히 `tribe_clan strong`
2. 경제층은 `guild_market support`
3. `state_house`는 `thin`을 넘지 않는다

즉 이 세력의 mismatch는
루트 문법 문제가 아니라
`씨족형 지배층`을 `국가형 귀족`으로 읽는 내용 해석 과독을 막는 경계다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 운영 규칙:
  - `section_style` 구조는 그대로 둔다
  - `state_house strong` 승격은 막는다

## 2. Red Desert Tribes

### Risk

- risk category: `clan_as_state_house`
- current structure label: `mixed_keep`
- current continent spine: `tribe_clan + guild_market`

### Mismatch Re-read

`붉은 사막 부족 연합`의 핵심 위험은
`대부족장`, `상업 부족장`, `원로`, `연맹 회의`를 보고
부족 상층을 국가형 가문 질서로 밀어 올리는 것이다.

하지만 현재 기준에서 잠기는 건 아래다.

1. 본체는 `tribe_clan strong`
2. 생존 교역과 시장 운용이 `guild_market strong-support`로 붙는다
3. 혈연 기반 상층이 있어도 `state_house`는 `thin`까지만 허용한다

즉 이 세력의 mismatch는
혼합 구조 여부와 별개로
부족 연합의 지배층을 `정통 가문 정치`로 과독하지 않도록 막는 경계다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 운영 규칙:
  - `mixed_keep` 구조는 그대로 둔다
  - `state_house strong` 승격은 막는다

## 3. Church of the Sea

### Risk

- risk category: `port_power_as_tribe_clan`
- previous structure label: `place_style`
- root grammar re-read: `section_style`
- current continent spine: `state_house adjacent / guild_market support`

### Mismatch Re-read

`바다의 교단`의 핵심 위험은
성지, 해양 신앙, 항로 통제, 감시 요새를 한데 묶어
토착 해양 공동체 근거처럼 읽는 것이다.

하지만 현재 기준에서 잠기는 건 아래다.

1. 본체는 `교단 권위 + 감시 기관 + 항로 통제`다
2. 해양 spine에서는 `state_house adjacent / guild_market support`가 맞다
3. `성지`, `신탁`, `해상 감시`는 `place pressure strong`일 뿐
   `tribe_clan` 근거는 아니다

그리고 구조 라벨 쪽에서도
실제 루트 문법은 공통 번호 섹션이 먼저 서므로
`place_style`보다 `section_style`로 읽는 편이 더 정확하다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 구조 판정: `section_style_reclassify`
- 운영 규칙:
  - 루트 문법은 `section_style`로 읽는다
  - 성지/감시/신탁 네트워크는 `place pressure strong`으로만 기록한다
  - `파도 신앙 = tribe_clan` 승격은 금지한다

## 4. Kingdom of the Dead

### Risk

- risk category: `nontraditional_elite_as_state_house`
- previous structure label: `place_style`
- root grammar re-read: `section_style`
- current continent spine: `frontier_survival + guild_market`

### Mismatch Re-read

`망자의 왕국`의 핵심 위험은
`망자왕`, `기억 귀족`, `궁정`, `묘역 영주` 같은 표현을 보고
전통 귀족국가로 과승격하는 것이다.

하지만 현재 기준에서 잠기는 건 아래다.

1. 본체는 `frontier_survival + guild_market`
2. `망자왕 / 기억 귀족 / 궁정`은 `nontraditional elite` 신호다
3. 기억 저당, 본 마켓, 전선 유지 비용이
   전통 귀족 네트워크보다 먼저 읽혀야 한다

그리고 구조 라벨 쪽에서도
실제 루트 문법은 공통 번호 섹션이 먼저 서므로
`place_style`보다 `section_style`가 더 정확하다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 구조 판정: `section_style_reclassify`
- 운영 규칙:
  - 루트 문법은 `section_style`로 읽는다
  - 장소 압력은 `place pressure strong` 메모로만 남긴다
  - `state_house strong` 승격은 막는다

## 5. Seal Wardens

### Risk

- risk category: `place_style_flattened_to_section_style`
- previous structure label: `place_style`
- root grammar re-read: `section_style`
- current continent spine: `frontier_survival`

### Mismatch Re-read

`봉인 수호단`은 내용상
`경계의 보루`, `봉인의 제단`, `균열 지대`, `서플라이 포트` 같은
장소 압력이 강하다.

하지만 현재 루트에서 실제로 확인되는 건 아래다.

1. 최상단 문법은 공통 번호 섹션형이다
2. 장소 밀도는 높지만 `place_style`이 평탄화된 흔적은 확인되지 않는다
3. 따라서 여기서 관리해야 하는 건
   `place pressure strong`이지 `flattened mismatch`가 아니다

즉 이 세력은
장소 압력이 강한 `section_style` 세력이지,
현재 증거만으로는 `place_style`에서 잘못 눌린 사례가 아니다.

### Conductor Judgment

- 유지 판단: `mismatch_clear`
- 구조 판정: `section_style_reclassify`
- 운영 규칙:
  - 루트 문법은 `section_style`로 읽는다
  - 장소 압력은 `place pressure strong`으로만 따로 기록한다
  - 활성 `P1 mismatch` 목록에서는 내린다

## First Pass Result

| Candidate | Risk Category | Structure Result | Spine Reading | Mismatch Result | Conductor Note |
|---|---|---|---|---|---|
| `용의 후예` | `clan_as_state_house` | `section_style` | `tribe_clan + guild_market` | `mismatch_keep` | 용혈 상층과 씨족 지배층을 국가형 귀족으로 승격하지 않기 |
| `붉은 사막 부족 연합` | `clan_as_state_house` | `mixed_keep` | `tribe_clan + guild_market` | `mismatch_keep` | 부족장 상층과 상업 부족장을 정통 가문 정치로 읽지 않기 |
| `바다의 교단` | `port_power_as_tribe_clan` | `section_style_reclassify` | `state_house adjacent / guild_market support` | `mismatch_keep` | 성지/항로/교단 권위를 토착 공동체 근거로 읽지 않기 |
| `망자의 왕국` | `nontraditional_elite_as_state_house` | `section_style_reclassify` | `frontier_survival + guild_market` | `mismatch_keep` | 기억 귀족과 궁정 표현을 전통 귀족국가 근거로 승격하지 않기 |
| `봉인 수호단` | `place_style_flattened_to_section_style` | `section_style_reclassify` | `frontier_survival` | `mismatch_clear` | 장소 압력은 강하지만 flattening mismatch 증거는 현재 없음 |

## Conductor Decision

이번 패스에서 잠그는 핵심은 셋이다.

1. `clan_as_state_house`는 크림슨에서 계속 강한 `P1` 경계로 유지한다
2. `port_power_as_tribe_clan`, `nontraditional_elite_as_state_house`도 구조 라벨과 분리해 계속 감시한다
3. `봉인 수호단`은 `place pressure strong`과 `place_style`을 분리해
   active mismatch에서는 내리고 구조 라벨만 바로잡는다

따라서 남은 `P1 mismatch` 1차 사이클은 닫고,
다음 실제 패스는 `P0 root_corruption` 비교와
`P2 section_style_forced_on_place_network` 분리를 우선한다.

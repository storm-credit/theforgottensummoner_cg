# Section 8 Spine Mismatch First Pass A

이 문서는 `Section_8_Spine_Mismatch_Queue.md`의
우선순위 `P1` 후보 중
이번 mixed 재검토 사이클과 직접 연결된 항목을 다시 읽은 시트다.

대상은 아래 셋이다.

1. `프로스트본 연합`
2. `해적 연합`
3. `잊힌 자들의 연합`

## Input

- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Mixed_Exception_Review_Queue.md`
- `audit/Section_8_Mixed_Exception_First_Pass_B.md`
- `audit/Section_8_Mixed_Exception_First_Pass_C.md`
- `audit/Frost_Core_Faction_Layers.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Obelisk_Core_Faction_Layers.md`

## 1. Frostborn Tribes

### Risk

- risk category: `clan_as_state_house`
- current structure label: `mixed_keep`
- current continent spine: `tribe_clan + guild_market`

### Mismatch Re-read

프로스트본 연합의 핵심 위험은
`부족장`, `원로단`, `국왕급`, `후작급` 같은 표현을 보고
클랜 상층을 곧바로 정주 귀족 질서로 읽는 것이다.

하지만 현재 기준에서 잠기는 건 아래다.

1. 본체는 여전히 `tribe_clan`
2. 경제층은 `guild_market strong-support`
3. `state_house`는 `thin`을 넘지 않는다

즉 이 세력의 mismatch는
구조 라벨 문제가 아니라
`클랜 상층의 과승격`을 막는 내용 해석 경계다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 운영 규칙:
  - `mixed_keep` 구조는 그대로 둔다
  - `state_house strong` 승격은 막는다

## 2. Pirate Confederacy

### Risk

- risk category: `port_power_as_tribe_clan`
- current structure label: `mixed_keep`
- current continent spine: `guild_market + thin state_house support`

### Mismatch Re-read

해적 연합의 핵심 위험은
섬, 항구, 혈연, 파벌이라는 표면 신호를 묶어
토착 씨족 공동체 근거처럼 과독하는 것이다.

하지만 현재 기준에서 잠기는 건 아래다.

1. 본체는 `guild_market`
2. 파벌 정치가 `state_house thin-support`로 붙는다
3. 항만/암시장/정박지 네트워크는 강하지만 `tribe_clan` 근거는 아니다

즉 이 세력의 mismatch는
장소망이 강하다는 이유로
해양의 약한 `tribe_clan` 축을 허위로 키우는 위험이다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 운영 규칙:
  - `mixed_keep` 구조는 그대로 둔다
  - `항만 권력 = 부족 공동체` 해석은 금지한다

## 3. Forgotten Alliance

### Risk

- risk category: `nontraditional_elite_as_state_house`
- current structure label: `section_style_reclassify`
- current continent spine: `frontier_survival + guild_market`

### Mismatch Re-read

`잊힌 자들의 연합`은 이번 패스에서 구조 라벨이
`mixed -> section_style`로 내려갔다.

하지만 이 재분류가 곧
`가문 중심 국가형 구조`로 읽어도 된다는 뜻은 아니다.

현재 기준에서 잠기는 건 아래다.

1. 구조 문법은 `section_style`
2. 내용 본체는 `frontier_survival + guild_market`
3. `3. 가문` 폴더는 `nontraditional elite` 신호이지
   전통 귀족국가 증거가 아니다

즉 이 세력의 mismatch는
구조 라벨이 안정됐어도
내용 해석을 귀족국가 쪽으로 끌고 갈 위험이 계속 남는 경우다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 운영 규칙:
  - `section_style` 재분류는 유지한다
  - `state_house strong` 승격은 막는다

## First Pass Result

| Candidate | Risk Category | Structure Result | Spine Reading | Mismatch Result | Conductor Note |
|---|---|---|---|---|---|
| `프로스트본 연합` | `clan_as_state_house` | `mixed_keep` | `tribe_clan + guild_market` | `mismatch_keep` | 클랜 상층을 정주 귀족으로 승격하지 않기 |
| `해적 연합` | `port_power_as_tribe_clan` | `mixed_keep` | `guild_market + thin state_house support` | `mismatch_keep` | 항만/섬/암시장을 토착 씨족 근거로 읽지 않기 |
| `잊힌 자들의 연합` | `nontraditional_elite_as_state_house` | `section_style_reclassify` | `frontier_survival + guild_market` | `mismatch_keep` | 구조는 section형이지만 가문 폴더를 귀족국가 증거로 읽지 않기 |

## Conductor Decision

이번 mismatch 패스에서 잠그는 핵심은 하나다.

`구조 라벨이 안정돼도 대륙 spine 오독 위험은 별도로 계속 감시한다.`

따라서 다음 실제 패스는
`용의 후예`, `붉은 사막 부족 연합`, `바다의 교단`, `망자의 왕국`, `봉인 수호단`
중 어디를 먼저 읽을지 정하되,
우선순위는 `P1` 리스크 밀도 기준으로 잡는다.

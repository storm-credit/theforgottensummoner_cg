# Section 8 Mixed Exception First Pass B

이 문서는 `Section_8_Mixed_Exception_Review_Queue.md`의
우선순위 3~4 항목인 `프로스트본 연합`과 `해적 연합`을
실제 근거 기준으로 다시 읽은 1차 재검토 시트다.

## Input

- `audit/Section_8_Mixed_Exception_Review_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Frost_Core_Faction_Layers.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Section_8_Frost_Notable_Anchor_Audit.md`
- `audit/Section_15_Oceanic_Place_Institution_Sidecar.md`
- `working/imports/phase3_section8_frost_frostborn_tribes`
- `working/imports/phase4_section8_oceanic_pirate_confederacy`
- `audit/Section_8_Status_Vocabulary_Guard.md`

## 1. Frostborn Tribes

### Reference Labels

- continent spine: `tribe_clan + guild_market`
- structure label: `mixed_keep`
- mismatch watch: `clan_as_state_house`

### Re-read

프로스트본 연합은 프로스트 대륙의 대표 세력이지만,
그렇다고 단순한 `section_style` 표준 샘플로 접어버리기엔
장소 네트워크의 압력이 너무 강하다.

핵심은 세 가지다.

1. `대부족장 평의회`, `전사 부족장회`, `주술사 원로단`이
   분명한 클랜 정치의 본체다.
2. 동시에 `빙하의 성소`, `얼음무덤 언덕`, `오로라 평원`,
   `푸른 폭풍 요새`, `겨울회의 의장막`이
   단순 배경이 아니라 실제 권력과 기억, 의례, 보급을 나눠 가진다.
3. 경제층도 분명하지만,
   이것이 정주 국가형 귀족 질서로 올라가지는 않는다.

즉 `mixed`의 본질은 구조가 흐릿해서가 아니라,
`클랜 정치`와 `혹한 생존 장소망`이 동시에 본체로 작동하기 때문이다.

### Conductor Judgment

- 최종 1차 판단: `mixed_keep`
- 이유:
  - `section_style`로 내리면 성소/묘역/요새/공방이 담당하는
    장소 기능 압력이 지워진다.
  - `place_style`로 내리면 부족장 평의회와 클랜 상층이라는
    정치 본체가 약화된다.
  - 따라서 이 1차 판독에서는
    `tribe_clan core + place-network strong-support` 혼합 구조로 유지하는 것이 맞다.

## 2. Pirate Confederacy

### Reference Labels

- continent spine: `guild_market + thin state_house support`
- structure label: `mixed_keep`
- mismatch watch: `port_power_as_tribe_clan`

### Re-read

해적 연합은 해양 대륙 안에서 가장 쉽게 오독되는 세력이다.

겉으로는 `해적 가문`, `4대 파벌`, `해적 평의회`가 보여
공통 `section_style`로 접고 싶어지지만,
실제 운용은 항만과 섬, 암시장과 정박지의 네트워크가 같이 본체다.

핵심은 세 가지다.

1. `블랙워터`, `그림자`, `스칼렛`, `실버하트` 같은 파벌 정치가 강하다.
2. 동시에 `블랙워터 항구`, `붉은 해골 섬`, `유령선의 안식처`,
   `폭풍의 만`, `배신자의 항구`가 세력 기능을 분산 운영한다.
3. 이 구조는 토착 씨족 질서가 아니라
   `항만 권력 + 범죄-교역 질서`다.

즉 이 세력의 `mixed`는
파벌 구조와 해상 거점 네트워크가 함께 강해서 생긴 혼합이지,
부족 공동체가 강해서 생긴 혼합이 아니다.

### Conductor Judgment

- 최종 1차 판단: `mixed_keep`
- 이유:
  - `section_style`만 남기면 항만/암시장/섬 거점이 세력 본체라는 사실이 약화된다.
  - `place_style`만 남기면 파벌 정치와 선장 질서가 지워진다.
  - 따라서 이 1차 판독에서는
    `guild_market core + faction politics + port-network strong-support` 혼합 구조로 유지하는 것이 맞다.

## First Pass Result

| Candidate | Previous Label | First Pass Result | Main Risk | Conductor Note |
|---|---|---|---|---|
| `프로스트본 연합` | `mixed` | `mixed_keep` | `clan_as_state_house` | 클랜 정치와 성소/요새/묘역 네트워크를 함께 유지 |
| `해적 연합 (Pirate Confederacy)` | `mixed` | `mixed_keep` | `port_power_as_tribe_clan` | 파벌 정치와 항만/섬/암시장 네트워크를 함께 유지 |

## Conductor Decision

이번 1차 재검토에서도
둘 다 `mixed`를 해제하지 않는다.

대신 아래를 잠근다.

1. `프로스트본 연합`의 위험은 `클랜 상층을 정주 귀족 질서로 과승격하는 것`
2. `해적 연합`의 위험은 `항만-암시장 질서를 토착 씨족 증거로 과독하는 것`

후속 패스는
`잊힌 자들의 연합`을 같은 방식으로 읽되,
`가문 폴더`와 `생존 네트워크` 중 무엇이 구조 라벨을 더 강하게 끄는지
한 번 더 분리하는 것이다.

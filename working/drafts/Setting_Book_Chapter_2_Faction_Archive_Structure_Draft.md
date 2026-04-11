# Setting Book Chapter 2 - Faction Archive Structure Draft

이 장은 `8. 세력 아카이브`를 설정집 본문에서 어떻게 읽을지 정리하는 1차 초안이다.

핵심은 하나다.

세력 문서는 폴더 모양만 보고 판정하지 않는다.
대륙 spine, structure label, place pressure, root 상태를 분리해서 읽는다.

## 2.0 Reading Rule

`Section 8`은 세력, 기관, 집단, 사회 구조, 장소 기반 조직을 다룬다.

그러나 모든 세력이 같은 문법으로 서지는 않는다.

같은 번호 섹션 구조를 가져도
어떤 세력은 국가형 질서에 가깝고,
어떤 세력은 부족/씨족 질서에 가깝고,
어떤 세력은 장소 네트워크나 생존 인프라가 본체일 수 있다.

따라서 설정집에서는 아래 네 층을 분리한다.

1. Root state.
2. Continent spine.
3. Structure label.
4. Place pressure / handoff owner.

## 2.1 Root State

현재 root 상태는 아래처럼 읽는다.

| Root Type | Meaning | Setting Book Use |
|---|---|---|
| `canonical_root` | 현재 정본 판단의 기준으로 읽는 루트 | 본문 근거로 사용 가능 |
| `quarantine_root` | 손상되었거나 중복 의심이 있어 격리된 루트 | 직접 정본화 금지 |
| `legacy_root / reference-only` | 과거 작업 흔적, backup, 비교용 루트 | 참고만 허용 |

정본 루트 후보:

1. `01-8. 세력 아카이브 (국가·조직 정리).md`
2. `1. 에테르 대륙 (Ether Continent)`
3. `2. 크림슨 대륙 (Crimson Continent)`
4. `3. 프로스트 대륙 (Frost Continent)`
5. `4. 오벨리스크 대륙 (Obelisk Continent)`
6. `5. 해양 대륙 (Oceanic Continent)`
7. `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)`

격리 대상:

- `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))`
- `_Legacy_중립세력 (Backup)`

설정집 guard:

- 손상 루트와 legacy 루트는 멋진 표현이 있어도 자동 복귀시키지 않는다.
- 이름이 비슷해도 부모 경로가 다르면 자동 병합하지 않는다.
- 삭제보다 격리와 reference-only 판정을 우선한다.

## 2.2 Continent Spine

대륙 spine은 세력 구조를 읽는 기본 배경이다.

| Continent | Spine Read |
|---|---|
| `에테르` | `state_house + guild_market`, 단 정령연합 내부는 특수 부족축 |
| `크림슨` | `tribe_clan + guild_market` |
| `프로스트` | `tribe_clan + guild_market` |
| `오벨리스크` | `frontier_survival + guild_market`, `state_house`는 nontraditional elite only |
| `해양` | `state_house + guild_market`, tribe_clan은 약함 |

같은 폴더 모양이라도 대륙 spine이 다르면 같은 정규화 규칙으로 밀어붙이지 않는다.

예를 들어 크림슨과 프로스트의 씨족/부족 상층은
곧바로 전통 귀족국가형 가문층으로 올리지 않는다.

오벨리스크의 기억 귀족이나 망명 실권층도
전통 왕국 귀족으로 복원하지 않는다.

## 2.3 Structure Labels

설정집 본문에서 사용할 structure label은 아래로 제한한다.

| Label | Meaning |
|---|---|
| `section_style` | 공통 번호 섹션 문법이 먼저 선다 |
| `mixed_keep` | 구조 예외가 살아 있어 section/place를 성급히 접지 않는다 |
| `section_style_reclassify` | 루트 문법은 section형으로 읽되 내용 압력은 별도 보존한다 |

현재 주요 후보 snapshot:

| Candidate | Structure Label | Pressure / Watch |
|---|---|---|
| `성국` | `section_style` | `low` |
| `왕국연합` | `section_style` | `low` |
| `정령연합` | `mixed_keep` | `watch_keep`, 에테르 특수축 |
| `용의 후예` | `section_style` | `watch_keep`, clan_as_state_house 주의 |
| `붉은 사막 부족 연합` | `mixed_keep` | `watch_keep` |
| `프로스트본 연합` | `mixed_keep` | `watch_keep` |
| `황금 함대` | `section_style` | `low` |
| `해적 연합` | `mixed_keep` | `watch_keep` |
| `바다의 교단` | `section_style_reclassify` | `place_pressure_strong` |
| `망자의 왕국` | `section_style_reclassify` | `place_pressure_strong` |
| `잊힌 자들의 연합` | `section_style_reclassify` | `watch_keep` |
| `봉인 수호단` | `section_style_reclassify` | `place_pressure_strong` |

설정집 guard:

- `mixed_keep`는 미완성 오류가 아니라 살아 있는 구조 예외다.
- `section_style_reclassify`는 내용 압력이 사라졌다는 뜻이 아니다.
- `place_pressure_strong`은 structure label이 아니라 pressure state다.

## 2.4 Mismatch Watch

아래 mismatch는 설정집 본문에서 과독하지 않는다.

| Risk | Safe Reading |
|---|---|
| `clan_as_state_house` | 씨족 상층을 국가형 귀족으로 과대 해석하지 않는다 |
| `port_power_as_tribe_clan` | 항만 권력, 함대, 교단을 tribe_clan 근거로 올리지 않는다 |
| `nontraditional_elite_as_state_house` | 기억 귀족, 망명 지배층을 state_house strong으로 올리지 않는다 |
| `place_style_flattened_to_section_style` | 장소 기능이 강한 세력을 억지로 section형으로 평탄화하지 않는다 |
| `root_corruption` | 손상 루트를 활성 판단에 섞지 않는다 |

`mismatch_clear`는 구조 오해가 해소됐다는 뜻이지,
장소 압력이나 기능 압력이 사라졌다는 뜻은 아니다.

## 2.5 Place Pressure / Handoff

place pressure는 구조 라벨 문서 안에 가두지 않는다.

장소와 기관이 실제 서사 기능을 강하게 갖는 경우,
주 기록처를 sidecar나 register로 넘긴다.

현재 주요 handoff:

| Candidate / Family | Primary Owner | Rule |
|---|---|---|
| `바다의 교단` | `Section_15_Oceanic_Place_Institution_Sidecar.md` | 교단의 place-institution pressure는 해양 sidecar가 주 기록처다 |
| `오로라 평원`, `빙하의 성소` | `Section_15_Frost_Place_Institution_Sidecar.md` | 프로스트 sidecar가 장소 압력 본체다 |
| `본 마켓` 계열 | `Section_15_Obelisk_Place_Institution_Sidecar.md` | 오벨리스크 보급/기억 거래 거점은 sidecar가 주 기록처다 |
| `잊힌 자들의 연합` exile-network pressure | `FS_Place_Function_Register.md` | 망명 네트워크 압력은 register가 주 기록처다 |

설정집 본문에서는 이 압력을 세력 본체 승인 논리로 역수입하지 않는다.

## 2.6 Section 8 -> 15 Handoff

`Section 8`에서 확인한 세력 / 장소 / 기관 압력은
`Section 15` Named Notables나 Operational Lines로 넘어갈 수 있다.

하지만 이 handoff는 새 인물 확장 명령이 아니다.

현재 본선은 `closure sync / watch-reference`다.

따라서:

- 새 후보를 늘리기보다 잠긴 결과가 서로 같은 현재 시점을 가리키는지 먼저 본다.
- `source_check_hold`, `deferred_expansion_hold`, `stable_15_workset` 상태는 Section 15 상태어 기준을 따른다.
- 하위 operational profile의 `3-1. Policy Guard`는 상위 summary가 덮어쓰지 않는다.

## 2.7 Setting Book Use

설정집 본문에서 `Section 8`을 쓸 때는 아래 순서를 따른다.

1. 대륙 spine을 먼저 본다.
2. root state를 확인한다.
3. structure label을 확인한다.
4. place pressure가 있으면 handoff owner를 확인한다.
5. mismatch watch를 통과한 safe read만 본문에 쓴다.
6. legacy / quarantine root는 appendix나 reference note로만 둔다.

## 2.8 Chapter Lock

이 장에서 고정하는 기준은 아래다.

- `Section 8`은 세력 문법과 장소 압력을 분리해서 읽는다.
- `canonical_root / quarantine_root / legacy_root`를 활성 판단에서 섞지 않는다.
- `mixed_keep`는 살아 있는 구조 예외다.
- `place_pressure_strong`은 구조 라벨이 아니다.
- `Section 8 -> 15`는 새 후보 확장이 아니라 `closure sync / watch-reference` 정합성 유지가 우선이다.
- 다음 장인 `3. Named Notables / Operational Lines`는 이 handoff 규칙을 넘지 않는다.

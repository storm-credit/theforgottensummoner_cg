# Section 8 Structure Labeling Queue

이 문서는 `Section 8` 세력 경로를
처음에는 legacy three-way structure-label queue였고,
closure 이후에는 `section_style / mixed_keep / section_style_reclassify`
체계로 읽는 reference 큐다.

## Input

- `audit/Section_8_Root_Label_Map.md`
- `audit/Section_8_Root_Normalization_Plan.md`
- `audit/Section_8_Standard_Spine.md`
- `audit/Ether_Core_Faction_Layers.md`
- `audit/Section_8_Crimson_Notable_Anchor_Audit.md`
- `audit/Frost_Core_Faction_Layers.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Obelisk_Core_Faction_Layers.md`

## Structure Labels

### 1. `section_style`

- 공통 번호 섹션이나 정형 파트가 구조의 중심인 경우
- 예: 가문, 경제, 내부 조직, 생활양식 같은 공통 섹션이 세력 문서 안에서 주축인 경우
- 기본 처리:
  - spine 라벨과 함께 읽기 쉽다
  - 정규화 우선순위가 높다

### 2. Place-Pressure Candidate Test

- 도시, 항구, 요새, 성소, 시장, 보루 같은 실제 장소 하위 구조가 중심인 경우
- 예: 장소 기능과 공간 이동이 세력 구조를 실질적으로 이끄는 경우
- 기본 처리:
  - 억지로 `section_style`로 평탄화하지 않는다
  - 장소 기능 장부와 같이 본다

### 3. Mixed_Keep Exception After Closure

- 공통 섹션 구조와 실제 장소 구조가 함께 섞여 있는 경우
- 즉시 재배치하지 않고 예외 목록으로 먼저 올린다
- 기본 처리:
  - `mixed_keep` exception으로 잠근 뒤
  - spine mismatch 여부를 따로 점검한다

## First-Pass Candidate Examples

| Candidate | Continent Spine | Structure Label | Why |
|---|---|---|---|
| `성국 (Saint Haven)` | `state_house + guild_market` | `section_style` candidate | 가문, 정치, 종교, 도시 질서가 공통 섹션형으로 읽히는 축이다. |
| `왕국연합 (Allied Kingdoms)` | `state_house + guild_market` | `section_style` candidate | 봉건 귀족, 상업 귀족, 국경 방어 같은 정형 파트 읽기가 자연스럽다. |
| `정령연합 (Spirit Union)` | `tribe_clan` inside Ether | `mixed_keep` candidate | 부족 영역과 자연권 구조가 강해 일반 에테르 section형과 분리해서 봐야 한다. |
| `용의 후예 (Dragon Descendants)` | `tribe_clan + guild_market` | `section_style` candidate | 씨족 상층, 상인 연합, 경제 축이 세력 중심으로 먼저 읽힌다. |
| `붉은 사막 부족 연합` | `tribe_clan + guild_market` | `mixed_keep` candidate | 부족 연합 구조와 실제 생존 거점/교역축이 함께 걸릴 가능성이 높다. |
| `프로스트본 연합` | `tribe_clan + guild_market` | `mixed_keep` candidate | 클랜 구조와 요새/공방/성소 축이 동시에 강하다. |
| `황금 함대 (Golden Armada)` | `state_house + guild_market` | `section_style` candidate | 가문, 함대, 무역 의회, 재정 구조가 세력 중심으로 먼저 읽힌다. |
| `해적 연합 (Pirate Confederacy)` | `guild_market + thin state_house support` | `mixed_keep` candidate | 파벌 구조와 항만/암시장/섬 거점 축이 함께 엮인다. |
| `바다의 교단 (Church of the Sea)` | `state_house adjacent / guild_market support` | `section_style_reclassify` candidate | 루트 문법은 공통 번호 섹션형이지만 성지, 감시 요새, 해상 신앙 거점 압력은 별도 메모가 필요하다. |
| `망자의 왕국 (Kingdom of the Dead)` | `frontier_survival + guild_market` | `section_style_reclassify` candidate | 루트 문법은 공통 번호 섹션형이고, 성채/시장/묘역 압력은 내용 해석으로 분리하는 편이 맞다. |
| `잊힌 자들의 연합 (Forgotten Alliance)` | `frontier_survival + guild_market` | `section_style_reclassify` candidate | 내용상 생존 연합과 시장/망명 구조는 강하지만 루트 문법은 공통 섹션형이 더 강하다. |
| `봉인 수호단 (Seal Wardens)` | `frontier_survival` | `section_style_reclassify` candidate | 루트 문법은 공통 번호 섹션형이며, 보루/제단/균열 지대 압력은 `place pressure strong` 메모로 따로 관리한다. |

## Labeling Order

1. `canonical_root`만 먼저 라벨링한다.
2. `quarantine_root`, `legacy_root`는 비교 샘플로만 본다.
3. `mixed_keep`는 구조 예외 목록으로 먼저 올린다.
4. `mixed_keep`를 곧바로 정리하지 않고 `spine_mismatch` 여부를 같이 본다.

## Stop Rules

- place-pressure candidate를 억지로 `section_style`로 바꾸지 않는다.
- `mixed_keep` 확인 전에는 폴더 이동이나 병합을 하지 않는다.
- 대륙 spine과 어긋나는 구조가 보여도 먼저 `의도된 예외`인지 확인한다.

## Round 4 Closure

`바다의 교단`, `망자의 왕국`, `봉인 수호단` 재확인 결과는 아래처럼 잠근다.

1. `바다의 교단`
   - `section_style_reclassify`
   - 이유: 성지/감시 요새 압력은 강하지만 실제 루트 문법은 공통 번호 섹션이 먼저 선다
2. `망자의 왕국`
   - `section_style_reclassify`
   - 이유: 성채/시장/묘역 압력은 강하지만 실제 루트 문법은 공통 번호 섹션이 먼저 선다
3. `봉인 수호단`
   - `section_style_reclassify`
   - 이유: 장소 압력은 강하지만 legacy place-style flattening 증거는 현재 없고, `place pressure strong`으로만 관리하는 편이 정확하다

## Conductor Decision

현재는 이 큐를 새 라벨 부여 작업으로 다시 열지 않고,
`Section_8_Structure_Label_Map_First_Pass.md`의
`section_style / mixed_keep / section_style_reclassify` closure를 확인하는
reference로만 유지한다.

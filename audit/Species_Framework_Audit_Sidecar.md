# Species Framework Audit Sidecar

이 문서는 `종족` 관련 설정을 바로 정본화하지 않고,
기존 문서에 흩어진 단서를 안전하게 모아
`종족 / 혈통 / 상태 / 몬스터`를 분리해 읽기 위한 병렬 감사용 sidecar다.

이 단계에서는 메인 `14/15`, `People Worth Seeking`, `FS Lore Engine` 본선에
강제 반영하지 않는다.

## Purpose

- 판타지 소설/영화에서 흔한 종족군을 나중에 흡수할 수 있는 큰 그릇을 먼저 만든다.
- 이미 문서에 등장한 `하이엘프`, `드워프 장인`, `수인 부족`, `혈통`, `정령화`, `언데드` 같은 조각을 같은 층위로 오독하지 않게 한다.
- `하피`, `라미아`, `해양 종`, `용인`, `요정`, `거인` 같은 후보를 나중에 넣어도 구조가 안 깨지게 한다.

## Non-Goals

- 아직 개별 종족을 정본으로 확정하지 않는다.
- 아직 대륙별 인구 분포표나 종족 우열 체계를 만들지 않는다.
- 아직 `언데드`, `정령화`, `축복 혈통`, `저주 변이`를 종족으로 승격하지 않는다.

## Core Classification

### 1. Race / People

공동체, 거주권, 언어, 외교, 생활권, 씨족/왕국/부족 구조가 있을 때 쓴다.

예:

- `엘프`, `드워프`, `수인 부족`, `해양 종`, `하피족`, `라미아 씨족`

### 2. Bloodline / Lineage

독립 종족이 아니라,
가문/후계/혼혈/축복/저주 계보처럼
개체나 가문에 붙는 혈통 신호일 때 쓴다.

예:

- `용의 피`, `고대 혈통`, `하프 엘프`, `왕가 계보`

### 3. State / Transformation

원래는 다른 종이었지만
정령화, 언데드화, 저주, 변이, 봉인, 부패 같은 변화 상태일 때 쓴다.

예:

- `언데드`, `정령화`, `반정령화`, `저주 변이`, `망령화`

### 4. Monster / Ecological Entity

사회와 외교보다 생태, 던전, 사냥, 재료, 위협 개체성이 중심일 때 쓴다.

예:

- 야생 하피 개체군
- 유적 수호 라미아 개체
- 화염 거인, 정령 개체, 괴수 군체

## Layered Intake Card

종족 감사는 단일 `race` 필드로 처리하지 않고,
아래 층을 겹쳐 읽는 intake card 방식으로 본다.

1. `Base kind`: people/species, spirit entity, artificial entity, monster/beast
2. `Heritage`: bloodline, hybrid ancestry, touched lineage, descended line
3. `State`: undead, cursed, ascended, possessed, corrupted, petrified
4. `Social anchor`: kingdom, tribe, clan, union, order, cult, guild
5. `Ecology role`: citizen, wild, summoned, war-beast, corrupted fauna
6. `Canon tier`: hard, soft, open question, rumor

주의:

- `국가/부족/연합`은 사회 앵커이지 자동으로 종족이 아니다.
- `혼혈`과 `용의 피`는 기본값이 `heritage`다.
- `언데드 왕국`처럼 사회 구조가 있어도, 그 기반이 `state`인지 `race`인지 따로 읽어야 한다.

## Broad Intake Families

아래 축은 지금 당장 다 확정하는 표가 아니라,
나중에 개별 후보를 받아 넣을 수 있는 상위 카테고리다.

| Family | Reading Snapshot | Status |
|---|---|---|
| `인간계` | 기본 인구축 | `implicit_core` |
| `장생종` | 엘프, 하이엘프, 다크엘프류 수용 | `open_family` |
| `광산/장인종` | 드워프, 포지 계열 수용 | `open_family` |
| `수인/야수인계` | 수인 부족, 야수형 공동체 수용 | `open_family` |
| `조익/익인계` | 하피, 조익인, 조류형 인외 공동체 수용 | `reserved_family` |
| `사행/반수반인계` | 라미아, 나가류 수용 | `reserved_family` |
| `용계/비늘계` | 용인, 드래곤 블러드, 비늘 계열 수용 | `reserved_family` |
| `거인계` | 거인족, 반거인, 태고 거체 민속 수용 | `reserved_family` |
| `소형/요정계` | 페어리, 픽시, 요정, 노움류 수용 | `reserved_family` |
| `수중/해양계` | 인어형, 해수 수인형, 심해 적응 공동체 수용 | `reserved_family` |
| `정령 인접 공동체` | 정령과 계약하거나 가까운 공동체 | `reserved_family` |
| `이계/천상/심연계` | 악마, 천사, 외계 존재류 수용 | `reserved_family` |

주의:

- `정령` 자체는 개체/존재/소환체일 가능성이 커서, 곧바로 `종족`으로 고정하지 않는다.
- `언데드`는 기본적으로 `state/transformation`으로 읽고, 독립 사회 구조가 반복 확인될 때만 별도 검토한다.

## Evidence Already In Canon Snapshot

| Signal | Reading Snapshot | File Evidence | Temporary Class |
|---|---|---|---|
| `하이엘프` | 엘다라 개별 사례에서 장생종 단서 확인 | `Section_15_Named_Notable_Eldara.md` | `race_signal / not_globalized` |
| `드워프 장인` | 프로스트 장인 슬롯에서 반복 | `FS_Place_Function_Register.md`, `FS_Slot_Maturation_Register.md` | `race_signal / slot_bound` |
| `수인 부족` | 정령연합 부족층 구조 암시 | `Ether_Core_Faction_Layers.md` | `race_signal / faction_bound` |
| `혈통 / 계보` | 이미 handoff와 reveal control에서 separate field로 존재 | `FS_Story_to_Lore_Handoff_Gate.md`, `FS_Reveal_Control_Register.md` | `bloodline_axis_exists` |
| `언데드 / 정령화` | 상태/변질로 읽어야 하는 사례가 많음 | `working/imports` 다수, `FS_Story_to_Lore_Handoff_Gate.md` | `state_first` |

## First Anchor Readings

| Anchor | Safest Reading | Why |
|---|---|---|
| `정령연합 (Spirit Union)` | `composite polity`, not a race | 엘프, 드루이드, 수인 부족, 샤먼이 함께 들어간 연합체다. |
| `그린스톰 부족` | `beastfolk people + tribal polity` | 늑대수인/곰수인/여우수인과 자치권 서술이 직접 확인된다. |
| `용의 후예` | `polity + bloodline layer` | `Dragonborn`, `용혈 전사단`, 혼혈/용혈 서술이 강하다. |
| `망자의 왕국` | `polity built on state/transformation` | 사회 구조는 강하지만 핵심은 언데드 상태와 사령 통치다. |
| `해양 / merfolk signal` | `reserved_family / thin sovereign proof` | 인어/merfolk 신호는 보이지만 독자 문명권 확정 근거는 아직 얇다. |
| `하피 signal` | `monster/ecological or mutation first` | 현재는 뮤턴트/세트피스 성격이 강하고 문명종 근거가 약하다. |
| `라미아 / naga signal` | `open question` | 현 import층에서 사회 구조 근거가 아직 거의 안 잡힌다. |

## Reserved Candidate Families

아직 근거를 더 모아야 하지만,
지금부터 빈 슬롯으로는 열어 둘 가치가 있는 후보:

- `하피 / 조익인`
- `라미아 / 나가`
- `수중 / 바닷속 종`
- `용인 / 드래곤 블러드`
- `거인족`
- `요정 / 페어리`
- `오크 / 고블린`
- `정령과 공생하는 인외 공동체`

## Guardrails

- 새 종족을 정본으로 추가하기 전에 먼저 `race / bloodline / state / monster` 중 어디인지 분류한다.
- 사회 구조가 없으면 기본값은 `monster/ecological` 또는 `state`다.
- 혼혈, 축복, 저주, 계승은 기본값이 `bloodline/lineage`다.
- `언데드`, `정령화`, `반정령화`는 기본값이 `state/transformation`이다.
- `정령연합`, `프로스트본 연합`, `용의 후예`, `망자의 왕국` 같은 조직/국가/부족연합 이름은 기본값이 `social anchor`다.
- 메인 `14/15` 판정과 `People Worth Seeking` 라우팅은 이 sidecar만으로 바꾸지 않는다.

## Parallel Track Rule

이 sidecar는 메인선과 병렬로 굴린다.

- 메인선: `14/15`, `People Worth Seeking`, `place-first slot`, `handoff`
- 사이드트랙: 종족/혈통/상태/몬스터 프레임 감사
- 합류 조건: 사례 3건 이상 + 세력/장소/인물 충돌 점검 + 오케스트라 승인

## Side-Track Batch Snapshot

1. `하이엘프`, `드워프 장인`, `수인 부족`, `언데드`, `정령화`를 1차 anchor case로 고정
2. `하피`, `라미아`, `수중/해양계`, `용인`, `거인`, `요정`을 `reserved_family` 후보로만 열어 둠
3. `race / bloodline / state / monster` 혼선 사례를 risk register에 따로 기록

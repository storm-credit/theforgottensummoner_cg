# Section 8 Place Network P2 Queue

이 문서는 `Section_8_Spine_Mismatch_Queue.md`의
`section_style_forced_on_place_network` 위험을
구조 라벨과 분리해서 관리하기 위한 `P2` 큐다.

핵심 원칙은 단순하다.

- `structure label`은 루트/파일 문법으로 잡는다
- `place pressure`는 내용 압력으로 따로 적는다
- 둘을 섞지 않는다

## Input

- `audit/Section_8_Standard_Spine.md`
- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Oceanic_Core_Faction_Layers.md`
- `audit/Frost_Core_Faction_Layers.md`
- `audit/Obelisk_Core_Faction_Layers.md`
- `audit/Section_15_Oceanic_Place_Institution_Sidecar.md`
- `audit/Section_15_Frost_Place_Institution_Sidecar.md`
- `audit/Section_15_Obelisk_Place_Institution_Sidecar.md`
- `audit/Section_8_Frost_Notable_Anchor_Audit.md`
- `audit/FS_Place_Function_Register.md`

## Closed P2 Watch Table

| Candidate | Continent | Current Structure Read | Place Pressure | Why Not Promote To Structure Label | Primary Handoff Target |
|---|---|---|---|---|---|
| `바다의 교단` | `Oceanic` | `section_style_reclassify` | `sanctuary + route-control + watch-fort` | 성지와 감시 요새 압력은 강하지만 루트 문법은 section형이고, 이를 `place_style`로 올리면 교단 제도권 구조와 토착 공동체 신호가 섞인다 | `Section_15_Oceanic_Place_Institution_Sidecar.md` |
| `오로라 평원` | `Frost` | `anchor-led place pressure` | `memory_site + sanctuary` | 전승, 예언, 샤먼 압력이 강하지만 이를 프로스트 전체 구조 라벨로 일반화하면 `프로스트본 연합 = place_style` 오독이 생긴다 | `Section_15_Frost_Place_Institution_Sidecar.md` |
| `빙하의 성소` | `Frost` | `anchor-led place pressure` | `sanctuary + ritual-validation` | 성소 기능이 강하지만 세력 루트 문법을 대체하는 근거는 아니다 | `Section_15_Frost_Place_Institution_Sidecar.md` |
| `본 마켓` 계열 | `Obelisk` | `section-linked place pressure` | `market + supply + memory-trade` | 시장과 보급 거점 압력을 근거로 세력 전체를 `place_style`로 밀면 `frontier_survival + guild_market` spine이 흐려진다 | `Section_15_Obelisk_Place_Institution_Sidecar.md` |
| `잊힌 자들의 연합` | `Obelisk` | `section_style_reclassify` | `place_pressure_strong + exile_network_pressure` | 거점과 망명 네트워크가 강해도 실제 파일 문법은 번호 섹션형이고, 구조 라벨은 이미 `section_style_reclassify`로 잠겼다 | `FS_Place_Function_Register.md` |

## Watch Reading Rule

현재 이 큐는 새 구조 재분류가 아니라 아래 drift만 확인한다.

1. `place pressure`가 이미 잠긴 `structure label`을 흔들고 있지 않은가
2. sidecar/register ownership이 handoff map과 같은가
3. summary/status vocabulary가 `handoff_applied / watch_keep`를 유지하는가

## Conductor Rules

- `place-heavy content`와 `place-led structure`를 같은 뜻으로 쓰지 않는다.
- 루트/파일 문법이 section형이면 먼저 `section_style`로 잠긴 상태를 확인한다.
- 장소 압력이 강해도 대륙 spine 오독을 만들면 `P2`로 따로 관리한다.
- `P2` 후보는 구조 재분류보다 `side-note / register / anchor` 보존 상태를 먼저 확인한다.
- 이 큐는 source-of-truth가 아니라 handoff staging 문서다. 실제 소유권은 `Section_8_Place_Network_Handoff_Map.md`와 도착 문서에서 이미 잠긴 상태로 본다.

## Conductor Decision

현재 `P2` watch의 핵심은
`place pressure strong`이 구조 라벨과 분리되어 기록됐는지 확인하는 것이다.

즉 이 큐는
`place_style` 세력을 늘리기 위한 목록이 아니라,
`section_style` 세력 안에 숨어 있는 공간 압력을
서사/앵커/거점 장부에 안전하게 귀속됐는지 확인하기 위한 목록이다.

구체 handoff 경로는
`Section_8_Place_Network_Handoff_Map.md`에 고정되어 있다.

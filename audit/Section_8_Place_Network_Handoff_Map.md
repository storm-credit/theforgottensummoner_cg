# Section 8 Place Network Handoff Map

이 문서는 `Section_8_Place_Network_P2_Queue.md`에 올라온 후보를
어느 sidecar, register, anchor 문서로 넘길지 정리하는 handoff 표다.

핵심 원칙은 아래다.

1. `place pressure`는 구조 라벨 문서 안에 가두지 않는다
2. 다음 작업자는 후보를 보고 바로 연결 문서를 찾을 수 있어야 한다
3. `서사 운용`, `15 슬롯`, `장소 기능` 용도를 섞지 않는다

## Input

- `audit/Section_8_Place_Network_P2_Queue.md`
- `audit/Section_15_Oceanic_Place_Institution_Sidecar.md`
- `audit/Section_15_Frost_Place_Institution_Sidecar.md`
- `audit/Section_15_Obelisk_Place_Institution_Sidecar.md`
- `audit/Section_8_Frost_Notable_Anchor_Audit.md`
- `audit/FS_Place_Function_Register.md`

## Handoff Table

| Candidate | Current Read | Primary Handoff Target | Handoff Type | Why This Route |
|---|---|---|---|---|
| `바다의 교단` | `section_style_reclassify + sanctuary/watch-fort pressure` | `Section_15_Oceanic_Place_Institution_Sidecar.md` | `place-institution sidecar` | 성지, 신탁선, 감시 요새 압력은 해양의 장소/기관 축에서 관리하는 편이 가장 자연스럽다 |
| `오로라 평원` | `memory_site + sanctuary pressure` | `Section_15_Frost_Place_Institution_Sidecar.md` | `place-institution sidecar` | 프로스트는 named person보다 장소 슬롯이 먼저 강하므로 sidecar에서 장소 기능을 먼저 잡고, anchor audit은 보조로 둔다 |
| `빙하의 성소` | `sanctuary + ritual-validation pressure` | `Section_15_Frost_Place_Institution_Sidecar.md` | `place-institution sidecar` | 의식, 검증, 치유 기능이 강해 프로스트 성소 압력을 sidecar 본체에서 관리하는 편이 맞다 |
| `본 마켓` 계열 | `market + supply + memory-trade pressure` | `Section_15_Obelisk_Place_Institution_Sidecar.md` | `place-institution sidecar` | 오벨리스크의 보급/거래 거점은 frontier 생존 인프라로 읽는 편이 정확하다 |
| `잊힌 자들의 연합` | `section_style_reclassify + exile-network pressure` | `FS_Place_Function_Register.md` | `register note` | 구조 라벨은 이미 잠겼고, 남는 건 거점/망명 네트워크 압력을 register note로 보존하는 일이다 |

## Ownership Lock

| Candidate / Family | Primary Owner | Secondary Support | Ownership Rule |
|---|---|---|---|
| `바다의 교단` | `Section_15_Oceanic_Place_Institution_Sidecar.md` | 없음 | 교단의 `place-institution pressure`는 해양 sidecar가 주 기록처다 |
| `오로라 평원`, `빙하의 성소` | `Section_15_Frost_Place_Institution_Sidecar.md` | `Section_8_Frost_Notable_Anchor_Audit.md` | 프로스트 sidecar가 장소 압력 본체고, anchor audit은 slot projection만 보조한다 |
| `본 마켓` 계열 | `Section_15_Obelisk_Place_Institution_Sidecar.md` | 없음 | 오벨리스크 보급/기억 거래 거점은 sidecar가 주 기록처다 |
| `잊힌 자들의 연합` exile-network pressure | `FS_Place_Function_Register.md` | `Section_15_Obelisk_Place_Institution_Sidecar.md` | 망명 네트워크 압력은 register가 주 기록처고, sidecar는 주변 place context만 보존한다 |

## Conductor Rules

- `anchor audit`는 인물보다 슬롯/장소 기능이 먼저 강한 경우에 우선 사용한다.
- `place-institution sidecar`는 장소와 기관이 같이 붙는 경우에 우선 사용한다.
- `register note`는 구조 라벨 수정 없이 기능 압력만 보존할 때 사용한다.
- 주 기록처가 정해진 뒤에는 다른 문서가 같은 압력을 재정의하지 않고 reference/support로만 받는다.

## Conductor Decision

이 문서는 `P2 place-network` 후보를
다음 작업자에게 정확한 도착점과 함께 넘기기 위한 연결표로 사용한다.

즉 다음 패스에서 해야 할 일은
`P2 후보를 다시 해석하는 것`이 아니라,
이미 잠근 판정을 적절한 sidecar와 register로 흘려 보내는 것이다.

현재 1차 handoff 반영은
`Section_15_Oceanic_Place_Institution_Sidecar.md`,
`Section_15_Frost_Place_Institution_Sidecar.md`,
`Section_15_Obelisk_Place_Institution_Sidecar.md`,
`Section_8_Frost_Notable_Anchor_Audit.md`,
`FS_Place_Function_Register.md`까지 적용된 상태로 본다.

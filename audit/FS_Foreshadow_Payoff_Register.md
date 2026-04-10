# FS Foreshadow Payoff Register

이 문서는 FS 엔진의 `Foreshadow / Payoff Registry` 운용판이다.

복선은 문장 장식이 아니라
나중에 회수될 객체로 본다.

## Fields

| FS ID | Seed Type | Seeded In | Planned Payoff | Status | Owner Axis | Note |
|---|---|---|---|---|---|---|

## Register

| FS ID | Seed Type | Seeded In | Planned Payoff | Status | Owner Axis | Note |
|---|---|---|---|---|---|---|
| `FS-FP-001` | `person` | `Section_15_Named_Notable_Erion_Dracovis.md` | `고대어/금서 해독 장면` | `seeded` | `15 Named Notables` | 해석자형 명사 복선 |
| `FS-FP-002` | `person` | `Section_15_Named_Notable_Wolfgar_Dragonforge.md` | `전설 무구 제련 / 수복 장면` | `seeded` | `15 Named Notables` | 장인형 명사 복선 |
| `FS-FP-003` | `person` | `Section_15_Named_Notable_Oghma.md` | `지워진 역사 / 고룡 조언 장면` | `seeded` | `15 Named Notables` | 전승 원천 복선 |
| `FS-FP-004` | `person` | `Section_15_Named_Notable_Sylvia.md` | `독성/임상 장부 해석 장면` | `seeded` | `15 Named Notables` | 기록자형 연금술 복선 |
| `FS-FP-005` | `line` | `Section_15_Subline_Profile_Black_Auction_Appraiser_Line.md` | `진품/가품 아이템 갈등 회수` | `seeded` | `15 Operational Lines` | 아이템 축 연결 |
| `FS-FP-006` | `line` | `Section_15_Subline_Profile_Signet_Forger_Line.md` | `허가문 위조 / 잠입 회수` | `seeded` | `15 Operational Lines` | 문서 위조 축 |
| `FS-FP-007` | `line` | `Section_15_Subline_Profile_Grave_Inscription_Decoder_Line.md` | `죽은 메시지 해독 회수` | `seeded` | `15 Operational Lines` | 침묵의 상회 축 |
| `FS-FP-008` | `relationship` | `FS_Relationship_Ledger.md` | `세실리아-벤투라 긴장 회수` | `seeded` | `relationship` | 공적/비합법 교차 |
| `FS-FP-009` | `item_pressure` | `FS_Story_to_Lore_Handoff_Seed_Cases.md / FS-HANDOFF-SEED-001` | `전설 무구 후보가 이름을 얻기 전 제작 책임과 사용자 손상 확인` | `handoff_test` | `Story-to-Lore` | 정본 아이템명 생성 금지 |

## Conductor Reading Rule

- 새 복선을 넣을 때는 먼저 여기 ID를 만든다.
- `Status`는 최소한 `seeded`, `armed`, `paid_off`, `dropped`로 관리한다.
- 회수 없는 멋있는 설정은 오래 유지하지 않는다.

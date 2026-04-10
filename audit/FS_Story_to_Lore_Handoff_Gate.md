# FS Story-to-Lore Handoff Gate

이 문서는 Story Engine에서 나온 새 설정이
Lore Engine의 정본 층으로 들어가기 전에 반드시 거쳐야 하는
handoff gate다.

목적:

- 장면 편의를 위해 즉흥적으로 나온 새 설정이 정본을 오염시키지 않게 한다.
- `새 지명`, `새 세력`, `새 유명인`, `새 아이템`, `새 소속`, `새 이동 경로`를
  어느 장부와 어느 섹션으로 보내야 하는지 고정한다.
- Story Engine과 Lore Engine의 책임 경계를 분명히 한다.

## Purpose

Story Engine은
`무엇을 언제 보여줄까`
를 정한다.

Lore Engine은
`그것이 세계 안에 실제로 무엇인가`
를 정한다.

따라서 원고나 장면 설계에서 새 설정이 튀어나오면,
바로 정본으로 쓰지 않고 이 gate를 먼저 통과시킨다.

## When Handoff Is Required

아래 중 하나라도 나오면 handoff gate를 건다.

- 새 지명
- 새 세력명
- 새 기관명
- 새 유명인 또는 명사형 인물
- 새 아이템 / 유물 / 장비
- 새 소속 / 혈통 / 계보
- 장거리 이동 또는 새 이동 경로
- 소문을 사실로 바꾸는 순간
- 기존 인물의 등급 위상이 크게 바뀌는 순간
- 기존 인물의 `14 / 15 / 8 / Place` 라우팅이 흔들리는 순간
- 새 장소 기능이 생겨 `FS_Place_Function_Register`를 건드리는 순간
- 복선이 실제 정본 정보로 회수되는 순간
- display canon 후보를 정본명처럼 쓰기 시작하는 순간

## Handoff Packet Fields

Story Engine 쪽에서 Lore Engine으로 넘길 최소 패킷:

| Field | Meaning |
|---|---|
| `story_source` | 어느 장면, 액트, 질문에서 나온 설정인가 |
| `scene_or_act` | 어떤 단위에서 등장하는가 |
| `proposed_new_element` | 무엇이 새로 생겼는가 |
| `proposal_type` | place / faction / institution / named_person / operational_line / item / lineage / route / rumor_to_fact |
| `working_name` | 해당 장면에서 쓰는 작업명 |
| `why_now` | 이 장면에 필요한 이유는 무엇인가 |
| `expected_reader_effect` | 독자에게 어떤 효과를 주려는가 |
| `lore_risk` | 이름 충돌, 등급 과열, 라우팅 흔들림, 톤 충돌 위험이 있는가 |
| `suggested_route` | 14 / 15 Named Notables / 15 Operational Lines / 8 / 지도 / 아이템 / hold 중 어디로 보이는가 |

## Lore Intake Questions

Lore Engine은 handoff를 받으면 아래를 확인한다.

1. 기존 출처와 충돌하지 않는가
2. 적용할 상태 라벨은 무엇인가
3. 어느 route가 가장 자연스러운가
4. 이름 톤이 세계 톤과 맞는가
5. 관계, 액트, 연표, 복선에 영향을 주는가
6. 장소/기관/자산/소문 장부에 먼저 기록해야 하는가

## Decision Outcomes

| Outcome | Meaning |
|---|---|
| `accept_as_lore_candidate` | 작업본 기준 사용 가능하지만 아직 hard canon은 아니다 |
| `hold_for_evidence` | route는 보이지만 근거가 약해 보류한다 |
| `route_to_14_review` | 영웅 중심성이 강해 14 검토가 먼저다 |
| `route_to_15_review` | 명사형 인물 가치가 있으나 경계 검토가 필요하다 |
| `route_to_place_register` | 인물보다 장소 기능부터 잡아야 한다 |
| `reject_or_reframe` | 정본 구조와 충돌하므로 장면 해법을 재구성해야 한다 |

## Hook Points

이 gate는 실행 하네스에서 아래 hook과 연결된다.

- `pre_write_hook`: story-born 신규 설정이 바로 문서 반영되지 않게 막는다
- `post_write_hook`: 반영 후 필요한 register와 change log가 갱신됐는지 본다
- `pre_close_hook`: 해당 배치의 후속 작업선에 handoff 후속이 남았는지 고정한다

## Fast Table

| Situation | Lore Route | Required Register |
|---|---|---|
| 장면에서 새 항구 이름이 튀어나왔다 | `지도` 또는 `Place Function` | `FS_Place_Function_Register` |
| 새로운 기록관 NPC가 필요하다 | `15 Named Notables` 또는 `15 Operational Lines` | `FS_State_Label_Register`, 필요 시 `FS_Decision_Ruling_Register` |
| 새 길드명을 붙이고 싶다 | `8` | `FS_State_Label_Register`, Naming Tone 점검 |
| 가짜 소문을 사실로 바꾸고 싶다 | 기존 route 유지 | `FS_Rumor_Fact_Register`, 필요 시 `FS_Canon_Change_Log` |
| 새 이동 경로가 필요하다 | `지도` 또는 `hold` | `FS_Travel_Logistics_Register` |

## Seed Trials

- `audit/FS_Story_to_Lore_Handoff_Seed_Cases.md`

## Handoff Queue Reference

- `audit/FS_Story_to_Lore_Live_Handoff_Queue.md`

## Conductor Note

이 gate의 목적은
Story Engine을 느리게 하는 것이 아니다.

오히려
장면에서 나온 좋은 아이디어를
나중에도 무너지지 않는 구조로 넘기는 데 있다.

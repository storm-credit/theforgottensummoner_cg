# Section 15 Frost Display Canon Candidates

이 문서는 프로스트 대륙의 `need_named_candidate` 슬롯을
더 정통 판타지 톤의 표면명 후보로 낮출 때 쓰는 후보표다.

naming active 판단은
`Section_15_Named_Notables_Register.md`,
`Section_15_Named_Notables_Status_Compass.md`,
`Continuous_Workstream.md`
기준으로 읽는다.

이 문서에서는 정본명이 아니라 `preferred_display_candidate` reference만 남긴다.

## Place / Role -> Display Canon Candidates

| Working Slot | Display Candidate A | Display Candidate B | State | Note |
|---|---|---|---|---|
| `전승 보존회 원로 사냥꾼` | `서리길 원로 사냥꾼` | `빙설 추적 원로` | `display_canon_candidate` | 생존/추적/구전 전승 기능을 함께 받는다. |
| `묘지기 장로` | `빙묘 수호장` | `서리무덤 이름지기` | `display_canon_candidate` | 단순 묘지기보다 기억과 수호 기능을 강조한다. |
| `대예언자` | `오로라 예언장` | `겨울 징조관` | `display_canon_candidate` | 하늘 징조와 공동체 결의 기능을 함께 담는다. |
| `수석 기술자 / 드워프 장인` | `빙철 공방장` | `폭풍요새 병기장` | `display_canon_candidate` | 공성 병기와 요새 공방 이미지를 유지한다. |
| `별의 샤먼` | `성광 샤먼` | `오로라 별술사` | `display_canon_candidate` | 오로라와 하늘 징조의 이미지가 살아난다. |
| `아이스포지 병기소 장인` | `빙로 병기장` | `서리벼림 장인` | `display_canon_candidate` | 단순 아이스포지 직역보다 무기 전승 톤이 강하다. |

## Preferred Candidate Reference Pass

| Working Slot | Preferred Candidate | State | Reason |
|---|---|---|---|
| `전승 보존회 원로 사냥꾼` | `서리길 원로 사냥꾼` | `preferred_display_candidate` | 프로스트의 길, 사냥, 전승 보존 기능이 한 번에 읽힌다. |
| `묘지기 장로` | `빙묘 수호장` | `preferred_display_candidate` | 묘역 관리보다 더 오래된 의식/기억 수호자 톤이 산다. |
| `대예언자` | `오로라 예언장` | `preferred_display_candidate` | 프로스트 대륙의 하늘빛 이미지와 예언 기능이 같이 선다. |
| `수석 기술자 / 드워프 장인` | `빙철 공방장` | `preferred_display_candidate` | 장인/병기/요새 이미지를 간결하게 묶는다. |
| `별의 샤먼` | `오로라 별술사` | `preferred_display_candidate` | 샤먼보단 별술사 쪽이 세계 톤과 더 잘 맞는다. |
| `아이스포지 병기소 장인` | `서리벼림 장인` | `preferred_display_candidate` | 아이스포지 직역을 피하면서 공방 전승 느낌을 살린다. |

## Polish Watchlist

| Candidate | Reason | Direction |
|---|---|---|
| `서리길 원로 사냥꾼` | 기능은 좋지만 직함이 조금 길다. | `서리길 원로`, `서리추적 원로` 검토 |
| `빙묘 수호장` | 수호자/사제/이름기록 기능이 더 들어갈 여지가 있다. | `빙묘 이름수호장`, `서리무덤 수호장` 검토 |
| `오로라 예언장` | 강하지만 직위보다 장소명처럼 들릴 수 있다. | `오로라 징조관`, `겨울 예언장` 검토 |
| `빙철 공방장` | 드워프 장인성을 직접 드러내진 않는다. | `빙철 장인장`, `폭풍요새 공방장` 검토 |
| `오로라 별술사` | 좋지만 공동체 원로 느낌이 약하다. | `별빛 원로술사`, `오로라 원로술사` 검토 |
| `서리벼림 장인` | 병기소의 권위가 조금 약하다. | `서리벼림 병기장`, `빙로 병기장` 검토 |

## Conductor Reading

프로스트 슬롯은 reference상 아래 preferred 후보로 읽는다.

- `서리길 원로 사냥꾼`
- `빙묘 수호장`
- `오로라 예언장`
- `빙철 공방장`
- `오로라 별술사`
- `서리벼림 장인`

Reference carryover:

- 이 우선 후보를 `FS_Place_Function_Register`와 더 직접 연결한다.
- 이후에만 실제 개인명이 확인된 슬롯을 `verify_before_15`로 올리는 기준으로 읽는다.

# Section 15 Frost Core Register Link

이 문서는 프로스트 대륙의 `need_named_candidate` 슬롯을
`FS_Place_Function_Register`,
`FS_Decision_Ruling_Register`,
`FS_Slot_Maturation_Register`
와 직접 연결한 결과를 묶는 브리지다.

목적:

- 프로스트 슬롯이 이름 없는 메모로 흩어지지 않게 한다.
- 장소 기능, 표면명 후보, 성장 단계가 한 줄에서 같이 보이게 한다.
- 실명 확인 전 성급한 `15 Named Notable` 승격을 막는다.

## Direct Link Pass

| Slot | Place Anchor | Place Function | Preferred Display Candidate | Register Hook | Current Stage | Next Gate |
|---|---|---|---|---|---|---|
| `전승 보존회 원로 사냥꾼` | `오로라 평원 / 전승 보존회` | `memory_site`, `sanctuary` | `서리길 원로 사냥꾼` | `place_first` | `slot_with_display_candidate` | 실제 개인명 확인 |
| `별의 샤먼` | `오로라 평원` | `memory_site`, `sanctuary` | `오로라 별술사` | `place_first` | `slot_with_display_candidate` | 샤먼/주술사 실명 확인 |
| `대예언자` | `겨울회의 의장막 + 오로라 평원` | `sanctuary`, `threshold`, `memory_site` | `오로라 예언장` | `dual_anchor_slot` | `slot_with_display_candidate` | 예언 지도부 실명 확인 |
| `묘지기 장로` | `얼음무덤 언덕` | `memory_site`, `sanctuary` | `빙묘 수호장` | `place_first` | `slot_with_display_candidate` | 기록/묘역 인명 확인 |
| `수석 기술자 / 드워프 장인` | `푸른 폭풍 요새` | `threshold`, `workshop` | `빙철 공방장` | `place_first` | `slot_with_display_candidate` | 공방/병기 장인 실명 확인 |
| `아이스포지 병기소 장인` | `아이스포지 병기소` | `workshop`, `memory_site` | `서리벼림 장인` | `place_first` | `slot_with_display_candidate` | 병기소 장인 실명 확인 |

## Boundary Hold Support

아래 인물은 이번 연결 이후에도 `verify_before_15` 또는 보류를 유지한다.

| Candidate | Anchor | State | Note |
|---|---|---|---|
| `시그리드 프로스트하트` | `퍼마프로스트 요새 / 아이스포지 병기소` | `verify_before_15` | 공성단장 / 냉기 병기 축이 강하다. |
| `마리안 더 윈터콜러` | `빙하의 성소 / 오로라 평원` | `verify_before_15` | 성소 반복 신호와 A급 정령술사 결이 남아 있다. |
| `울프릭` | `빙하의 성소 / 프로스트본 연합` | `verify_before_15` | 영웅록/주술 영웅 신호가 남아 있다. |
| `프리야 글래시아` | `빙하의 성소 / 원로단` | `keep_14_or_verify` | 성소 지도부/의식 운영축이 강하다. |
| `카이라 프리즌윈드` | `빙하의 성소 / 원로단` | `keep_14_or_verify` | 성소 지도부/원로단 신호가 크다. |

## Register Actions Applied

1. `FS_Place_Function_Register`에 프로스트 전용 direct link pass를 추가한다.
2. `FS_Decision_Ruling_Register`에 프로스트 `place_first` / `dual_anchor_slot` 판정을 추가한다.
3. `FS_Slot_Maturation_Register`의 프로스트 표에 `Primary Anchor`, `Register Gate`를 붙인다.
4. `FS_Canon_Change_Log`에 프로스트 슬롯의 `slot_only -> slot_with_display_candidate` 변화 기록을 남긴다.

## Conductor Decision

프로스트는 여전히 `안정 15 후보 대륙`이 아니다.

현재 단계에서는
개별 영웅 이름보다
`오로라 평원`, `얼음무덤 언덕`, `푸른 폭풍 요새`, `아이스포지 병기소`, `빙하의 성소`, `겨울회의 의장막`
이 여는 명사형 슬롯을 먼저 고정한다.

다음 실제 작업:

- `Story-to-Lore Handoff Gate` 초안 작성
- 기존 `verify_before_15` 항목 중 일부를 `Decision Ruling Register`와 연결

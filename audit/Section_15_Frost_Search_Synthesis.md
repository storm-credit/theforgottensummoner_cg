# Section 15 Frost Search Synthesis

이 문서는 프로스트 대륙의 `15 Named Notables` 후보와 역할 슬롯을 압축한 종합표다.

프로스트는 현재 안전한 15 확정 후보가 적고,
대신 전승, 묘역, 예언, 공방, 성소 같은 장소-기관 슬롯이 강하다.

## Conductor Verdict

프로스트에서는 새 15 확정자를 만들지 않는다.

현재 이름 있는 후보들은 대부분 전설 영웅록, A/S급 신호, 지도부 신호와 겹치므로
`verify_before_15` 또는 `keep_14_or_verify`로 유지한다.

## Stable 15 Candidate

현재 없음.

프로스트는 아직 안정 15 후보보다 `need_named_candidate` 슬롯이 더 중요하다.

## Verify Before 15

| Candidate | Anchor | Reason | State |
|---|---|---|---|
| `시그리드 프로스트하트` | `퍼마프로스트 공성단 / 아이스포지 병기소` | 공성단장, 냉기 마법과 공학 기술, 방어 시설/공성 병기 제작 축. | `verify_before_15` |
| `마리안 더 윈터콜러` | `오로라 평원 / 빙하의 성소` | A급 정령술사, 오로라 평원과 성소 축 반복 신호. | `verify_before_15` |
| `울프릭` | `프로스트본 연합 / 전설적 주술 영웅록` | 빙하의 주술사, 부족의 장로. | `verify_before_15` |
| `프리야 글래시아` | `주술사 원로단 / 빙하의 성소` | 원로단 지도부 신호. | `keep_14_or_verify` |
| `카이라 프리즌윈드` | `주술사 원로단 / 빙하의 성소` | 원로단 지도부 신호. | `keep_14_or_verify` |

## Need Named Candidate Slots

| Slot | Anchor | Function | State |
|---|---|---|---|
| `전승 보존회 원로 사냥꾼` | `오로라 평원 / 전승 보존회` | 이동 경로, 생존 기술, 구전 전승 회수. | `need_named_candidate` |
| `묘지기 장로` | `얼음무덤 언덕` | 죽은 자의 기록, 족보, 잊힌 전설/유물 단서. | `need_named_candidate` |
| `대예언자` | `오로라 평원 / 겨울회의 의장막` | 하늘 징조, 운명 예언, 부족 결의 중재. | `need_named_candidate` |
| `수석 기술자 / 드워프 장인` | `푸른 폭풍 요새` | 방어선, 생산 구역, 공성 병기 제작. | `need_named_candidate` |
| `별의 샤먼` | `오로라 평원` | 오로라 징조 해석, 의식 전파. | `need_named_candidate` |
| `아이스포지 병기소 장인` | `퍼마프로스트 요새 / 아이스포지 병기소` | 얼음 공성심장, 냉기 병기, 공방 전승. | `need_named_candidate` |

## Place / Institution Anchors

| Anchor | Function | Notable Use |
|---|---|---|
| `오로라 평원` | `memory_site`, `sanctuary` | 전승 보존회, 별의 샤먼, 대예언자 슬롯. |
| `얼음무덤 언덕` | `memory_site`, `sanctuary` | 묘지기 장로, 죽은 자의 이름, 유물 단서. |
| `푸른 폭풍 요새` | `threshold`, `workshop` | 수석 기술자, 드워프 장인, 공성 병기 생산. |
| `퍼마프로스트 요새` | `threshold`, `workshop` | 시그리드, 공성단, 냉기 병기 보관. |
| `아이스포지 병기소` | `workshop`, `memory_site` | 냉기 병기와 공방 전승. |
| `빙하의 성소` | `sanctuary`, `memory_site` | 마리안, 울프릭, 주술사 원로단 검증 축. |
| `겨울회의 의장막` | `sanctuary`, `threshold` | 부족 간 조정, 대예언자/원로단 회의. |

## Conductor Decision

프로스트는 지금 인물명을 더 찾기보다
장소-기관 슬롯을 유지하는 쪽이 안전하다.

- `시그리드`, `마리안`, `울프릭`은 15 후보가 아니라 `verify_before_15`.
- `프리야`, `카이라`는 고위 지도부 신호 때문에 `keep_14_or_verify`.
- 이름 없는 슬롯들은 후속 설정에서 개인명이 확인될 때까지 역할 슬롯으로만 보존한다.

## Next Action

프로스트는 이제 다음 mainline으로 올린다.

다음 배치는 `전승 보존회 원로 사냥꾼`, `묘지기 장로`, `대예언자`, `수석 기술자 / 드워프 장인`, `별의 샤먼` read-only narrowing이다.

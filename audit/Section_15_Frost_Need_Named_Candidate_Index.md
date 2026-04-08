# Section 15 Frost Need Named Candidate Index

이 문서는 프로스트 대륙에서 아직 개인명이 없는
`유명 NPC형 역할 슬롯`을 모아두는 색인이다.

## Rule

- 새 이름을 만들지 않는다.
- 장소-기관 앵커를 먼저 보존한다.
- 후속 원본/설정에서 이름이 확인되면 14 신호 확인 후 15 후보로 올린다.

## Slot Index

| Slot | Place / Institution Anchor | Function | State |
|---|---|---|---|
| `전승 보존회 원로 사냥꾼` | `오로라 평원 / 전승 보존회` | 구전 전승, 생존 지식, 이동 경로 보존 | `need_named_candidate` |
| `묘지기 장로` | `얼음무덤 언덕` | 족보, 장례길, 죽은 자의 이름, 유물 단서 | `need_named_candidate` |
| `대예언자` | `오로라 평원 / 겨울회의 의장막` | 하늘 징조와 부족 결의 해석 | `need_named_candidate` |
| `수석 기술자 / 드워프 장인` | `푸른 폭풍 요새` | 공성 병기, 생산 구역, 방어선 정비 | `need_named_candidate` |
| `별의 샤먼` | `오로라 평원` | 별빛 의식, 오로라 징조, 예언 전파 | `need_named_candidate` |
| `아이스포지 병기소 장인` | `퍼마프로스트 요새 / 아이스포지 병기소` | 얼음 공성심장, 냉기 병기, 공방 전승 | `need_named_candidate` |

## Routing Notes

프로스트 슬롯은 이름보다 장소 기능이 먼저다.

따라서 후속 작업은 다음 순서로만 진행한다.

1. 장소/기관 기능 유지.
2. 실제 개인명 확인.
3. 등급/Act/영웅록 신호 확인.
4. `verify_before_15` 또는 `named_notable_candidate` 상태 부여.
5. 필요하면 개별 15 Named Notable 시트 생성.

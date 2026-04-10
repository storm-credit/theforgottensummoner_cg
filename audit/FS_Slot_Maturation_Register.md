# FS Slot Maturation Register

이 문서는 `need_named_candidate` 슬롯이
어떻게 실제 `15 Named Notable` 후보로 자라는지 추적하는 장부다.

## Stages

1. `slot_only`
2. `slot_with_display_candidate`
3. `named_signal_found`
4. `verify_before_15`
5. `named_notable_candidate`
6. `hold_or_merge_review`

## Rule

- 새 이름을 만들었다고 바로 15 후보로 올리지 않는다.
- 먼저 슬롯이 어떤 장소/기관 기능을 여는지 확인한다.
- 그다음 실제 이름 신호가 있는지 본다.
- 등급/Act/영웅록/독립 14 파일 신호가 강하면 `verify_before_15` 또는 `hold`로 둔다.

## Frost Slot Snapshot

| Slot | Primary Anchor | Snapshot Stage | Snapshot Name Layer | Register Gate | Next Check |
|---|---|---|---|---|---|
| `전승 보존회 원로 사냥꾼` | `오로라 평원 / 전승 보존회` | `slot_with_display_candidate` | `서리길 원로 사냥꾼` | `place_first` | 실제 개인명 확인 |
| `묘지기 장로` | `얼음무덤 언덕` | `slot_with_display_candidate` | `빙묘 수호장` | `place_first` | 기록/묘역 인명 확인 |
| `대예언자` | `겨울회의 의장막 + 오로라 평원` | `slot_with_display_candidate` | `오로라 예언장` | `dual_anchor_slot` | 예언 지도부 실명 확인 |
| `수석 기술자 / 드워프 장인` | `푸른 폭풍 요새` | `slot_with_display_candidate` | `빙철 공방장` | `place_first` | 공방/병기 장인 실명 확인 |
| `별의 샤먼` | `오로라 평원` | `slot_with_display_candidate` | `오로라 별술사` | `place_first` | 샤먼/주술사 실명 확인 |
| `아이스포지 병기소 장인` | `아이스포지 병기소` | `slot_with_display_candidate` | `서리벼림 장인` | `place_first` | 병기소 장인 실명 확인 |

## Oceanic Slot Snapshot

| Slot | Snapshot Stage | Snapshot Name Layer | Next Check |
|---|---|---|---|
| `수석 오라클` | `slot_with_display_candidate` | `파도 신탁장` | 개인명 확인 |
| `항로 기록관` | `slot_with_display_candidate` | `해로 장부관` | 길드/항로 실무 인명 확인 |
| `왕실 조선소 수석 공병` | `slot_with_display_candidate` | `왕실 선공장 수석장` | 조선소 책임자 실명 확인 |
| `장물 감정사` | `slot_with_display_candidate` | `흑조 감정관` | 경매/감정 인명 확인 |
| `심해 금고 보관인` | `slot_with_display_candidate` | `심연 장부관` | 금고/장부 관리자 실명 확인 |

## Ether Slot Snapshot

대표 Ether 슬롯은 `Slot`에 작업용 anchor를 남기되,
`Snapshot Name Layer`는 최신 `preferred_display_candidate`를 따른다.

| Slot | Snapshot Stage | Snapshot Name Layer | Next Check |
|---|---|---|---|
| `금서 도서관 사서장` | `slot_with_display_candidate` | `봉인서고지기` | 실명 확인 |
| `금서 관리국 검열관` | `slot_with_display_candidate` | `금서 검인관` | 검인관 실명 확인 |
| `마나 공방 공방장` | `slot_with_display_candidate` | `비전로 장인장` | 장인 실명 확인 |
| `마도 제작 감독관` | `slot_with_display_candidate` | `비전 제작관` | 제작축 실명 확인 |
| `아스트랄 관측장` | `slot_with_display_candidate` | `성좌 관측장` | 관측소 핵심 인명 확인 |
| `별의 예언 기록관` | `slot_with_display_candidate` | `별기록관` | 예언 원문 관리 인명 확인 |
| `중앙 도서관 학장` | `slot_with_display_candidate` | `대서고 학장` | 도서관 학장 실명 확인 |
| `지식의 수호자 대표` | `slot_with_display_candidate` | `대서고 수호장` | 대서고 보안 인명 확인 |
| `성채 결계관` | `slot_with_display_candidate` | `성채 봉인관` | 루멘 성채 실무 인명 확인 |
| `순교자 묘역 관리 사제` | `slot_with_display_candidate` | `순교묘역 사제장` | 순교묘역 의식 인명 확인 |
| `성검 요새 무기 장인` | `slot_with_display_candidate` | `성검 병장관` | 성검 요새 실무 인명 확인 |
| `감옥 무기고 관리관` | `slot_with_display_candidate` | `옵시디안 무기지기` | 옵시디안 실무 인명 확인 |
| `연합 의회 기록관` | `slot_with_display_candidate` | `서약의회 기록관` | 연합 의회 기록 인명 확인 |
| `상업 조정관` | `slot_with_display_candidate` | `전비 장부관` | 아덴브루크 금융 실무 인명 확인 |
| `밀수 통로 기록관` | `slot_with_display_candidate` | `그늘항로 기록관` | 포트 넥서스 비공식 항로 인명 확인 |
| `계약문 보관관` | `slot_with_display_candidate` | `서약문 보관관` | 머시너리 게이트 계약 원본 인명 확인 |
| `정령 계약 해석자` | `slot_with_display_candidate` | `정령서약 해석자` | 루미라/정령연합 실명 확인 |
| `정령의 무덤 이름 새김꾼` | `slot_with_display_candidate` | `정령묘 이름새김꾼` | 정령묘 의식 인명 확인 |

## Conductor Note

이 장부가 있으면
`이 슬롯은 아직 이름 없는 구조인가`
`아니면 실제 후보로 올라왔는가`
를 바로 구분할 수 있다.

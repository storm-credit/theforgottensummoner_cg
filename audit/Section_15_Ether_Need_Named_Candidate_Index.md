# Section 15 Ether Need Named Candidate Index

이 문서는 에테르 큐 1-9번에서 확인된
`개인명 없는 유명 NPC 슬롯`을 장소-기관 앵커별로 묶은 색인이다.

named-candidate active 판단은
`Section_15_Named_Notables_Register.md`,
`Section_15_Named_Notables_Status_Compass.md`,
`Continuous_Workstream.md`
기준으로 읽는다.

원칙:

- 새 이름을 지금 만들지 않는다.
- 슬롯은 장소와 기관 기능으로 먼저 보존한다.
- 실제 이름이 원본 또는 후속 설정에서 확인될 때만 15 후보로 승격한다.
- 14 신호가 강한 인물의 직함을 이 슬롯에 억지로 덮어씌우지 않는다.

## Slot Index

| Slot | Place / Institution Anchor | Function | State | Notes |
|---|---|---|---|---|
| `봉인서고지기` | `금서 도서관 / 마법 서고단` | 금서 보관, 봉인문서 관리, 접근권 통제 | `need_named_candidate` | 대런 크레센트와 구분. |
| `금서 검인관` | `금서 도서관 / 마법 서고단` | 금서 반출/열람 검인, 위험 서적 판정 | `need_named_candidate` | 서고 행정 실무 명사 슬롯. |
| `비전로 장인장` | `마나 공방` | 비전 제작로 관리, 마법 장비 제작 감독 | `need_named_candidate` | 에드가 룬워커와 구분. |
| `비전 제작관` | `마나 공방 / 마법협회 제작축` | 공방 제작 검수, 룬/마도 제작 표준화 | `need_named_candidate` | 아이템 소진행과도 연결 가능. |
| `성좌 관측장` | `아스트랄 관측소` | 별자리 관측, 예언 자료 수집 | `need_named_candidate` | 칼리스트와 구분. |
| `별기록관` | `별의 예언자단` | 별기록 보존, 예언 원문 관리 | `need_named_candidate` | 예언/복선 레지스터와 연결 가능. |
| `탑서기` | `아르카노스 탑 / 학파 회의실` | 학파 회의록, 탑 공문, 탑주 기록 정리 | `need_named_candidate` | 7개 탑주와 구분. read-only pass에서 direct holder 미확인. |
| `대서고 학장` | `아스트라르 중앙 도서관` | 성국 학술 질서, 도서관 의사결정 | `need_named_candidate` | 래퍼티/라파엘 드리프트와 구분. |
| `대서고 수호장` | `아스트라르 중앙 도서관` | 금서 보안, 대서고 방어와 봉인 관리 | `need_named_candidate` | 지식의 수호자 계열 표면명 후보. |
| `성채 봉인관` | `루멘 성채` | 신성 결계, 성채 봉인 장치 관리 | `need_named_candidate` | 대사제 요한과 구분. |
| `순교묘역 사제장` | `순교자의 지하 묘지` | 순교자 유물, 순교묘역 의식, 성유물 공명 관리 | `need_named_candidate` | 발레리우스/헬렌 로컬 슬롯과 구분. |
| `성검 병장관` | `성검 요새` | 성검단 병장/무기고 관리 | `need_named_candidate` | 알렉산드로와 구분. |
| `옵시디안 무기지기` | `옵시디안 / 검은 대장간` | 감옥 무기고, 검은 대장간 제작물 관리 | `need_named_candidate` | 실라스 블랙쏜과 구분. |
| `서약의회 기록관` | `레갈리아 / 연합 의회관` | 왕국연합 서약문, 조약, 회의록 보존 | `need_named_candidate` | 레온하르트와 구분. |
| `왕실 의전서기` | `레갈리아 / 왕실 의전실` | 왕실 접견, 외교 의전, 의식 순서 기록 | `need_named_candidate` | 의회 기록 축과 분리. read-only pass에서 direct holder 미확인. |
| `전비 장부관` | `아덴브루크 / 파브리스 상권` | 전비 어음, 관세율, 군수 장부 관리 | `need_named_candidate` | 제라르드/리아나와 구분. |
| `성벽 설계서기` | `브룬발트 대성채 / 성벽 설계 보관고` | 성벽 설계도, 요새 보수 기록, 방어선 공정 관리 | `need_named_candidate` | 병참 영웅 축과 구분. read-only pass에서 direct holder 미확인. |
| `상단 조율관` | `골든마르크 / 상단 회의장` | 상단 분쟁 중재, 상업권 조율, 외교 연회 실무 | `need_named_candidate` | 세실리아 접점과 구분. read-only pass에서 direct holder 미확인. |
| `항만 인장관` | `포트 넥서스 / 항만 인장소` | 입항 인장, 출입 증표, 부두 문서 관리 | `need_named_candidate` | 셀레나 와일드웨이브와 구분. read-only pass에서 direct holder 미확인. |
| `그늘항로 기록관` | `포트 넥서스 / 항만청 / 밀항 루트` | 밀항로, 비공식 항로, 밀수 기록 관리 | `need_named_candidate` | 셀레나 와일드웨이브와 구분. |
| `서약문 보관관` | `황금 맹약의 신전` | 계약 원본, 공증문, 지하 서고 관리 | `need_named_candidate` | 대집행관 role slot과 연결 가능. |
| `탐사 기록관` | `아크브릿지 연구소` | 탐사 보고서, 연구 의뢰, 발견 기록 정리 | `need_named_candidate` | 발타자르/에드윈/에드가와 구분. read-only pass에서 direct holder 미확인. |
| `연구소 보존관` | `아크브릿지 연구소 / 실험 보존고` | 실패작, 격리 기록, 표본 보존 관리 | `need_named_candidate` | 제작축과 분리된 연구 슬롯. read-only pass에서 direct holder 미확인. |
| `정령서약 해석자` | `루미라 / 최초 정령왕 계약서 사본` | 고대 정령어 계약 해석, 정령서약 중재 | `need_named_candidate` | 엘다라와 가장 가깝지만 동일 인물로 고정하지 않음. |
| `대현자 보좌 기록관` | `루미라 / 대현자 기록대` | 의회 기록, 번역 보조, 고대 정령어 주석 정리 | `need_named_candidate` | 엘다라 보좌축이지만 동일 인물로 고정하지 않음. read-only pass에서 direct holder 미확인. `엘라라 문힘`은 도서관장/기록관 축으로만 보임. |
| `침묵의 감시자` | `잠든 정령의 숲 / 재판식 원` | 숲의 금기 감시, 침묵 의례, 묘역 접근 통제 | `need_named_candidate` | 정령묘 이름새김꾼과 역할 분리. read-only pass에서 개인명 아닌 집단 직함만 확인됨. |
| `정령묘 이름새김꾼` | `잠든 정령의 숲 / 정령의 무덤 / 비석의 숲` | 사라진 정령 이름 기록, 정령묘 의식 관리 | `need_named_candidate` | 독립 이름 미확인. |

## Routing Notes

이 색인은 15번 인물백과의 실제 인물 시트가 아니다.
후속 설정에서 개인명이 확인되면 아래 순서로만 승격 흐름을 읽는다.

1. 원본 또는 작업본에서 개인명 확인.
2. 14번 영웅 신호 확인.
3. `verify_before_15` 또는 `named_notable_candidate`로 상태 라벨 부여.
4. 대륙 -> 세력/도시/조직 앵커 지정.
5. 필요하면 Named Notables 개별 시트 생성.

## Low-Priority Follow-Up Progress

이 read-only snapshot에서 아래 7개는 direct holder가 확인되지 않아 role slot 유지로 잠갔다.

- `탑서기`
- `왕실 의전서기`
- `성벽 설계서기`
- `상단 조율관`
- `항만 인장관`
- `탐사 기록관`
- `연구소 보존관`

이 read-only snapshot에서 아래 2개도 direct holder가 확인되지 않아 role slot 유지로 잠갔다.

- `대현자 보좌 기록관`
- `침묵의 감시자`

## Reference State Snapshot

에테르 표면명 기본값은 한 번 잠긴 상태로 유지한다.
low-priority auxiliary slot 9개도 read-only closure를 마친 reference 결과로 유지한다.
이 색인은 coverage / closure / anchor bridge 압축표를 보조하는 reference 장부로 읽는다.

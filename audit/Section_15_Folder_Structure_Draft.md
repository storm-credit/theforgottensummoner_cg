# Section 15 Folder Structure Draft

이 문서는 `15 People Worth Seeking`의 folder route/reference mock 구조를
문서 레벨에서 먼저 잠그는 설계도다.

folder structure reading은
`Section_15_Named_Notables_Status_Compass.md`,
`Section_15_Named_Notables_Register.md`,
`Section_15_Index_Draft.md`,
`Section_15_Actual_Draft_Package_Freeze.md`,
`Section_15_Group_Index.md`,
`Section_15_Profile_Draft_Index.md`,
`Section_15_Subline_Register.md`,
`Section_15_Named_Notables_Name_Collision_Register.md`,
`Section_14_15_Boundary_Verification_Queue.md`,
`Section_15_Frost_Place_Institution_Sidecar.md`,
`Section_15_Oceanic_Place_Institution_Sidecar.md`,
`Section_15_Ether_Place_Institution_Sidecar.md`,
`Section_15_Obelisk_Place_Institution_Sidecar.md`,
`Section_15_Named_Notables_Frost_Scout.md`,
`Section_15_Named_Notables_Oceanic_Scout.md`,
`Section_15_Named_Notables_Ether_Scout.md`,
`Section_15_Named_Notables_Obelisk_Scout.md`,
`Section_15_Frost_Display_Canon_Candidates.md`,
`Section_8_15_Closure_Sync_Carryover_Watch.md`,
`Continuous_Workstream.md`
기준으로 읽는다.

중요:

- live 폴더 생성/이동은 하지 않는다.
- 이 문서는 `route freeze` 이후에 잠긴 route reference 상태를 기록한다.
- 이 문서는 `cg` 안의 설계도다.
- 원본 저장소는 수정하지 않는다.
- 구조 기준은 직업이 아니라 `대륙 -> 세력 / 도시 / 조직`이다.

## Proposed Top Structure

```text
15. 인물백과
  15-A. People Worth Seeking
    1. 크림슨
    2. 에테르
    3. 프로스트
    4. 해양
    5. 오벨리스크
    6. 범대륙 후기 확장
  15-B. Operational Lines
    1. 도시 운영층
    2. 항만 / 경매 / 금융 / 첩보
    3. 역할 계열 색인
  15-C. Need Named Candidate Slots
    1. 에테르 슬롯
    2. 프로스트 슬롯
    3. 해양 슬롯
    4. 오벨리스크 슬롯
```

## 15-A. People Worth Seeking

### 1. 크림슨

```text
크림슨
  용의 후예
    드래곤포지 공방
      울프가르 드래곤포지
    연금술 / 공병대장 경계
      드락사르 블레이즈포지 [verify_before_15]
    예언 / 조언자 경계
      카사르 더 시어 [verify_before_15]
  엘드라칸
    학술-전승층
      에리온 드라코비스
    전승 보관층
      오그마
  붉은 사막 부족
    현자 회의
      벨라나 스톰브링어 [verify_before_15]
      아리안 블레이즈하트 [verify_before_15]
```

### 2. 에테르

```text
에테르
  정령연합
    루미라
      엘다라 [source_check_hold / hold reference split]
    기록 / 노래술사 경계
      엘라라 문힘 [verify_before_15]
    자연 율법회 / 생명의 의회 경계
      드라이덴 썬더루트 [verify_before_15]
    외교 사절단 경계
      메라 라일윈드 [verify_before_15]
    그늘까마귀단 경계
      실라스 나이트쉐이드 [verify_before_15]
  마법협회
    서고 / 공방 / 관측 경계
      대런 크레센트 [verify_before_15]
      에드가 룬워커 [verify_before_15]
      칼리스트 [verify_before_15]
  성국
    아스트라르 / 루멘 성채 / 옵시디안 경계
      래퍼티 아르카디아 [verify_before_15]
      대사제 요한 [verify_before_15]
      실라스 블랙쏜 [keep_14_likely]
  왕국연합
    레갈리아 / 아덴브루크 경계
      리아나 실버레이크 [verify_before_15]
  자유도시연합
    포트 넥서스 / 머시너리 게이트 경계
      셀레나 와일드웨이브 [verify_before_15]
      레온 벨가르드 [verify_before_15]
```

### 3. 프로스트

```text
프로스트
  빙하의 성소 / 주술사 원로단
    울프릭 [verify_before_15]
    마리안 더 윈터콜러 [verify_before_15]
    프리야 글래시아 [keep_14_or_verify]
    카이라 프리즌윈드 [keep_14_or_verify]
  퍼마프로스트 공성단 / 아이스포지
    시그리드 프로스트하트 [verify_before_15]
```

### 4. 해양

```text
해양
  황금 함대
    미다스 [verify_before_15]
    해양 실비아 [verify_before_15 / name_collision]
    이소벨 골드리프 [verify_before_15]
  거상 연합
    마르코 바르텔로 [verify_before_15]
    엘레오노라 라 크루즈 [verify_before_15]
    크리스토퍼 델마르 [verify_before_15]
  해적 연합
    골드핑거 바스 [verify_before_15]
    리나 웨이브서프 [verify_before_15]
    에릭 시스트롬 [verify_before_15]
    모로스 [verify_before_15]
  바다의 교단
    오렌 [verify_before_15]
    세일블레스 마리아 [verify_before_15]
```

### 5. 오벨리스크

```text
오벨리스크
  봉인 수호단
    바리온 [verify_before_15]
    아이기스 [verify_before_15 / item_name_collision]
    베스 스크롤 [verify_before_15]
    이안 옵저버 [verify_before_15]
  잊힌 자들의 연합
    카트린 라베로스 [verify_before_15]
    레보니아 셰이드 [verify_before_15]
    우로스 디 모르간 [verify_before_15]
  망자의 왕국
    카론 [verify_before_15]
    세르반 알테르만 [verify_before_15]
    레티시아 모르투스 [verify_before_15]
```

### 6. 범대륙 후기 확장

```text
범대륙 후기 확장
  키르케 영약회
    실비아 [deferred_expansion_hold / hold reference split]
    멜리산드르 [verify_before_15]
```

## 15-C. Need Named Candidate Slots

`15-C`는 live 이름 인물 문서가 아니라,
reference backlog용 슬롯 색인이다.

## Profile Format Carryover

- `15-B. Operational Lines` 아래로 내려가는 `Section_15_Profile_*` 문서는
  `Section_15_Profile_Template.md`의 `3-1. Policy Guard` 형식을 그대로 유지한다.
- 즉 폴더 구조 초안은 `People Worth Seeking` route와 operational profile route를 같이 보여주더라도,
  하위 profile의 policy carryover 형식을 별도로 유지하는 구조다.
- 자유도시/오벨리스크 operational profile 문구는
  `People Worth Seeking` 고정 근거로 역수입하지 않고,
  lower-card carryover reference로만 유지한다.
- 폴더 구조 문서는 이 profile carryover 범주를 참조할 수는 있어도,
  개별 operational profile의 정확한 guard 문장을 대신 정의하지 않는다.
- exact operational guard wording authority는 각 `Section_15_Profile_*` 카드의
  `3-1. Policy Guard`에 남고, 이 구조 초안은 그 wording source를 구조 설계층에서만 참조한다.
- continent sidecar/scout/display wording umbrella는
  lower current-state watch/reference authority로만 읽고,
  이 folder structure draft가 place/institution owner나 candidate build queue를 새로 만들지 않는다.

```text
Need Named Candidate Slots
  에테르
    금서 / 공방 / 관측 / 대서고 / 성채 / 성검 / 서약 / 정령묘
  프로스트
    오로라 평원 / 얼음무덤 언덕 / 푸른 폭풍 요새 / 아이스포지 / 빙하의 성소
  해양
    포트 아우렐리온 / 크로스윈드 포트 / 오라클 바지 / 블랙워터 항구 / 볼트 오브 아우룸
  오벨리스크
    템플 오브 바운더리 / 경계의 보루 / 기억 경매장 / 영원의 기록탑 / 망각의 회랑
```

## Route Hierarchy Lock

frozen route/reference set에서는
`상위 route anchor`와 `보조 place lock`을 섞지 않는다.

| Candidate | Upper Route Anchor | Place Lock | Rule |
|---|---|---|---|
| `울프가르 드래곤포지` | `크림슨 / 용의 후예 / 드래곤포지 공방` | `드래곤포지`, `프라이멀 엠버` | 폴더 route는 `드래곤포지 공방`까지로 고정하고, 개별 시트에서만 재료/화염 전승 place lock을 병기한다. |
| `에리온 드라코비스` | `크림슨 / 엘드라칸 / 학술-전승층` | `엘드라칸 학자 구역`, `용언 도서관` | 폴더 route는 `학술-전승층`으로 고정하고, 학자 구역/용언 도서관은 기능성 place lock으로만 둔다. |
| `오그마` | `크림슨 / 엘드라칸 / 전승 보관층` | `몽상가의 바위`, `지혜의 샘` | 폴더 route는 `전승 보관층`으로 고정하고, 대면/조언과 기억/전승 place lock은 개별 시트에만 둔다. |
| `엘다라` | `에테르 / 정령연합 / 루미라` | `고대수 도서관`, `현자 의회` | 현재는 hold reference split 안의 `source_check_hold / hold reference split`이므로 route 후보만 보존하고 hold reference split 바깥으로 확장하지 않는다. |

## Policy Carryover Lock

- `크림슨` 폴더 route는 씨족 중심 질서와 학술/전승/공방 thin-support를 정리하는 용도지, 전통 귀족국가형 `state_house strong` 근거 선언이 아니다.
- `해양` Operational Lines route는 도시-항만 그림자경제를 정리하는 용도지, `토착 공동체층` 본체 폴더가 아니다.
- `오벨리스크` route는 `nontraditional elite thin-support` 또는 `dark institution` 기능축을 정리하는 용도지, 전통 왕국/귀족국가 복원 route가 아니다.
- `범대륙 후기 확장` route는 5대륙 본선과 분리된 `deferred_expansion_hold / hold reference split` route이며, `실비아`도 그 범위에서만 유지한다.
- 따라서 이 구간의 문장은 route-level reminder일 뿐,
  개별 operational profile을 대체하는 policy text로 쓰지 않는다.

## Conductor Decision

현재 구조는
`closure sync / watch-reference` 기준의 route/reference mock으로 본다.

현재 메인 본선은 live 폴더 생성이나 재해석 reopen을 다루지 않고,
이 초안을 `bridge / routing / revision gate / closure sync watch` 문서들과 맞춰
closure sync / watch-reference 기준으로 유지하는 것이다.

이 초안은 lower-card authority를 재정의하지 않으며,
operational profile의 `3-1. Policy Guard`는 하위 카드층에서 그대로 우선한다.
exact operational guard wording authority도 상위 구조 초안이 아니라
각 `Section_15_Profile_*` 카드의 `3-1. Policy Guard`에 남는다.

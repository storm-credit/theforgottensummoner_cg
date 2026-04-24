# Section 15 Intake Structure

이 문서는 `15번 인물 백과`의
흩어진 인물 회수 기준을 정리한 intake reference guard다.

핵심 원칙은 이미 고정되어 있다.

- `14번`에 있는 인물은 빼지 않는다.
- `15번`은 다른 문서에 흩어진 인물을 회수하는 축이다.
- 지금은 실제 이동이 아니라 `회수 기준`만 보존한다.

reference intake reading은
`Section_15_Group_Index.md`,
`Section_15_Profile_Draft_Index.md`,
`Section_15_Subline_Register.md`,
`Section_15_Operational_Lines_Track.md`,
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

## Intake Buckets

### 1. Faction Embedded

- 세력 문서 본문 안에서만 존재하는 인물
- 예:
  - 가문 문서의 실무자
  - 길드 지부장
  - 상회 대표
  - 정보망 연락책

### 2. Region Embedded

- 지역 문서나 도시 문서, 생활상 문서에만 흩어진 인물
- 예:
  - 항구 감독관
  - 성문 수비대장
  - 시장 조정관
  - 지하도 안내인

### 3. Event Embedded

- 사건 문서, 역사 문서, 외교 문서에서만 등장하는 인물
- 예:
  - 조약 체결자
  - 내전 반란 지도자
  - 한 번 언급되는 암살 대상

### 4. Organization Mesh

- 국가/가문이 아니라 조직망에 매달린 인물
- 예:
  - 국제 길드 연합 규정 담당자
  - 대륙 무역 연맹 후원 중개자
  - 그림자 첩보망 현장 관리자
  - 철의 금융 연맹 채무 집행관

### 5. Orphan Recovery

- 현재처럼 폴더 바깥에 떨어진 고아 인물
- 예:
  - `이리나 폰 루즈`
  - `칼리크 디트리히`

## Intake Fields

`15번` 후보는 최소 아래 필드를 가져야 한다.

- 이름
- source path
- candidate anchor
- bucket
- current status
- relation usefulness
- move now / hold / promote to 14
- policy guard

## First Intake Rule

아래 셋 중 하나라도 만족하면 `15번 후보`로 본다.

1. `14번` 폴더에 정식 앵커가 없다.
2. 세력/지역/사건 문서 안에서만 반복 등장한다.
3. 관계망에서 연결 노드 역할이 큰데 영웅 축은 약하다.

## Promote to 14 Rule

반대로 아래를 만족하면 `15번`이 아니라 `14번 유지 또는 승격` 여부를 가르는 reference 기준으로 본다.

1. 액트 핵심 갈등에 직접 개입한다.
2. 반복적으로 전투, 정치, 관계의 중심축에 선다.
3. 독립 인물문서가 이미 있고 영웅 축에서 기능한다.

## Reference Candidates

### Hold in 14, Tag for 15 Review

- `이리나 폰 루즈`
- `칼리크 디트리히`

둘 다 현재는 `14번 보류`이며, 구조적으로는 `15번` 회수 판단 대상이다.

## Policy Intake Rule

- intake 단계에서도 candidate를 검토하는 순간
  이 카드가 어떤 층을 보강하는지와 무엇으로 오독하면 안 되는지를 같이 적는다.
- 자유도시 운영층이면 `urban_market / shadow_port / debt-enforcement` 축으로,
  오벨리스크 제도 운영층이면 `nontraditional elite thin-support / dark institution` 축으로 먼저 읽는다.
- 즉 intake는 단순 회수만을 적는 문서가 아니라,
  `policy guard` 없이 카드를 기록하지 않는 reference gate로 유지한다.
- subline draft와 group draft도 이 intake rule을 따르는 하위 reference로 읽는다.
- operational profile로 분류된 카드들은
  `Section_15_Profile_Template.md`의 `3-1. Policy Guard` 형식을 그대로 유지한다.
- representative subline pair
  (`Port Authority / Black Auction / Gravewell / Counterfeit Workshop`)는
  draft/profile 교차감사가 닫힌 샘플로 유지하고,
  intake는 새 drift가 생겼을 때만 해당 pair를 다시 검토한다.
- intake는 card를 어느 축으로 받을지 분류하는 입구일 뿐,
  operational profile의 정확한 guard 문장을 대신 작성하는 문서는 아니다.
- 따라서 intake 문구는 lower-card authority를 참조만 하고,
`People Worth Seeking` 승인 논리나 상위 summary로 역수입하지 않는다.
- intake는 provisional guard family만 배정하고,
  최종 operational guard wording은 downstream `Section_15_Profile_*` 카드의 `3-1. Policy Guard`에서 작성/유지한다.
- group draft와 subline draft도 intake 방향을 상속할 뿐,
  profile-level guard text 권한을 가져가지는 않는다.
- exact operational guard wording authority는 각 `Section_15_Profile_*` 카드의
  `3-1. Policy Guard`에 남고, intake는 그 wording source를 intake classification 층에서만 참조한다.
- subline 확장으로 실제 내려간 경우에는
  exact operational guard wording authority가 각 `Section_15_Subline_Profile_*` 카드의
  `3-1. Policy Guard`에 남고, intake는 그 wording source를 intake 층에서만 참조한다.
- continent sidecar/scout/display wording umbrella도
  lower current-state watch/reference authority로만 읽고,
  intake가 place/institution owner나 candidate build queue를 새로 만들지 않는다.

## Conductor Note

`15번`은 쓰레기통이 아니라,
영웅 서사를 지탱하는 `중간 인간층`을 모아두는 reference layer여야 한다.

즉 `14번`이 영웅의 첨탑이라면,
`15번`은 그 첨탑 아래에 실제 세계를 떠받치는 사람들의 층이다.
그리고 exact operational guard wording authority는 이 intake 문서가 아니라
각 `Section_15_Profile_*` 카드의 `3-1. Policy Guard`에 남는다.

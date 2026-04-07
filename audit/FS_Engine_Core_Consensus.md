# FS Engine Core Consensus

이 문서는 오케스트라 전문가 논의를 바탕으로
`FS Engine`의 필수 코어를 합의안 형태로 정리한 것이다.

핵심 결론:

- `역설계`와 `복선 회수`만으로는 부족하다.
- FS 엔진의 본체는
  `설정을 잘 만드는 장치`이면서 동시에
  `설정이 섞이지 않게 유지하는 장치`여야 한다.

## Final Core Set

### P0. Reverse Design Engine

- 흩어진 문서와 파편을 보고
  나중의 정본 구조를 거꾸로 복원한다.
- `8번`, `14번`, `15번`, 레거시, 고아 문서 정리에 필수.

### P0. Canon Tier Engine

- 모든 항목을 최소한 아래로 분류한다.
  - `Hard Canon`
  - `Soft Canon`
  - `Open Question`
  - `Deprecated / Legacy`
- 충돌 시 무엇이 맞는지보다 먼저
  무엇이 몇 티어인지를 판정한다.

### P0. Archive Routing Engine

- 새 정보가 들어오면 어디에 꽂힐지 정한다.
  - `14 Hero Archive`
  - `15 Named Notables`
  - `15 Operational Lines`
  - `8 Faction Archive`
  - `hold`
  - `legacy quarantine`
- 큰 설정집은 내용보다 `배치`가 먼저다.

### P0. Relationship Ledger

- 인물-인물, 인물-조직 관계를 타입과 시점으로 기록한다.
- 최소 타입:
  - `ally`
  - `former_ally`
  - `enemy`
  - `rumor_only`
  - `crossed_paths`
  - `asymmetric_awareness`
  - `intermittent_alignment`

### P0. Chronology / Causality Engine

- 사건, 이동, 부재, 만남, 소문이 시간축에서 말이 되게 묶는다.
- 우연 재회와 작위적 교차를 막는 핵심 장치다.

### P0. Act Outcome Ledger

- 액트마다 무엇이 바뀌었는지 기록한다.
  - 동맹
  - 결별
  - 상실
  - 획득
  - 상처
  - 부채
- 복선 회수와 별개로 `결과`를 보존한다.

### P1. Foreshadow / Payoff Registry

- 복선 ID, 배치 위치, 회수 예정 위치, 회수 상태를 추적한다.
- 인물, 약속, 유품, 소문, 결번, 상처까지 등록 가능해야 한다.

### P1. Plausibility Engine

- 이 설정이 왜 지금 여기서 성립하는지 검사한다.
- 기본 체크:
  - 동기
  - 비용
  - 제약
  - 대가
  - 이전 사건과의 연결

### P1. Naming Normalization Engine

- 대표 표기, 허용 별칭, 금지 표기, 레거시 표기를 분리한다.
- 작업용 라벨과 세계 안 `display canon` 이름도 분리해 관리한다.

### P1. Faction / House / Clan / Guild Layer Engine

- 국가보다 아래, 개인보다 위에 있는 중간 사회층을 고정한다.
- 이 층이 없으면 세계가 국가와 영웅만 있는 배경으로 무너진다.

### P1. Legacy Quarantine Engine

- `_Legacy_`, `Backup`, 구버전 초안은 삭제보다 먼저 격리한다.
- 참고는 가능하지만 자동 인용되면 안 된다.

## Optional but Strong Modules

### P2. Source Priority Engine

- `어떤 문서가 상위 근거인가`를 정한다.

예:

1. 세계관 헌장
2. 대륙 프레임
3. 세력 루트
4. 인물 문서
5. 소문성 기록

### P2. State Label Engine

- `active`, `hold`, `rumor`, `legacy`, `duplicate_candidate`, `needs_merge`
  같은 상태 라벨을 붙인다.

### P2. Revision Gate Engine

수정 전 최소 확인:

1. canon tier는?
2. 명칭은 정규화됐나?
3. 어디로 라우팅되는가?
4. 연표/관계와 충돌 없는가?
5. 충돌 시 hold 처리했는가?

## Consensus Summary

전문가 의견을 합치면
FS 엔진의 최소 코어는 아래 7개가 가장 중요하다.

1. `Reverse Design`
2. `Canon Tier`
3. `Archive Routing`
4. `Relationship Ledger`
5. `Chronology / Causality`
6. `Act Outcome Ledger`
7. `Foreshadow / Payoff Registry`

그 다음이:

8. `Plausibility`
9. `Naming Normalization`
10. `Faction / House / Clan / Guild Layer`
11. `Legacy Quarantine`

## Conductor Note

한 줄 결론:

FS 엔진은
`관계와 시간축 위에 설정을 올리고,
그 설정이 섞이지 않게 유지하는 엔진`이어야 한다.

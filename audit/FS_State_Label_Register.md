# FS State Label Register

이 문서는 FS Lore Engine이
설정, 인물, 세력, 아이템, 장소에 붙이는
상태 라벨을 정의한다.

라벨은 삭제나 확정을 대신하지 않는다.
오케스트라가 지금 무엇을 믿고,
무엇을 보류하고,
무엇을 검증해야 하는지 표시하기 위한 장치다.

## Canon Labels

### `hard_canon`

현재 정본으로 강하게 고정한다.

조건:

- 상위 비전과 충돌하지 않는다.
- 여러 문서에서 반복적으로 지지된다.
- 이름, 소속, 기능, 관계가 안정적이다.

### `soft_canon`

현재 유력하지만 바뀔 수 있다.

조건:

- 방향은 맞지만 세부 명칭이나 폴더 위치가 흔들린다.
- 인물/세력의 기능은 분명하지만 액트 연결이 미완성이다.

### `active_working`

현재 작업 기준으로 쓰지만 아직 정본 선언은 아니다.

조건:

- 오케스트라가 비교와 정리를 위해 임시 채택했다.
- 추후 원본 대조나 사용자 확인이 필요할 수 있다.

## Review Labels

### `verify_before_15`

15번으로 회수하기 전에
14번 영웅백과에 이미 독립 시트가 있는지 확인해야 한다.

사용 예:

- 영웅식 이름과 기능을 가진 자유도시 인물
- 마법협회 지원 인물
- Named Notables와 14 중심 영웅 사이에 걸친 인물

### `named_notable_candidate`

15번 Named Notables 후보.

조건:

- 세계 안에서 이름이 알려진 명사형 인물이다.
- 현자, 저술가, 연금술사, 장인, 감정사, 항해사, 지도 제작자 같은 층이다.
- 중심 영웅은 아니지만 찾아갈 이유가 있다.

### `operational_line`

15번 Operational Lines 후보.

조건:

- 개별 유명 인물보다 조직 작동을 보여주는 실무층이다.
- 항만, 경매, 금융, 첩보, 위조, 운반, 용병 운영 같은 기능을 가진다.
- 표면명은 나중에 판타지 톤으로 재명명될 수 있다.

### `display_canon_candidate`

세계 안 표면명 후보.

조건:

- 작업용 기능 라벨을 판타지 명칭으로 바꾸기 위한 후보명이다.
- 아직 원본 폴더명을 직접 바꾸지 않는다.

## Conflict Labels

### `conflict`

문서 경로, 세력 소속, 본문 맥락, 명칭이 서로 맞지 않는다.

처리:

- 바로 이동하지 않는다.
- `Section_14_Conflict_Register.md` 또는 해당 충돌 등록부에 올린다.

### `macro_overlink`

거시 엔진, 7축 구조, 범대륙 연결 등이
과하게 붙어 있어 실제 관계처럼 보일 위험이 있다.

처리:

- 관계 장부에 바로 올리지 않는다.
- 먼저 실관계인지 메타 구조인지 분리한다.

### `legacy_hold`

레거시, 백업, 손상 루트, 폐기 후보를 보류한다.

처리:

- 삭제하지 않는다.
- 정본처럼 쓰지 않는다.
- 필요하면 Quarantine 문서에 연결한다.

### `open_question`

판단 보류.

조건:

- 현재 증거로 확정하면 위험하다.
- 사용자 의도, 액트 구조, 원본 대조가 더 필요하다.

### `duplicate_candidate`

중복 후보.

조건:

- 같은 이름, 비슷한 영문 표기, 같은 기능의 문서가 둘 이상 보인다.
- 아직 어느 쪽을 대표 정본으로 삼을지 결정하지 않았다.

처리:

- 바로 병합하지 않는다.
- Source Priority와 Revision Gate를 통과한 뒤 `needs_merge`로 올린다.

### `needs_merge`

병합 필요.

조건:

- 중복 후보 중 어느 자료를 남길지 방향이 잡혔다.
- 단, 실제 병합 전 관계, 이름, 폴더 라우팅 영향 검토가 필요하다.

처리:

- 원본은 수정하지 않는다.
- `cg` 안에서 병합안이나 display canon 후보로만 관리한다.

## Information-State Note

`fact`, `rumor`, `misread`, `propaganda` 같은 단어는
`FS_Rumor_Fact_Register.md`의 로컬 정보 상태다.

전역 상태 라벨이 필요할 때는
이 문서의 `hard_canon`, `soft_canon`, `open_question`, `conflict` 등을 함께 붙인다.

## Current Label Examples

| Target | Label | Note |
|---|---|---|
| `14 = 서사 중심 영웅` | `hard_canon` | 사용자와 오케스트라가 고정한 구조 |
| `15 = Named Notables + Operational Lines` | `hard_canon` | 15번은 잡캐 창고가 아니라 분리 백과 |
| `카르텔` 표면명 | `display_canon_candidate` | 기능 분류로는 가능하나 표면명은 완화 필요 |
| `Hidden Exchange` 등 Operational Group | `display_canon_candidate` | 세계 안 명칭은 `은막 교역회` 같은 후보로 별도 관리 |
| 자유도시 실무 라인 | `operational_line` | 정본명은 별도 검토 |
| `모이라/레이나/이사벨` 계열 | `verify_before_15` | 14 신호 확인 필요 |
| `울프가르/에리온/오그마` | `named_notable_candidate` | 크림슨 안정 15 시트 시험 후보 |
| `벨라나/아리안` | `verify_before_15` | 현자회 명사 가치가 있으나 SS/S급 신호가 강함 |
| 손상 범대륙 루트 | `legacy_hold` | 바로 정본화 금지 |

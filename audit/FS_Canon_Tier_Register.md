# FS Canon Tier Register

이 문서는 FS 엔진의 `Canon Tier Engine`을
실제로 운용하기 위한 등록부다.

목적:

- 어떤 정보가 정본인지
- 어떤 정보가 보류인지
- 어떤 정보가 레거시인지
- 어떤 정보가 소문인지

를 항목 단위로 분리한다.

## Tier Definitions

### Hard Canon

- 정본으로 바로 참조하는 정보
- 충돌 시 우선권이 높다

### Soft Canon

- 유력하나 수정 가능성이 남아 있는 정보
- 인용 가능하나, 확정처럼 쓰지 않는다

### Open Question

- 아직 결론을 내리지 못한 항목
- 참조는 가능하지만 정본처럼 확장하지 않는다

### Rumor

- 작중에서 떠도는 정보
- 세계 안에 존재하지만 사실로 확정하지 않는다

### Deprecated / Legacy

- 구상 구버전, 백업, 폐기 후보
- 자동 인용 금지

## Register

| Subject | Scope | Tier | Source Priority | Recorded Use | Recorded Action | Note |
|---|---|---|---|---|---|---|
| `14 = 서사 중심 영웅` | `archive policy` | `Hard Canon` | `workflow` | `active` | `maintain` | `14`는 중심 영웅축으로 유지 |
| `15 = People Worth Seeking + Operational Lines` | `archive policy` | `Hard Canon` | `workflow` | `active` | `maintain` | `15`는 이중 레이어로 운영 |
| `동양 / 무협 제외` | `tone policy` | `Hard Canon` | `vision` | `active` | `maintain` | 다른 크로니클로 분리 |
| `범대륙은 후기 확장` | `expansion policy` | `Hard Canon` | `master plan` | `active` | `maintain` | 메인 축보다 후순위 |
| `에리온 드라코비스 = 15 People Worth Seeking` | `character routing` | `Soft Canon` | `audit` | `candidate` | `promote_if_stable` | 현재 `named_notable_candidate / stable_15_workset / grade_caution / name_collision_watch` |
| `울프가르 드래곤포지 = 15 People Worth Seeking` | `character routing` | `Soft Canon` | `audit` | `candidate` | `promote_if_stable` | 장인형 명사로 강함 |
| `오그마 = 15 People Worth Seeking` | `character routing` | `Soft Canon` | `audit` | `candidate` | `promote_if_stable` | 전승 보관자축 |
| `실비아 = deferred supranational named boundary` | `character routing` | `Soft Canon` | `audit` | `hold` | `deferred_hold_split` | 현재 `deferred_expansion_hold / hold reference split / name_collision_watch` |
| `멜리산드르 = 14/15 경계` | `character routing` | `Open Question` | `audit` | `hold` | `dual_review` | 세력 최고위와 명사성이 겹침 |
| `카사르 더 시어 = 14/15 경계` | `character routing` | `Open Question` | `audit` | `hold` | `dual_review` | 예언자/조언자/영웅축 중첩 |
| `Operational Lines working labels` | `naming policy` | `Soft Canon` | `audit` | `active` | `replace_with_display_candidates` | 작업용 구조 라벨 |
| `_Legacy_ / Backup 문서군` | `legacy handling` | `Deprecated / Legacy` | `legacy policy` | `quarantined conceptually` | `keep_isolated` | 참고만 허용 |

## Conductor Reading Rule

- 충돌을 발견하면 바로 고치지 않고 먼저 여기서 티어를 붙인다.
- `Open Question`은 다른 문서에서 정본처럼 확장하지 않는다.
- `Deprecated / Legacy`는 이름이 멋져도 자동 복귀시키지 않는다.

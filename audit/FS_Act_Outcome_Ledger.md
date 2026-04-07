# FS Act Outcome Ledger

이 문서는 FS 엔진의 `Act Outcome Ledger` 운용판이다.

복선 회수와 별개로,
각 액트가 끝날 때 무엇이 실제로 바뀌었는지를 남긴다.

## Fields

| Act / Arc | Subject | Change Type | Before | After | Cost | Carry Forward | Note |
|---|---|---|---|---|---|---|---|

## Seed Ledger

| Act / Arc | Subject | Change Type | Before | After | Cost | Carry Forward | Note |
|---|---|---|---|---|---|---|---|
| `FS-ACT-SEED-01` | `세실리아 메르카토르 vs 자유도시 그림자 경제` | `awareness_shift` | `공적 상업 질서 중심` | `그림자 구조를 더 직접 의식` | `정치적 압박 증가` | `도미닉/로렌조/벤투라 축 심화` | contact table 기반 시드 |
| `FS-ACT-SEED-02` | `키르케 영약회` | `dependency_shift` | `임상 교착 상태` | `에반 개입으로 돌파 가능성 발생` | `맹목적 의존 형성` | `멜리산드르/실비아 축 변화` | 세력 문서 기반 |
| `FS-ACT-SEED-03` | `엘드라칸 지식축` | `access_shift` | `금서 접근 제한` | `에반 개입 시 조건부 해금 가능` | `위험 인지 상승` | `에리온/오그마 축 강화` | 엘드라칸 문서 기반 |
| `FS-ACT-SEED-04` | `용의 후예 제작축` | `artifact_shift` | `장인 지식은 내부 축적` | `외부 영웅과 접점 가능` | `전설 무구 개입 리스크` | `울프가르/드락사르 축 확장` | 드래곤포지 관련 |

## Conductor Rule

- 인물이나 세력 문서를 늘리기 전에,
  액트가 실제로 무엇을 바꾸는지 먼저 적는다.
- `Before`와 `After`가 비슷하면 그 액트는 다시 봐야 한다.

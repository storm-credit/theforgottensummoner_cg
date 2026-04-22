# Section 8 Root Label Map

이 문서는 `Section 8` 최상위 루트에
`canonical_root / quarantine_root / legacy_root` 라벨을 먼저 고정하기 위한 분류표다.

## Input

- `audit/Section_8_Root_Findings.md`
- `audit/Section_8_Root_Normalization_Plan.md`
- `audit/reports/factions_root_audit.md`

## Root Label Table

| Top-Level Entry | Type | Root Label | Why |
|---|---|---|---|
| `01-8. 세력 아카이브 (국가·조직 정리).md` | file | `canonical_root` | `Section 8` 본문 인덱스이자 정본 루트 기준 파일이다. |
| `1. 에테르 대륙 (Ether Continent)` | dir | `canonical_root` | 5대륙 본체 루트다. |
| `2. 크림슨 대륙 (Crimson Continent)` | dir | `canonical_root` | 5대륙 본체 루트다. |
| `3. 프로스트 대륙 (Frost Continent)` | dir | `canonical_root` | 5대륙 본체 루트다. |
| `4. 오벨리스크 대륙 (Obelisk Continent)` | dir | `canonical_root` | 5대륙 본체 루트다. |
| `5. 해양 대륙 (Oceanic Continent)` | dir | `canonical_root` | 5대륙 본체 루트다. |
| `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)` | dir | `canonical_root` | 범대륙 후기 확장 축이지만 현재 정본 루트 후보로 유지한다. |
| `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))` | dir | `quarantine_root` | 이름 손상과 중복이 확인된 충돌 경로다. 정본 루트로 읽지 않는다. |
| `_Legacy_중립세력 (Backup)` | dir | `legacy_root` | 백업/레거시 경로로 보이며, 정본 판단에 직접 쓰지 않는다. |

## Conductor Reading

현재 `Section 8` 루트 판단은 아래처럼 잠근다.

1. `canonical_root`만 정본 구조 판단의 기본 입력으로 쓴다.
2. `quarantine_root`는 손상/중복/오염 여부 비교용으로만 쓴다.
3. `legacy_root`는 삭제 대상이 아니라 보류/격리 대상으로 먼저 둔다.

## Why `legacy_root` Stays Reference-Only

- `_Legacy_중립세력 (Backup)`은 이름 자체가 `Legacy`와 `Backup`을 함께 들고 있어, 현재 정본 구조보다 과거 작업 흔적일 가능성이 더 높다.
- `Section 8` 루트에는 이미 정상 `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)`와 손상된 중복 루트가 같이 남아 있어, 여기서 `legacy_root`까지 활성 판단에 섞으면 기준점이 세 겹으로 흔들린다.
- 현재 본선은 `closure sync / watch-reference`라서, 레거시 경로를 활성 입력으로 올리면 구조 감사와 내용 감사가 다시 뒤섞인다.
- `legacy_root`는 활성 경로와 같은 이름 또는 유사한 내용을 가질 수 있어도, 부모 라벨이 다르기 때문에 바로 병합 근거로 쓰면 오판 가능성이 크다.
- 지금 단계에서 `_Legacy_`는 `정본 판단 입력`이 아니라 `비교 / 참고 / 누락 확인` 용도로만 쓰는 편이 가장 안전하다.
- 즉 `_Legacy_중립세력 (Backup)`은 보존 가치가 있을 수 있으므로 지우지 않지만, 구조 정규화가 끝나기 전까지는 `reference-only`로 두는 것이 맞다.

## Stop Rules

- `quarantine_root`를 `canonical_root`로 자동 승격하지 않는다.
- `legacy_root`를 활성 경로와 바로 병합하지 않는다.
- 이름이 비슷해도 부모 루트 라벨이 다르면 자동 병합하지 않는다.
- 루트 라벨이 없는 상태에서 이동, 삭제, 합치기를 하지 않는다.

## Watch Use

이 분류표는 새 이동/병합 실행표가 아니라,
`root / structure / mismatch / P2 handoff` watch-reference 기준에서
아래 기준을 확인하는 reference로 쓴다.

1. `Section 8` 루트별 `section_style / mixed_keep / section_style_reclassify` closure 상태
2. 대륙 spine과 맞지 않는 `spine_mismatch` 후보 분리 상태
3. `Supranational & Neutral` 충돌 루트의 비교 샘플링 readiness
4. `_Legacy_` 경로의 보존 가치와 중복 위험 분리 상태
5. 핵심 canonical 세력의 1차 구조 라벨 맵 유지 상태

사용 문서:

- `audit/Section_8_Structure_Labeling_Queue.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`

## Conductor Decision

이 문서는 지금 단계에서 `Section 8` 루트 watch 기준을 확인할 때
가장 먼저 보는 고정 분류표로 사용한다.

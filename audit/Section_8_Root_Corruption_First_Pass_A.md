# Section 8 Root Corruption First Pass A

이 문서는 `Section 8` 루트 감사에서
가장 먼저 잡아야 하는 `P0 root_corruption`을
이미 잠긴 정본 판정으로 유지하는 첫 패스 reference다.

이 reference의 대상은 아래 셋이다.

1. `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)`
2. `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))`
3. `_Legacy_중립세력 (Backup)`

## Input

- `audit/reports/factions_root_audit.md`
- `audit/Section_8_Root_Findings.md`
- `audit/Section_8_Root_Label_Map.md`
- `audit/Section_8_Root_Normalization_Plan.md`
- `audit/Section_8_Standard_Spine.md`

## Root Conflict Snapshot

현재 `cg` 기준으로 확정 가능한 사실은 아래다.

1. 범대륙 루트는 정상 이름과 손상 이름이 동시에 존재한다
2. `_Legacy_중립세력 (Backup)`도 루트 레벨에 남아 있다
3. 따라서 범대륙 축은 `canonical / quarantine / legacy`를 먼저 고정하지 않으면
   이후 구조, spine, display canon 판단이 모두 흔들린다

이번 세션에서 원본 `X:` 드라이브를 직접 재귀 비교하진 못했지만,
`cg` 안의 root audit 문서들은 이미 이 충돌을
루트 레벨 `P0` 문제로 일관되게 고정하고 있다.

## 1. Canonical Root

### Reading

정상 범대륙 루트는
`6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)` 하나만
`canonical_root`로 유지하는 편이 맞다.

이유는 아래와 같다.

1. 다른 `1~5 대륙` 루트와 같은 네이밍 체계를 따른다
2. `Section_8_Root_Label_Map.md`에서 이미 유일한 `canonical_root`로 잠겨 있다
3. 이후 `display canon` 보정은 가능해도
   실제 원본 경로 기준은 하나로 유지해야 구조 판단이 흔들리지 않는다

### Conductor Judgment

- root status: `canonical_root_keep`
- 운영 규칙:
  - 정상 범대륙 루트만 정본 구조 판단의 기본 입력으로 사용한다
  - 이후 하위 샘플링과 subtree 비교도 이 루트를 기준축으로 삼는다

## 2. Broken-Name Duplicate Root

### Reading

`6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))`는
단순 변주가 아니라
`이름 손상 + 중복 충돌 루트`로 보는 게 맞다.

핵심 이유는 아래다.

1. `마립`은 현재 정상 표기 체계 어디에도 연결되지 않는다
2. 동일 루트 번호 `6.` 아래에 정상 이름과 손상 이름이 동시에 존재한다
3. 이 경로를 정본 판단에 섞으면
   정상 루트와 손상 루트가 같은 수준에서 경쟁하게 된다

현재 watch 기준에서 중요한 건
이 루트가 얼마나 많은 하위 중복을 갖는가보다 먼저,
루트 자체를 `quarantine_root`로 유지하는 판정이다.

### Conductor Judgment

- root status: `quarantine_root_keep`
- 운영 규칙:
  - `Supranational & 마립 세력 (Neutral)`는 `root_corruption` 사례로 고정한다
  - 정상 루트와 자동 병합하거나 정본 경로로 승격하지 않는다
  - 하위 중복률은 subtree 샘플링 큐에서만 따로 본다

## 3. Legacy Backup Root

### Reading

`_Legacy_중립세력 (Backup)`은
손상 루트와 성격이 다르다.

이 경로는 이름 오염보다는
과거 작업 흔적과 백업 성격이 더 강하다.

따라서 이 단계에서는
`reference-only legacy root`로 격리 유지하는 편이 정확하다.

핵심 이유는 아래다.

1. 이름 자체에 `Legacy`, `Backup`이 직접 박혀 있다
2. 활성 정본 경로와 같은 레벨에 두면 판정축이 세 겹으로 흔들린다
3. 그렇다고 곧바로 지우면 비교 근거와 복구 경로도 같이 사라진다

### Conductor Judgment

- root status: `legacy_root_keep`
- 운영 규칙:
  - `legacy_root`는 격리 보존 상태로 다룬다
  - 정본 구조 판단에는 직접 쓰지 않고 비교/참조에만 사용한다

## First Pass Result

| Entry | Current Role | Risk | Result | Conductor Note |
|---|---|---|---|---|
| `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)` | canonical candidate | low | `canonical_root_keep` | 범대륙 정본 기준 루트는 이 경로 하나로 고정 |
| `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))` | broken-name duplicate | `root_corruption` | `quarantine_root_keep` | 이름 손상과 루트 중복이 확인되어 정본 판단에서 제외 |
| `_Legacy_중립세력 (Backup)` | legacy backup | `legacy_drift` | `legacy_root_keep` | 삭제하지 않고 reference-only 경로로 격리 유지 |

## Conductor Rules

- 루트 이름이 비슷해도 부모 라벨이 다르면 자동 병합하지 않는다.
- 손상 루트는 하위 내용이 많아 보여도 정본 판단에 바로 끌어오지 않는다.
- `legacy_root`는 보존 가치와 정본 가치를 분리해서 읽는다.
- 범대륙 루트는 `display canon` 보정과 실제 경로 정본화를 같은 작업으로 섞지 않는다.

## Conductor Decision

이번 패스에서 잠그는 핵심은 하나다.

`범대륙 루트 문제는 내용 이전에 경로 계급 문제다.`

따라서 실제 실측이 재개될 때는
정상 `canonical_root`와 `quarantine_root`의 하위 subtree를 샘플링해
중복률과 손상 범위는 queue 기준으로 관찰 기록만 보강하고,
동시에 `P2 section_style_forced_on_place_network` 후보를 별도 큐로 관리한다.

샘플링 순서는
`Section_8_Root_Subtree_Sampling_Queue.md`에 고정한다.

# Section 8 Spine Mismatch First Pass C

이 문서는 `Section_8_Spine_Mismatch_Queue.md`의
남은 `P0 root_corruption`과 `P2 section_style_forced_on_place_network`를
1차로 다시 읽은 시트다.

## Input

- `audit/Section_8_Root_Label_Map.md`
- `audit/Section_8_Root_Findings.md`
- `audit/Section_8_Root_Normalization_Plan.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/reports/factions_root_audit.md`

## 1. Supranational Broken Root

### Risk

- risk category: `root_corruption`
- canonical path: `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)`
- compared path: `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))`
- support path: `_Legacy_중립세력 (Backup)`

### Mismatch Re-read

이 항목의 핵심 위험은
구조 스타일보다 `root label discipline`이 무너지는 것이다.

현재 기준에서 잠기는 건 아래다.

1. 정상 `Supranational & Neutral`만 `canonical_root`
2. 손상된 `Supranational & 마립`은 `quarantine_root`
3. `_Legacy_중립세력 (Backup)`은 `legacy_root / reference-only`

즉 여기서 막아야 하는 건
손상 루트와 레거시 루트를
정상 범대륙 루트와 같은 활성 입력으로 섞는 것이다.

### Conductor Judgment

- 유지 판단: `mismatch_keep`
- 운영 규칙:
  - 손상 루트는 비교/샘플링 외 용도로 쓰지 않는다
  - 정상 루트와 손상 루트를 같은 활성 입력으로 읽지 않는다
  - `_Legacy_`는 reference-only 비교 경로로만 유지한다

## 2. Place-Pressure Family

### Risk

- risk category: `section_style_forced_on_place_network`
- candidate family:
  - `바다의 교단`
  - `오로라 평원 / 빙하의 성소` 계열
  - `본 마켓 / 잊힌 시장 / 서플라이 포트 알파` 계열

### Mismatch Re-read

이 계열의 핵심 위험은
`장소 압력이 강하다`는 이유만으로
곧바로 place-pressure structure 또는 구조 오류로 읽는 것이다.

현재 기준에서 잠기는 건 아래다.

1. 일부 세력은 실제 루트 문법이 `section_style`이다
2. 장소 밀도가 높아도 그것만으로 place-pressure structure를 뜻하지는 않는다
3. 따라서 지금 관리해야 하는 건 `place pressure strong` 메모이지,
   자동 구조 재분류가 아니다

즉 이 항목의 핵심은
`place-pressure`와 `structure label`을 분리해 기록하는 것이다.

### Conductor Judgment

- 유지 판단: `watch_keep`
- 운영 규칙:
  - `place pressure strong`은 내용 메모로 유지한다
  - 구조 라벨은 실제 루트 문법 기준으로만 바꾼다
  - 장소 밀도만으로 `mixed_keep`이나 place-pressure structure를 자동 승격하지 않는다

## First Pass Result

| Candidate | Risk Category | Current Structure Read | Mismatch Result | Conductor Note |
|---|---|---|---|---|
| `Supranational & 마립` broken root | `root_corruption` | `quarantine_root` | `mismatch_keep` | 손상 루트는 활성 입력에서 제외 유지 |
| `_Legacy_중립세력 (Backup)` | `root_corruption` support | `legacy_root / reference-only` | `mismatch_keep` | 비교/참고 전용으로 유지 |
| `place-pressure family` | `section_style_forced_on_place_network` | `section_style` 우세, 일부 `mixed_keep` | `watch_keep` | 장소 압력과 구조 라벨을 분리 기록 |

## Conductor Decision

이 패스에서 잠그는 핵심은 둘이다.

1. `P0 root_corruption`은 구조 라벨 문제가 아니라 `root label discipline` 문제다.
2. `P2 place-pressure`는 구조 오류 확정보다 `place pressure strong` 메모 체계로 관리하는 편이 맞다.

따라서 mismatch 1차 사이클의 다음 단계는
새 후보를 더 늘리기보다,
현재 잠근 `structure label / mismatch / place pressure`를
서로 충돌 없이 유지하는지 점검하는 것이다.

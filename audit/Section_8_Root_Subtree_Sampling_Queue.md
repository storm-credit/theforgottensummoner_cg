# Section 8 Root Subtree Sampling Queue

이 문서는 `Section_8_Root_Corruption_First_Pass_A.md` 다음 단계에서
실제로 어떤 하위 subtree를 샘플링할지 고정하는 큐다.

이번 큐의 목적은 둘이다.

1. `canonical_root`와 `quarantine_root`의 중복 범위를 실측할 준비를 한다
2. `legacy_root`를 무엇과 비교해야 하는지 순서를 정한다

## Input

- `audit/reports/factions_root_audit.md`
- `audit/Section_8_Root_Findings.md`
- `audit/Section_8_Root_Label_Map.md`
- `audit/Section_8_Root_Corruption_First_Pass_A.md`

## Sampling Targets

| Priority | Target Path | Root Role | Why Sample First | Expected Read |
|---|---|---|---|---|
| `S1` | `6. 범대륙 초국가 및 중립 세력 (Supranational & Neutral)` | `canonical_root` | 범대륙 정본 기준 루트라 모든 상대 비교의 기준점이 된다 | 정상 범대륙 하위 문법과 실제 section 분기 확인 |
| `S1` | `6. 범대륙 초국가 및 중립 세력 (Supranational & 마립 세력 (Neutral))` | `quarantine_root` | 이름 손상과 중복 충돌이 확인된 `P0` 핵심 대상이다 | 손상명이 하위까지 반복되는지, 단순 복제인지 부분 오염인지 확인 |
| `S1` | `_Legacy_중립세력 (Backup)` | `legacy_root` | 삭제가 아니라 reference-only 격리 유지가 맞는지 확인해야 한다 | 백업 흔적, 구형 naming, 비교 가치 확인 |
| `S2` | `6-2. 대륙 무역 상단 (Syndicates)\06. 테라바이트 마석 유통단 (Terabyte Aether Traders)` | `canonical_root subtree` | 현대적 어휘와 범대륙 분기 오염이 함께 보이는 대표 샘플이다 | display canon 문제와 root corruption 문제를 분리해 읽기 |
| `S2` | `6-4. 마도 공학 연맹 (Megacorps)\01. 에테르 마동기어 공방 (Aether Machina Forge)` | `canonical_root subtree` | 범대륙 하위에서 가장 현대 기업물 결이 강한 대표 샘플이다 | naming drift와 subtree 문법을 함께 확인 |
| `S3` | `1. 에테르 대륙 (Ether Continent)\4. 마법협회 (Arcane Society)\9. 내부 암약 조직 (Clandestine Organizations)\4. 마력 밀수단 (Aether Smugglers)` | `control sample` | root corruption이 아니라 본래 section형 내부에서도 현대 어휘/오염이 생기는지 비교하는 대조군이다 | 범대륙 특수 문제와 전체 구조 드리프트를 분리하는 control read |

## Reading Order

1. 루트 셋 `S1`을 먼저 읽는다
2. 그다음 범대륙 내부 대표 샘플 `S2` 두 개를 읽는다
3. 마지막에 에테르 control sample `S3`를 읽어
   범대륙 고유 오염과 전체 naming drift를 분리한다

## Conductor Rules

- 원본 `X:` 경로가 열리기 전까지는 이 큐를 준비 문서로만 사용한다.
- `S1` 비교 전에는 하위 subtree를 정본 병합 근거로 쓰지 않는다.
- `S2`는 naming drift와 root corruption을 동시에 보되, 같은 문제로 뭉개지 않는다.
- `S3` control sample은 범대륙 문제를 일반 구조 문제와 분리하기 위한 비교축이다.

## Conductor Decision

다음 실제 실측 패스가 가능해지면
이 큐 순서대로 subtree를 샘플링한다.

즉 `P0 root_corruption`의 다음 단계는
막연한 추가 비교가 아니라,
이미 보고서에서 튀어나온 의심 경로를
우선순위대로 좁혀 읽는 것이다.

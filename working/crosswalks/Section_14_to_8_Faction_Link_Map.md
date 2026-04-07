# Section 14 to Section 8 Faction Link Map

이 문서는 `14. 영웅 백과`의 세력 폴더와 `8. 세력 아카이브`의 정본 세력 축을 연결하는 표준 링크맵이다.

핵심 원칙은 간단하다.

- `14번`의 폴더명은 서술 편의상 흔들릴 수 있다.
- `8번`의 세력 spine과 import anchor를 먼저 정본 후보로 본다.
- 한국어 축이 같으면 영문 표기는 우선 `display canon conflict`로 분리 기록한다.
- `_Legacy_` 경로는 이 링크맵의 정본 근거로 사용하지 않는다.

## Pilot Scope

- 대륙: `Ether Continent`
- 대상:
  - `01-14-1. 성장 영웅`
  - `01-14-2. 현존 영웅`
  - `phase3_section8_ether_*` import set

## Ether Pilot Map

| 14 Source Bucket | Observed Form | Canonical 8 Anchor | Display Canon | Status | Notes |
|---|---|---|---|---|---|
| 성장 영웅 | `성국 (Saint Haven)` | `phase3_section8_ether_sainthaven` | `Saint Haven` | `Hard Canon` | `14번`과 `8번`이 동일하게 맞는다. |
| 현존 영웅 | `1. 성국 (Saint Haven)` | `phase3_section8_ether_sainthaven` | `Saint Haven` | `Hard Canon` | 번호만 다르고 세력 축은 동일하다. |
| 성장 영웅 | `왕국연합 (Allians)` | `phase3_section8_ether_allied_kingdoms` | `Allied Kingdoms` | `Conflict` | 한국어 축은 같고 영문 `Allians`는 철자 흔들림으로 본다. |
| 현존 영웅 | `2. 왕국연합 (Allied Kingdoms)` | `phase3_section8_ether_allied_kingdoms` | `Allied Kingdoms` | `Hard Canon` | 현존 영웅 쪽 표기가 현재 임시 정본과 일치한다. |
| 성장 영웅 | `자유도시연합 (Crossroad Cities)` | `phase3_section8_ether_crossroad_cities` | `Crossroad Cities` | `Hard Canon` | 동일 축으로 본다. |
| 현존 영웅 | `3. 자유도시연합 (Crossroad Cities)` | `phase3_section8_ether_crossroad_cities` | `Crossroad Cities` | `Hard Canon` | 번호만 다르고 세력 축은 동일하다. |
| 성장 영웅 | `마법협회 (Arcane Society)` | `phase3_section8_ether_arcane_society` | `Arcane Society` | `Hard Canon` | 동일 축으로 본다. |
| 현존 영웅 | `4. 마법협회 (Arcane Society)` | `phase3_section8_ether_arcane_society` | `Arcane Society` | `Hard Canon` | 번호만 다르고 세력 축은 동일하다. |
| 성장 영웅 | `정령 연합 (Spirit Union)` | `phase3_section8_ether_spirit_union` | `Spirit Union` | `Soft Canon` | 현재 import anchor와 가장 잘 맞는다. 다만 현존 영웅 쪽 영문과 충돌한다. |
| 현존 영웅 | `5. 정령 연합 (Elemental Alliance)` | `phase3_section8_ether_spirit_union` | `Spirit Union` | `Conflict` | 한국어 축은 같고 영문 표기만 흔들린다. 현 단계에서는 `Spirit Union`을 우선 임시 정본으로 둔다. |

## Ether Pilot Decisions

1. 대륙 표시는 `Ether Continent`를 기본 display canon으로 둔다.
2. `Allians`는 정본이 아니라 철자 충돌로 누적한다.
3. `정령 연합`의 한국어 축은 유지한다.
4. `정령 연합`의 영문 display canon은 현재 `Spirit Union`을 우선 사용한다.
5. `Elemental Alliance`는 삭제하지 않고 `display canon conflict`로 추적한다.

## Why `Spirit Union` First

- `8번` import anchor가 이미 `spirit_union` 축으로 분리되어 있다.
- `Section 8 Standard Spine`에서도 에테르 부족 특수축을 `Spirit Union`으로 읽고 있다.
- `Elemental Alliance`는 번역형 대체 표현일 가능성은 있지만, 현 단계에서는 `8번` 기준 앵커가 더 중요하다.

## Replication Rule

다른 대륙으로 확장할 때도 같은 순서를 따른다.

1. `14번`의 성장 영웅과 현존 영웅 폴더를 나란히 둔다.
2. `8번` import anchor를 정본 후보로 둔다.
3. 한국어 축 일치 여부를 먼저 본다.
4. 영문 충돌은 `Hard Canon`이 아니라 `Conflict` 또는 `Soft Canon`으로 분리한다.
5. 고아 인물 파일은 이 링크맵에 걸리지 않으면 `15번 후보` 또는 `분류 누락`으로 보류한다.

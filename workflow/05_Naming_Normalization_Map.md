# Naming Normalization Map

이 문서는 대륙명, 세력명, 영문 표기의 흔들림을 잠정 정리하는 기준표다.

## Current Watchlist

| Canon Form | Known Variant | Action |
|---|---|---|
| `Ether Continent` | `Aether Continent` | `Ether Continent`를 기본 표기로 둔다. |
| `Allied Kingdoms` | `Allians`, 기타 철자 흔들림 | 실제 파일명과 다르면 `Conflict`로 기록한다. |
| `Spirit Union` | `Elemental Alliance` | 한국어 축은 `정령 연합`으로 유지하고 영문 표시는 `Spirit Union`을 우선 임시 정본으로 둔다. |
| `Supranational & Neutral` | `Supranational & 마립 세력 (Neutral)` | 깨진 이름으로 보고 구조 감사 최우선 대상으로 지정한다. |
| `실비아` | `키르케 실비아`, `실비아 아캄`, `해양 실비아`, `실비아 팬텀` | 같은 이름의 별개 인물 후보로 분리하고 병합하지 않는다. |
| `Aegis / 아이기스` | `아이기스`, `알렉산더 이지스`, `이지스 그림쉴드`, 방패/결계/유물명 | 인물명, 성씨, 아이템명, 마법명 사용을 분리한다. |

## Rules

- 파일명 기준과 문서 본문 기준이 다르면 먼저 파일 경로를 조사한다.
- 한번에 전부 고치지 말고 `Conflict`로 누적한 뒤 루트 안정화 단계에서 정리한다.
- `_Legacy_` 경로의 명칭은 정본 판단 근거로 사용하지 않는다.
- 한국어 세력명이 일치하면 영문 표기는 우선 `display canon conflict`로 분리 기록한다.
- `14번`과 `8번`이 충돌할 때는 `8번 세력 spine`과 import 경로를 먼저 앵커로 사용한다.
- 현대 조직범죄/기업물 어휘는 바로 정본명으로 승격하지 않고 톤 검토를 먼저 거친다.
- 같은 이름이 여러 대륙/세력에 반복되면 `이름 같음 = 동일 인물`로 보지 않는다.
- 아이템/마법명으로도 쓰이는 단어는 인물명 승격 전 `item_name_collision`으로 둔다.

## Update Procedure

1. 새 변형 표기를 찾는다.
2. 어느 경로에서 쓰였는지 기록한다.
3. 정본 후보 경로와 비교한다.
4. `Hard Canon`, `Soft Canon`, `Conflict` 중 하나로 분류한다.

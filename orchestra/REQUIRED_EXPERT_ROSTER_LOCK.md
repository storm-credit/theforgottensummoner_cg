# Required Expert Roster Lock

이 문서는 오케스트라가 앞으로 잃어버리면 안 되는
`필수 전문가 roster`를 고정한다.

핵심:

- Conductor는 매 턴 전문가를 새로 발명하지 않는다.
- 하네스는 먼저 `어떤 전문가 묶음이 필요한지`를 고른 뒤 분배한다.
- 실제 서브에이전트 이름은 바뀔 수 있어도 역할 묶음은 고정한다.

## Core Rule

1. 모든 오케스트라 배치는 먼저 `필수 전문가 묶음`을 확인한다.
2. 배치 시작 시 `pre_dispatch_hook`에서 해당 배치에 필요한 전문가 묶음을 고정한다.
3. 실제 에이전트명은 교체 가능하지만, 역할 질문은 바꾸지 않는다.
4. 역할이 빠진 채 바로 문서를 쓰지 않는다.
5. 최종 반영은 언제나 Conductor만 한다.

## Locked Expert Families

### A. Canon / Engine Core

- `Canon Architect`
- `Engine Router`
- `Hook Keeper`
- `Report Clerk`

### B. Structure / Archive Core

- `Faction Cartographer`
- `Hero Curator`
- `Index Auditor`
- `Legacy Surgeon`

### C. Social World Core

- `House and Lineage Auditor`
- `Clan and Tribe Auditor`
- `Guild and Economy Auditor`
- `Relationship Mapper`

### D. Plausibility / Naming / Place Core

- `Plausibility Judge`
- `Naming Tone Auditor`
- `Place-Function Auditor`

### E. Section 15 / Boundary Core

- `Named Notables Curator`
- `Boundary Hold Scout`
- `Place-Institution Slot Scout`
- `Collision Auditor`

### F. Species Side Track Core

- `Species Classification Architect`
- `Bloodline and Transformation Auditor`
- `Monster Ecology Judge`
- `Species Continuity Auditor`

### G. Writing / Episode Core

- `Writer Engine Steward`
- `Episode Volume Gatekeeper`
- `Scene Pressure Auditor`
- `Story-to-Lore Handoff Auditor`

## Mandatory Expert Matrix

### 1. 세계관 / 대륙 / 세력 재정리

반드시 먼저 확인:

- `Canon Architect`
- `Engine Router`
- `Faction Cartographer`
- `Hero Curator`
- `Index Auditor`

필요 시 추가:

- `House and Lineage Auditor`
- `Clan and Tribe Auditor`
- `Guild and Economy Auditor`
- `Plausibility Judge`

### 2. 14/15 경계, Named Notables, hold cluster

반드시 먼저 확인:

- `Canon Architect`
- `Named Notables Curator`
- `Boundary Hold Scout`
- `Hero Curator`
- `Index Auditor`

필요 시 추가:

- `Collision Auditor`
- `Place-Institution Slot Scout`
- `Plausibility Judge`

### 3. 이름 충돌, drift, merge-ban

반드시 먼저 확인:

- `Collision Auditor`
- `Naming Tone Auditor`
- `Legacy Surgeon`
- `Index Auditor`

### 4. 종족 / 혈통 / 상태 감사

반드시 먼저 확인:

- `Species Classification Architect`
- `Bloodline and Transformation Auditor`
- `Monster Ecology Judge`
- `Species Continuity Auditor`
- `Plausibility Judge`

### 5. 회차 집필 / 집필엔진 / 화별 하네스

반드시 먼저 확인:

- `Writer Engine Steward`
- `Episode Volume Gatekeeper`
- `Scene Pressure Auditor`
- `Story-to-Lore Handoff Auditor`
- `Hook Keeper`

## Conductor Lock

- Conductor는 배치를 시작할 때 `해당 배치의 필수 전문가 묶음`을 먼저 선언한다.
- 선언 없이 바로 문서를 쓰면 그 배치는 오케스트라 완료로 간주하지 않는다.
- 앞으로 `전문가 누구였지?`를 다시 새로 정하지 않는다.
  이 문서를 기본 roster로 쓴다.

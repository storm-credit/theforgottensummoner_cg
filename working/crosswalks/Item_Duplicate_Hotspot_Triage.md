# Item Duplicate Hotspot Triage

이 문서는 별도 추적 아티팩트인 `Extracted_Item_Candidates.md`를 직접 건드리지 않고,
아이템 사이드트랙의 duplicate hotspot과 오탐 위험을 안전하게 관리하기 위한 triage 문서다.

## Goal

- duplicate hotspot을 별도 장부에서 먼저 해석한다.
- 재료명, 공용 명사, 카탈로그 표제어가 고유 아이템처럼 승격되는 일을 막는다.
- 다음 정제 단계를 `Extracted_Item_Candidates.md` 직접 편집이 아니라
  `Item_Candidate_Register.md` 상태 정리로 유도한다.

## Locked Safe Rule

1. 별도 추적 아티팩트인 `Extracted_Item_Candidates.md`는 이 단계에서 직접 수정하지 않는다.
2. duplicate hotspot은 먼저 `broad material / catalog heading / true unique item`으로 나눈다.
3. broad material이나 카탈로그 표제어는 `ready_for_encyclopedia`로 올리지 않는다.
4. 인물명, 성씨, 마법명, 기능어와 충돌하면 `Item_Name_Collision_Register.md`로 먼저 보낸다.
5. 탈것, 생물, 장치, 개념어는 고유 물건으로 확정하기 전까지 `unknown` 유지가 기본이다.

## Current Duplicate Hotspots

| Term | Duplicate Count | Current Risk | Safe Temporary Read |
|---|---:|---|---|
| `황금 (Gold)` | 11 | 재료/배지/상징어/통화성 명사가 고유 아이템처럼 보일 수 있다 | `broad material candidate` |
| `보석 (Gems)` | 5 | 액세서리 분류 표제어와 실제 보석 유물이 섞였을 가능성이 높다 | `catalog heading candidate` |
| `흑요석 (Obsidian)` | 4 | 소재명과 고유 장비명이 동시에 쓰인다 | `material-linked duplicate candidate` |
| `흑철 (Iron)` | 2 | 재료명인지 개별 장비명인지 문맥 확인이 더 필요하다 | `material-linked duplicate candidate` |

## False-Positive Families

### 1. Broad Material Terms

- `황금 (Gold)`
- `보석 (Gems)`
- `흑요석 (Obsidian)`
- `흑철 (Iron)`

이 계열은 개별 전설 장비명보다 재료나 공용 분류명일 가능성이 높다.
정본 백과 승격 전에 owner, 맥락, 고유 호칭이 더 확인돼야 한다.

### 2. Catalog Heading Leakage

- `외투 (Surcoats)`
- `마도구 (Magitek)`

이 계열은 도감 경로나 상위 분류명이 추출표에 함께 들어왔을 가능성이 있다.
고유 아이템이 아니라면 승격 대상에서 제외하거나 register note만 남긴다.

### 3. Living / Mount / Device Ambiguity

- `은빛 그리폰 '칼리스토'`
- `광전사의 심장 펌프`
- `차원의 열쇠`

생물, 생체장치, 구조물형 도구는 일반 장비와 같은 규칙으로 합치지 않는다.
`unknown` 유지 후 별도 bucket 판단이 필요하다.

## Minimal Triage Route

1. `Extracted_Item_Candidates.md`는 현행 유지
2. `Item_Candidate_Register.md`에서만 상태를 조정
3. broad material / catalog heading은 `duplicate_candidate` 또는 note 강화
4. 이름 충돌은 `Item_Name_Collision_Register.md`에 추가
5. 고유성, 사용자 맥락, 첫 등장 근거가 모두 확인된 항목만 `ready_for_encyclopedia` 검토

## Next Non-Invasive Action

- 2026-04-13 KST 기준, `Item_Candidate_Register.md`에서 duplicate hotspot 4개
  (`황금`, `보석`, `흑요석`, `흑철`)의 상태어를 `duplicate_candidate`로 낮췄다.
- 2026-04-13 KST 기준, living / mount / device ambiguity 후보도
  `Item_Name_Collision_Register.md`의 sidecar section으로 분리했다.
- 다음 안전 작업은 원본 추출표 직접 정제가 아니라,
  source context 확인이 끝난 `proper_name_not_item`, living / mount exclusion,
  device bucket 후보가 정본 아이템 백과로 넘어가지 않게 exclusion routing과 sidecar 차단선을 유지하는 것이다.
- 그 전까지는 이 문서를 side-track guard로 유지한다.

## Cross Reference

- `working/crosswalks/Extracted_Item_Candidates.md`
- `working/crosswalks/Item_Candidate_Register.md`
- `working/crosswalks/Item_Name_Collision_Register.md`
- `working/crosswalks/Item_Encyclopedia_Pipeline.md`
- `workflow/07_Item_Canon_Schema.md`
- `workflow/08_Item_Desire_Design.md`

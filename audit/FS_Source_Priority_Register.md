# FS Source Priority Register

이 문서는 FS Lore Engine이
서로 충돌하는 설정을 만났을 때
어떤 출처를 더 우선할지 판단하는 장부다.

원본을 수정하지 않고,
`cg` 작업본 안에서만 판정 근거를 남긴다.

## Priority Ladder

### Tier 1. Canon Spine Reference

가장 우선한다.

- 오케스트라가 `Hard Canon` 또는 `Active Spine`으로 판정한 문서
- `workflow`와 `audit`에서 반복적으로 기준으로 쓰는 문서
- 대륙, 세력, 14/15 라우팅의 기준 reference

사용 예:

- `workflow/00_Astralis_Vision.md`
- `workflow/11_FS_Engine.md`
- `audit/FS_Canon_Tier_Register.md`
- `audit/Five_Continent_Missing_Layer_Master_Lock.md`
- `working/drafts/Five_Continent_Synthesis.md`
- `audit/Section_8_Standard_Spine.md`

주의:

- 결손층 5개 판단에서는 `audit/Five_Continent_Missing_Layer_Master_Lock.md`가
  단일 entry authority다.
- `working/drafts/Five_Continent_Synthesis.md`는 대륙 종합 reference로 보되,
  missing-layer thin/support 판정을 master lock 바깥에서 새로 확정하지 않는다.

### Tier 2. Imported Working Copy Snapshot

원본에서 복사해 온 작업본 snapshot이다.

- `working/imports` 아래의 참조 복사본
- 원본의 특정 구역을 비교하기 위해 가져온 문서
- 직접 수정하지 말고, 판정과 추출 근거로 사용한다.

사용 예:

- `working/imports/phase1_*`
- `working/imports/phase2_*`
- `working/imports/phase3_*`
- `working/imports/phase4_*`
- `working/imports/phase5_*`

### Tier 3. Derived Analysis

오케스트라가 원본과 작업본을 읽고 만든 분석 문서다.

- 충돌 등록부
- 후보 등록부
- 정규화표
- 지도/도시 기능표
- 이름 톤 교체표

주의:

- 분석 문서는 원본보다 강하지 않다.
- 다만 실제 작업 결정을 내릴 때는 분석 문서가 실행 기준이 된다.

### Tier 4. Legacy / Backup / Corrupted Root

정본 후보로 바로 쓰면 안 되는 층이다.

- `_Legacy_`
- `Backup`
- 깨진 폴더명
- 중복 루트
- 후대 증설로 보이지만 정리되지 않은 파편

사용 원칙:

- 삭제하지 않는다.
- 바로 정본으로 올리지 않는다.
- 먼저 `Legacy Quarantine` 또는 `Open Question`으로 둔다.

### Tier 5. Rumor / In-World Text

세계 안에서 떠도는 소문, 저술, 도감, 플럭스넷류 정보다.

주의:

- 흥미 요소로는 강하다.
- 정본 사실과 동일시하지 않는다.
- 아이템, 명사형 영웅, 복선 장부와 연결할 때 특히 조심한다.

## Conflict Rule

충돌이 생기면 아래 순서로 처리한다.

1. 더 높은 Priority Tier를 확인한다.
2. 그래도 충돌하면 `FS_State_Label_Register.md`에서 상태 라벨을 붙인다.
3. 수정하기 전에 `FS_Revision_Gate_Checklist.md`를 통과한다.
4. 판단이 안 되면 `Open Question`으로 보류한다.

## Evidence vs Action Rule

Source Priority는 `무엇이 더 강한 증거인가`를 정한다.

Derived Analysis는 `해당 작업에서 무엇을 할 것인가`를 정한다.

따라서:

- 증거 판단은 Source Priority가 우선한다.
- 실행 판단은 Derived Analysis가 맡을 수 있다.
- 하지만 Derived Analysis가 더 높은 출처 증거와 충돌하면
  즉시 `conflict` 또는 `open_question`으로 낮춘다.

## Recorded Notes

| Topic | Higher Priority | Lower Priority | Recorded Action |
|---|---|---|---|
| `카르텔` 표면명 | Naming Tone Guide | 기존 기능 라벨 | `금융 연맹`, `침묵의 상회` 후보로 관리 |
| `14/15` 분리 | Section 15 Split Policy | 기존 혼재 문맥 | `14` 유지, `15`는 People Worth Seeking / Operational Lines로 분리 |
| 범대륙 후기 확장 | Five Continent Spine | 후기 증설 파편 | 후순위 확장으로 보류 |
| 레거시 루트 | Legacy Quarantine Policy | `_Legacy_` 원문 | 바로 정본화 금지 |

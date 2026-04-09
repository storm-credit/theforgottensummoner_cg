# Race Species Boundary Guard

이 문서는 종족 사이드트랙에서 나온 신호가
언제까지 side-track에 머물고,
어느 시점에만 메인선으로 넘어갈 수 있는지 정하는 경계 가드다.

## Core Escalation Rules

### 1. Species Clue Only

단어만 등장하거나,
개체 설명만 있고 사회 구조가 보이지 않으면 side-track에 남긴다.

예:

- `세이렌 하피`
- `화염 거인`
- `저주받은 하피`
- `하급 정령`

처리:

- `Race_Species_Evidence_Log.md`에만 기록
- `crosswalk`에서 `monster`, `unclear`, `state`로 유지
- 메인 `14/15`와 `FS_*_Register`에는 쓰지 않음

### 2. Social Unit Impact

부족, 자치권, 왕국, 공동체, 언어, 외교, 계층 구조가 보이면
`people + polity` 신호로 읽고, 이후 `8` 계열 evidence로 연결 가능성을 본다.

예:

- `수인 부족`
- `부족 영역`
- `수인족 자치권`
- `인어 공주`, `이종족 대표`

처리:

- side-track first pass에 반영
- 충분히 쌓이면 `8` 세력 evidence에 later feed
- 여전히 메인 `14/15` 라우팅은 자동 변경하지 않음

### 3. Individual Biography Impact

종족/혈통/상태 신호가 특정 인물의 프로필 읽기에 직접 영향을 주면
`annotate only` 원칙으로 다룬다.

예:

- `하이엘프`
- `하프엘프`
- `Dragonborn`
- `용의 피`
- `언데드 귀족`

처리:

- side-track과 crosswalk에는 기록
- 필요 시 `14/15 evidence` 문서에 주석 수준으로만 연결
- 이 가드만으로 인물 라우팅이나 candidate state를 바꾸지 않음

### 4. Mixed or Contradictory

종족처럼 보이면서 상태/몬스터/소모 전력처럼도 읽히면
즉시 `hold / open question`으로 둔다.

예:

- `육식성 어인`
- `정령화`
- `언데드 왕국`
- `요정 부대`

처리:

- `First Pass`에는 `mixed`, `thin`, `reserved`, `open question`만 사용
- 추가 evidence 없이 `species`로 승격 금지

## Promotion Gate

아래 4개가 모이기 전에는 메인 캐논 승격 금지:

1. 사례 3건 이상
2. 사회 구조 또는 자치권 증거 1건 이상
3. `race / bloodline / state / monster` 혼선 정리
4. 오케스트라 Conductor 승인

## Mainline Separation Rule

- 이 트랙은 메인 `14/15` workstream과 경쟁하지 않는다.
- `verify_before_15`, `named_notable_candidate`, `place-first slot`, `FS_*_Register` write는 자동 유입 금지다.
- mainline으로 넘어가더라도 먼저 `evidence`나 `impact bridge` 단계가 있어야 한다.

## Current Guard Calls

| Signal | Current Guard Call |
|---|---|
| `merfolk / 인어` | localized enclave / mixed-polity contact는 확인, sovereign civilization은 아직 보류 |
| `세이렌 하피` | `monster first` |
| `라미아` | `open question` |
| `나가` | one-character signal only, stable society 미확정 |
| `거인족` | mythic/threat signal 우세, peoplehood 미확정 |
| `요정` | Ether/Spirit Union 내부 ally/community signal은 강해졌지만 global standalone dossier는 보류 |
| `오크 부락` | people signal은 있으나 사회 구조 증거 더 필요 |
| `고블린` | bloodline/integration signal only, polity 미확정 |

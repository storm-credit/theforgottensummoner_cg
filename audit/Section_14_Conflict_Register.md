# Section 14 Conflict Register

이 문서는 `14번 영웅 백과`에서
단순 표기 흔들림을 넘어서 실제 문맥 충돌 가능성이 있는 인물을 모아두는 등록부다.

## Conflict Types

- `label_conflict`: 표기나 영어 이름만 충돌
- `anchor_conflict`: 세력 앵커가 둘 이상 경쟁
- `context_conflict`: 파일 경로와 본문 문맥이 다른 축을 가리킴
- `macro_overlink`: 범대륙 조직망 연결이 과반복되어 세계 구조인지 자동 확장 잔재인지 확인 필요

## Current Register

| Character / Node | Conflict Type | Current Path Reading | Competing Context | Current Judgment | Next Action |
|---|---|---|---|---|---|
| `왕국연합 (Allians)` | `label_conflict` | `왕국연합 (Allied Kingdoms)` 축 | 영문 철자 `Allians` | `Conflict` | display canon은 `Allied Kingdoms`로 유지 |
| `정령 연합 (Elemental Alliance)` | `label_conflict` | `정령 연합 (Spirit Union)` 축 | 영문 `Elemental Alliance` | `Conflict` | 한국어 축 유지, 영문은 `Spirit Union` 우선 |
| `제레시스 아르카디아` | `context_conflict` | `에테르 / 마법협회` | aliases와 본문 일부가 `크림슨 대륙 / 아르카나 제국 잔재`를 가리킴 | `High Risk Conflict` | 별도 문맥 검토 필요 |
| `크세노스 아르카디아` | `context_conflict` | `에테르 / 마법협회` | aliases와 본문 일부가 `크림슨 대륙 / 아르카나 제국 잔재`를 가리킴 | `High Risk Conflict` | 별도 문맥 검토 필요 |
| `발리아스 이그나리온` | `context_conflict` | `에테르 / 마법협회` | aliases와 본문 일부가 `크림슨 대륙 / 아르카나 제국 잔재`를 가리킴 | `High Risk Conflict` | 별도 문맥 검토 필요 |
| `에테르 현존 영웅군 전반` | `macro_overlink` | 각 대륙 세력 앵커 | `Guilds / Syndicates / Shadow Intelligence / Megacorps`가 과반복 | `Watch` | 세계 구조인지 자동 확장 잔재인지 분리 판정 |
| `이리나 폰 루즈` | `macro_overlink` | `그림자 첩보망` 중심 인물 | 문서 서두에 메타 시스템 블록이 본문보다 앞선다 | `Watch` | 접점은 유지하되 메타 문장은 정본 서술로 채택하지 않음 |
| `칼리크 디트리히` | `macro_overlink` | `침묵의 상회` 및 금융/첩보 접점 | `길드/상단/마탑/첩보` 블록이 일괄 삽입됨 | `Watch` | 실제 접점만 남기고 과반복 블록은 환원 필요 |
| `세실리아 메르카토르` | `macro_overlink` | `자유도시연합 / 페어딜러 상단` | `상단/마탑/기업/첩보` 블록이 일괄 삽입됨 | `Watch` | 인물-조직 관계로 재서술하고 기계적 축 나열은 감산 |

## Arcane Society Context Conflict Set

현재 확인된 고위험 문맥 충돌 파일:

- `01. 제레시스 아르카디아 (Jeresys Arcadia).md`
- `02. 크세노스 아르카디아 (Xenos Arcadia).md`
- `08. 발리아스 이그나리온 (Valias Ignarion).md`

이 셋은 공통적으로

- 폴더 경로는 `에테르 대륙 / 마법협회`
- aliases와 제목, 기본 정보 일부는 `크림슨 대륙 / 아르카나 제국 잔재`

를 가리킨다.

즉 단순 오탈자가 아니라
`파일 배치와 본문 소속 축이 어긋난 상태`일 가능성이 높다.

## Conductor Rule

이 등록부에 올라온 항목은 다음 규칙을 따른다.

1. 지금은 이동하지 않는다.
2. 관계표에는 `Conflict` 상태를 붙인다.
3. display canon만으로 덮어쓰지 않는다.
4. 나중에 `14 유지 / 15 이동 / 별도 축 분리` 판단 전까지 보류한다.

## Latest Note

- `macro_overlink`는 이제 단순 감이 아니라
  `이리나`, `칼리크`, `세실리아`의 실제 문서 패턴으로 근거가 확보됐다.
- 자세한 근거는 `Section_14_Macro_Overlink_Findings.md`에 누적한다.

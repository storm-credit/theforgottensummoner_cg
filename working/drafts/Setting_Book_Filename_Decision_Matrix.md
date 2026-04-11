# Setting Book Filename Decision Matrix

## Purpose

이 문서는 현재 설정집 패키지에서
어떤 파일명이 유지되어야 하고,
어떤 이름 변경은 아직 미뤄야 하는지 판단하기 위한 결정표다.

핵심은 문서 품질보다 먼저
`역할이 섞이지 않는가`를 보는 것이다.

## Current Filename Jobs

| File | Current Job | Why Keep It Now |
| --- | --- | --- |
| `Setting_Book_Preview_Readable_v0.md` | 가장 먼저 공유하는 reader-facing preview | 지금 단계에서 가장 책처럼 읽히는 파일이기 때문이다. |
| `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md` | 본문+부록을 한 파일에 압축한 compressed reference | 전체 구조와 appendix A-E 동기화를 한 번에 점검하기 좋기 때문이다. |
| `Setting_Book_Preview_Package_v0.md` | preview 공유 순서와 포함 범위를 정하는 conductor guide | 원고 파일이 아니라 공유/조립 지시서이기 때문이다. |

## Decision Criteria

아래 네 기준이 동시에 맞아야
파일명을 더 reader-facing 하게 바꾸거나 별도 RC 파일명을 만든다.

| Criteria | Ask This First | Current Call |
| --- | --- | --- |
| Role separation | 이 이름이 preview / reference / conductor 역할을 섞지 않는가 | keep current names |
| Reader clarity | 지금 독자나 협업자에게 가장 덜 헷갈리는 이름인가 | `Preview_Readable_v0`가 가장 명확함 |
| Preserved artifact level | 다음 산출물이 broad draft가 아니라 보존 가능한 package인가 | 아직 hold |
| Cross-document sync | front matter, preview, prototype, release gate가 같은 naming 결정을 가리키는가 | 아직 부분 정렬 상태 |

## Why The Current Names Stay

### `Setting_Book_Preview_Readable_v0.md`

- 지금 단계의 공유 목적이 `완성본 출간`이 아니라 `책처럼 읽히는 preview`를 보여 주는 데 맞아 있다.
- `preview`와 `readable`이 함께 있어 독자용 원고라는 역할이 바로 보인다.
- 너무 이른 `RC` 이름은 아직 닫히지 않은 filename/layout hold를 가린다.

### `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`

- 이 파일은 독자용 한 권이 아니라 본문과 부록 동기화를 확인하는 압축 reference다.
- `Prototype_v0`라는 이름이 아직 작업 보존본이라는 사실을 숨기지 않는다.
- 지금 이름을 reader-facing 쪽으로 바꾸면 preview와 reference의 역할 경계가 흐려진다.

## Rename Only When

아래가 맞을 때만 새 이름을 다시 검토한다.

1. 다음 산출물이 `preview 유지`가 아니라 `보존용 패키지`로 확정될 때
2. `Setting_Book_Packaging_Direction_Matrix.md`에서 reader-facing layout 또는 production bible 방향이 명확히 닫힐 때
3. `Setting_Book_Release_Readiness_Checklist.md`의 filename hold가 실제로 해제될 때
4. 새 이름이 preview와 prototype의 역할 분리를 더 선명하게 만들 때

## Do Not Do Yet

- `Setting_Book_Preview_Readable_v0.md`를 성급하게 RC 파일명으로 바꾸지 않는다.
- `Prototype_v0`를 책 제목처럼 보이는 이름으로 덮어쓰지 않는다.
- preview, prototype, package guide를 같은 층위 파일처럼 리네이밍하지 않는다.

## Current One-Line Call

지금은 `파일명 유지 + 역할 분리 보존`이 맞고,
새 이름은 `패키징이 다음 보존 산출물`로 닫히는 순간에만 다시 연다.

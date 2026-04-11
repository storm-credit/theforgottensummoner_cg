# Setting Book Packaging Direction Matrix

## Purpose

이 문서는 설정집의 다음 보존 산출물이
`reader-facing layout`인지,
아니면 `production bible`인지 판단하기 위한 결정표다.

지금 단계에서는 둘 다 동시에 만들지 않는다.
먼저 어느 쪽이 다음 산출물인지 고른 뒤,
그 결정에 맞는 파일명과 패키지 범위를 다시 정한다.

## Two Directions

| Direction | Use When | Main Reader | Keep Strong | Do Not Overdo Yet |
| --- | --- | --- | --- | --- |
| reader-facing layout | 누군가에게 책처럼 읽히는 설정집을 먼저 보여줘야 할 때 | reader, early collaborator | front matter, readable preview, TOC, public body flow | appendix 확장, production jargon, 협업용 control lane 과다 노출 |
| production bible | 후속 창작자나 아트/음악/adaptation 팀이 구조와 위험 지도를 먼저 알아야 할 때 | collaborator, internal production | appendix source notes, cross-reference, control language, bridge docs | reader-facing 표지/판형 확정, 상업용 책꼴 환상 |

## Current Orchestra Decision

현재는 `reader-facing layout`이 다음 보존 산출물에 더 가깝다.

이유:

- `Setting_Book_Preview_Readable_v0.md`가 이미 공유 가능한 preview 역할을 한다.
- 허브와 역할 지도, 상태판, core profile bridge가 preview 진입을 안정적으로 받친다.
- filename hold는 `Setting_Book_Filename_Decision_Matrix.md`에서 따로 문서화되어 있어 조기 RC rename을 다시 열 이유가 줄었다.
- 아직 RC 파일명이나 상업용 판형을 확정할 만큼 naming/layout hold가 닫히지 않았다.
- production bible은 만들 수 있지만, 지금은 필요 이상으로 control 문서를 먼저 비대화시킬 위험이 있다.

## Decision Signals

아래 신호가 더 강해질 때 방향을 다시 판정한다.

| If This Becomes True | Prefer |
| --- | --- |
| 지금 필요한 피드백이 “읽히는가, 책처럼 보이는가”에 몰림 | reader-facing layout |
| 지금 필요한 피드백이 “어디가 hold고 어떤 근거가 붙는가”에 몰림 | production bible |
| front matter / subtitle / body flow polishing이 다음 핵심 작업이 됨 | reader-facing layout |
| appendix cross-reference / source note density가 다음 핵심 작업이 됨 | production bible |
| RC 파일명과 보존 패키지 범위를 정해야 함 | reader-facing layout |
| 협업자가 bridge docs와 appendix control lanes를 먼저 요구함 | production bible |

## Current Safe Actions

지금 바로 해도 되는 일:

- `Setting_Book_Preview_Readable_v0.md`를 shareable preview completion target으로 유지
- `Setting_Book_Filename_Decision_Matrix.md`를 naming hold control로 유지
- body-facing scan 결과를 기준으로 Appendix B/C는 현재 anchored row만 유지
- Appendix B/C evidence queue에서 필요한 행만 추가
- core profile bridge와 허브 인덱스 문장을 미세 수정
- RC 파일을 만들지 않은 채 packaging decision만 더 선명하게 만들기

지금 미루는 일:

- 별도 RC 파일 생성
- 상업용 책 판형 확정
- production bible 이름으로 새 메인 패키지 복제
- preview/reference 역할을 다시 섞는 리네이밍

## Trigger To Revisit

아래 중 하나가 생기면 이 문서를 다시 연다.

1. reader-facing 파일명을 정해야 할 때
2. collaborator 전용 패키지를 별도로 내보낼 때
3. appendix source note 밀도를 현재보다 한 단계 더 올려야 할 때
4. RC file trigger를 다시 판정할 때

## Current One-Line Call

지금은 `shareable preview 유지 + packaging decision 선명화`가 맞고,
`별도 RC 파일 생성`이나 `production bible 확장`은 다음 보존 필요가 생길 때 다시 연다.

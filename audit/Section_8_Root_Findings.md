# Section 8 Root Findings

## Scope

- Source: `X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)`
- Directories: `1474`
- Files: `3905`

## Primary Findings

1. `6. 범대륙 초국가 및 중립 세력` 루트가 중복되어 있다.
2. 깨진 이름의 변형 루트가 섞여 있다.
3. `_Legacy_중립세력 (Backup)`이 루트 레벨에 남아 있다.
4. 세력 내부 구조가 두 가지 스타일로 섞여 있다.
   - 공통 섹션형
   - 실제 장소 하위 폴더형
5. 템플릿성 반복 파일이 대량으로 존재한다.

## Risks

- 구조를 고치기 전에 내용 수정을 시작하면 모순이 더 늘어난다.
- 이름만 보고 중복 정리하면 정상 문서까지 잘못 합칠 수 있다.
- 레거시와 활성 경로가 섞이면 정본 판단이 계속 흔들린다.

## Immediate Actions

1. `Supranational & Neutral` 루트 충돌을 `P0`로 유지
2. `_Legacy_`와 `Backup`을 격리 대상으로 고정
3. 세력 내부 표준 뼈대를 먼저 정하고 예외를 기록
4. 서사 개정은 루트 안정화 이후로 미룸

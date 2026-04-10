# Section 14 Root Findings

## Scope

- Source: `X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)`
- Directories: `261`
- Files: `1491`

## Primary Findings

1. 기본 축은 이미 있다.
   - `성장 영웅`
   - `현존 영웅`
   - `소환 영웅`
2. 분류 방식이 서로 다르다.
   - 성장 영웅은 대륙/세력 기반
   - 현존 영웅은 세력 번호 기반
   - 소환 영웅은 랭크 기반
3. 세력명과 영문 표기 흔들림이 보인다.
4. `_Legacy_중립세력 (Backup)`이 남아 있다.
5. 고아 파일과 자유서술형 관계 정보가 존재한다.

## Risks

- 정본 스키마 없이 문체부터 손보면 예쁜 모순이 된다.
- 관계 정보가 자유서술에 묻혀 있어 대규모 감사를 어렵게 만든다.
- `8번` 세력명과 연결이 안 맞으면 인물 백과의 정리도 다시 흔들린다.

## Locked Action Reading

1. 영웅 정본 스키마 적용 필요를 locked finding으로 유지
2. 관계 타입 지정형 어휘 고정 필요를 locked finding으로 유지
3. `_Legacy_`와 고아 파일 분리 필요를 locked finding으로 유지
4. `8번` 명칭 표준과 연결한 뒤 세부 개정을 본다는 기준을 reference rule로 유지

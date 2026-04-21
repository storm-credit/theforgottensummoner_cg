# FS Engine Mode Routing

이 문서는 오케스트라가
`FS Lore Engine`, `FS Story Engine`, `FS Media Engine` 중
어느 엔진을 먼저 쓸지 정하는 라우팅 표다.

## Default Routing Snapshot

설정집 정리 단계의 기본값:

1. `FS Lore Engine`
2. `FS Story Engine`
3. `FS Media Engine`

즉 이 단계에서는 설정집 구조와 정합성이 먼저다.

## Mode Table

| Work Type | Primary Engine | Secondary Engine |
|---|---|---|
| 세계관 코어 | Lore | Story |
| 대륙 프레임 | Lore | Story |
| 세력/가문/길드/부족 | Lore | Story |
| 14 영웅백과 | Lore | Story |
| 15 People Worth Seeking | Lore | Story |
| 15 Operational Lines | Lore | Story |
| 아이템 후보 수집 | Lore | Story |
| 아이템 수집욕 설계 | Lore | Story |
| 지도/도시/건물 내부 맵 후보 | Lore | Media |
| 실제 액트 설계 | Story | Lore |
| 실제 장면 집필 | Story | Lore |
| 외부 reader-response 평론 번역 | Story | Lore for boundary only |
| 음악/이미지/영상 브리프 | Media | Lore |
| 커밋/푸쉬 | None | Lore for context only |

## Switch Triggers

### Switch to Lore Engine

아래가 보이면 Lore Engine을 우선한다.

- 어디에 넣을지 애매함
- 정본/소문/레거시 구분 필요
- 이름 톤 문제
- 폴더링 문제
- 대륙/세력/인물 소속 문제
- 원본 참조와 작업본 비교

### Switch to Story Engine

아래가 보이면 Story Engine을 우선한다.

- 액트의 감정 질문
- 캐릭터 아크
- 장면의 압력
- 독자가 언제 알게 되는지
- 외부 reader-response 평론을 reference-only Story Craft heuristic로 번역해야 할 때
- 관계가 어떻게 바뀌는지
- 복선 회수 타이밍

### Switch to Media Engine

아래가 보이면 Media Engine을 우선한다.

- 세계지도/도시/건물 내부 맵 브리프
- 캐릭터 이미지 브리프
- 음악 분위기 브리프
- 영상 컷 구조
- 보여줘도 되는 정보와 숨겨야 하는 정보

## Conductor Reading Rule

엔진은 고정된 순서가 아니라
해당 작업의 위험에 따라 선택한다.

하지만 이 단계에서는
`설정집 안정화`가 우선이므로
특별한 이유가 없으면 Lore Engine을 먼저 적용한다.

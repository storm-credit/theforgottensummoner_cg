# FS Media Engine Consensus

이 문서는
음악, 이미지, 영상 쪽을
`여기서 직접 제작`하기보다
`체크용 브리프/검수 엔진`으로 설계할 때의 합의안이다.

핵심 결론:

- 설정집 규모가 큰 현재 단계에서는
  `생성 엔진`보다 `canon-safe brief engine`이 맞다.
- 음악, 이미지, 영상은 각각 따로 보되,
  위에 공통 코어를 둬야 한다.

## Overall Judgment

### 지금 여기서 가능한 것

- 미디어용 기준 정리
- canon-safe 브리프 생성
- 금지 요소와 스포일러 통제
- 세계관 정합성 검수

### 지금 여기서 비효율적인 것

- 실제 완성 음악 제작
- 실제 완성 일러스트/영상 대량 제작
- 거대한 설정집을 충분히 검수하지 않은 상태에서의 대량 생성

즉:

- `만드는 곳`은 다른 곳
- `체크하고 브리프 짜는 곳`은 여기

로 나누는 게 맞다.

## Shared Core

### 1. Canonical Brief Core

입력:

- 대상 엔티티
- 시점
- 대륙 / 세력 / 관계 상태
- 감정 톤
- 금지 요소
- Hard / Soft canon 범위

체크:

- 시점 불일치
- 관계 상태 불일치
- 복선 조기 노출
- 인간 중심 톤 이탈

출력:

- 1페이지 브리프
- `must keep`
- `optional`
- `forbidden`

### 2. Reveal Control Layer

역할:

- 미디어가 어디까지 드러내도 되는지 통제

등급:

- `safe`
- `tease-only`
- `spoiler-risk`
- `forbidden`

## Music Engine

### Required Inputs

- 장면 / 인물 / 세력 / 액트
- 감정 arc
- 템포감
- 문화권 / 대륙성
- 악기 금지 / 허용

### Required Checks

- 대륙 문화와 악기/보컬 질감이 맞는가
- 장면보다 과도한 영웅주의로 튀지 않는가
- 관계 장면인데 전투 음악처럼 오판하지 않는가

### Output Brief

- 감정 키워드 3~5개
- 악기 방향
- 리듬 / 밀도
- 피해야 할 레퍼런스 성격
- 장면 내 사용 위치

## Image Engine

### Required Inputs

- 대상 인물 / 장소 / 아이템 / 세력
- 시점과 복장 단계
- 소속 / 계급 / 상처 / 장비 상태
- 환경 정보

### Required Checks

- 명칭과 외형 불일치
- 대륙 / 세력 / 기후 / 복식 충돌
- 아직 없는 장비나 상징의 조기 노출
- generic fantasy로 흐르는지

### Output Brief

- 피사체 요약
- 반드시 보여야 할 요소
- 보여주면 안 되는 요소
- 구도 / 거리감
- 색 / 재질 / 광원 / 손상도
- canon note

## Video Engine

### Required Inputs

- 장면 목적
- 등장 인물과 관계 상태
- 액트 내 위치
- 공개 가능 정보 범위
- 필요 소품 / 장소

### Required Checks

- 미래 회수 정보를 누설하는가
- 캐릭터 관계가 현재 시점과 맞는가
- 전투 / 서정 / 회상 톤이 오판되었는가
- 이미지적으로는 맞아도 연출상 개연성을 깨는가

### Output Brief

- scene objective
- 등장 인물 / 금지 인물
- shot priority
- reveal level
- dialogue / no-dialogue
- ending beat

## Visual-Side Extra Modules

### 3. Visual Canon Registry

- 대륙, 세력, 종족, 기후, 재질, 색채, 금기 요소의 시각 기준표

### 4. Character-to-World Binding Registry

- 인물, 가문, 길드, 지역, 소지품, 생활권의 시각 연결표

### 5. Map / Location Visual Briefing Module

- 지도용, 일러스트용, 씬용 장소 브리프 분리
- 랜드마크, 생활 밀도, 이동 동선, 권력 구조, 전투 흔적 포함

### 6. Style Conflict Checker

- 기존 설정과 시각 톤이 충돌하는지 검사

### 7. Motif & Repetition Tracker

- 상징, 문양, 색조, 무기 형태, 도시 구조 반복 추적

### 8. Visual QA Checklist Registry

최소 체크:

- 대륙 / 기후와 맞는가
- 세력 계층과 맞는가
- 생활 흔적이 있는가
- 시대감이 맞는가
- 너무 generic fantasy가 아닌가

## Conductor Note

한 줄 결론:

음악, 이미지, 영상은
지금 여기서 `직접 완성`하기보다
`FS 미디어 엔진`으로 브리프와 정합성 체크를 먼저 잡는 게 맞다.

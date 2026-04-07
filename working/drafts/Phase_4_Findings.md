# Phase 4 Findings

## What Was Imported

- `phase4_oceanic_trade_flow.md`
- `phase4_oceanic_strategic_chokepoints.md`
- `phase4_section8_oceanic_pirate_confederacy`
- `phase4_section8_oceanic_golden_armada`
- `phase4_section8_oceanic_church_of_sea`

## Structural Read

해양 대륙은 현재 import 기준으로 `길드 / 상단 / 항만 / 종교 / 함대` 구조가 매우 선명하다.

### Oceanic Guild / Economy Layer

- `enough`
- 근거:
  - 해양 무역 체계 문서가 무역 품목, 세력별 경제 강압, 공식/비공식 무역 루트를 직접 제공한다.
  - 해적 연합은 암시장 조합, 자유 항구 관리부, 밀수/장물 경제를 가진다.
  - 황금 함대는 무역 연합 의회, 해양 상단 연합, 통행세와 화폐 독점을 가진다.
  - 바다의 교단은 항구 도시 치료소, 축복세, 성지-항해 안전 네트워크를 가진다.

### Oceanic House Layer

- `enough`
- 근거:
  - 황금 함대에 `3. 가문 (Noble Houses)`가 분리돼 있고, 5대 해상 귀족 연합 구조가 직접 보인다.
  - 해적 연합도 전통 귀족이 아니라 해적 귀족/가문/파벌 구조를 일부 갖고 있다.

### Oceanic Tribe Layer

- `thin`
- 근거:
  - 현재 batch 안에서는 항구, 함대, 교단, 해적 조직은 강하게 보이지만
    토착 씨족/섬 부족/해양 원주민 공동체는 직접적으로 약하다.

## Spatial Read

해양 대륙은 지도 축 잠재력이 크다.

- `검은 해적항`
- `황금항`
- `심해 궁전`
- `포트 아우렐리온`
- `골든 앵커 하버`
- `마레온`
- `어비스 대성당`
- `검은 해협 감시탑`

즉 도시/항구/성지/요새/해협 병목이 모두 선명해,
`세계지도 -> 대륙 지도 -> 항구 도시 지도`로 이어지기 좋다.

## Conductor Decision

이제 대륙 판정은 이렇게 읽을 수 있다.

- 에테르: 가문/길드 strong, 부족은 정령연합 쪽만 strong
- 크림슨: 부족 strong
- 프로스트: 부족 strong
- 해양: 가문/길드 strong, 부족 thin
- 오벨리스크: 아직 unknown

즉 다음 가장 합리적인 batch는 `오벨리스크`다.
이제 남은 빈 축을 메우면 대륙 5축 중 4축이 실제 evidence 기반으로 서게 된다.

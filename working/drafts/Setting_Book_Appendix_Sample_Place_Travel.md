# Setting Book Appendix Sample: Place and Travel Functions

## Purpose

이 appendix 샘플은 장소와 이동이 설정집에서 어떻게 함께 관리되어야 하는지 보여준다.

본문은 장소가 어떤 장면을 여는지, 길이 어떤 긴장을 만드는지 설명한다.
이 부록은 그 장소와 길이 실제로 어떤 기능 태그와 이동 압력을 가지는지 정리한다.

## Function Pairing Rule

장소와 이동은 분리해서 읽지 않는다.

- 장소는 장면을 여는 기능이다.
- 길은 그 장면에 도달하기 위해 지불해야 하는 비용이다.
- 같은 장소라도 어떤 길로 들어오느냐에 따라 분위기와 권력관계가 달라진다.

## Place / Route Sample Table

| Place | Primary Function | Route Type | What Moves Here | Cost or Gate | Story Pressure |
| --- | --- | --- | --- | --- | --- |
| 골든마르크 | market | merchant_road | 합법 상권 정보, 사치품, 외교 문서, 계약 소문 | 통행세, 상단 허가, 금융 추적 | 번영과 감시가 함께 작동한다. |
| 포트 넥서스 | threshold, underworld_node | sea_lane, underpath | 화물, 밀수품, 외지인, 재회, 배신 소문 | 항만세, 입항 허가, 소개자, 야간 통행 위험 | 합법 무역과 불법 접선이 같은 부두에서 충돌한다. |
| 머시너리 게이트 | threshold | merchant_road | 용병 계약, 평판, 중재 기록, 블랙리스트 | 계약 보증금, 길드 승인, 분쟁 기록 | 명예와 실리가 같은 장부에 적힌다. |
| 공식 경매장 | market | merchant_road | 진품, 가품, 감정서, 귀족 거래, 수집가 욕망 | 초대권, 보증금, 신분 확인 | 거래가 곧 외교와 대결이 되는 공간이다. |
| 검은 고양이 | underworld_node | underpath | 청부 연락, 밀수 약속, 비밀 정보, 사라진 이름 | 암호, 단골 신뢰, 현장 소개 | 말 한마디가 계약이 되기도 함정이 되기도 한다. |
| 제3 부두 비밀 창고 | underworld_node | sea_lane, underpath | 신고되지 않은 상자, 위조 문서, 은닉 화물 | 야간 접근, 선적 협조자, 배신 위험 | 도시의 밤 지도가 실제로 작동하는 장소다. |
| 아르카노스 탑 | workshop | arcane_route | 연구 기록, 금서, 실험 물자, 허가된 지식 | 접근 권한, 의식 비용, 학회 승인 | 지식은 자산이면서 통제 수단이 된다. |
| 봉인 제단 | memory_site, sanctuary | pilgrim_road | 기도, 봉인 점검, 잊힌 이름, 순례 소문 | 순례 시간, 보호 인력, 봉인 주기 | 경건함과 두려움이 함께 유지되는 장소다. |
| 네크로 우물 | memory_site, underworld_node | arcane_route, underpath | 사령 잔향, 금지된 연락, 묘지 정보 | 금기 의식, 오염 위험, 추적 가능성 | 너무 깊이 들여다볼수록 되돌아오기 어려워진다. |
| 드래곤포지 | workshop | mountain_forge_route | 단조 비밀, 화염 재료, 장인 명성 | 재료 확보, 장인 허가, 대가 지불 | 물건 하나가 가문과 전승의 무게를 함께 짊어진다. |

## Route Pressure Notes

각 길은 단순한 거리 단축이 아니라
누가 그 길을 쓸 수 있는가를 정하는 권력 장치다.

| Route Type | Safe Body Translation | Appendix Note |
| --- | --- | --- |
| royal_road | 공식 보호를 받지만 감시가 심한 길 | 통행증, 검문, 귀족/군대 우선권 |
| merchant_road | 상품과 소문이 함께 움직이는 길 | 계약, 세금, 지부 권한, 시장 우회 |
| pilgrim_road | 기억과 신앙이 오래 남는 길 | 느리지만 정당성이 강하고, 순례 규칙이 있다 |
| sea_lane | 바다의 기회와 병목이 교차하는 길 | 계절풍, 해협, 해적, 항만 허가 |
| underpath | 기록되지 않는 그림자 길 | 소개자, 암호, 배신, 비공식 물류 |
| arcane_route | 시간을 줄일 수 있지만 대가가 큰 길 | 의식 비용, 제약, 오염, 추적 위험 |

## Body Conversion Example

Technical appendix language:

```text
Place: Port Nexus
Function: threshold / underworld_node
Route: sea_lane + underpath
Cost: harbor tax, permit, shadow contact
```

Reader-facing body language:

```text
포트 넥서스는 바다에서 온 모든 것이 한 번쯤 얼굴을 드러내는 항구다. 정식 입항 허가를 받은 상선도, 밤의 소개자를 통해 미끄러져 들어오는 밀수선도 결국 이 도시의 숨결을 거친다.
```

## Promotion Rule

장소나 길이 본문에서 독립 항목을 받으려면 아래 중 적어도 두 가지가 필요하다.

1. 여러 세력이 그 장소나 길을 두고 경쟁한다.
2. 인물의 재회, 추적, 배신, 탈출, 거래 같은 핵심 장면이 가능해진다.
3. 물건과 소문이 함께 이동한다.
4. 비용이나 통제권이 세계의 위계를 드러낸다.
5. 같은 장소가 낮과 밤에 다른 의미를 가진다.

## Conductor Decision

이 appendix 샘플의 목적은 하나다.

지도는 예쁜 배경이 아니라
누가 들어오고,
누가 막히고,
누가 숨어 움직이며,
무엇이 값이 되는지를 보여주는 장치라는 점을 끝까지 유지하는 것이다.


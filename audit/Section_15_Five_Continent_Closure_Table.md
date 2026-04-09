# Section 15 Five Continent Closure Table

이 문서는 `15 Named Notables`의 5대륙 1차 압축 종료표다.

목적:

- 14번 영웅과 15번 명사형 인물을 섞지 않는다.
- 안정 15 후보, 경계 후보, 이름 없는 역할 슬롯을 한눈에 본다.
- 다음 배치가 새 이름 창작이 아니라 근거 기반 회수로 진행되게 한다.

## Closure Summary

| Continent | Stable 15 Candidates | Boundary / Hold Candidates | Need Named Candidate Slots | Closure State |
|---|---|---|---|---|
| `크림슨` | `울프가르 드래곤포지`, `에리온 드라코비스`, `오그마` | `벨라나`, `아리안`, `드락사르`, `카사르` | 현자회/사막부족 일부 슬롯은 후속 확인 | `closed_for_now` |
| `에테르` | `엘다라` | `대런`, `엘드린`, `마르쿠스/맥스웰`, `이사도르`, `세리오스`, `네리사`, `다미엔`, `칼리스트`, `래퍼티`, `요한`, `엘라라`, `드라이덴`, `메라`, `실라스 나이트쉐이드` | 금서/공방/관측/대서고/성채/성검/서약/그늘항로/정령묘 + low-priority auxiliary 9개 role slot closure 완료 | `closed_for_now` |
| `프로스트` | 없음 | `울프릭`, `시그리드`, `마리안`, `프리야`, `카이라` | `원로 사냥꾼`, `묘지기 장로`, `대예언자`, `수석 기술자`, `별의 샤먼`, `아이스포지 병기소 장인`은 모두 role slot 유지로 closure 완료 | `closed_for_now` |
| `해양` | 없음 | `미다스`, `해양 실비아`, `이소벨`, `마르코`, `엘레오노라`, `골드핑거`, `리나`, `에릭`, `오렌`, `마리아`, `모로스`, `크리스토퍼 델마르` | 오라클, 항로/해도, 조선소, 감정사, 금고, 경매장, 은행, 세관, 무역왕, 폭풍추적대, 검은 돛 조선공, 진혼 악기, 유령선 기록 슬롯. `top 5 slot`, `city-role batch`, `tail unnamed slot batch` read-only pass 완료 | `closed_for_now` |
| `오벨리스크` | 없음 | `바리온`, `아이기스`, `카론`, `베스`, `이안`, `카트린`, `레보니아`, `우로스`, `세르반`, `레티시아`, `렌`, `라일`, `루가르` | `기록의 수호자`, `오벨리스크 관측대장`, `신성 기록소 관리 사제`, `묘역 감독관`, `기억 경매장 중개자`, `사후 서기관`은 slot 유지. `기억 지기 = 렌/라일`, `심연 계약 중개자 = 루가르 strong link` | `closed_for_now` |

## Current Safe 15 Work Set

현재 실제 15번 시트 시험에 가장 안전한 후보:

1. `울프가르 드래곤포지`
2. `에리온 드라코비스`
3. `오그마`
4. `엘다라`
5. `실비아`

주의:

- `실비아`는 키르케/범대륙 후기 확장 축이라 메인 진행 후순위다.
- `엘다라`는 에테르 정령연합의 강한 15 후보지만, 정령연합 전체 14 확인 전 Hard Canon으로 고정하지 않는다.

## Hard Hold Clusters

| Cluster | Reason |
|---|---|
| `SS/S/A급 및 Act 신호` | 14 영웅축과 겹칠 수 있어 15 확정 금지. |
| `전설 영웅록` | 이름 있는 명사처럼 보여도 영웅백과 중심 인물일 수 있음. |
| `제독 / 단장 / 탑주 / 원로단 지도부` | 조직 핵심 인물로 14 또는 세력 핵심 문서에 남을 가능성이 높음. |
| `이름 충돌` | `실비아`, `아이기스`, `메라`, `Ravenfell`, `실라스`, `Selena`, `Valerius`, `Drake` 등 병합 금지. |
| `개인명 없는 역할 슬롯` | 새 이름을 만들지 않고 장소-기관 슬롯으로 보존. |

## Routing Rule

앞으로 15번 후보는 아래 순서로만 처리한다.

1. `대륙 -> 세력 / 도시 / 조직` 앵커 확인.
2. 14번 독립 파일 또는 영웅표 신호 확인.
3. 이름 충돌 확인.
4. `named_notable_candidate`, `verify_before_15`, `need_named_candidate`, `keep_14` 중 하나로 상태 라벨 부여.
5. 안정 후보만 15 Named Notables 개별 시트로 승격.

## Next Orchestrated Move

다음 큰 흐름은 전역 closure sync를 바탕으로
`크림슨 안정 3명`의 실제 15 작업선을 재가동하는 것이다.

이유:

- Ether low-priority auxiliary slot 9개 closure와 압축표 동기화가 완료됐다.
- `해양`의 `신탁 방주`, `해로 장부관`, `왕실 선공장 수석장`, `흑조 감정관`, `심연 장부관`은 direct holder 없이 1차 pass가 닫혔다.
- `항해사 길드장`, `마스터 쉽라이트`, `수석 기상관`, `대경매장 주인`, `은행장`, `세관장`도 direct holder 없이 city-role batch가 닫혔다.
- 이번 턴에서 `수석 무역왕`, `스톰 체이서 대장`, `조선공 길드 장인`, `진혼 악기지기`, `망자항해 기록관`도 direct holder 미확인 role slot으로 닫혔다.
- 따라서 해양 unnamed slot read-only pass는 1차 마감 상태다.
- `오벨리스크`는 2차 narrowing에서 `신성 기록소 관리 사제`, `묘역 감독관`도 direct holder 없이 role slot 유지로 닫았다.
- `기억 지기`는 `렌 / 라일` 복수 existing holder, `심연 계약 중개자`는 `루가르` strong-link verify 상태로 읽힌다.
- 따라서 오벨리스크 핵심 slot read-only narrowing은 2차까지 한 번 닫혔고, 프로스트를 mainline으로 올리는 편이 효율이 높다고 판정했다.
- `프로스트`는 원로단/대예언자/장로 신호가 강하지만, `오로라 평원 / 얼음무덤 언덕 / 푸른 폭풍 요새 / 겨울회의 의장막 / 퍼마프로스트 요새 / 아이스포지 병기소` 앵커 기준의 place-first role slot pass로 오염을 통제할 수 있다는 점을 확인했다.
- 이번 턴에 `아이스포지 병기소 장인`까지 named holder 없이 role slot으로 닫혀 프로스트 unnamed slot 6개 closure가 한 번 완료됐다.
- 따라서 다음 batch는 새 인물 회수가 아니라 `울프가르`, `에리온`, `오그마`의 실제 15 시트 hardening / foldering test다.
- `엘다라`는 보조 후보로 유지하되 정령연합 전체 14 확인 전 Hard Canon 승격은 보류한다.

# Section 15 Named Notables Anchor Map

이 문서는 `15 Named Notables` 후보를
`대륙 -> 세력 / 도시 / 조직` 기준으로 정렬하기 위한 앵커 맵이다.

핵심 원칙:

- 직업별 폴더링은 본체가 아니다.
- 본체는 기존 구조처럼 `대륙 -> 세력 / 도시 / 조직`이다.
- `현자`, `연금술사`, `대장장이`, `기록자` 같은 역할은 보조 태그로 둔다.
- `14` 신호가 강한 후보는 앵커만 기록하고 15 확정은 보류한다.

## Anchor Table

| Name | Continent Anchor | Faction / Place Anchor | Role Tag | State Label | Routing Note |
|---|---|---|---|---|---|
| `실비아` | `범대륙 / 후기 확장` | `키르케 영약회` | `기록자 / 약제사` | `named_notable_candidate` | 키르케 내부 기억과 계량을 보여주는 15 명사형 후보. |
| `멜리산드르` | `범대륙 / 후기 확장` | `키르케 영약회` | `수석 대약제사 / 조직 최고위` | `verify_before_15` | S+급 최고위라 14와 겹칠 수 있다. 15 확정 금지. |
| `울프가르 드래곤포지` | `크림슨` | `용의 후예 / 드래곤포지 공방` | `대장장이 / 공방주` | `named_notable_candidate` | 장인형 유명 NPC로 강한 15 후보. |
| `드락사르 블레이즈포지` | `크림슨` | `용의 후예 / 연금술 공방` | `연금술사 / 공병대장` | `verify_before_15` | 공방 명사 가치가 있지만 A급 영웅표 신호가 있어 14 확인 필요. |
| `에리온 드라코비스` | `크림슨` | `엘드라칸 / 용의 후예` | `대현자 / 고대어 해석가` | `named_notable_candidate` | 학술 도시성과 전승 해석을 담당하는 15 명사형 후보. |
| `오그마` | `크림슨` | `엘드라칸` | `고룡 / 살아있는 도서관` | `named_notable_candidate` | 전승 보관자형 유명 NPC로 강한 15 후보. |
| `카사르 더 시어` | `크림슨` | `용의 후예 / 시험의 탑` | `예언자 / 최고 조언자` | `verify_before_15` | S급 예언자이며 14 중심 영웅 신호가 있어 보류. |
| `벨라나 스톰브링어` | `크림슨` | `붉은 사막 부족 / 현자 회의` | `주술사 / 사제 / 고고학자` | `verify_before_15` | 사막 부족 현자층 가치가 있지만 SS급 폭풍의 여왕 신호가 있어 14 확인 전 15 확정 금지. |
| `아리안 블레이즈하트` | `크림슨` | `붉은 사막 부족 / 현자 회의` | `사제 / 전승 보존자` | `verify_before_15` | 부족 전승과 의례 축의 15 가치가 있지만 S급 대사제 신호가 있어 14 확인 전 15 확정 금지. |
| `엘다라` | `에테르` | `정령연합 / 루미라` | `대현자 / 고대 정령어 권위자` | `named_notable_candidate` | 에테르의 정령/전승층을 사람 얼굴로 보강하는 15 후보. |
| `크리스토퍼 델마르` | `해양` | `황금 함대 / 거상 연합` | `장물 금융 / 암시장 자금` | `verify_before_15` | 검은 동전, 장물 처리, 암시장 자금 담당 신호가 있으나 14/15 경계 확인 전 확정 금지. |

## Current Reading

- `크림슨` 쪽 Named Notables 후보가 가장 많다.
- `범대륙 / 후기 확장` 후보는 키르케 계열이지만, 범대륙 자체가 후순위라 15 확정도 천천히 간다.
- `에테르` 쪽은 현재 `엘다라`가 정령연합 내부 전승층의 대표 후보로 보이고, low-priority auxiliary slot 9개는 각 도시/기관 앵커 아래 role slot 유지로 closure를 마쳤다.
- `프로스트`, `오벨리스크`, `해양` 쪽은 안정 15 후보보다 장소-기관 역할 슬롯이 강하다.

## Section 8 Bridge Update

`Section_8_to_15_Notable_Anchor_Bridge.md` 기준으로
15번 후보는 아래처럼 읽는다.

| Continent | Routing Reading |
|---|---|
| `크림슨` | 부족/씨족 spine과 생존 경제 spine이 본체. 안정 15 후보는 용의 후예/엘드라칸 쪽에 둔다. |
| `에테르` | state_house/guild_market spine이 본체이며, 정령연합만 tribe_clan 특수축으로 본다. 엘다라는 정령연합/루미라 앵커이고, low-priority auxiliary slot 9개는 각 도시/기관 앵커 아래 role slot 유지로 읽는다. |
| `프로스트` | tribe_clan/frontier survival 감각으로 읽고, 확정 인물보다 오로라 평원/빙하의 성소/아이스포지 슬롯을 보존한다. |
| `해양` | state_house/guild_market spine이 본체. 포트 아우렐리온/크로스윈드 포트/오라클 바지 같은 도시 기능형 슬롯을 보존한다. |
| `오벨리스크` | frontier_survival/guild_market spine이 본체. 기록/기억/봉인/망각 장소-기관 슬롯을 먼저 보존한다. |
| `범대륙 / 후기 확장` | 현재 후순위. 키르케 외 확장 세력은 표면명/위상 안정화 뒤 다시 본다. |

## Next Recovery Targets

다음 수집에서는 아래 결손층을 먼저 본다.

1. Ether low-priority auxiliary slot 9개 closure 결과를 8번 spine과 15번 후보/슬롯 브리지에 반영
2. 안정 15 후보의 대륙/세력/도시 앵커 고정
3. `need_named_candidate` 슬롯의 장소-기관 색인 유지
4. 14/15 경계 후보는 14 확인 전 확정 금지
5. 실제 폴더 초안은 브리지 검토 이후에만 작성

현재 정찰 결과는 `Section_15_Five_Continent_Closure_Table.md`와
`Section_8_to_15_Notable_Anchor_Bridge.md`를 우선 기준으로 삼는다.

## Conductor Rule

Named Notables는 `대륙 -> 세력 / 도시 / 조직` 앵커로 보관한다.

직업명은 찾기 쉬운 보조 태그로만 쓰고,
정본 폴더링 기준으로 쓰지 않는다.

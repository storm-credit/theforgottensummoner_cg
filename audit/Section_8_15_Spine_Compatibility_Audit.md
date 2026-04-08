# Section 8 / 15 Spine Compatibility Audit

이 문서는 `8. 세력 아카이브`의 대륙별 spine과
`15. 인물백과` 가상 폴더 구조가 서로 맞는지 점검하는 감사표다.

## Verdict

현재 15번 가상 구조는 8번 spine과 대체로 맞다.

단, 아래 원칙을 지켜야 한다.

- 크림슨은 직업보다 부족/씨족/용의 후예 앵커가 먼저다.
- 에테르는 정령연합을 제외하면 state_house/guild_market 앵커가 먼저다.
- 프로스트는 이름보다 생존/전승/성소/요새 슬롯이 먼저다.
- 해양은 도시/항만/함대/교단/상단 앵커가 먼저다.
- 오벨리스크는 인물보다 기록/기억/봉인/망각 장소-기관 앵커가 먼저다.

## Compatibility Table

| Continent | Section 8 Spine | Section 15 Draft Match | Risk | Decision |
|---|---|---|---|---|
| `크림슨` | `tribe_clan`, `guild_market` | `용의 후예`, `엘드라칸`, `붉은 사막 부족`으로 라우팅되어 spine과 맞음. | `low` | 유지. |
| `에테르` | `state_house`, `guild_market`; 정령연합만 `tribe_clan` | `마법협회`, `성국`, `왕국연합`, `자유도시연합`, `정령연합`으로 분리되어 맞음. | `medium` | 정령연합 후보와 마법협회 후보가 섞이지 않게 유지. |
| `프로스트` | `tribe_clan`, `guild_market`, state_house thin | `빙하의 성소`, `퍼마프로스트 공성단`, `오로라 평원` 중심이라 맞음. | `low` | 이름보다 장소/성소/요새 슬롯 유지. |
| `해양` | `state_house`, `guild_market`; tribe_clan weak | `황금 함대`, `거상 연합`, `해적 연합`, `바다의 교단`, 항구 도시 슬롯으로 라우팅되어 맞음. | `medium` | 도시 기능형 슬롯과 제독/히어로급 후보를 분리. |
| `오벨리스크` | `frontier_survival`, `guild_market`, nontraditional elite | `봉인 수호단`, `잊힌 자들의 연합`, `망자의 왕국`, 기록/기억 장소로 라우팅되어 맞음. | `medium` | 초월 어휘보다 기록/기억/거래 기능으로 낮춰 읽기 유지. |
| `범대륙 후기 확장` | deferred expansion | `키르케 영약회`만 후순위로 보존되어 맞음. | `medium` | 범대륙 전체 확정 금지. |

## Mismatch Watch

| Watch Item | Reason | Mitigation |
|---|---|---|
| `에테르 / 정령연합` | 에테르 전체 spine은 state_house/guild_market인데 정령연합만 tribe_clan 특수축이다. | 정령연합은 별도 특수축으로 유지. |
| `해양 / 해적 연합` | 해양은 state_house/guild_market이 강하지만 해적 연합은 비국가/암시장 성격이 강하다. | 해적 연합은 `guild_market / underworld maritime` 보조 라벨로 둔다. |
| `오벨리스크 / 망자의 왕국` | 초월/망자 어휘가 강해 인간 서사를 밀 수 있다. | `기록`, `기억`, `거래`, `죄책감`, `망명` 기능으로 낮춰 읽는다. |
| `범대륙` | 후기 증설 파트라 전체 구조를 흔들 수 있다. | 메인 대륙 정리 후순위로 둔다. |

## Foldering Gate Result

`Section_15_Folder_Structure_Draft.md`는 8번 spine과 호환된다.

다만 실제 폴더 생성은 아직 보류한다.

다음에 필요한 것은 실제 이동이 아니라,
`15번 안정 후보 4명 + 실비아 후순위 후보`를 8번 앵커와 더 강하게 묶는
작은 색인이다.

## Next Action

다음 문서:

- `Section_15_Stable_Candidate_8_Anchor_Index.md`

목표:

- 울프가르, 에리온, 오그마, 엘다라, 실비아의 8번 앵커를 한 번 더 고정한다.

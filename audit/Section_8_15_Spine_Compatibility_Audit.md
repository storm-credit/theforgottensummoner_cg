# Section 8 / 15 Spine Compatibility Audit

이 문서는 `8. 세력 아카이브`의 대륙별 spine과
`15. 인물백과` 가상 폴더 구조가 서로 맞는지 점검하는 감사표다.

## Input

- `audit/Section_8_Normalization_Status_Compass.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Place_Network_Handoff_Map.md`
- `audit/Section_8_Status_Vocabulary_Guard.md`
- `audit/Section_8_to_15_Notable_Anchor_Bridge.md`
- `audit/Section_15_Stable_Candidate_8_Anchor_Index.md`
- `audit/Section_15_Profile_Draft_Index.md`
- `audit/Section_15_Operational_Lines_Track.md`
- `audit/Section_8_15_Closure_Sync_Carryover_Watch.md`
- `audit/Five_Continent_Missing_Layer_Policy_Lock.md`

## Verdict

현재 15번 가상 구조는 8번 spine과 대체로 맞다.

단, 아래 원칙을 지켜야 한다.

- 결손층 5개의 thin/support 판정은 이 compatibility audit이 새로 확정하지 않고,
  `audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 참조한다.
- 크림슨은 직업보다 부족/씨족/용의 후예 앵커가 먼저다.
- 에테르는 정령연합을 제외하면 state_house/guild_market 앵커가 먼저다.
- 프로스트는 이름보다 생존/전승/성소/요새 슬롯이 먼저다.
- 해양은 도시/항만/함대/교단/상단 앵커가 먼저다.
- 오벨리스크는 인물보다 기록/기억/봉인/망각 장소-기관 앵커가 먼저다.
- 결손층 5개는 master lock이 허용한 thin/support 범위를 넘겨 읽지 않는다.
- named notable 카드와 operational profile 카드는 같은 carryover 원칙 아래 움직이되,
  하위 profile의 `3-1. Policy Guard`를 상위 summary가 덮어쓰지 않는다.

## Compatibility Table

| Continent | Section 8 Spine | Section 8 Carryover | Section 15 Draft Match | Risk | Decision |
|---|---|---|---|---|---|
| `크림슨` | `tribe_clan`, `guild_market` | `용의 후예 = section_style + clan_as_state_house watch`; `붉은 사막 부족 연합 = mixed_keep + clan_as_state_house watch` | `용의 후예`, `엘드라칸`, `붉은 사막 부족`으로 라우팅되어 spine과 맞음. | `low` | 유지. 크림슨은 씨족 상층을 국가형 가문 라우팅으로 과승격하지 않는다. |
| `에테르` | `state_house`, `guild_market`; 정령연합만 `tribe_clan` | `정령연합 = mixed_keep / special_axis_generalization` | `마법협회`, `성국`, `왕국연합`, `자유도시연합`, `정령연합`으로 분리되어 맞음. | `medium` | 정령연합 후보와 마법협회 후보가 섞이지 않게 유지. |
| `프로스트` | `tribe_clan`, `guild_market`, state_house thin | `프로스트본 연합 = mixed_keep + clan_as_state_house watch`; `오로라 평원`, `빙하의 성소`는 `place_pressure_strong / handoff_applied` | `빙하의 성소`, `퍼마프로스트 공성단`, `오로라 평원` 중심이라 맞음. | `low` | 이름보다 장소/성소/요새 슬롯 유지. 구조 라벨과 place pressure를 섞지 않는다. |
| `해양` | `state_house`, `guild_market`; tribe_clan weak | `해적 연합 = mixed_keep + port_power_as_tribe_clan`; `바다의 교단 = section_style_reclassify + place_pressure_strong / handoff_applied` | `황금 함대`, `거상 연합`, `해적 연합`, `바다의 교단`, 항구 도시 슬롯으로 라우팅되어 맞음. | `medium` | 도시 기능형 슬롯과 제독/히어로급 후보를 분리하고, 토착 공동체층은 `support range`를 넘겨 본체화하지 않는다. |
| `오벨리스크` | `frontier_survival`, `guild_market`, nontraditional elite | `망자의 왕국 = section_style_reclassify + nontraditional_elite watch`; `잊힌 자들의 연합 = section_style_reclassify + watch_keep / handoff_applied`; `봉인 수호단 = section_style_reclassify + mismatch_clear` | `봉인 수호단`, `잊힌 자들의 연합`, `망자의 왕국`, 기록/기억 장소로 라우팅되어 맞음. | `medium` | 초월 어휘보다 기록/기억/거래 기능으로 낮춰 읽고, 가문/왕국 신호는 `nontraditional elite thin-support`를 넘겨 읽지 않는다. |
| `범대륙 후기 확장` | deferred expansion | `canonical_root / quarantine_root / legacy_root` 분리와 `root_corruption` 경계 유지 | `키르케 영약회`만 후순위로 보존되어 맞음. | `medium` | 범대륙 전체 확정 금지. 루트 안정화 전 15 확장 금지. |

해양 자유도시/오벨리스크 제도 사례는
named notable 즉시 승인 근거가 아니라
operational lower-card carryover reference로만 유지한다.

## Mismatch Watch

| Watch Item | Reason | Mitigation |
|---|---|---|
| `에테르 / 정령연합` | 에테르 전체 spine은 state_house/guild_market인데 정령연합만 tribe_clan 특수축이다. | 정령연합은 별도 특수축으로 유지. |
| `해양 / 해적 연합` | 해양은 state_house/guild_market이 강하지만 해적 연합은 비국가/암시장 성격이 강하다. | 해적 연합은 `guild_market / underworld maritime` 보조 라벨로 둔다. |
| `오벨리스크 / 망자의 왕국` | 초월/망자 어휘가 강해 인간 서사를 밀 수 있다. | `기록`, `기억`, `거래`, `죄책감`, `망명` 기능으로 낮춰 읽는다. |
| `범대륙` | 후기 증설 파트라 전체 구조를 흔들 수 있다. | 메인 대륙 정리 후순위로 둔다. |

## Section 8 Carryover Rule

`15` 브리지에서 반드시 같이 들고 가야 하는 `Section 8` 기준은 아래다.

1. `structure label`과 `place pressure`를 같은 것으로 쓰지 않는다.
2. `mixed_keep`는 아직 살아 있는 구조 예외이지, 정리되지 않은 오류가 아니다.
3. `section_style_reclassify`는 구조 문법 판정이고,
   내용 압력은 `place_pressure_strong` 또는 `watch_keep`로 별도 보존한다.
4. `root_corruption`이 잠긴 범대륙 축은
   `15`에서 적극 확장하지 않고 deferred 상태로만 연결한다.
5. 상위 `named notable` summary와 bridge는
   하위 operational profile 카드의 `3-1. Policy Guard`를 참조하되,
   카드 해석선을 재정의하지 않는다.
6. subline 확장까지 내려간 경우에도
   exact operational guard wording authority는 각 `Section_15_Subline_Profile_*` 카드의
   `3-1. Policy Guard`에 남고,
   spine compatibility audit은 그 wording source를 호환성 층에서만 참조한다.
7. representative `Port Authority / Black Auction / Gravewell / Counterfeit Workshop` pair는
   닫힌 subline 교차감사 샘플로 유지하고,
   compatibility audit은 그 closure 상태를 named notable spine 판정과 분리해 읽는다.

## Foldering Gate Result

`Section_15_Folder_Structure_Draft.md`는 8번 spine과 호환된다.

다만 실제 폴더 생성은 아직 보류한다.

필요했던 작은 색인은
`Section_15_Stable_Candidate_8_Anchor_Index.md`로 이미 잠겼다.

## Reference Watch Snapshot

현재 watch 기준:

1. `Section_15_Stable_Candidate_8_Anchor_Index.md`의 `stable triad / support_hold / deferred_expansion_hold` 상태를 bridge와 package freeze에서 계속 같은 상태어로 유지한다.
2. `P2 place-pressure handoff`는 candidate index가 아니라 sidecar/register에서 계속 관리한다.
3. 원본 접근이 가능해질 때까지는 새 candidate를 늘리지 않고 `P0 / P2 / carryover sync`만 유지한다.
4. 현재 carryover mainline은 `Section_8_15_Closure_Sync_Carryover_Watch.md` 기준 `5대륙 closure sync / Section 8 -> 15 carryover watch`로 유지한다.
5. 현재 메인 본선은 stable triad package 재개방이 아니라 closure sync / carryover watch 유지다.
6. named notable coverage 표와 bridge 요약은 operational profile 카드가 이미 잠근 `3-1. Policy Guard`를 존중하는 상위 reference층으로만 유지한다.
7. named notable coverage 표와 bridge 요약은 `Section_15_Subline_Profile_*` 카드가 잠근
   `3-1. Policy Guard`도 같은 lower-card authority로 존중하는 상위 reference층으로만 유지한다.

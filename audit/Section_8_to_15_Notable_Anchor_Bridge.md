# Section 8 to 15 Notable Anchor Bridge

이 문서는 `8. 세력 아카이브`의 대륙별 spine과
`15 Named Notables` 후보/역할 슬롯을 연결하는 브리지다.

목적:

- 15번 인물을 직업별로 흩뜨리지 않는다.
- 후보마다 `대륙 -> 세력 / 도시 / 조직` 앵커를 먼저 잡는다.
- 14번 영웅인지, 15번 명사형 인물인지, 아직 이름 없는 슬롯인지 분리한다.

결손층 5개 정책 잠금과 evidence/firewall 묶음의 단일 entry는
`Five_Continent_Missing_Layer_Master_Lock.md`를 우선 따른다.

## Input

- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Normalization_Status_Compass.md`
- `audit/Section_8_Place_Network_Handoff_Map.md`
- `audit/Section_8_Status_Vocabulary_Guard.md`
- `audit/Section_15_State_Vocabulary_Guard.md`
- `audit/Section_15_Profile_Draft_Index.md`
- `audit/Section_15_Operational_Lines_Track.md`

## Routing Rule

15번 라우팅 reference는 아래 순서로 읽는다.

1. 대륙 spine 확인.
2. 세력/도시/조직 앵커 확인.
3. `Section 8` 구조 라벨과 `place pressure` carryover 확인.
4. 14번 영웅 신호 확인.
5. `named_notable_candidate`, `stable_15_workset`, `verify_before_15`, `need_named_candidate`, `keep_14`, `support_hold`, `deferred_expansion_hold`, `hold_for_dual_review` 중 잠긴 상태 라벨을 확인한다.
6. 폴더링은 `대륙 -> 세력 / 도시 / 조직` 기준으로만 한다.
7. operational profile 카드가 필요한 경우 하위 카드의 `3-1. Policy Guard`를 유지하고,
   named notable 요약과 혼합하지 않는다.

즉 `15` 라우팅은
`Section 8` 구조 라벨을 무시하지 않고,
동시에 `place pressure strong`이 있는 항목은
sidecar/register handoff를 먼저 존중한다.

## Continent Bridge

| Continent | Section 8 Spine | Section 8 Carryover | Stable 15 Candidate | Boundary / Hold | Need Named Candidate Routing |
|---|---|---|---|---|---|
| `크림슨` | `tribe_clan`, `guild_market` | `용의 후예 = section_style + clan_as_state_house watch`; `붉은 사막 부족 연합 = mixed_keep` | `울프가르 -> 용의 후예 / 드래곤포지 공방`; `에리온 -> 엘드라칸 / 학술-전승층`; `오그마 -> 엘드라칸 / 전승 보관층` | `벨라나/아리안 -> 붉은 사막 부족 / 현자 회의`; `드락사르/카사르 -> 용의 후예` | stable triad는 actual draft package freeze 상태로 유지한다. 현자회/사막부족 슬롯은 부족/씨족 spine 아래 보존한다. |
| `에테르` | `state_house`, `guild_market`; 정령연합만 `tribe_clan` | `정령연합 = mixed_keep / special_axis_generalization` | `엘다라 -> 정령연합 / 루미라 [support_hold]` | `대런/칼리스트/에드가 -> 마법협회`; `래퍼티/요한/실라스 블랙쏜 -> 성국`; `리아나 -> 왕국연합`; `셀레나/레온 벨가르드 -> 자유도시연합`; `엘라라/드라이덴/메라/실라스 나이트쉐이드 -> 정령연합` | 금서/공방/관측/대서고/성채/성검/서약/그늘항로/정령묘 슬롯은 각 도시/기관 앵커 아래 보존한다. `드라이덴 / 메라 / 실라스 나이트쉐이드`는 각각 `great_druid_hold / spirit_envoy_hold / shadow_crow_hold`로 읽는다. |
| `프로스트` | `tribe_clan`, `guild_market`; state_house thin | `프로스트본 연합 = mixed_keep`; `오로라 평원`, `빙하의 성소`는 `place_pressure_strong / handoff_applied` | 없음 | `울프릭/마리안/프리야/카이라 -> 빙하의 성소 / 주술사 원로단`; `시그리드 -> 퍼마프로스트 공성단 / 아이스포지` | 오로라 평원, 얼음무덤 언덕, 푸른 폭풍 요새, 아이스포지 병기소 슬롯으로 보존. unnamed slot 6개는 direct holder 없이 role slot 유지로 한 번 닫혔다. |
| `해양` | `state_house`, `guild_market`; tribe_clan weak | `해적 연합 = mixed_keep`; `바다의 교단 = section_style_reclassify + place_pressure_strong / handoff_applied` | 없음 | `미다스/이소벨/해양 실비아 -> 황금 함대`; `마르코/엘레오노라/크리스토퍼 -> 거상 연합`; `골드핑거/리나/에릭/모로스 -> 해적 연합`; `오렌/마리아 -> 바다의 교단` | 포트 아우렐리온, 크로스윈드 포트, 오라클 바지, 블랙워터 항구, 볼트 오브 아우룸 슬롯으로 보존한다. |
| `오벨리스크` | `frontier_survival`, `guild_market`; state_house as nontraditional elite | `망자의 왕국 = section_style_reclassify + place_pressure_strong`; `잊힌 자들의 연합 = section_style_reclassify + watch_keep / handoff_applied`; `봉인 수호단 = section_style_reclassify + mismatch_clear` | 없음 | `바리온/아이기스/베스/이안 -> 봉인 수호단`; `카트린/레보니아/우로스 -> 잊힌 자들의 연합`; `카론/세르반/레티시아 -> 망자의 왕국` | 템플 오브 바운더리, 경계의 보루, 기억 경매장, 영원의 기록탑, 망각의 회랑, 그림자 도서관 슬롯으로 보존한다. |
| `범대륙 / 후기 확장` | deferred expansion; `guild_market` 중심 | `root_corruption`과 deferred routing 유지 | `실비아 -> 키르케 영약회` | `멜리산드르 -> 키르케 영약회` | 범대륙은 후순위. 정본명/표면명/위상 안정화 뒤 다시 본다. |

## Foldering Consequence

15번 문서 라우팅 reference를 읽을 때는 아래 방식으로 본다.

예시:

- `15 / 크림슨 / 용의 후예 / 드래곤포지 공방 / 울프가르 드래곤포지`
- `15 / 크림슨 / 엘드라칸 / 학술-전승층 / 에리온 드라코비스`
- `15 / 크림슨 / 엘드라칸 / 전승 보관층 / 오그마`
- `15 / 에테르 / 정령연합 / 루미라 / 엘다라 [support_hold]`
- `15 / 해양 / 포트 아우렐리온 / 대경매장 주인 슬롯`
- `15 / 오벨리스크 / 영원의 기록탑 / 사후 서기관 슬롯`

단, live 폴더 이동은 하지 않는다.
현재는 `cg` 안에서 라우팅 기준만 reference로 유지한다.

## Bridge Guard

브리지 문서에서 반드시 지킬 기준은 아래다.

1. `section_style_reclassify`는 폴더링 기준에 영향을 주지만,
   `place_pressure_strong`은 sidecar/register handoff를 먼저 본다.
2. `mixed_keep` 세력은 성급히 `section_style` 표준 폴더로 접지 않는다.
3. `mismatch_clear`는 구조 오해가 해소됐다는 뜻이지,
   장소 압력이나 기능 압력이 사라졌다는 뜻은 아니다.
4. `support_hold`와 `deferred_expansion_hold`는 stable triad actual draft package에 섞지 않는다.
5. 개별 카드의 `Policy Guard`가 `state_house strong`, `토착 공동체층`, `전통 국가기관` 과독해를 막고 있으면 브리지도 그 해석선을 넘겨 읽지 않는다.
6. 개별 operational profile 카드의 `3-1. Policy Guard`는 하위 권한선이다.
   bridge는 그것을 요약해서 참조할 뿐, 다른 국가형/공동체형 본체 근거로 다시 승격하지 않는다.
7. 자유도시 `urban_market / shadow_port / debt-enforcement`와
   오벨리스크 `dark institution / nontraditional elite thin-support` 문구는
   operational profile cluster를 통해서만 이어지고,
   named notable 승인 근거로 직접 수입하지 않는다.
8. exact operational guard wording authority는 계속 각 `Section_15_Profile_*` 카드의
   `3-1. Policy Guard`에 남고, bridge는 그 wording source를 구조 브리지 층에서만 참조한다.
9. subline 확장까지 내려간 경우에도
   exact operational guard wording authority는 각 `Section_15_Subline_Profile_*` 카드의
   `3-1. Policy Guard`에 남고, bridge는 그 wording source를 구조 브리지 층에서만 참조한다.
10. representative `Port Authority / Black Auction / Gravewell / Counterfeit Workshop` pair는
    닫힌 subline 교차감사 샘플로 유지하고,
    bridge는 그 closure 상태를 named notable routing 근거와 분리해 읽는다.
11. `결손층 5개`의 thin/support 판정은 이 bridge가 새로 확정하지 않고,
    `audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 참조한다.

## Card Layer Separation

- `Section_15_Named_Notable_*` 카드는 `Policy Guard` 또는 `Separation Guard`를 유지한다.
- `Section_15_Profile_*` operational card는 `3-1. Policy Guard`를 유지한다.
- bridge는 이 두 카드층을 같은 carryover 원칙 아래 묶되,
  named notable card와 operational profile card를 같은 증거층으로 합치지 않는다.

## Conductor Decision Snapshot

15번의 recorded carryover focus는 새 인물 확장이 아니라,
위 브리지와 `Section_15_Folder_Structure_Draft.md`를 기준으로
이미 잠근 anchor / state wording을 closure sync / carryover watch 기준으로 유지하는 것이다.

stable triad actual draft package freeze는 이미 닫혀 있으므로 다시 열지 않는다.
현재는 폴더 draft reference 구조를 문서 레벨에서 유지/점검하는 단계다.

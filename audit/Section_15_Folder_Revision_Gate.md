# Section 15 Folder Revision Gate

이 문서는 `Section_15_Folder_Structure_Draft.md`와
closure sync / watch-reference의
안전 점검표다.

folder gate reading은
`Section_15_Named_Notables_Status_Compass.md`,
`Section_15_Named_Notables_Register.md`,
`Section_15_Index_Draft.md`,
`Section_15_Folder_Structure_Draft.md`,
`Section_15_Folder_Draft_Routing_Plan.md`,
`Section_15_Actual_Draft_Package_Freeze.md`,
`Section_15_Group_Index.md`,
`Section_15_Profile_Draft_Index.md`,
`Section_15_Subline_Register.md`,
`Section_15_Named_Notables_Name_Collision_Register.md`,
`Section_14_15_Boundary_Verification_Queue.md`,
`Section_15_Frost_Place_Institution_Sidecar.md`,
`Section_15_Oceanic_Place_Institution_Sidecar.md`,
`Section_15_Ether_Place_Institution_Sidecar.md`,
`Section_15_Obelisk_Place_Institution_Sidecar.md`,
`Section_15_Named_Notables_Frost_Scout.md`,
`Section_15_Named_Notables_Oceanic_Scout.md`,
`Section_15_Named_Notables_Ether_Scout.md`,
`Section_15_Named_Notables_Obelisk_Scout.md`,
`Section_15_Frost_Display_Canon_Candidates.md`,
`Section_8_15_Closure_Sync_Carryover_Watch.md`,
`Continuous_Workstream.md`
기준으로 읽는다.

목표:

- stable_triad_frozen_reference_set / hold reference split / hold cluster watch-reference snapshot에서 위험을 먼저 확인한다.
- live 폴더 생성/이동 전에 마지막 안전 조건을 잠근다.
- 14번 영웅과 15번 명사형 인물을 섞지 않는다.
- 이름 충돌과 후기 확장 구역을 과확정하지 않는다.

## Gate Checklist

| Gate | Question | Recorded Result |
|---|---|---|
| `G1. Archive Split` | 14 중심 영웅과 15 명사형 인물이 분리되어 있는가? | `pass_with_holds` |
| `G2. Folder Basis` | 직업별이 아니라 대륙 -> 세력/도시/조직 기준인가? | `pass` |
| `G3. Boundary Safety` | `source_check_hold / hold reference split` 후보를 live 15 고정자로 다루지 않았는가? | `pass` |
| `G4. Name Collision Safety` | 실비아, 아이기스, 메라, Ravenfell, 실라스 등 충돌을 병합하지 않았는가? | `pass` |
| `G5. Need Named Candidate Safety` | 개인명 없는 슬롯에 새 이름을 만들지 않았는가? | `pass` |
| `G6. Original Repo Safety` | 원본 저장소를 건드리지 않았는가? | `pass` |
| `G7. Late Expansion Safety` | 범대륙 후기 확장을 메인 정본처럼 과확정하지 않았는가? | `pass_with_deferred_expansion_hold / hold reference split` |
| `G8. Stable Triad Route Safety` | `울프가르 / 에리온 / 오그마`가 `드래곤포지 공방 / 학술-전승층 / 전승 보관층` `stable_triad_frozen_reference_set` 기준으로 분리되어 있는가? | `pass_with_frozen_reference_lock` |
| `G9. source_check_hold Separation` | `엘다라`가 `stable_triad_frozen_reference_set`에 섞이지 않고 hold reference split 안의 `source_check_hold`로 분리되어 있는가? | `pass_with_source_check_hold / hold reference split` |
| `G10. Move Freeze Safety` | bridge / routing consistency 점검 단계에서도 live 파일 이동은 여전히 금지되어 있는가? | `pass` |
| `G11. Route Hierarchy Consistency` | 상위 route anchor와 보조 place lock이 같은 계층처럼 혼용되지 않는가? | `pass_with_hierarchy_lock` |
| `G12. stable_triad_frozen_reference_set Completeness` | `stable_triad_frozen_reference_set`과 hold reference split / hold cluster가 별도 freeze 시트까지 포함해 잠겨 있는가? | `pass_with_frozen_reference_lock` |

## Risks

| Risk | Severity | Mitigation |
|---|---|---|
| `에테르 후보 과밀` | `medium` | 마법협회/성국/정령연합 경계 후보는 전원 `source_check_hold / hold reference split` 또는 `keep_14` 유지. |
| `해양 역할 슬롯 과다` | `medium` | 포트 아우렐리온/크로스윈드 포트 중심으로 장소 기능을 먼저 보존. |
| `오벨리스크 초월 서사 과열` | `medium` | 사람보다 기록/기억/거래/죄책감/망명 기능으로 낮춰 읽음. |
| `범대륙 후기 확장 과확정` | `medium` | 키르케는 강한 후보처럼 보일 수 있는 항목도 `deferred_expansion_hold / hold reference split`으로만 보존하고 전체 범대륙은 watch-reference mainline 바깥에 유지. |
| `live 폴더 이동 시 충돌` | `high` | 아직 이동하지 않는다. 현재도 `cg` 설계문서로만 유지한다. |
| `stable triad route drift` | `medium` | `울프가르 = 드래곤포지 공방`, `에리온 = 학술-전승층`, `오그마 = 전승 보관층` 기준을 bridge/routing docs에 고정 유지. |
| `엘다라 premature promotion` | `medium` | `source_check_hold / hold reference split`, `정령연합 전체 14 확인 전 Hard Canon 금지`를 동시에 유지. |
| `route/place 계층 혼용` | `medium` | 상위 route는 `공방 / 층 / 보관층`, 보조 place는 `도서관 / 샘 / 재료지`로 분리 표기한다. |
| `package scope blur` | `medium` | stable triad와 hold reference split을 `Section_15_Actual_Draft_Package_Freeze.md`에서 분리 유지한다. |
| `policy overread recurrence` | `medium` | 카드층의 `Policy Guard`와 summary/folder carryover 문장을 같이 유지해 `state_house strong`, `토착 공동체층`, `전통 국가기관` 과독해를 막는다. |

## Profile Format Gate

- `결손층 5개`의 thin/support 판정은 revision gate가 새로 결정하지 않고,
  `audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 참조한다.
- operational profile card는 `Section_15_Profile_Template.md`의 `3-1. Policy Guard` 형식을 유지해야 한다.
- 폴더/route/revision gate 문서는 이 하위 profile 형식을 덮어쓰지 않고,
  같은 carryover rule이 유지되는지만 검사한다.
- People Worth Seeking summary와 profile summary가 함께 보일 때도,
  lower-card authority는 operational profile의 `3-1. Policy Guard`에 남겨 둔다.
- exact operational guard wording authority는 계속 각 `Section_15_Profile_*` 카드의
  `3-1. Policy Guard`에 남고, revision gate는 그 wording source를 대체하지 않는다.
- subline 확장까지 내려간 경우에도
  exact operational guard wording authority는 각 `Section_15_Subline_Profile_*` 카드의
  `3-1. Policy Guard`에 남고, revision gate는 그 wording source를 대체하지 않는다.
- representative `Port Authority / Black Auction / Gravewell / Counterfeit Workshop` pair는
  닫힌 교차감사 샘플로 유지하며,
  revision gate는 새 drift가 생길 때만 해당 pair를 다시 점검한다.
- continent sidecar/scout/display wording umbrella는
  lower current-state watch/reference authority로만 읽고,
  revision gate가 새 package build queue로 재상승시키지 않는다.

## Gate Decision

`Section_15_Folder_Structure_Draft.md`는
`stable_triad_frozen_reference_set`과 watch-reference용으로만 유지 가능하다.

하지만 live 폴더 이동 또는 문서 이동은 아직 금지한다.

현재는 아래 두 가지를 `watch-reference 기준`으로만 유지한다.

1. `stable_triad_frozen_reference_set` 유지와 closure sync / watch-reference 점검
2. `15번 live 폴더 생성/이동 계획`은 계속 보류
3. continent sidecar/scout/display wording umbrella는
   lower current-state watch/reference authority로만 유지

추가 기준:

- `크림슨` route는 씨족 중심 질서와 thin-support까지만 반영한다.
- `해양` route는 자유도시 shadow-market cluster를 `urban_market` 범위에서만 반영한다.
- `오벨리스크` route는 `nontraditional elite thin-support / dark institution` 범위에서만 반영한다.

## Conductor Decision

현재 `Section 15` 내부 기준은
stable_triad_frozen_reference_set / hold reference split / hold cluster watch-reference snapshot을 유지한 채,
hold reference split / hold cluster 쪽 경계 보류군 유지 점검과
carryover wording consistency를 함께 유지하는 것이다.

# Section 8 Mainline Sync Register

이 문서는 `Section 8` 본선에서
서로 반드시 같은 판정을 가리켜야 하는 문서 묶음을 정리한 장부다.

목적은 단순하다.

`한 문서에서 판정이 바뀌면 어느 문서를 같이 봐야 하는지 즉시 알 수 있게 한다.`

## Input

- `audit/Section_8_Status_Vocabulary_Guard.md`
- `audit/Section_8_Normalization_Status_Compass.md`
- `audit/Section_8_Structure_Label_Map_First_Pass.md`
- `audit/Section_8_Spine_Mismatch_Queue.md`
- `audit/Section_8_Next_Audit_Targets.md`
- `audit/Section_8_Place_Network_Handoff_Map.md`
- `audit/Section_8_15_Spine_Compatibility_Audit.md`
- `audit/Section_8_15_Closure_Sync_Carryover_Watch.md`
- `audit/Five_Continent_Missing_Layer_Policy_Lock.md`
- `audit/Section_15_State_Vocabulary_Guard.md`
- `audit/Section_15_Stable_Candidate_8_Anchor_Index.md`
- `audit/Next_Sequential_Workstream.md`
- `audit/Audit_Queue.md`

## Sync Groups

| Sync Group | Primary Source | Must Mirror In | What Must Stay Aligned |
|---|---|---|---|
| `status_vocabulary` | `Section_8_Status_Vocabulary_Guard.md` | `Section_8_Structure_Label_Map_First_Pass.md`, `Section_8_Normalization_Status_Compass.md`, `Section_8_Next_Audit_Targets.md` | `mixed_keep`, `section_style_reclassify`, `mismatch_clear`, `watch_keep` 같은 상태어 |
| `structure_snapshot` | `Section_8_Structure_Label_Map_First_Pass.md` | `Section_8_Normalization_Status_Compass.md` | 핵심 세력의 현재 구조 라벨과 pressure 상태 |
| `mismatch_snapshot` | `Section_8_Spine_Mismatch_Queue.md` | `Section_8_Normalization_Status_Compass.md`, `Section_8_Next_Audit_Targets.md` | canonical mismatch 범주명과 active/clear 상태 |
| `root_mainline` | `Section_8_Root_Corruption_First_Pass_A.md`, `Section_8_Root_Subtree_Sampling_Queue.md` | `Section_8_Normalization_Status_Compass.md`, `Next_Sequential_Workstream.md`, `Audit_Queue.md` | `canonical / quarantine / legacy`, subtree sampling readiness |
| `place_network_handoff` | `Section_8_Place_Network_Handoff_Map.md` | `Section_8_Normalization_Status_Compass.md`, related sidecars/registers | 어느 후보가 어느 sidecar/register로 넘어갔는지 |
| `section8_to_15_carryover` | `Section_8_15_Spine_Compatibility_Audit.md`, `Section_15_State_Vocabulary_Guard.md`, `Section_15_Stable_Candidate_8_Anchor_Index.md` | `Section_8_to_15_Notable_Anchor_Bridge.md`, `Next_Sequential_Workstream.md`, related package freeze docs | stable triad / support_hold / deferred_expansion_hold와 `Section 8` carryover 상태 |
| `closure_sync_watch` | `Section_8_15_Closure_Sync_Carryover_Watch.md` | `Section_15_Named_Notables_Status_Compass.md`, `Section_15_Five_Continent_Closure_Table.md`, `Audit_Queue.md` | 현재 본선이 `closure sync / carryover watch`인지, 이미 닫힌 hold cluster를 다시 active처럼 쓰지 않는지 |
| `profile_format_carryover` | `Section_15_Profile_Template.md`, `Section_15_Profile_Draft_Index.md` | `Section_15_Operational_Lines_Track.md`, `Section_15_Operational_Display_Canon_Candidates.md`, `Section_15_Intake_Structure.md`, `Section_15_Folder_Revision_Gate.md` | operational profile layer가 `3-1. Policy Guard` 형식을 유지한 채 carryover rule을 공유하는지 |
| `lower_card_authority` | `Section_15_Profile_Template.md`, `Section_15_Named_Notables_Register.md` | `Section_15_Named_Notables_Coverage_Matrix.md`, `Section_8_to_15_Notable_Anchor_Bridge.md`, `Section_8_15_Spine_Compatibility_Audit.md`, `Audit_Queue.md`, `Continuous_Workstream.md` | 상위 summary/bridge/watch 문서가 named notable 카드와 operational profile 카드의 권한선을 섞지 않는지 |
| `subline_profile_authority` | `Section_15_Profile_Draft_Index.md`, `Section_15_Subline_Register.md` | `Section_15_Operational_Lines_Track.md`, `Section_15_Operational_Display_Canon_Candidates.md`, `Section_15_Folder_Draft_Routing_Plan.md`, `Section_15_Named_Notables_Coverage_Matrix.md`, `Section_8_15_Closure_Sync_Carryover_Watch.md` | `Section_15_Subline_Profile_*`의 `3-1. Policy Guard`가 exact wording source로 유지되고, representative subline pair closure가 상위 문서에서 승인 논리로 역수입되지 않는지 |
| `missing_layer_policy` | `Five_Continent_Missing_Layer_Policy_Lock.md` | `Continents_Framework.md`, `Continental_Adequacy_Map.md`, `Five_Continent_Synthesis.md`, related core faction layers | 에테르 변방 부족층, 크림슨 국가형 가문층, 프로스트 정주 귀족층, 해양 토착 공동체층, 오벨리스크 비정통 엘리트를 어디까지 thin/support로 허용하는지 |
| `execution_priority` | `Next_Sequential_Workstream.md` | `Audit_Queue.md`, `Section_8_Next_Audit_Targets.md` | 지금 메인 본선이 실제로 어디에 있는지 |

## Drift Triggers

아래 경우에는 이 register를 기준으로 sync check를 다시 돈다.

1. 구조 라벨이 `mixed_keep -> section_style_reclassify`처럼 변할 때
2. mismatch 결과가 `mismatch_keep -> mismatch_clear`로 바뀔 때
3. `place pressure strong` 후보가 새 sidecar/register로 handoff될 때
4. `root_corruption` 관련 새 샘플링 결과가 들어올 때
5. stable candidate의 `support_hold / deferred_expansion_hold / stable_15_workset` 상태가 바뀌거나 legacy 상태어가 guard 밖 live 문서에 다시 나타날 때
6. 메인 본선이 `closure sync / carryover watch` 밖 다른 축으로 넘어갈 때
7. 결손층 메모가 policy lock 바깥의 새 설정 발명처럼 다시 적힐 때
8. operational profile guard 문장이 named notable 승인 논리로 역수입될 때
9. `Section_15_Subline_Profile_*` 카드의 `3-1. Policy Guard`가 상위 summary / bridge / watch 문서에서 재정의되거나,
   representative subline pair closure가 named notable 승인 논리로 역수입될 때

## Conductor Checklist

변경 후 최소 확인 문서:

1. `Section_8_Status_Vocabulary_Guard.md`
2. `Section_8_Structure_Label_Map_First_Pass.md`
3. `Section_8_Normalization_Status_Compass.md`
4. `Section_8_Next_Audit_Targets.md`
5. `Next_Sequential_Workstream.md`
6. `Audit_Queue.md`
7. `Section_8_15_Spine_Compatibility_Audit.md`
8. `Section_15_State_Vocabulary_Guard.md`
9. `Section_15_Stable_Candidate_8_Anchor_Index.md`
10. `Section_8_15_Closure_Sync_Carryover_Watch.md`
11. `Five_Continent_Missing_Layer_Policy_Lock.md`
12. `Section_15_Profile_Draft_Index.md`
13. `Section_15_Operational_Lines_Track.md`
14. `Section_15_Named_Notables_Register.md`

## Conductor Decision

다음부터 `Section 8` 오케스트라 업데이트는
이 register를 기준으로
`판정`, `요약`, `진행표`, `handoff`가 같이 움직였는지 확인한다.

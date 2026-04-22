# Section 8 Next Audit Targets

이 문서는 `1~5 대륙 프레임`과 `가문 / 부족 / 길드 충분성` 기준을 닫은 뒤,
`8. 세력 아카이브`에서 무엇이 닫혔고 무엇이 reference backlog인지 정리하는 큐다.

## Conductor Verdict

현재 메인 본선은
이미 닫힌 결과를 유지하는
`5대륙 closure sync / Section 8 -> 15 watch-reference` 단계다.

`결손층 5개`의 thin/support 판단과 overread 금지선은
항상 `audit/Five_Continent_Missing_Layer_Master_Lock.md`를 단일 entry로 읽는다.

이 문서에 남은 `다음 8번 감사` 서술은
현재 workstream이 아니라 closed/reference backlog로 읽는다.

우선순위:

1. `크림슨 / 부족-씨족 중심 spine`과 `state_house thin` 검증
2. `에테르 / 정령연합`의 tribe_clan 특수축 검증
3. `프로스트 / 클랜 정치 + 생존 경제` spine 검증
4. `해양 / 항만 권력 + 해상 경제 + 가문 정치` spine 검증
5. `오벨리스크 / frontier_survival + nontraditional elite` 정책 검증
6. `범대륙 후기 확장`

## Priority Table

| Priority | Section 8 Target | Cycle Status | Why Now | Expected Output |
|---|---|---|---|---|
| 1 | `크림슨 / 용의 후예 / 붉은 사막 부족 연합` | `closed_round1` | `tribe_clan + guild_market`가 크림슨 spine의 핵심이라, 여기서 `state_house thin`의 실제 범위를 먼저 봐야 했다. | 씨족형 지배층과 국가형 가문층의 경계를 분리한 감사표. |
| 2 | `에테르 / 정령연합 / 루미라` | `closed_round1` | 에테르는 기본적으로 `state_house + guild_market` 대륙이지만, 정령연합만 `tribe_clan` 특수축이 강했다. | 에테르 전체 기준과 정령연합 특수 규칙을 분리한 감사표. |
| 3 | `프로스트 / 프로스트본 연합` | `closed_round1` | 프로스트는 `tribe_clan + guild_market` 구조가 안정적이라, 도시 귀족/정주 상층이 얼마나 얇은지 잠그는 샘플이었다. | 클랜 상층, 생존 경제, 정주 귀족 결손을 함께 적은 감사표. |
| 4 | `해양 / 황금 함대 / 해적 연합 / 바다의 교단` | `closed_round1` | 해양은 `state_house + guild_market`가 강하나 토착 공동체층은 약해서, 항만 권력 구조와 부족층 결손을 함께 보는 샘플이었다. | 항만 권력 구조와 토착 공동체 결손을 함께 적은 감사표. |
| 5 | `오벨리스크 / 망자의 왕국 / 잊힌 자들의 연합 / 봉인 수호단` | `closed_round1` | 오벨리스크는 `frontier_survival + guild_market` 본체와 `nontraditional elite thin-support`를 어떻게 분리할지 정책을 고정하는 샘플이었다. | 비정통 엘리트 정책 고정과 부족층 결손 유지 여부 판정. |
| 6 | `범대륙 후기 확장` | `deferred_expansion_track` | 중요하지만 후기 증설 구역이라 후순위다. | display canon/deferred expansion 추가 검토. |

## Closed Target Snapshot

`크림슨 / 용의 후예 / 붉은 사막 부족 연합` 1차 spine sample은 닫힌 것으로 본다.

`에테르 / 정령연합 / 루미라` 1차 spine sample도 닫힌 것으로 본다.

`프로스트 / 프로스트본 연합` 1차 spine sample도 닫힌 것으로 본다.

`해양 / 황금 함대 / 해적 연합 / 바다의 교단` 1차 spine sample도 닫힌 것으로 본다.

`오벨리스크 / 망자의 왕국 / 잊힌 자들의 연합 / 봉인 수호단` 1차 spine sample도 닫힌 것으로 본다.

현재 실제 본선은 `5대륙 closure sync / Section 8 -> 15 watch-reference`다.

이전 신규 감사 target은 `Section 8 루트 구조 / 표준 spine / 레거시 분리`였고,
현재는 watch backlog로 유지한다.

이유:

- `1~5 대륙` 샘플이 모두 닫혀, 실제 루트 구조를 이 기준으로 읽는 근거가 마련됐다.
- 개별 대륙 추가 배치가 아니라 `Section 8 루트 전체`의 중복, spine mismatch, legacy 분리 watch가 남아 있다.
- 이 단계는 현재 신규 실행선이 아니라 closure sync / watch-reference의 reference backlog다.

## Reference Action Map

현재 유지 문서:

- `Section_8_Normalization_Status_Compass.md`
- `Section_8_Mainline_Sync_Register.md`
- `Section_8_Root_Corruption_First_Pass_A.md`
- `Section_8_Root_Subtree_Sampling_Queue.md`
- `Section_8_Place_Network_Handoff_Map.md`
- `Section_8_to_15_Notable_Anchor_Bridge.md`
- `Section_15_Stable_Candidate_8_Anchor_Index.md`
- `Section_8_15_Closure_Sync_Carryover_Watch.md`
- `Five_Continent_Missing_Layer_Master_Lock.md`

reference-only 참고 문서:

- `Section_8_Root_Findings.md`
- `Section_8_Root_Label_Map.md`
- `Section_8_Structure_Labeling_Queue.md`
- `Section_8_Structure_Label_Map_First_Pass.md`
- `Section_8_Spine_Mismatch_Queue.md`
- `Section_8_Mixed_Exception_Review_Queue.md`
- `Section_8_Mixed_Exception_First_Pass_A.md`
- `Section_8_Mixed_Exception_First_Pass_B.md`
- `Section_8_Mixed_Exception_First_Pass_C.md`
- `Section_8_Spine_Mismatch_First_Pass_A.md`
- `Section_8_Spine_Mismatch_First_Pass_B.md`
- `Section_8_Root_Corruption_First_Pass_A.md`
- `Section_8_Root_Subtree_Sampling_Queue.md`
- `Section_8_Place_Network_P2_Queue.md`
- `Section_8_Place_Network_Handoff_Map.md`
- `Section_8_Status_Vocabulary_Guard.md`

reference backlog 상태:

- `Section 8` 루트 전체는 닫힌 5대륙 spine 기준으로 읽되, 현재는 신규 이동/병합/원본 수정 없이 watch reference로만 유지한다.
- 중복 루트, 레거시 경로, spine mismatch, mixed_keep exception, P1 mismatch round는 각 first-pass 문서에서 닫힌 상태로 본다.
- `P0 root_corruption`은 `Section_8_Root_Corruption_First_Pass_A.md`와 `Section_8_Root_Subtree_Sampling_Queue.md` 기준으로만 유지한다.
- `P2 section_style_forced_on_place_network`는 `Section_8_Place_Network_P2_Queue.md`와 `Section_8_Place_Network_Handoff_Map.md` 기준 handoff drift watch로만 유지한다.
- `Section_8_Status_Vocabulary_Guard.md`는 `mixed_keep`, `section_style_reclassify`, `mismatch_clear`, `watch_keep`, `handoff_applied` 상태어를 같은 의미로 유지하는 기준표로 사용한다.
- `Section_8_Mainline_Sync_Register.md`는 구조 라벨, mismatch, root, handoff, 진행표가 같은 현재 시점을 가리키는지 확인하는 장부로 사용한다.
- `Five_Continent_Missing_Layer_Master_Lock.md`는 `결손층 5개`의 thin/support, evidence, firewall 순서를 현재 본선 바깥 component shorthand로 재해석하지 않게 막는 단일 entry authority로 사용한다.
- representative `Port Authority / Black Auction / Gravewell / Counterfeit Workshop` pair는 닫힌 subline 교차감사 샘플로 보고, 새 drift가 생길 때만 해당 pair를 국소 재대조한다.
- 현재 시점의 메인 유지선은 `Section_8_15_Closure_Sync_Carryover_Watch.md` 기준 closure sync / watch-reference다.

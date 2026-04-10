# FS Canon Change Log

이 문서는 상태 라벨, 라우팅, 판정이 실제로 바뀐 지점을
짧게 남기는 변경 기록 장부다.

목적:

- `왜 이 항목이 바뀌었는가`를 나중에도 복원할 수 있게 한다.
- `hold -> verify_before_15 -> named_notable_candidate` 같은 이동을 잃지 않는다.
- Named Notables, Operational Lines, Place Register 사이의 변화 흔적을 남긴다.

## Rule

- 사소한 문장 수정은 남기지 않는다.
- 상태 라벨, 라우팅, 판정, 표면명 층 변화만 남긴다.
- 한 줄에 `날짜 / 대상 / 변화 / 이유 / 연결 장부`만 적는다.

## Change Log Snapshot

| Date | Target | Change | Why | Linked Registers |
|---|---|---|---|---|
| `2026-04-08` | `울프가르 드래곤포지 / 에리온 드라코비스` | `named_notable_candidate` 유지 + `grade_caution` 명시 | A급 / 영웅록 / 세력 핵심표 신호가 있어 안정 후보이되 과확정은 금지 | `FS_Decision_Ruling_Register`, `Section_8_Crimson_Notable_Anchor_Audit` |
| `2026-04-08` | `벨라나 / 아리안` | 안정 15 시험군에서 `verify_before_15`로 하향 | SS/S급 현자회 핵심 인물 신호가 강하다 | `FS_State_Label_Register`, `Section_14_15_Crimson_Boundary_Batch_02` |
| `2026-04-08` | `프로스트 unnamed slots 6종` | `slot_only -> slot_with_display_candidate` | 장소-기관 기능과 표면명 후보가 먼저 안정됐다 | `FS_Place_Function_Register`, `FS_Slot_Maturation_Register`, `Section_15_Frost_Core_Register_Link` |
| `2026-04-08` | `프로스트 명사층 판정` | `stable candidate보다 role slot 우선` 고정 | 프로스트는 인물보다 성소/묘역/공방/예언 슬롯이 먼저 강하다 | `FS_Decision_Ruling_Register`, `Section_8_Frost_Notable_Anchor_Audit` |
| `2026-04-08` | `Operational Lines 표면명 정책` | 작업용 구조명과 `display_canon_candidate`를 분리 | 현대적/직역감 있는 실무 라벨을 바로 정본명으로 올리지 않기 위해 | `FS_Cross_Chronicle_Firewall`, `Section_15_Operational_Display_Canon_Candidates` |
| `2026-04-08` | `Story-to-Lore cross-check` | 독립 `handoff gate` 문서 추가 | Story Engine에서 나온 새 설정 요소를 Lore Engine으로 되돌리는 절차를 고정하기 위해 | `FS_Story_to_Lore_Handoff_Gate`, `FS_Revision_Gate_Checklist`, `FS_Story_Engine`, `FS_Lore_Engine` |
| `2026-04-08` | `FS-HANDOFF-SEED-001` | handoff seed case를 `item_hold`로 시험 적용 | `FS-AQ-004`의 전설 무구 압력을 정본 아이템명 없이 Asset/Foreshadow 장부로만 보냈다 | `FS_Story_to_Lore_Handoff_Seed_Cases`, `FS_Asset_Secret_Register`, `FS_Foreshadow_Payoff_Register`, `FS_Decision_Ruling_Register` |
| `2026-04-08` | `Story-to-Lore live queue` | live handoff queue 문서 추가 | 실제 원고 입력과 seed case를 섞지 않기 위해 queue를 비워 둔 상태로 분리했다 | `FS_Story_to_Lore_Live_Handoff_Queue`, `FS_Story_to_Lore_Handoff_Gate`, `OPEN_INDEX` |
| `2026-04-08` | `벨라나 스톰브링어` | `verify_before_15` 근거를 Decision Ruling에 직접 연결 | SS급 현자 회의 지도자 신호가 강해 명사형 가치보다 14 검증이 먼저다 | `FS_Decision_Ruling_Register`, `Section_14_15_Crimson_Boundary_Batch_02`, `Section_15_Named_Notables_Register` |
| `2026-04-08` | `드락사르 블레이즈포지` | `verify_before_15` 근거를 Decision Ruling에 직접 연결 | 공방 명사 가치가 커도 A급 공병대장, 실험 의뢰 축이 강하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Crimson_Boundary_Batch_02`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-08` | `칼리스트` | `verify_before_15` 근거를 Decision Ruling에 직접 연결 | A+ 탑주, 대예언자, Act 신호가 예언자형 명사 가치보다 먼저 잡힌다 | `FS_Decision_Ruling_Register`, `Section_14_15_Ether_Boundary_Evidence`, `Section_15_Named_Notables_Register` |
| `2026-04-08` | `카사르 더 시어` | `hold_for_dual_review`로 별도 보류 고정 | S급 용의 예언자, 최고 조언자, 시험의 탑, 수호파 핵심, 전설 영웅록 신호가 동시에 강하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Crimson_Boundary_Batch_02`, `Section_15_Named_Notables_Register` |
| `2026-04-08` | `세리오스 벤타리스` | `verify_before_15 -> keep_14_likely` | 검토한 import 범위에서 14 현존 영웅 파일과 hero/s_rank 태그가 직접 확인된다 | `FS_Decision_Ruling_Register`, `Section_14_15_Ether_Boundary_Evidence`, `Section_15_Named_Notables_Register` |
| `2026-04-08` | `Ravenfell / Corvus name drift` | `verify_before_15 -> name_drift / merge_ban` | `마르쿠스 레이븐펠`, `맥스웰 레이븐펠`, `마르쿠스 코르부스`가 서로 다른 문서 신호로 엇갈린다 | `FS_Decision_Ruling_Register`, `Section_14_15_Ether_Boundary_Batch_02`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `Ravenfell / Corvus anchor split` | `name_drift -> maxwell_anchor / corvus_separate_entity` refinement | phase3 마법협회 세력 문서와 레이븐펠 학파 기준 흑색 탑 주앵커는 `맥스웰 레이븐펠`이고, `마르쿠스 레이븐펠`은 로컬/구형 표기, `마르쿠스 코르부스`는 직접 14 영웅 파일이다 | `FS_Decision_Ruling_Register`, `Section_15_Named_Notables_Name_Collision_Register`, `Section_14_15_Ether_Boundary_Evidence` |
| `2026-04-09` | `이사도르 템페스트 / 이사도르 솔레아 split` | `name-adjacent risk -> split hold refinement` | `이사도르 템페스트`는 phase3의 청색 탑/템페스트 학파 탑주 축이고 `이사도르 솔레아`는 phase2의 직접 14 영웅 파일과 솔레아 가문 치유 장로 축이라 병합하면 안 된다 | `FS_Decision_Ruling_Register`, `Section_15_Named_Notables_Name_Collision_Register`, `Section_14_15_Boundary_Verification_Queue` |
| `2026-04-08` | `해양 경계 후보군` | 새 15 확정자 없음 + `verify_before_15` cluster 유지 | 해양은 이름 있는 후보가 많지만 A급/SS급/히어로급/전설 축이 강해 보조 기능축으로만 보존한다 | `FS_Decision_Ruling_Register`, `Section_14_15_Oceanic_Boundary_Batch_02`, `Section_15_Oceanic_Search_Synthesis` |
| `2026-04-08` | `오벨리스크 경계 후보군 / 아이기스` | 확정 15 보류 + 장소-기관 슬롯 우선 + Aegis 충돌 분리 | 기록/봉인/망각 명사층은 강하지만 전설/히어로급/조직 핵심/아이템명 충돌이 크다 | `FS_Decision_Ruling_Register`, `Section_14_15_Obelisk_Boundary_Batch_02`, `Section_15_Obelisk_Search_Synthesis` |
| `2026-04-08` | `크리스토퍼 델마르 / 검은 동전` | `new_boundary_candidate -> verify_before_15 / role_slot_merge_ban` | `Christopher Delmar, the Black Coin`은 장물 금융/암시장 자금 담당자로 확인되지만 `대경매장 주인`, `항해사 길드장`의 이름은 아니다 | `FS_Decision_Ruling_Register`, `Section_15_Oceanic_Search_Findings_Batch_02`, `Section_15_Oceanic_Search_Synthesis` |
| `2026-04-08` | `메라 라일윈드 / 메라 실피드` | `verify_before_15 -> name_drift / merge_ban` | 외교 사절단의 `메라 라일윈드`와 14 현존 영웅 파일의 `메라 실피드`가 서로 다른 앵커로 확인되어 병합 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Ether_Boundary_Batch_02`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-08` | `Rafferty / Raphael Arcadia drift` | `verify_before_15 -> name_drift / merge_ban` | `래퍼티 아르카디아`는 성국 핵심 인물표의 A급/Act 도서관장이고 `라파엘 아르카디아`는 아스트라르 도시 문서의 도서관장 슬롯으로 확인되어 병합 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_04`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-08` | `Sylas / 실라스 collision` | `verify_before_15 / keep_14_likely -> anchor_split / merge_ban` | `실라스 블랙쏜`은 성국 옵시디안 축, `실라스 나이트쉐이드`는 정령연합 그늘까마귀단 축이라 세력 앵커가 다르다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_06`, `Section_15_Ether_Search_Findings_Batch_09`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-08` | `Valerius / 발레리우스 collision` | `local_named_slot_needs_identity_check -> merge_ban backfill` | 성국 14 현존 영웅 `레오니스 발레리우스`와 루멘 성채의 `Valerius the Lightbringer`가 서로 다른 앵커로 확인되어 이름 기반 병합을 금지해야 한다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_05`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-08` | `Drake Ruga / Rawson drift` | `name_drift -> keep_14_anchor / rawson_merge_hold` | 14 현존 영웅 파일명은 `드레이크 루가 (Drake Ruga)`로 직접 확인되고 `Drake Rawson`은 포트 넥서스 관련 문서의 링크 표기 흔들림으로 보여 별도 인물화하면 안 된다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_08`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-08` | `셀레나 아르시엔 / 셀레나 와일드웨이브` | `verify_before_15 / keep_14 -> name_drift / merge_ban` | 왕국연합 14 현존 영웅 `셀레나 아르시엔`과 자유도시연합 포트 넥서스 정보원 `셀레나 와일드웨이브`는 세력/역할 앵커가 달라 병합 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_08`, `Section_15_Ether_Search_Synthesis`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-09` | `Sylvia / 실비아 collision` | `name_collision -> merge_ban backfill` | 키르케/에테르/해양/오벨리스크의 `Sylvia` 계열이 서로 다른 앵커로 확인되어 이름 기반 병합을 금지해야 한다 | `FS_Decision_Ruling_Register`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-09` | `Wolfgar / 울프가르 collision` | `name_collision_watch -> continent_anchor_split / merge_ban` | 크림슨 `울프가르 드래곤포지`와 프로스트 `Wulfgard/Wulfgar` 이름군은 대륙/출처 앵커가 달라 병합 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-09` | `Erion / 에리온 collision` | `name_collision_watch -> continent_anchor_split / merge_ban` | 크림슨 `에리온 드라코비스`와 에테르 `에리온 베르날리스`는 세력/기능 앵커가 달라 병합 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Named_Notables_Name_Collision_Register` |
| `2026-04-09` | `Aegis / 아이기스 person-item-concept split` | `aegis_collision_lock -> person_item_concept_split refinement` | `Aegis`가 인물명, 성씨/가문명, 방패/결계/유물명으로 넓게 반복되어 기존 대표군 판정을 item/name collision crosswalk와 직접 연결했다 | `FS_Decision_Ruling_Register`, `Section_15_Named_Notables_Name_Collision_Register`, `Section_15_Obelisk_Search_Synthesis`, `working/crosswalks/Item_Name_Collision_Register` |
| `2026-04-09` | `아리안 블레이즈하트` | `verify_before_15 direct ruling backfill` | 현자 회의 / 붉은 사막 부족 명사 가치가 있으나 S급 대사제와 정신적 지도자 신호가 강해 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Crimson_Boundary_Batch_02`, `Section_15_Crimson_Wise_Council_Evidence` |
| `2026-04-09` | `대런 크레센트` | `verify_before_15 direct ruling backfill` | 마법 서고단 관장과 협회 행정 실권자 신호가 강하지만 A+ 부탑주와 Act 1-3 축이 있어 15 확정 전 14 검증이 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_01`, `Section_15_Ether_Search_Synthesis` |
| `2026-04-09` | `시그리드 프로스트하트` | `verify_before_15 -> siege_artificer_hold backfill` | 프로스트 퍼마프로스트 공성단/아이스포지 병기소의 공성단장과 공학/공성 병기 제작 축이 강해 장소-기관 슬롯 우선 판정이 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Frost_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `이소벨 골드리프` | `verify_before_15 -> finance_power_hold backfill` | 해양 SS급 재무 실권자이자 볼트 오브 아우룸/포탄 구매 허가권 축이 강해 15 확정 전 14 검증이 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Oceanic_Boundary_Batch_02`, `Section_15_Oceanic_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `카론` | `verify_before_15 -> soul_guide_hold backfill` | 망자의 왕국 전설 마도 영웅록과 잊힌 자들의 전술 문서에 반복되어 영혼 인도자 명사 가치와 전설/전술 축이 겹친다 | `FS_Decision_Ruling_Register`, `Section_14_15_Obelisk_Boundary_Batch_02`, `Section_15_Obelisk_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `엘라라 문힘` | `verify_before_15 direct ruling backfill` | 기록/노래 전승 명사 가치가 크지만 A급 영웅표, Act, 전설 영웅록 신호가 함께 있어 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_09`, `Section_15_Named_Notables_Register` |
| `2026-04-09` | `대사제 요한` | `verify_before_15 -> holy_barrier_hold backfill` | 루멘 성채 총괄과 결계 공명 신호가 강하지만 성채 핵심 지휘축이라 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_05`, `Section_15_Ether_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `에드가 룬워커` | `verify_before_15 direct ruling backfill` | 룬 제작과 고대 탐구의 명사 가치가 크지만 A급과 Act 1/3 신호가 함께 있어 15 확정 전 14 검증이 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_02`, `Section_15_Ether_Search_Synthesis` |
| `2026-04-09` | `엘드린 문브링어` | `verify_before_15 -> white_tower_barrier_hold backfill` | 백색 탑주, S급, Act 1~3, 비전 결계단과 협회 결계 인프라 직할 신호가 강해 15 확정 전 14 검증이 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Ether_Boundary_Batch_02`, `Section_14_15_Ether_Boundary_Evidence`, `Section_15_Ether_Search_Synthesis` |
| `2026-04-09` | `네리사 블러드위버` | `verify_before_15 -> abyss_blood_taboo_hold backfill` | 적색 탑주, S급, Act 1/3, 심연 연구단 단장과 금기 연구 중심축 신호가 강해 15 확정 전 14 검증이 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Ether_Boundary_Batch_02`, `Section_14_15_Ether_Boundary_Evidence`, `Section_15_Ether_Search_Synthesis` |
| `2026-04-09` | `다미엔 이클립스` | `verify_before_15 -> shadow_intelligence_hold backfill` | 은색 탑주, S급, Act 1~5, 어둠술사단 수장과 첩보/환영/암살 중심축 신호가 강해 15 확정 전 14 검증이 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Ether_Boundary_Batch_02`, `Section_14_15_Ether_Boundary_Evidence`, `Section_15_Ether_Search_Synthesis` |
| `2026-04-09` | `레온 벨가르드` | `verify_before_15 -> mercenary_guild_hold backfill` | 머시너리 게이트 조합장과 용병 조합 지배자 신호가 강하지만 세력 핵심축 가능성이 커 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_08`, `Section_15_Ether_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `리아나 실버레이크` | `verify_before_15 -> banking_power_hold backfill` | 아덴브루크 재무/은행권 핵심 인물이지만 왕국연합 핵심표와 Act 신호가 겹쳐 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_07`, `Section_15_Ether_Search_Synthesis` |
| `2026-04-09` | `드라이덴 썬더루트` | `verify_before_15 -> great_druid_hold backfill` | 정령연합 Top 3 대드루이드와 생명의 의회 의장 신호가 강해 독립 15 후보보다 14 핵심축 검증이 우선이다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Search_Findings_Batch_09`, `Section_15_Ether_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-10` | `메라 라일윈드` | `verify_before_15 / name_drift -> spirit_envoy_hold / name_collision_watch` | 정령연합 외교 사절단과 희귀 재료 교역 조건 명사 가치는 유지하되 `메라 실피드`와의 드리프트를 먼저 잠그는 편이 안전하다고 재판정했다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Spirit_Union_Hold_Continuation`, `Section_15_Named_Notables_Register`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-10` | `실라스 나이트쉐이드` | `verify_before_15 / likely_keep_14 -> shadow_crow_hold / name_collision_watch` | 정령연합 `그늘까마귀단 / 잠든 정령의 숲` 축을 성국 `실라스 블랙쏜`과 분리해 보존하고, 15 승격보다 세력 앵커 분리를 우선한다 | `FS_Decision_Ruling_Register`, `Section_15_Ether_Spirit_Union_Hold_Continuation`, `Section_15_Named_Notables_Register`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `바리온` | `verify_before_15 direct ruling backfill` | 금서 해석과 룬 기록의 명사 가치는 크지만 봉인 수호단/전설 영웅록 신호가 강해 15 확정 전 직접 보류 판정이 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Obelisk_Boundary_Batch_02`, `Section_15_Obelisk_Search_Synthesis` |
| `2026-04-09` | `베스 스크롤` | `verify_before_15 direct ruling backfill` | 기록자/서고단 명사 가치는 크지만 봉인 수호단과 B급 인물표 신호가 있어 15 확정 전 직접 보류 판정이 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Obelisk_Boundary_Batch_02`, `Section_15_Obelisk_Search_Synthesis` |
| `2026-04-09` | `이안 옵저버` | `verify_before_15 direct ruling backfill` | 관측/경보 명사 가치는 크지만 오벨리스크 관측대와 B급 인물표 신호가 있어 15 확정 전 직접 보류 판정이 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Obelisk_Boundary_Batch_02`, `Section_15_Obelisk_Search_Synthesis` |
| `2026-04-09` | `카트린 라베로스` | `verify_before_15 -> archive_cipher_hold backfill` | 잊힌 서고 학자와 고대 암호 해독 신호가 강하지만 히어로급 표기가 겹쳐 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Obelisk_Boundary_Batch_02`, `Section_15_Obelisk_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `레보니아 셰이드` | `verify_before_15 -> language_memory_hold backfill` | 언어학자와 거짓 기록 조작 축이 강하지만 히어로급/조작 핵심 신호가 겹쳐 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_14_15_Obelisk_Boundary_Batch_02`, `Section_15_Obelisk_Search_Synthesis`, `Section_15_Named_Notables_Status_Compass` |
| `2026-04-09` | `세르반 알테르만` | `verify_before_15 direct ruling backfill` | 영혼 보관과 정보 추출의 명사 가치는 크지만 망자의 왕국 / 흑막 연구 조직 신호가 함께 있어 15 확정 전 직접 보류 판정이 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Obelisk_Search_Synthesis`, `Section_15_Named_Notables_Register` |
| `2026-04-09` | `우로스 디 모르간` | `verify_before_15 -> archive_infiltration_hold backfill` | 지식 강탈과 도서관 침투 기능은 선명하지만 `망각의 조율자` 핵심축 가능성이 커 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Obelisk_Search_Synthesis`, `Section_15_Named_Notables_Register`, `working/imports/.../망각의 조율자 개요 및 강령.md` |
| `2026-04-09` | `레티시아 모르투스` | `verify_before_15 -> necromantic_bestiary_hold backfill` | 사령 괴수 도감 제작이라는 15 가치가 크지만 `죽음의 행진단` 핵심축 신호가 강해 14 확인 전 15 확정 금지가 필요하다 | `FS_Decision_Ruling_Register`, `Section_15_Obelisk_Search_Synthesis`, `Section_15_Named_Notables_Register`, `working/imports/.../죽음의 행진단 개요 및 강령.md` |

## Usage Note

이 장부는 연표가 아니라
`판정 이동 이력` 장부다.

따라서 이후에도
대상마다 모든 변화를 다 적기보다,
나중에 되짚어야 할 변화만 남긴다.

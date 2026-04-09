# Race Species Term Crosswalk

이 문서는 종족/혈통/상태/몬스터 용어를
같은 층위로 오독하지 않기 위한 교차표다.

현재 단계에서는 `정본명 선언`이 아니라
`normalized reading`과 `bucket`을 고정한다.

| Source Term | Normalized Reading | Bucket | Continent/Faction Anchor | Source Path | Keep Separate From | Current Confidence | Note |
|---|---|---|---|---|---|---|---|
| `하이엘프` | 장생종 엘프 계열 | `species` | `에테르 / 루미라` | `audit/Section_15_Named_Notable_Eldara.md` | `하프엘프`, `정령화` | `medium` | 개별 사례는 강하지만 대륙 일반화 금지 |
| `드워프 장인` | 광산/장인종 드워프 계열 | `species` | `프로스트 / 푸른 폭풍 요새` | `audit/FS_Place_Function_Register.md` | `장인 직책`, `공방 소속` | `medium` | 종족 신호와 직업 신호를 분리 |
| `수인 부족` | 수인/야수인계 people | `species` | `에테르 / 정령연합` | `working/imports/phase3_section8_ether_spirit_union/정령연합 (Spirit Union).md` | `정령연합`, `부족장 직위` | `high` | 공동체/자치권/부족 구조가 직접 보임 |
| `늑대수인` | 수인 하위 people tag | `species` | `에테르 / 그린스톰 부족` | `working/imports/phase3_section8_ether_spirit_union/3. 부족 (Tribes)/4. 그린스톰 부족 (Greenstorm Tribe).md` | `늑대 계열 몬스터` | `high` | 개인 개체가 아니라 공동체 내부 people tag |
| `하프엘프` | 엘프-인간 혼혈 | `bloodline` | `에테르 / 정령연합` | `working/imports/phase3_section8_ether_spirit_union/정령연합 (Spirit Union).md` | `엘프 종족`, `장생종 전체` | `high` | 독립 종족 승격 금지 |
| `Dragonborn` | 용+인간 혼혈 특수 존재 | `bloodline` | `크림슨 / 용의 후예` | `working/imports/phase3_section8_crimson_dragon_descendants/용의 후예.md` | `용계 전체`, `용의 후예 polity` | `high` | 혼혈/유전 특수 계열로 읽음 |
| `용의 피 / 용혈` | 드래곤 혈통 계열 | `bloodline` | `크림슨 / 용의 후예` | `working/imports/phase3_section8_crimson_dragon_descendants/용의 후예.md` | `드래곤 종족`, `용인 국가` | `high` | 가문/전사단/혈통 질서에 가깝다 |
| `언데드` | 죽음 이후 변질 상태 | `state` | `오벨리스크 / 망자의 왕국` | `working/imports/phase5_section8_obelisk_kingdom_of_dead/망자의 왕국 (Kingdom of the Dead).md` | `망자의 왕국 polity`, `뱀파이어 계층` | `high` | 사회 구조가 있어도 기본값은 상태 |
| `정령화` | 정령 인접 변질/승화 상태 | `state` | `오벨리스크 / 봉인 수호단` | `working/imports/phase5_section8_obelisk_seal_wardens/14. 생활양식/14-0. 고유 식문화와 생활상 (Food & Lifestyle).md` | `정령 people`, `정령 entity` | `medium` | acquired state로 읽음 |
| `Merfolk` | 수중/해양계 people signal | `species` | `해양 / 에테르 해안` | `working/drafts/Oceanic_Tribe_Gap_Findings.md` | `해양 교단`, `바다의 정령` | `low` | 주권 문명권 증거는 아직 얇음 |
| `인어 공주` | 수중/해양계 people representative signal | `species` | `에테르 / 세레니아` | `working/imports/phase3_section8_ether_sainthaven/1. 주요 장소 (Locations)/요새/6. 세레니아 (Serenia).md` | `호수의 요정`, `물의 정령` | `medium` | 지역 대표성은 보이지만 전역 문명권은 아님 |
| `Siren Harpy` | 조익계 monster signal | `monster` | `해양 / 해적 연합 이벤트층` | `working/imports/phase4_section8_oceanic_pirate_confederacy/11. 예술 및 건축 (Art & Architecture)/0. 해적 연합 예술 및 건축.md` | `조익/익인 people`, `하피족` | `low` | 현재는 세트피스/몬스터 우세 |
| `Lamia / Naga` | 미확정 사행계 후보 | `unclear` | `global pending` | `no stable import anchor yet` | `monster`, `species`, `state` | `low` | 사회 구조 증거 전까지 보류 |
| `나가족(반인반사)` | 사행계 단일 개체 signal | `unclear` | `에테르 / 맹독의 숨결` | `working/imports/phase3_section8_ether_spirit_union/9. 내부 암약 조직 (Clandestine Organizations)/3. 맹독의 숨결 (Breath of Venom)/1. 맹독의 숨결 개요 및 강령.md` | `라미아 사회`, `monsterized serpent` | `low` | 개인 1건만 있어 사회 구조 근거로 쓰지 않음 |
| `요정` | 소형/요정계 ally/community mixed signal | `unclear` | `에테르 / 정령연합` | `working/imports/phase3_section8_ether_spirit_union/14. 생활양식/14-0. 고유 식문화와 생활상 (Food & Lifestyle).md` | `정령`, `하급 정령`, `포획 자원` | `medium` | Ether 내부 공동체 신호는 강하지만 전역 standalone dossier는 보류 |
| `거인족` | 거인계 mythic people signal | `unclear` | `오벨리스크` | `working/imports/phase5_section8_obelisk_kingdom_of_dead/16. 예하 부대 및 기사단 (Military Units)/02. 해골 군단 (Bone Legion).md` | `화염 거인`, `언데드 거인` | `low` | 전설/유해/병기층 우세 |
| `오크 부락` | 오크 people signal | `species` | `오벨리스크 / 봉인 수호단 전선` | `working/imports/phase5_section8_obelisk_seal_wardens/16. 예하 부대 및 기사단 (Military Units)/08. 보급로 사수대 (Lifeline Defenders).md` | `오크보다 강한 괴물`, `monsterized orc image` | `low` | people signal은 있으나 사회 구조 근거는 더 필요 |
| `고블린혼혈` | 고블린계 bloodline/integration signal | `bloodline` | `에테르 / 자유도시연합` | `working/imports/phase3_section8_ether_crossroad_cities/자유도시연합 (Crossroad Cities).md` | `고블린 사회`, `고블린 부족` | `low` | 사회 구조보다 혼혈/통합 신호만 보임 |

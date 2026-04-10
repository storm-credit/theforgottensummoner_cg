# Section 15 Folder Draft Routing Plan

이 문서는 `15 Named Notables`의 실제 폴더링을 하기 전,
후보별 가상 라우팅을 설계하는 초안이다.

중요:

- 실제 파일 이동 계획이 아니다.
- 원본 저장소를 수정하지 않는다.
- `cg` 안에서만 라우팅 기준을 점검한다.
- 폴더 기준은 직업이 아니라 `대륙 -> 세력 / 도시 / 조직`이다.

## Stable Candidate Routing

| Candidate | Draft Route | State | Reason |
|---|---|---|---|
| `울프가르 드래곤포지` | `15 / 크림슨 / 용의 후예 / 드래곤포지 공방` | `stable_15_workset / route_hierarchy_locked / grade_caution` | 용의 대장장이/공방주. 상위 route와 place lock을 분리한 actual draft 기준을 따르되 14 재확인 전 Hard Canon route로 고정하지 않는다. |
| `에리온 드라코비스` | `15 / 크림슨 / 엘드라칸 / 학술-전승층` | `stable_15_workset / route_hierarchy_locked / grade_caution / name_collision_watch` | 고대어 해석가/대현자. 엘드라칸 학술-전승층을 상위 route로 읽되 `에리온 베르날리스` 충돌 감시를 유지한다. |
| `오그마` | `15 / 크림슨 / 엘드라칸 / 전승 보관층` | `stable_15_workset / route_hierarchy_locked / act_watch` | 살아있는 도서관/고룡 조언자. 전승 보관층 route와 place lock을 분리한 actual draft 기준을 우선한다. |
| `엘다라` | `15 / 에테르 / 정령연합 / 루미라` | `support_hold / verify_source_before_profile` | 루미라 대현자/고대 정령어 권위자. 정령연합 전체 14 확인 전 Hard Canon 금지, stable triad actual draft에는 즉시 합류시키지 않는다. |
| `실비아` | `15 / 범대륙 후기 확장 / 키르케 영약회` | `deferred_expansion_hold / name_collision_watch` | 강한 15 후보지만 범대륙 후기 확장이라 메인 진행 후순위. |

## Boundary Candidate Routing

아래 후보는 경로를 잡아두되,
14 확인 전 실제 15로 승격하지 않는다.

| Candidate Cluster | Draft Anchor | State |
|---|---|---|
| `벨라나 / 아리안` | `크림슨 / 붉은 사막 부족 / 현자 회의` | `verify_before_15` |
| `드락사르 / 카사르` | `크림슨 / 용의 후예` | `verify_before_15` |
| `대런 / 칼리스트 / 에드가 / 탑주 계열` | `에테르 / 마법협회` | `verify_before_15` |
| `래퍼티 / 요한 / 실라스 블랙쏜` | `에테르 / 성국` | `verify_before_15_or_keep_14` |
| `엘라라 / 드라이덴 / 메라 / 실라스 나이트쉐이드` | `에테르 / 정령연합` | `verify_before_15` |
| `울프릭 / 마리안 / 프리야 / 카이라` | `프로스트 / 빙하의 성소 / 주술사 원로단` | `verify_before_15` |
| `시그리드` | `프로스트 / 퍼마프로스트 공성단 / 아이스포지` | `verify_before_15` |
| `미다스 / 이소벨 / 해양 실비아` | `해양 / 황금 함대` | `verify_before_15` |
| `마르코 / 엘레오노라 / 크리스토퍼` | `해양 / 거상 연합` | `verify_before_15` |
| `골드핑거 / 리나 / 에릭 / 모로스` | `해양 / 해적 연합` | `verify_before_15` |
| `오렌 / 세일블레스 마리아` | `해양 / 바다의 교단` | `verify_before_15` |
| `바리온 / 아이기스 / 베스 / 이안` | `오벨리스크 / 봉인 수호단` | `verify_before_15` |
| `카트린 / 레보니아 / 우로스` | `오벨리스크 / 잊힌 자들의 연합` | `verify_before_15` |
| `카론 / 세르반 / 레티시아` | `오벨리스크 / 망자의 왕국` | `verify_before_15` |

## Need Named Candidate Folder Buckets

개인명 없는 슬롯은 아래 버킷으로만 보존한다.

| Continent | Draft Bucket | Slot Examples |
|---|---|---|
| `에테르` | `에테르 / 성국 / 마법협회 / 왕국연합 / 자유도시연합 / 정령연합` | 금서 검인관, 비전로 장인장, 성좌 관측장, 대서고 수호장, 성채 봉인관, 서약의회 기록관, 정령묘 이름새김꾼 |
| `프로스트` | `프로스트 / 오로라 평원 / 얼음무덤 언덕 / 푸른 폭풍 요새 / 아이스포지 / 빙하의 성소` | 원로 사냥꾼, 묘지기 장로, 대예언자, 수석 기술자, 별의 샤먼, 아이스포지 장인 |
| `해양` | `해양 / 포트 아우렐리온 / 크로스윈드 포트 / 오라클 바지 / 블랙워터 항구 / 볼트 오브 아우룸` | 수석 오라클, 항해사 길드장, 마스터 쉽라이트, 대경매장 주인, 은행장, 세관장, 심해 금고 보관인 |
| `오벨리스크` | `오벨리스크 / 템플 오브 바운더리 / 경계의 보루 / 기억 경매장 / 영원의 기록탑 / 망각의 회랑 / 그림자 도서관` | 기록의 수호자, 관측대장, 기억 경매장 중개자, 사후 서기관, 기억 지기, 신성 기록소 관리 사제 |

## Policy Routing Guard

- `크림슨` route는 씨족 중심 질서와 현자/장인/전승 thin-support까지만 보존하고, `state_house strong` route로 해석하지 않는다.
- `해양` 자유도시 profile route는 `urban_market / shadow_port / debt-enforcement` 축까지만 보존하고, `토착 공동체층` route와 섞지 않는다.
- `오벨리스크` 제도 route는 `nontraditional elite thin-support` 또는 `dark institution` 축까지만 보존하고, 전통 귀족국가형 route로 해석하지 않는다.
- `실비아`는 `범대륙 후기 확장 / 키르케 영약회` hold route로만 보존한다.
- operational profile route 문장은 lower-card authority를 따르며,
  named notable 승격 논리로 직접 역수입하지 않는다.
- 이 routing plan은 허용된 route family만 적고,
  operational cluster의 정확한 guard 문장은 하위 profile 카드의 `3-1. Policy Guard`에서 상속한다.

## Revision Gate

실제 폴더 초안을 만들기 전 반드시 확인한다.

1. 14번 독립 파일 존재 여부.
2. 이름 충돌 레지스터 등재 여부.
3. 대륙 spine과 맞는지.
4. 세력/도시/조직 앵커가 명확한지.
5. `Hard Canon`이 아니라면 `draft_route` 또는 `verify_before_15`로 유지.
6. named-notable route 결정이 operational profile guard 문장을 덮어쓰지 않는지.

## Conductor Decision

아직 실제 이동은 하지 않는다.

현재 이 문서의 역할은 stable triad actual draft `package freeze`를 다시 여는 것이 아니라,
freeze 밖 hold queue와 `Section 8 -> 15 carryover watch`를 유지하는 것이다.

즉 routing plan은 상위 경로 설계층으로만 읽고,
하위 operational profile의 `3-1. Policy Guard`를 재정의하지 않는다.

# Section 14 / 15 Boundary Verification Queue

이 문서는 `14번 영웅백과`와 `15번 인물백과` 사이에 걸친
경계 인물을 검증하기 위한 큐다.

원칙:

- `14`에 이미 있는 인물은 빼지 않는다.
- 유명하다고 무조건 `14`에 넣지 않는다.
- 명사형 영웅이지만 서사 중심 영웅이 아니면 `15 Named Notables` 후보가 될 수 있다.
- 조직 실무층이면 `15 Operational Lines` 후보가 된다.
- 현재 작업본에서 14 신호가 보이면 `verify_before_15`로 둔다.

## Decision Labels

| Label | Meaning |
|---|---|
| `keep_14` | 서사 중심 영웅으로 14 유지 |
| `named_notable_candidate` | 유명 NPC형 명사로 15 후보 |
| `operational_line` | 조직 작동을 보여주는 실무층 |
| `verify_before_15` | 15 후보지만 14 독립 시트나 중심 영웅 신호 확인 필요 |
| `hold_for_dual_review` | 14와 15 가치가 모두 커서 보류 |
| `conflict` | 소속, 문맥, 명칭 충돌이 있어 별도 등록 필요 |

## Tier A. Immediate Boundary Review

먼저 검증할 인물이다.

| Name | Current Signal | Likely Route | Verification Need | Current Action |
|---|---|---|---|---|
| `드락사르 블레이즈포지` | 연금술 공방 / A급 / 공병대장 / 신무기 테스트 | `15 Named Notables` 또는 `keep_14` | 14 독립 영웅 시트 존재 여부, 액트 중심성 확인 | `verify_before_15` |
| `멜리산드르` | S+급 수석 대약제사 / 키르케 최고위 | `keep_14` 또는 `15 Named Notables` | 중심 영웅인지, 조직 명사인지 확인 | `hold_for_dual_review` |
| `카사르 더 시어` | S급 용의 예언자 / 최고 조언자 / 시험의 탑 관리 | `keep_14` 또는 `15 Named Notables` | 전투/액트 중심성, 예언자 기능 확인 | `hold_for_dual_review` |
| `모이라 와일드웨이브` | 자유도시 본문에서 영웅식 직접 호명 | `keep_14` 가능성 높음 | 14 독립 시트 확인 | `verify_before_15` |
| `레이나 브라이트헤븐` | 자유도시 본문에서 영웅식 직접 호명 | `keep_14` 가능성 높음 | 14 독립 시트 확인 | `verify_before_15` |
| `이사벨 카르도` | 자유도시 본문에서 영웅식 직접 호명 | `keep_14` 가능성 높음 | 14 독립 시트 확인 | `verify_before_15` |

### Immediate Review Evidence

| Name | Evidence Found | Updated Judgment |
|---|---|---|
| `드락사르 블레이즈포지` | `용의 후예` 핵심표에서 15번, A급, 불꽃 연금술사로 등록되고, `드래곤하트`에서는 공병대장 / 신무기 테스트 의뢰자로 반복 등장한다. | `verify_before_15` 유지. 명사형 연금술사 가치가 크지만 전투/영웅록 신호가 강하다. |
| `멜리산드르` | `키르케 영약회`에서 수석 대약제사, S+급, 플라스크의 여제, 영약회 최고 의사결정자로 확인된다. | `hold_for_dual_review` 유지. 조직 최고위 명사지만 14급 위상과 겹칠 가능성이 크다. |
| `카사르 더 시어` | `용의 후예` 핵심표에서 8번, S급, 용의 예언자 / 최고 조언자로 확인되고 `전설적 마도 영웅록` 항목도 보인다. | `hold_for_dual_review` 유지. 예언자형 명사 가치가 있지만 14 중심 영웅 신호가 강하다. |
| `모이라 와일드웨이브` | 자유도시연합 핵심표에서 9번, B급, 해적 연락책, Act 1/4, 이명 `파도의 속삭임`으로 확인된다. | `verify_before_15` 유지. 조직 연결 가치가 크지만 영웅식 인물표 신호가 있다. |
| `레이나 브라이트헤븐` | 자유도시연합 핵심표에서 7번, A급, 경매장 관리인, Act 1/2, `황금의 성녀`로 확인되고 브라이트헤븐 가문 출신 신호가 있다. | `verify_before_15` 유지. 경매/힐링 명사 가치가 있지만 14 신호가 강하다. |
| `이사벨 카르도` | 자유도시연합 핵심표에서 11번, B급, 운송 길드장, Act 1/3, 이명 `철의 마부`로 확인된다. | `verify_before_15` 유지. 물류 얼굴로 중요하지만 14 신호 확인 전까지 15 확정 금지. |

## Tier B Evidence

| Name | Evidence Found | Updated Judgment |
|---|---|---|
| `대런 크레센트` | `마법협회` 핵심표에서 No.9, 부탑주, A+급, Act 1~3, `협회의 살림꾼`으로 확인된다. `마법 서고단`과 `아르카디아`에서도 행정/예산/보급 실권자로 반복 등장한다. | `verify_before_15` 유지. 실무 명사 가치가 크지만 A+급 Act 축과 부탑주 신호가 있어 14 확인 전 15 확정 금지. |
| `칼레스트 나이트쉐이드` | `마법협회` 핵심표에서 No.10, 집행관, A급, Act 1~2, `침묵의 칼날`로 확인된다. `흑색의 탑`과 `아르카디아`에서는 암살/비밀 집행자 및 나이트쉐이드 클랜 연결 신호가 있다. | `verify_before_15` 유지. 실무 집행 라인으로도 중요하지만 암살 영웅/클랜 서사 신호가 있어 14 검증 대상이다. |
| `이리나 폰 루즈` | `phase1_orphans`에 `[현존] 정보단 여왕` 14 영웅 파일로 존재하고, 그림자 정보단 거울방과 에반 조우 미션의 직접 접점이 확인된다. `그림자 정보단 개요`에서도 수장으로 연결된다. | `keep_14_with_anchor_review`로 보정. 15 흡수 대상이 아니라 14 유지 후 `그림자 첩보망/그림자 정보단` 세력 앵커를 정리한다. |
| `칼리크 디트리히` | `phase1_orphans`에 `[현존] 카르텔 수장` 14 영웅 파일로 존재하고, 이리나와 적대하는 네크로 우물/강령술 거래망 수장으로 확인된다. `침묵의 카르텔 개요`에서도 수장으로 연결된다. | `keep_14_with_naming_review`로 보정. 15 흡수 대상이 아니라 14 유지 후 `카르텔` 표면명을 `침묵의 상회` 등 판타지 톤으로 재검토한다. |

## Tier B. Institutional Boundary Review

조직 실무층과 명사형 인물 사이에 있는 후보.

| Name | Current Signal | Likely Route | Verification Need | Current Action |
|---|---|---|---|---|
| `대런 크레센트` | 마법협회 행정 실권자 반복 등장 | `15 Operational Lines` 또는 `15 Named Notables` | 협회 내 직능이 인물성보다 강한지 확인 | `verify_before_15` |
| `칼레스트 나이트쉐이드` | 집행부 책임자 / 비밀 유지 축 | `15 Operational Lines` 또는 `keep_14` | 집행 영웅인지 실무 권력자인지 확인 | `verify_before_15` |
| `이리나 폰 루즈` | 정보망 중심 노드 / 고아 파일 | `15 Named Notables` 또는 별도 정보조직 앵커 | 14 중심성, 정보조직 대표성 확인 | `hold_for_dual_review` |
| `칼리크 디트리히` | 금융/암시장/강령술 접점 | `15 Named Notables` 또는 조직 앵커 | 이름 톤, 세력 앵커, 14 중심성 확인 | `hold_for_dual_review` |

## Tier C. Named Notable Stable Candidates

현재는 15 Named Notables 쪽이 더 자연스러운 후보.

| Name | Current Signal | Likely Route | Current Action |
|---|---|---|---|
| `실비아` | 기록자 / 시약 계량관 | `15 Named Notables` | `promote_to_named_notables` |
| `울프가르 드래곤포지` | 용의 대장장이 / 공방장 | `15 Named Notables` | `promote_to_named_notables` |
| `에리온 드라코비스` | 고대어 해석가 / 대현자 / 관리자 | `15 Named Notables` | `promote_to_named_notables` |
| `오그마` | 고룡 / 살아있는 도서관 | `15 Named Notables` | `promote_to_named_notables` |
| `벨라나 스톰브링어` | 현자 회의 / 대주술사 | `15 Named Notables` | `collect_more_context` |
| `아리안 블레이즈하트` | 현자 회의 / 대사제 | `15 Named Notables` | `collect_more_context` |
| `엘다라` | 대현자 / 고대 정령어 권위자 | `15 Named Notables` | `collect_more_context` |

## Verification Steps

각 인물 검증 순서:

1. 현재 import 작업본에서 같은 이름의 14 독립 시트가 있는지 확인한다.
2. 경로가 `14 Hero Archive`인지, 세력 문서 안 인물표인지 구분한다.
3. 전투/액트 중심성이 강하면 `keep_14`로 둔다.
4. 현자, 장인, 기록자, 약제사, 감정사, 조언자 기능이 강하면 `15 Named Notables`로 둔다.
5. 조직 기능을 대표하지만 개별 명사성보다 실무층이면 `15 Operational Lines`로 둔다.
6. 판단이 갈리면 `hold_for_dual_review`로 남긴다.

## Conductor Rule

경계 인물은 절대 성급히 이동하지 않는다.

현재는 `cg` 안에서 큐와 판정표만 만들고,
원본 저장소나 원본 클론은 수정하지 않는다.

# Section 14 / 15 Ether Boundary Evidence

이 문서는 `Tier E. Ether Institution Boundary Candidates`의 1차 대조 결과다.

검증 범위:

- `working/imports/phase2_section14_current_ether`
- `working/imports/phase1_section14_growth_aether`

원칙:

- 작업본 기준 14 독립 시트가 직접 보이면 `keep_14` 쪽으로 기울인다.
- 직접 14 시트가 보이지 않아도 원본 전체 검증 전에는 `15 확정`으로 승격하지 않는다.
- 세력 문서 내부의 직위/탑주/기관장 신호는 `verify_before_15`로 유지한다.

## Direct Match Result

| Candidate | Direct 14 Match in Current Imports | Updated Judgment | Note |
|---|---|---|---|
| 대런 크레센트 | `no_direct_14_match` | `verify_before_15` 유지 | 마법 서고단 대표 / 부탑주 신호는 있으나 현재 import된 14 독립 파일은 보이지 않는다. |
| 엘드린 문브링어 | `no_direct_14_match` | `verify_before_15 / white_tower_barrier_hold` 유지 | 백색의 탑 탑주. 현재 import된 14 독립 파일은 보이지 않는다. |
| 마르쿠스 레이븐펠 | `no_direct_14_match` | `verify_before_15 / name_drift` 유지 | 흑색의 탑 주앵커는 phase3 기준 `맥스웰 레이븐펠`로 읽고, `마르쿠스 레이븐펠`은 drift 표기로만 보존한다. `마르쿠스 코르부스`와 병합하지 않는다. |
| 이사도르 템페스트 | `no_direct_14_match` | `verify_before_15 / name_split_hold` 유지 | 청색의 탑 / 템페스트 가문 축으로 보존하고, phase2 직접 14 파일 `이사도르 솔레아`와 병합하지 않는다. |
| 세리오스 벤타리스 | `direct_14_match` | `keep_14_likely` | `phase2_section14_current_ether/4. 마법협회/07. 세리오스 벤타리스`가 직접 확인된다. 태그도 `hero, s_rank`다. |
| 네리사 블러드위버 | `no_direct_14_match` | `verify_before_15 / abyss_blood_taboo_hold` 유지 | 적색의 탑 탑주. 현재 import된 14 독립 파일은 보이지 않는다. |
| 다미엔 이클립스 | `no_direct_14_match` | `verify_before_15 / shadow_intelligence_hold` 유지 | 은색의 탑 탑주. 현재 import된 14 독립 파일은 보이지 않는다. |
| 칼리스트 | `no_direct_14_match` | `verify_before_15` 유지 | 황금의 탑 탑주. 연금/제작 명사층 가치가 있지만 14 확인 필요. |
| 래퍼티 아르카디아 | `no_direct_14_match` | `verify_before_15` 유지 | 성국 핵심표에서는 도서관장으로 보이지만 현재 import된 14 독립 파일은 보이지 않는다. |
| 대사제 요한 | `no_direct_14_match` | `verify_before_15 / holy_barrier_hold` 유지 | 루멘 성채 문서의 지역 거점 명사. 현재 import된 14 독립 파일은 보이지 않는다. |
| 엘라라 문힘 | `no_direct_14_match` | `verify_before_15` 유지 | 정령연합 핵심표에서 A급 노래술사 신호가 있으나 현재 import된 14 독립 파일은 보이지 않는다. |
| 드라이덴 썬더루트 | `no_direct_14_match` | `verify_before_15` 유지 | 자연 율법회 / 생명의 의회 신호가 있으나 현재 import된 14 독립 파일은 보이지 않는다. |
| 메라 라일윈드 | `no_direct_14_match` | `verify_before_15` 유지 | 외교 사절단 / Top 4 신호가 있으나 현재 import된 14 독립 파일은 보이지 않는다. |

## Evidence Note

`세리오스 벤타리스`는 다음 이유로 15번 승격 후보에서 내려야 한다.

- 파일 경로가 14번 현존 영웅 import 내부에 있다.
- frontmatter aliases가 영웅 백과 경로를 가리킨다.
- tags에 `hero`, `s_rank`, `arcane_society`가 들어 있다.
- 본문 기본 정보에서 신분이 `영웅 / 마법협회 차원 도약 및 방위 전략 장로`로 나온다.

따라서 세리오스는 `15 People Worth Seeking`이 아니라 `14 keep + faction anchor review`가 맞다.

## Verification Queue Snapshot

다음 검증은 `현재 import에 없는 이름`이 원본 전체에 14 독립 파일로 존재하는지 확인하는 것이다.

우선순위:

1. `래퍼티 아르카디아`: 성국 핵심표에서 도서관장으로 이미 이름이 보인다.
2. `대런 크레센트`: 마법 서고단 대표이자 부탑주 신호가 있다.
3. `칼리스트`: 연금/제작 명사층 가치가 커서 15 후보로 남길 수 있는지 확인한다.
4. `엘라라 문힘`: 기록/노래 전승 기능이 강하지만 A급 영웅표 신호가 있다.

## Priority Evidence Pass

추가로 `cg` 내부 reference / working / audit 범위에서 우선 후보 4명을 재검색했다.

| Candidate | Additional Evidence | Updated Judgment |
|---|---|---|
| 래퍼티 아르카디아 | `성국 (Saint Haven).md` 핵심표에서 `도서관장`, `A (Elite)`, `Act 2, 3`, `Scholar`, `금서 / 고대 마법 연구`로 확인되고, `아스트라르` 도시 문서에는 같은 도서관장 슬롯이 `Raphael Arcadia`로도 잡힌다. | `verify_before_15 / library_core_hold` 유지. 독립 14 파일은 현재 import에 없지만 성국 핵심표 신호와 `Rafferty / Raphael` 드리프트를 같이 관리해야 한다. |
| 대런 크레센트 | `마법협회` 본문에서 행정총무부 실질 운영 책임자, No.9, 부탑주, `A+ (Elite)`, `Act 1~3`, `협회의 살림꾼`, 마법 서고단 관장으로 반복 확인된다. | `verify_before_15 / archive_admin_hold` 유지. 15 Operational Lines 가치가 크지만 A+와 Act, 기관 운영 심장부 신호가 강해 15 확정 금지. |
| 칼리스트 | `마법협회` 본문에서 Top 8, 황금의 탑주, `A+ (Elite)`, `Act 1, 4`, `천리안`, 별의 예언자단 대예언자로 반복 확인된다. | `verify_before_15 / tower_seer_hold` 유지. 예언자형 명사 가치가 크지만 14급 탑주 / Act / 전략 두뇌 신호가 강하다. |
| 엘라라 문힘 | `정령연합` 본문에서 No.10, `A (Elite)`, Act 1, 2, `달의 찬가`, 기록/가호 증폭으로 보이고, 전설적 마도 영웅록과 루미라 도서관장/걸어다니는 도서관 신호도 확인된다. | `verify_before_15 / bardic_archive_hold` 유지. People Worth Seeking 가치가 매우 크지만 전설 영웅록과 A급 신호가 함께 걸린다. |

## Updated Conductor Read

에테르 우선 후보는 `유명 NPC형 명사` 가치가 분명하지만,
검토한 자료상 14번 영웅 신호가 예상보다 강하다.

따라서 다음처럼 임시 판정한다.

- `세리오스 벤타리스`: `keep_14_likely`
- `래퍼티 아르카디아`: `verify_before_15 / library_core_hold`, 성국 도서관장 코어와 Arcadia 이름 드리프트를 같이 관리
- `대런 크레센트`: `verify_before_15 / archive_admin_hold`, Operational Lines 가치보다 기관 실권 압력이 더 강함
- `칼리스트`: `verify_before_15 / tower_seer_hold`, 예언자형 명사지만 탑주 / Act / 전략 두뇌 신호 강함
- `엘라라 문힘`: `verify_before_15 / bardic_archive_hold`, 15 가치가 가장 살아 있지만 전설 영웅록 신호도 큼

## Second Evidence Pass

추가로 마법협회와 정령연합 세력 문서를 다시 훑어
아래 후보를 보강했다.

| Candidate | Additional Evidence | Updated Judgment |
|---|---|---|
| `엘드린 문브링어` | Top 2 백색의 탑주, S급, Act 1~3, 치유/방어 학파, 비전 결계단 책임자로 확인된다. | `verify_before_15 / white_tower_barrier_hold` 유지. |
| `마르쿠스 레이븐펠 / 맥스웰 레이븐펠 / 마르쿠스 코르부스` | 기존 스카우트에는 `마르쿠스 레이븐펠`로 기록됐지만, phase3 세력 문서에서는 Top 3 흑색의 탑 주앵커가 `맥스웰 레이븐펠`로 읽힌다. `마르쿠스 레이븐펠`은 drift 표기로만 보존하고, `마르쿠스 코르부스`는 별도 phase2 14 현존 영웅 파일이다. | `name_drift / verify_before_15`. `맥스웰` anchor 고정, `코르부스` merge-ban. |
| `이사도르 템페스트 / 이사도르 솔레아` | phase3 세력 문서에서는 `이사도르 템페스트`가 청색의 탑 / 템페스트 가문 축의 현재 앵커로 읽히고, `이사도르 솔레아`는 별도 phase2 14 현존 영웅 파일이다. | `name_split_hold / verify_before_15`. 병합 금지. |
| `네리사 블러드위버` | Top 6 적색의 탑주, S급, Act 1/3, 생체/금기 학파, 심연 연구단 연결이 보인다. | `verify_before_15 / abyss_blood_taboo_hold` 유지. |
| `다미엔 이클립스` | Top 7 은색의 탑주, S급, Act 1~5, 정보/환영 학파, 어둠술사단 연결이 보인다. | `verify_before_15 / shadow_intelligence_hold` 유지. |
| `드라이덴 썬더루트` | 엘더 루트, 생명의 의회, 정령연합 관계도에서 대드루이드, 뿌리의 수호자, 정책 조언자, 전설 마도 영웅록 신호가 보인다. | `verify_before_15` 유지. |
| `메라 라일윈드 / 메라 실피드` | 세력 문서에서는 `메라 라일윈드` 외교관 신호가 있고, 14 현존 영웅 import에는 `메라 실피드` 독립 파일이 있다. | `name_drift / verify_before_15`. 병합 금지. |

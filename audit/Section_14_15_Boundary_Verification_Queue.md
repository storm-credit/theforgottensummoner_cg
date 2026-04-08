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


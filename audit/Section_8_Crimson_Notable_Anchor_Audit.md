# Section 8 Crimson Notable Anchor Audit

이 문서는 `크림슨 / 용의 후예 / 엘드라칸` 앵커를 다시 보며
안정 15 후보 3명(`울프가르`, `에리온`, `오그마`)의 배치를 점검한 결과다.

## Conductor Verdict

크림슨 후보 3명은 여전히 15 Named Notables 시험 후보로 유용하다.

하지만 `울프가르`와 `에리온`은 8번 세력 문서 안에서
A급/전설적 마도 영웅록/세력 핵심표 신호가 보이므로
Hard Canon식 안정 후보가 아니라 `working stable with grade-caution`으로 낮춰 읽는다.

`오그마`는 엘드라칸 장소 문서에서 고룡 NPC/조언자/살아있는 도서관 신호가 강해
현재 셋 중 가장 명사형 NPC 성격이 선명하다.

## Evidence Table

| Candidate | Section 8 Evidence | Updated Judgment |
|---|---|---|
| `울프가르 드래곤포지` | 용의 후예 핵심표에서 `A급`, `공방장`, `드래곤포지` 앵커. 블루플레어 씨족의 공방장/무구 제작 축. 프라이멀 엠버의 대장장이 슬롯. | `named_notable_candidate / grade_caution` |
| `에리온 드라코비스` | 엘드라칸 관리자/통역사/중재자. 용의 후예 핵심표에서 `A급`, `기록관`, `용의 심장`. 블러드 본드 알타의 계약 증인. | `named_notable_candidate / grade_caution` |
| `오그마` | 엘드라칸의 몽상가의 바위에 머무는 고룡. 에반에게 고대 주문과 숨겨진 역사를 가르치는 조언자. | `named_notable_candidate` |

## Name Collision Watch

| Cluster | Evidence | Decision |
|---|---|---|
| `울프가르` | 프로스트에도 `울프가르 블레이즈프로스트`, `울프가르 룬팽`, `울프가르 스톰본` 등 다수 신호가 있음. | `울프가르 드래곤포지`와 병합 금지. 크림슨/용의 후예/드래곤포지 앵커로만 본다. |
| `에리온` | 에테르 정령연합 14 현존 영웅에 `에리온 베르날리스`가 있음. | `에리온 드라코비스`와 병합 금지. 크림슨/엘드라칸/용의 후예 앵커로만 본다. |

## Routing Decision

| Candidate | Draft Route | Route State |
|---|---|---|
| `울프가르 드래곤포지` | `15 / 크림슨 / 용의 후예 / 드래곤포지 공방` | `draft_route_ok / grade_caution` |
| `에리온 드라코비스` | `15 / 크림슨 / 엘드라칸 / 학술-전승층` | `draft_route_ok / grade_caution / name_collision_watch` |
| `오그마` | `15 / 크림슨 / 엘드라칸 / 전승 보관층` | `draft_route_ok` |

## Conductor Decision

세 후보를 15 시험 후보로 유지하되,
`울프가르`와 `에리온`은 14 확인 전 Hard Canon으로 고정하지 않는다.

다음 작업:

- `Section_15_Stable_Candidate_Profile_QA.md`의 판정을 보정한다.
- 이름 충돌 레지스터에 `Wolfgar`, `Erion` 클러스터를 추가한다.

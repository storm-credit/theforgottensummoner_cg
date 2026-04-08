# Section 15 Duplicate Verification

이 문서는 `15번 후보` 중
이미 `14번`에 존재할 가능성이 있는 이름들을
현재 가져온 작업본 기준으로 검증한 중간 메모다.

중요한 점은,
이 검증은 `cg에 현재 import된 범위` 기준이라는 것이다.
즉 `없음`은 절대 부재가 아니라
`현재 작업본에서는 standalone hero file이 안 보인다`는 뜻이다.

## Verification Result

| Name | Signal Type | Current Finding | Working Judgment |
|---|---|---|---|
| `레이나 브라이트헤븐` | `inline hero-style reference` | `자유도시연합` 본문 인덱스와 `페어딜러 상단` 문서에서 개별 인물처럼 직접 호명됨 | `14 signal present` |
| `모이라 와일드웨이브` | `inline hero-style reference` | `자유도시연합` 본문 인덱스와 `밤의 무역상` 문서에서 핵심 인물로 직접 호명됨 | `14 signal present` |
| `이사벨 카르도` | `inline hero-style reference` | `자유도시연합` 본문 인덱스와 `페어딜러 상단` 문서에서 직접 호명됨 | `14 signal present` |
| `대런 크레센트` | `institutional named role` | `마법협회`, `아르카디아`, `서고단` 문서에서 실무 권력자로 반복 등장 | `verify before 15` |
| `칼레스트 나이트쉐이드` | `institutional named role` | `마법협회`, `아르카디아` 문서에서 집행부 책임자로 반복 등장 | `verify before 15` |
| `벤투라 모레티` | `organization-only named role` | 현재 작업본에서는 `숨은 거래단` 문서 안에서만 확인 | `safe 15 candidate` |
| `엘리자베스 로슈포르` | `organization-only named role` | 현재 작업본에서는 `숨은 거래단` 문서 안에서만 확인 | `safe 15 candidate` |
| `리카르도 살바토레` | `organization-only named role` | 현재 작업본에서는 `숨은 거래단` 문서 안에서만 확인 | `safe 15 candidate` |
| `에블린 더모트` | `organization-only named role` | 현재 작업본에서는 `숨은 거래단` 문서 안에서만 확인 | `safe 15 candidate` |
| `도미닉 발사노` | `organization-only named role` | 현재 작업본에서는 `철혈 보증단` 문서 안에서만 확인 | `safe 15 candidate` |
| `레오나르도 피에트로` | `organization-only named role` | 현재 작업본에서는 `철혈 보증단` 문서 안에서만 확인 | `safe 15 candidate` |
| `로자 바르톨로` | `organization-only named role` | 현재 작업본에서는 `철혈 보증단` 문서 안에서만 확인 | `safe 15 candidate` |
| `에밀리오 가르시아` | `organization-only named role` | 현재 작업본에서는 `철혈 보증단` 문서 안에서만 확인 | `safe 15 candidate` |
| `로렌조 카르미네` | `organization-only named role` | 현재 작업본에서는 `검은 해골단` 문서 안에서만 확인 | `safe 15 candidate` |
| `이사벨라 산토스` | `organization-only named role` | 현재 작업본에서는 `검은 해골단` 문서 안에서만 확인 | `safe 15 candidate` |
| `마르코 라메즈` | `organization-only named role` | 현재 작업본에서는 `검은 해골단` 문서 안에서만 확인 | `safe 15 candidate` |
| `카를로스 벨몬테` | `organization-only named role` | 현재 작업본에서는 `검은 해골단` 문서 안에서만 확인 | `safe 15 candidate` |

## Conductor Rule

이제부터는 아래 규칙으로 간다.

1. `14 signal present`
   - 당장 `15`로 옮기지 않는다.
   - `14 중복 여부 확인 후 보강` 대상으로 둔다.
2. `verify before 15`
   - 협회/세력 실무층이라 `15` 가치가 높지만
     별도 영웅 파일 존재 가능성을 한 번 더 본다.
3. `safe 15 candidate`
   - 현재 작업본 기준으로는 `15` 회수 쪽이 안전하다.

## Practical Use

- `Section_15_Candidate_Register.md`의 상태 보정
- `Section_14_15_Boundary_Verification_Queue.md`의 검증 순서 기준
- `자유도시연합` 인물은
  `모이라 / 레이나 / 이사벨`을 바로 15로 확정하지 않고
  `부분 중복 신호`로 관리
- 반면 `숨은 거래단 / 철혈 보증단 / 검은 해골단` 인물들은
  `15` 쪽으로 더 자신 있게 확장 가능

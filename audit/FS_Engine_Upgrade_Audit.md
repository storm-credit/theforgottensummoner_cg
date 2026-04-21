# FS Engine Upgrade Audit

이 문서는 FS 엔진을 다시 점검하고,
이 단계에서 어떤 업그레이드가 실제로 필요한지 정리한 감사표다.

기준:

- 엔진의 `모듈 수`를 늘리는 것이 목적이 아니다.
- 큰 설정집에서 반복적으로 같은 혼선이 생기는 지점을 줄이는 것이 목적이다.

## Verdict Snapshot

FS 엔진의 뼈대는 이미 충분히 강하다.

이미 있는 핵심:

- `Reverse Design`
- `Canon Tier`
- `Archive Routing`
- `Relationship Ledger`
- `Chronology / Causality`
- `Act Outcome Ledger`
- `Foreshadow / Payoff`
- `Plausibility`
- `Naming`
- `Place / Asset / Institution`
- `Travel / Resource / Rumor`

즉 이 단계에서 부족한 건 `큰 이론`이 아니라
`반복 판단을 기억하고 누수 방지하는 장치`다.

## Upgrade Priority

### Upgrade A. Decision / Ruling Register

필요 이유:

- 같은 인물, 같은 세력, 같은 이름 충돌을
  나중에 다시 처음부터 논의하는 비용이 커졌다.
- `왜 이렇게 판정했는가`를 한 줄로 남기는 장부가 필요하다.

예:

- `울프가르 드래곤포지 = named_notable_candidate / grade_caution`
- `에리온 드라코비스 = name_collision_watch`
- `범대륙 후기 확장 = deferred expansion`

효과:

- Conductor의 판정을 되짚기 쉬워진다.
- 나중에 Story / Media 쪽이 붙어도 판정 근거를 잃지 않는다.

상태:

- `build_now`

### Upgrade B. Cross-Chronicle Firewall

필요 이유:

- 이 프로젝트는 연대기 분기가 이미 강하고,
  사용자도 `동양/무협은 다른 크로니클`이라고 명시했다.
- 이름, 세력 결, 어휘 톤, 초월 서사 방식이 다른 연대기와 섞이면
  로어 엔진 전체가 천천히 오염된다.

효과:

- 아스트라리스 판타지 버전의 금지 문법을 명확히 유지한다.
- 후속 확장 시 “다른 크로니클 설정 차용”을 바로 경고할 수 있다.

상태:

- `build_now`

### Upgrade C. Slot Maturation Register

필요 이유:

- `need_named_candidate` 슬롯이 많이 쌓였고,
  이 슬롯이 언제 `verify_before_15`로 올라가고,
  언제 실제 `People Worth Seeking`이 되는지 추적 장치가 필요하다.

효과:

- 이름 없는 명사층을 안전하게 운영할 수 있다.
- 새 이름을 섣불리 만드는 실수를 줄인다.

상태:

- `build_now`

### Upgrade D. Canon Change Log

필요 이유:

- 상태가 `hold -> verify_before_15 -> named_notable_candidate`처럼 바뀔 때
  변경 이력이 남아야 한다.

효과:

- 나중에 “왜 바뀌었지?”를 추적하기 쉬워진다.

상태:

- `draft_built`

### Upgrade E. Story-to-Lore Handoff Gate

필요 이유:

- 나중에 집필이 본격화되면 Story Engine이 새 지명, 새 유명인, 새 아이템을 계속 던질 가능성이 높다.
- 그때 Lore Engine으로 다시 되돌려 보내는 게이트가 있어야 한다.

효과:

- 원고에서 나온 즉흥 설정이 정본을 오염시키는 걸 막는다.

상태:

- `draft_built`

## Conductor Decision Snapshot

우선 적용 업그레이드 snapshot은 아래 3개다.

1. `FS_Decision_Ruling_Register.md`
2. `FS_Cross_Chronicle_Firewall.md`
3. `FS_Slot_Maturation_Register.md`

이 3개가 생기면

- 판정 기억
- 연대기 누수 방지
- 슬롯에서 People Worth Seeking으로 올라가는 성장선

이 세 가지가 안정된다.

그다음 우선이던 `Canon Change Log` 초안도 붙였다.

후속 엔진 보강축으로 남아 있던
`Story-to-Lore Handoff Gate`도 이미 붙였다.

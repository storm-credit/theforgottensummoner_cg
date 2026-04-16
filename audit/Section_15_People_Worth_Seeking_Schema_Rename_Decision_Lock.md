# Section 15 People Worth Seeking Schema Rename Decision Lock

## Purpose

이 문서는 `People Worth Seeking` prose authority가 확정된 뒤에도
`Named_Notable*`, `Named_Notables*`, `named_notable_candidate`,
`type: Named Notable`, `15 Named Notables` 같은 legacy schema / status /
path identity를 즉시 rename하지 않는 결정을 고정한다.

핵심 원칙:

- current-facing prose와 live routing instruction은 `People Worth Seeking`을 쓴다.
- file path, title, schema, status, action token, report history는 별도 migration plan 전까지 보존한다.
- 단순 search hit를 전부 치환하지 않는다.

---

## 1. Decision

이번 maintenance bundle에서는 아래 작업을 하지 않는다.

- `Section_15_Named_Notable_*` 파일 rename
- `Section_15_Named_Notables_*` 파일 rename
- `named_notable_candidate` 상태어 rename
- `promote_to_named_notables` action token rename
- `type: Named Notable` schema value rename
- `15 Named Notables` secondary index / frozen sample / snapshot heading 일괄 치환

이 결정은 `People Worth Seeking` authority를 약화하는 것이 아니라,
prose authority와 internal identity layer를 분리해 링크와 상태 장부를 보존하기 위한 것이다.

---

## 2. Preserve As Legacy Identity

아래 값은 current-facing label이 아니라 legacy identity로 읽는다.

- `Section_15_Named_Notable_*`
- `Section_15_Named_Notables_*`
- `named_notable_candidate`
- `promote_to_named_notables`
- `type: Named Notable`
- `15 Named Notables` inside secondary index, schema, frozen sample, snapshot opening, report history

보존 이유:

- 실제 파일과 링크가 이 이름을 사용한다.
- 상태 장부와 boundary queue가 이 토큰을 action key로 참조한다.
- report / dispatch history는 과거 drift를 언제 닫았는지 추적하는 근거다.
- schema/status rename은 prose cleanup보다 큰 migration이다.

---

## 3. Allowed Local Cleanup

아래에 해당하면 `People Worth Seeking`으로 교체한다.

- current-facing prose
- live routing instruction
- active conductor decision
- reader-facing draft label
- workflow engine guidance

이번 pass에서 `workflow` current guidance의 남은 live label residue는 이 원칙에 따라 정리했다.

---

## 4. Migration Gate

나중에 실제 rename을 하려면 최소한 아래가 먼저 필요하다.

- old path -> new path rename map
- `OPEN_INDEX`, setting-book hubs, source maps, crosswalks의 link rewrite plan
- `named_notable_candidate` / `promote_to_named_notables` compatibility alias plan
- `type: Named Notable` schema migration table
- report / dispatch history preservation policy
- post-migration broken-link audit

이 gate가 없으면 schema/status/path 계층은 그대로 둔다.

---

## 5. Current Reading

2026-04-16 기준 current prose authority는 `People Worth Seeking`이다.

남은 legacy hits는 아래 둘 중 하나로 판정한다.

1. live prose / routing drift이면 `People Worth Seeking`으로 정리한다.
2. schema / status / path / title / snapshot / history이면 이 lock에 따라 보존한다.

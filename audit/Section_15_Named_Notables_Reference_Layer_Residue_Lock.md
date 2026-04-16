# Section 15 Named Notables Reference Layer Residue Lock

## Purpose

이 문서는 2026-04-16 watch-only maintenance 이후에도 남겨 두는
`Named Notables` / `Named Notable` / `named notable` / `named-notable`
계열 잔여를 current prose drift가 아니라 reference-layer residue로 고정한다.

핵심 원칙:

- current-facing live prose는 `People Worth Seeking`을 쓴다.
- 아래 범주의 잔여는 문서 정체성, schema, snapshot, history, frozen sample 성격이므로
  임의로 일괄 교체하지 않는다.
- 파일명과 과거 snapshot 제목을 바꾸는 작업은 별도 rename plan이 있을 때만 진행한다.

---

## 1. Frozen Routing Sample

보존 대상:

- `Section_15_Foldering_Test_Crimson.md`

보존 이유:

- 문서 자체가 `frozen routing sample`이라고 못박고 있다.
- 이 안의 `15 Named Notables` wording은 현재 authority prose가 아니라
  당시 라우팅 샘플을 재현하는 reference text다.

대표 위치:

- `Section_15_Foldering_Test_Crimson.md:1`
- `Section_15_Foldering_Test_Crimson.md:3`
- `Section_15_Foldering_Test_Crimson.md:16`
- `Section_15_Foldering_Test_Crimson.md:38`
- `Section_15_Foldering_Test_Crimson.md:119`

---

## 2. Snapshot / Batch Opening

보존 대상:

- `Section_15_Frost_Search_Findings_Batch_01.md`
- `Section_15_Frost_Search_Findings_Batch_02.md`
- `Section_15_Obelisk_Search_Findings_Batch_01.md`
- `Section_15_Obelisk_Search_Findings_Batch_02.md`
- `Section_15_Oceanic_Search_Findings_Batch_02.md`
- `Section_15_Oceanic_Search_Findings_Batch_03.md`
- `Section_15_Oceanic_Search_Findings_Batch_04.md`
- `Section_15_Oceanic_Search_Findings_Batch_05.md`

보존 이유:

- 남은 hit는 대부분 `이 문서는 ... 후보명 탐색의 ... 결과다` 형태의
  snapshot / batch opening이다.
- live judgment prose는 이전 pass에서 이미 `People Worth Seeking` 기준으로 정리했다.

---

## 3. Title / Document Identity

보존 대상:

- `Section_15_Named_Notable_*`
- `Section_15_Named_Notables_*`

보존 이유:

- 제목과 파일명은 legacy path / document identity로 기능한다.
- 현재 authority 문장과 다르게, title layer는 기록의 위치를 가리키는 reference다.
- rename이 필요하면 파일명, 링크, dispatch log, report history를 함께 다루는 별도 plan이 필요하다.

대표 위치:

- `Section_15_Named_Notable_Arian_Blazeheart.md:1`
- `Section_15_Named_Notables_Ether_Scout.md:1`
- `Section_15_Named_Notables_First_Pass.md:1`
- `Section_15_Named_Notables_Gap_Scout.md:1`
- `Section_15_Named_Notables_Recovery_Batch_01.md:1`

---

## 4. Schema / Status / Index

보존 대상:

- `type: Named Notable`
- `15 Named Notables` used as secondary index / primary candidate schema
- `Named Notable` inside fenced template schema

보존 이유:

- 이 값들은 current prose가 아니라 과거 상태어, schema, 색인값, 파일-family identity다.
- `People Worth Seeking`로 모두 바꾸면 status migration과 file naming migration을 동시에 요구한다.
- 현재 maintenance pass의 범위는 prose authority 정렬이며, schema migration은 별도 결정이 필요하다.

대표 위치:

- `Section_15_Named_Notable_Arian_Blazeheart.md:32`
- `Section_15_Named_Notable_Bellana_Stormbringer.md:33`
- `Section_15_Named_Notable_Draxar_Blazeforge.md:33`
- `Section_15_Named_Notable_Eldara.md:39`
- `Section_15_Named_Notable_Erion_Dracovis.md:11`
- `Section_15_Named_Notable_Template.md:21`

---

## 5. Snapshot Scout / Recovery Opening

보존 대상:

- `Section_15_Named_Notables_Gap_Scout.md:3`
- `Section_15_Named_Notables_Recovery_Batch_01.md:4`

보존 이유:

- 이 줄들은 snapshot 문서의 opening reference다.
- active 판단 문장과 queue judgment는 이미 `People Worth Seeking` 기준으로 정리했다.

---

## 6. Report / Dispatch History

보존 대상:

- `audit/reports/*`
- `orchestra/AGENT_DISPATCH_LOG.md`

보존 이유:

- report와 dispatch log 안의 `Named Notables` hit는
  과거 작업에서 무엇을 정리했는지 설명하는 history다.
- 이력을 current wording으로 덮어쓰면 어떤 drift를 언제 닫았는지 추적하기 어려워진다.

---

## 7. Working Draft Status

현재 상태:

- `working/drafts`의 current-facing `Named Notables` / `Named Notable` / `named notable` /
  `named-notable` / `named-notables` residue는 닫힌 상태다.
- `Setting_Book_Appendix_Assembly_Manuscript_Draft.md`의
  Aegis row-level evidence note에 남아 있던
  `named-notable collision register`는
  `People Worth Seeking collision register`로 정리했다.

---

## 8. Operational Rule

앞으로 동일 search hit가 다시 잡히면 아래 순서로 판정한다.

1. current-facing prose인가?
2. live judgment / conductor decision / routing instruction인가?
3. reader-facing draft 문장인가?
4. title / file identity / schema / snapshot / report history인가?

1~3이면 `People Worth Seeking` 기준으로 정리한다.
4이면 이 lock에 따라 보존한다.

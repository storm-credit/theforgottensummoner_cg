# Setting Book Chapter 8 Draft: Register Appendix

## Chapter Purpose

This chapter defines how the setting book should use registers, queues, manifests, and verification tables.

The appendix is not a second body text. It is the evidence and control layer behind the readable setting book. It keeps long tables, boundary decisions, source priority, unresolved questions, and future expansion hooks out of the main prose while preserving enough traceability for later revision.

The reader-facing setting book should feel clean. The appendix should make the clean version trustworthy.

## Appendix Authority Rule

Registers support body chapters, but they do not automatically override them.

Use this authority order:

1. source priority register for evidence strength
2. canon tier register for certainty level
3. state label register for current handling
4. chapter body for reader-facing synthesis
5. appendix tables for traceability, conflict notes, and future work

If a body chapter and appendix disagree, do not silently rewrite the body. Mark the disagreement as `open_question`, then route it through the relevant register or boundary queue.

## What Belongs in the Appendix

Move material into the appendix when it is useful but too heavy for body prose.

Appendix material includes:

- source priority ladders
- canon tier tables
- state label definitions
- boundary verification queues
- candidate registers
- conflict and name-collision registers
- reveal and foreshadow controls
- place and travel function tables
- asset secret lists
- rumor versus fact notes
- manifests used for completeness checking

The appendix should not become a dumping ground. Every table needs a clear use.

## Core Register Families

| Register Family | Primary Files | Setting-Book Use |
| --- | --- | --- |
| Canon and source control | `FS_Canon_Tier_Register.md`, `FS_Source_Priority_Register.md`, `FS_State_Label_Register.md`, `FS_Decision_Ruling_Register.md` | Defines what can be treated as hard, soft, unresolved, deprecated, or action-ready. |
| Story control | `FS_Story_Act_Question_Register.md`, `FS_Reveal_Control_Register.md`, `FS_Foreshadow_Payoff_Register.md` | Keeps body chapters from revealing too much or flattening future story timing. |
| World function control | `FS_Place_Function_Register.md`, `FS_Travel_Logistics_Register.md`, `FS_Ecology_Resource_Register.md`, `FS_Institution_Memory_Register.md` | Converts place, travel, ecology, and institution notes into story-useful functions. |
| Expansion and maturity control | `FS_Slot_Maturation_Register.md`, `Section_14_15_Boundary_Verification_Queue.md`, `Section_15_Candidate_Register.md` | Prevents premature promotion of candidates into final body entries. |
| Secrecy and rumor control | `FS_Asset_Secret_Register.md`, `FS_Rumor_Fact_Register.md` | Separates what is true, what is rumored, what is hidden, and what should remain unrevealed. |
| Completeness control | `reference/manifests/factions_manifest.md`, `reference/manifests/heroes_manifest.md` | Checks whether major source areas have been seen without treating every source as equally authoritative. |

## Canon Tier Appendix

The canon tier appendix should summarize certainty, not retell the whole world.

Use the following body-facing categories:

| Tier | Body-Chapter Behavior |
| --- | --- |
| Hard Canon | May be written plainly. Avoid hedging unless the body chapter is explaining source policy. |
| Soft Canon | May be used, but should not be phrased as irreversible. |
| Open Question | Should appear as unresolved, optional, or appendix-only unless the uncertainty itself is important. |
| Rumor | May be written as in-world rumor, not objective fact. |
| Deprecated / Legacy | Should not return to body canon unless explicitly re-promoted. |

The appendix can list examples, but the main body should only carry the examples that help the reader understand the chapter.

## State Label Appendix

State labels are operational controls. They are not prose style.

Reader-facing chapters may explain the meaning of a state, but the exact label should remain in appendix tables unless the label itself is useful for the production workflow.

Important labels for current setting-book use:

- `hard_canon`
- `soft_canon`
- `active_working`
- `verify_before_15`
- `named_notable_candidate`
- `operational_line`
- `display_canon_candidate`
- `conflict`
- `macro_overlink`
- `legacy_hold`
- `open_question`
- `stable_15_workset`
- `source_check_hold`
- `deferred_expansion_hold`
- `hold_for_dual_review`

The appendix should preserve these labels exactly. Body chapters can translate them into natural language.

## 14 / 15 Boundary Appendix

The boundary appendix is essential because it protects the difference between central heroes and named world figures.

Body chapter rule:

- `14` remains the narrative-centered hero axis.
- `15 Named Notables` collects notable figures people seek out inside the world.
- `15 Operational Lines` collects practical systems and working layers of organizations.

Appendix rule:

- Keep boundary candidates in queue until the 14 signal is checked.
- Do not demote a hero into 15 just because the person has a profession.
- Do not promote an operational function into a named notable just because a role sounds important.
- Do not merge name-collision candidates without source proof.

The boundary appendix should include candidate tables by review tier, not long biography prose.

## Place and Travel Appendix

The place and travel appendix should keep geography useful.

Use place registers to answer:

- What does this location allow to happen?
- Which faction benefits from it?
- What memory, market, sanctuary, workshop, threshold, or underworld function does it carry?

Use travel registers to answer:

- Who controls the route?
- What does it cost?
- Who uses the official path?
- Who knows the unofficial path?
- What blocks movement?
- What rumors and goods move along it?

The body map chapter should stay readable. The appendix can hold route tables, function tags, obstruction notes, and unresolved map questions.

## Foreshadow, Reveal, and Secret Appendix

The setting book should not accidentally spoil the story by explaining every hidden mechanism too early.

Use the reveal and secret registers to separate:

- what the author knows
- what the world knows
- what factions know
- what the protagonist knows
- what the reader should know now
- what should be withheld

If an item, place, faction, or bloodline has hidden truth value, the body chapter should present only the safe layer. The appendix can record the deeper layer with a reveal control note.

## Rumor and In-World Text Appendix

Rumors are useful because they make the world feel lived in. They are dangerous because they can be mistaken for objective canon.

Appendix handling:

- Preserve rumor wording when it creates flavor.
- Mark whether a rumor is false, partly true, exaggerated, propaganda, misunderstood history, or future clue.
- Do not use rumor as hard evidence for faction structure, item power, species history, or character identity.

Body handling:

- Phrase rumors as rumors.
- Let contradictory rumors coexist when they create useful world texture.
- Do not resolve a rumor unless the story or canon tier register supports it.

## Manifest Appendix

Manifests are completeness tools, not canon by themselves.

Use manifests to answer:

- Which source files exist?
- Which faction or hero files have been seen?
- Which areas may be missing from the current synthesis?
- Which names need source checks before promotion?

Do not treat manifest presence as proof of final status. A file existing in a manifest may still be legacy, duplicated, corrupted, preliminary, or superseded.

## Appendix Entry Template

Use this compact pattern for appendix entries:

```text
Entry Name:
Register Family:
Source File:
Current Label:
Canon Tier:
Body Chapter Link:
Use in Body:
Known Conflict:
Next Action:
```

## Setting-Book Assembly Rule

When assembling the final setting book:

1. Body chapters should explain the world.
2. Appendix chapters should explain the evidence controls.
3. Candidate tables should stay in appendix until promoted.
4. Reader-facing prose should not expose every internal label.
5. The appendix should preserve enough traceability for future edits.

## Chapter Lock

This chapter locks appendix handling for the current setting-book recomposition pass:

- Registers support the body; they do not replace it.
- Long tables, conflicts, candidates, and queues belong in appendix.
- Canon tier, source priority, and state labels must remain separable.
- Boundary candidates stay queued until verification.
- Rumors, secrets, and reveal timing must not be flattened into objective body text.
- Manifests check coverage but do not create canon.


# Setting Book Post-Closeout Assembly Gate

## Purpose

This gate starts the setting-book work after the cleanup closeout.

It does not reopen broad cleanup, candidate discovery, release-candidate naming, or production-bible expansion. It tells the orchestra what to assemble next now that `audit/Setting_Book_Cleanup_Closeout.md` has closed the current setting-book cleanup loop.

## Current Gate State

`post_closeout_reader_facing_layout_gate`

Current call:

- Cleanup state: `closed_for_current_cleanup / watch-reference mode`
- Shareable manuscript: `Setting_Book_Preview_Readable_v0.md`
- Compressed reference: `The_Forgotten_Summoner_Setting_Book_Prototype_v0.md`
- Default next artifact direction: `reader-facing layout`
- Production bible direction: `not next yet`
- Release-candidate rename: `controlled hold`

## Source Authority

Use these as the active assembly authority stack:

1. `audit/Setting_Book_Cleanup_Closeout.md`
2. `working/drafts/Setting_Book_Reassembly_Source_Map.md`
3. `working/drafts/Setting_Book_Document_Roles_Map.md`
4. `working/drafts/Setting_Book_Assembly_Index.md`
5. `working/drafts/Setting_Book_Current_Status_Dashboard.md`
6. `audit/Continuous_Workstream.md`, `audit/Next_Sequential_Workstream.md`, and `audit/Audit_Queue.md`
7. `audit/FS_Source_Priority_Register.md` and `audit/FS_Canon_Tier_Register.md`
8. `audit/Historical_Batch_Reading_Guard.md`

Reference-only lanes:

- `working/imports/**`
- `reference/manifests/**`
- historical batch/search/scout/recovery docs
- raw extraction files such as `working/crosswalks/Extracted_Item_Candidates.md`
- release/process docs, except when checking gates

## Reader-Facing Assembly Order

Use the reader-facing world-companion order, not the internal technical 0-8 draft order.

| Order | Part | Role |
|---|---|---|
| 0 | Front Matter: A Living World Companion | Promise, audience, and how to use the book. |
| 1 | How to Read This World | Human-centered canon rules and confirmed/uncertain/rumor distinctions. |
| 2 | The Five Continents | Core world identity before detailed factions or entries. |
| 3 | Powers, Orders, and Hidden Systems | Factions by story function, not folder structure. |
| 4 | Places, Routes, and Maps That Create Story | Geography as movement, pressure, trade, secrecy, and scene function. |
| 5 | People Worth Seeking | Sages, artisans, archivists, brokers, and operational figures without replacing central heroes. |
| 6 | Names, Languages, and World Tone | Display names, variants, protected collisions, and tone. |
| 7 | Relics, Gear, Trade Goods, and Things People Want | Desire-first item logic, not a raw item dump. |
| 8 | Peoples, Bloodlines, Monsters, and Changed States | Wonder with species/race overread control. |
| 9 | Appendix and Production Notes | Evidence, status, queues, collisions, and unresolved edges. |

The recommended body flow is:

`Opening -> Continents -> Powers -> Places -> People -> Names -> Items -> Species -> Appendix`

`Places` stays before `People` because current preview flow opens the world through movement and city/route pressure before asking who must be found there.

## Do Not Promote

Keep these out of the usable setting-book body unless a current gate explicitly promotes them:

- `reference/manifests/*`
- `working/imports/**`
- historical batch/search/scout/recovery docs
- candidate rows and recovery queues
- legacy, backup, corrupted-root, `_Legacy_`, and broken-name material
- missing-layer proof tables and overread firewall details
- raw item extraction files
- release/process docs

## Hard Guardrails

- Do not reopen stable triad, hold batches, or new candidate discovery by default.
- Keep stable, hold, deferred, role-slot, P2 place-pressure, and missing-layer states separate.
- Keep `P2 place-pressure` ownership in sidecar/register docs.
- Keep lower-card `3-1. Policy Guard` authority on profile/subline profile cards.
- Treat historical docs as archive evidence unless current mainline promotes them.
- Keep manifests and raw imports as reference/appendix evidence only.
- Keep `Setting_Book_Preview_Readable_v0.md` as the stable shareable preview.
- Keep `Prototype_v0` as compressed reference.
- Do not create a release-candidate file or production bible until the existing gates flip.
- Do not globally replace protected legacy identity terms such as `Named Notables` until a migration plan exists.

## Next Safe Batch

The next safe batch is not broad rewriting.

Recommended sequence:

1. Record this post-closeout gate in the assembly index, dashboard, source map, and thread checkpoint.
2. Run a narrow reader-facing layout check against `Setting_Book_Preview_Readable_v0.md`.
3. If a real body-final entry is promoted, add only the needed row-level Appendix B/C evidence.
4. Re-check packaging direction only if collaborator or production-bible demand becomes concrete.
5. Re-check filename/RC only if the next preserved artifact actually needs a release-candidate file.

## Reopen Triggers

Reopen this gate only if:

- a current source-of-truth doc changes the mainline reference;
- stable/hold/deferred states collapse into each other;
- `P2 place-pressure` ownership moves outside sidecar/register authority;
- upper summaries override lower-card policy guard wording;
- live manuscript input, new source access, confirmed evidence drift, or source conflict appears;
- a body-final entry actually requires new Appendix B/C row-level evidence;
- a real path/schema/status migration plan is created for the protected `Named Notables` legacy identity layer.

## Conductor Decision

The setting-book cleanup loop is closed. The next setting-book loop is a controlled reader-facing layout gate, with `Preview_Readable_v0` preserved as the shareable manuscript and no broad redraft unless a current gate opens it.

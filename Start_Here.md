# Astralis Lore Orchestra

이 저장소는 `THE FORGOTTEN SUMMONER` 원본 전체를 직접 수정하기 전에,
`아스트라리스 연대기` 기준으로 설정집을 정리하기 위한 총괄 본부다.

핵심 목적은 세 가지다.

1. 작품 철학을 먼저 고정한다.
2. `8. 세력 아카이브`와 `14. 인물 백과`를 사람이 감당 가능한 단위로 쪼갠다.
3. 문서 기준과 기계 감사를 함께 굴려서 빈 구멍, 충돌, 중복, 레거시를 정리한다.

## 먼저 읽을 파일

1. `workflow/00_Astralis_Vision.md`
2. `workflow/01_Canon_Policy.md`
3. `workflow/02_Lore_Audit_Rules.md`
4. `workflow/03_Relationship_Types.md`
5. `workflow/04_Hero_Canon_Schema.md`
6. `workflow/05_Naming_Normalization_Map.md`
7. `workflow/06_Legacy_Quarantine_Policy.md`
8. `workflow/07_Item_Canon_Schema.md`
9. `workflow/08_Item_Desire_Design.md`
10. `workflow/09_House_Clan_Guild_Adequacy.md`
11. `workflow/10_Spatial_Map_Progression.md`
12. `workflow/11_FS_Engine.md`
13. `workflow/11_Writer_Engine.md`
14. `audit/FS_Engine_Core_Consensus.md`
15. `audit/FS_Engine_Writing_Craft_Map.md`
16. `workflow/14_FS_Media_Engine.md`
17. `audit/FS_Media_Engine_Consensus.md`
18. `working/crosswalks/Character_Archive_Split.md`
19. `working/crosswalks/Item_Encyclopedia_Pipeline.md`
20. `orchestra/AGENT_ROSTER.md`
21. `orchestra/Active_Agent_Split.md`
22. `orchestra/MASTER_PLAN.md`
23. `orchestra/ORCHESTRA_ADVANTAGE_LOCK.md`
24. `orchestra/EXECUTION_HARNESS_LOCK.md`
25. `orchestra/MODEL_ROLE_SPLIT_LOCK.md`
26. `audit/Audit_Queue.md`

## 운영 원칙

- 원본 GitHub 저장소와 원본 로컬 클론은 절대 수정하지 않는다.
- 원본 로컬 클론 `X:\theforgottensummoner`는 읽기 전용 참조 경로다.
- 원본 저장소는 바로 고치지 않는다.
- 먼저 `cg` 저장소에서 기준과 이슈를 정리한다.
- 실행은 `MCP -> Skills -> Agents -> Hooks -> Registers -> Conductor final integration` 순서를 기본으로 한다.
- 모든 판단은 `인간 서사 중심`, `액트 단위 여운`, `엇갈린 관계망`, `초월전 비중 제한` 원칙을 따른다.
- 확정되지 않은 내용은 삭제하지 않고 `Soft Canon` 혹은 `Open Question`으로 보류한다.
- 폴더별 에이전트 분할보다 `기능별 전문가 + 총괄 Conductor` 구조를 우선한다.
- `8. 세력 아카이브`는 서사 수정 전에 구조와 명칭부터 안정화한다.
- 대륙마다 가문, 부족, 길드 층이 충분한지 먼저 본다.
- `14. 인물 백과`는 전기문보다 관계망과 정본 스키마를 먼저 고정한다.
- `15번`은 `14번` 대체가 아니라 흩어진 인물 회수 축이다.
- 아이템은 문서마다 흩어진 후보를 먼저 수집표에 모은 뒤에만 백과로 승격한다.
- 지도는 메인 진행을 막지 않는 선에서 세계 -> 대륙 -> 도시 -> 건물 순으로 점진적으로 붙인다.
- 작법 이론은 참고용 메모가 아니라 `FS Engine`으로 통합해 실제 판단 순서에 사용한다.

## 첫 실행

```powershell
python scripts/export_reference_manifest.py `
  --name factions `
  --source "X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)" `
  --output "reference/manifests/factions_manifest.md"

python scripts/export_reference_manifest.py `
  --name heroes `
  --source "X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)" `
  --output "reference/manifests/heroes_manifest.md"
```

이후에는 `audit/Audit_Queue.md` 순서대로 섹션별 감사를 진행한다.

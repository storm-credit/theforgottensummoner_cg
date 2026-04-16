# Runbook

## 기본 순서

0. 원본 저장소는 읽기 전용으로 취급한다.
1. Conductor가 현재 작업 단위를 고른다.
2. 필요하면 병렬 scout를 분리해서 같은 배치 안에서 서로 다른 축을 조사하게 한다.
3. `FS Engine`에서 이번 작업에 먼저 적용할 엔진 층을 고른다.
4. Canon Architect가 기준 충돌 여부를 본다.
5. Continent Adequacy Scout 성격의 역할이 `가문 / 부족 / 길드` 결손층을 먼저 본다.
6. Faction Cartographer 또는 Hero Curator가 구조를 분석한다.
7. House and Lineage Auditor, Clan and Tribe Auditor, Guild and Economy Auditor가 중간 사회 단위를 세분화해서 본다.
8. Relationship Mapper가 인간 관계 관점에서 재평가한다.
9. Plausibility Judge가 개연성 판정을 내린다.
10. Index Auditor가 링크와 분류 정리를 맡는다.
11. Legacy Surgeon이 레거시를 분리한다.
12. Report Clerk가 보고서를 남긴다.

## 병렬 운용

- Conductor는 필요할 때 역할을 더 세분화해서 같은 배치를 병렬 조사한다.
- 현재 기본 분할은 `Continent Adequacy Scout`, `Faction Cartographer`, `House and Lineage Auditor`, `Clan and Tribe Auditor`, `Guild and Economy Auditor`, `Hero Curator`다.
- 병렬 역할은 증거 수집과 1차 판단만 하고, 최종 우선순위와 정본 판단은 Conductor가 통합한다.
- 어떤 역할을 먼저 부를지는 `orchestra/REQUIRED_EXPERT_ROSTER_LOCK.md`를 기본 roster로 쓴다.

## 오케스트라 고정 원칙

- 병렬 운용의 목표는 `더 많이 부르기`가 아니라 `더 빨리 분리해서 더 늦게 섞지 않기`다.
- 같은 파일을 여러 역할이 동시에 수정하지 않는다.
- 같은 대상을 여러 역할이 읽더라도, 서로 다른 질문만 맡긴다.
- Conductor는 항상 마지막에 `판정 통합 -> 문서 반영 -> 다음 작업선 고정` 순서로 끝낸다.

## 실행 하네스

- 기본 실행층은 `MCP -> Skills -> Agents -> Hooks -> Registers -> Conductor final integration -> Next Workstream lock`이다.
- `MCP`는 조회와 문맥 수집을 맡고, 정본 판단은 하지 않는다.
- `Skills`는 반복 절차와 출력 형식을 고정하고, 정책 변경은 하지 않는다.
- `Agents`는 병렬 진단과 제안을 맡고, 최종 반영은 하지 않는다.
- `Hooks`는 전환 누락 방지용 검사/기록 층이다.
- `Registers`는 판정과 상태 이동의 장기 기억 장부다.
- 세부 기준은 `orchestra/EXECUTION_HARNESS_LOCK.md`를 따른다.
- `Agents`에 들어가기 전, 해당 배치의 필수 전문가 묶음은 `orchestra/REQUIRED_EXPERT_ROSTER_LOCK.md`에서 먼저 고른다.

## 필수 전문가 잠금

- 오케스트라는 배치마다 전문가를 새로 발명하지 않는다.
- `정본 / 엔진 / 구조 / 사회단위 / 경계 / 종족 / 집필` 축의 기본 전문가 roster는 고정한다.
- 세부 목록과 expert matrix는 `orchestra/REQUIRED_EXPERT_ROSTER_LOCK.md`를 따른다.

## 분량 게이트

- 분량은 하네스 구조에서 최상위 핵심 검사다.
- `1화마다` 무조건 분량 체크를 건다.
- 분량 미달은 `보완 가능`이 아니라 `실패`로 본다.
- 분량이 기준에 못 미치면 해당 화는 무조건 재작성으로 돌린다.
- 이 규칙은 나중 집필엔진에도 그대로 승계한다.

## Model Route

- `서사 개연성`, `감정선`, `세계관 철학`, `확장 억제`, `무엇이 더 작품다운가` 같은 판단은 ChatGPT-first 검토를 우선한다.
- `queue`, `register`, `crosswalk`, `index`, `naming normalization`, `branch/commit/push`는 Codex-first로 처리한다.
- 애매하면 `ChatGPT형 판단 메모 -> Codex evidence 수집/반영` 또는 `Codex evidence bundle -> ChatGPT형 판정 -> Codex 반영`의 hybrid route를 쓴다.
- 세부 기준은 `orchestra/MODEL_ROLE_SPLIT_LOCK.md`를 따른다.

## 언제 병렬 분할을 켜는가

아래 중 둘 이상이 걸리면 오케스트라 분할을 우선한다.

- `대륙 spine`과 `엔진 장부`를 같이 건드린다.
- `People Worth Seeking`, `Operational Lines`, `Place Register`가 같이 엮인다.
- 상태 라벨 변경과 이름 톤 조정이 동시에 필요하다.
- 다음 작업선까지 바로 정해야 한다.

## 기대 이점

- 조사 속도: 긴 문서를 역할별로 쪼개 병렬 진단한다.
- 판단 품질: 라우팅, 톤, 장소 기능, 관계 충돌을 초기에 분리한다.
- 운영 안정성: 최종 반영 권한을 Conductor 하나로 묶어 문서 drift를 줄인다.
- 회수 용이성: 배치 기록과 역할 산출물이 남아 다음 턴 이어받기가 쉬워진다.

## FS Engine Routing

- 세계관, 대륙, 세력, 인물, 관계망, 아이템, 지도는 모두 같은 방식으로 읽지 않는다.
- 각 단계는 `workflow/11_FS_Engine.md`의 엔진 층을 따라 먼저 볼 관점을 고른다.
- 작법 이론은 참고자료가 아니라 실제 판단 순서의 일부다.
- 필수 코어 합의안은 `audit/FS_Engine_Core_Consensus.md`를 우선 참고한다.
- 작법 층과 운영 층의 실제 연결은 `audit/FS_Engine_Writing_Craft_Map.md`를 함께 본다.

## 현재 병렬 운용

- `ACTIVE_AGENT_SPLIT.md`에 현재 배치의 분업을 적는다.
- 실제 서브에이전트를 띄운 경우 `AGENT_DISPATCH_LOG.md`에 배치 기록을 남긴다.
- 병렬 에이전트는 읽기와 진단만 맡고, 최종 반영은 Conductor가 한다.
- 같은 파일을 동시에 편집하지 않는다.

## 장기 섹션 우선순위

### 초기 build 순서

- `8. 세력 아카이브` 루트 구조
- `14. 인물 백과` 루트 구조

### 중간 build 순서

- `8번`의 대륙별 세력 루트
- `14번`의 성장 영웅과 세력 연결

### 후반 build 순서

## Mainline Note Reference

현재 active mainline은 위 장기 순서를 다시 밟는 것이 아니라,
`audit/Continuous_Workstream.md`,
`audit/Next_Sequential_Workstream.md`,
`audit/Audit_Queue.md`에 적힌
`closure sync / Section 8 -> 15 watch-reference`
기준을 따른다.

- 문화, 경제, 예술, 생활상 세부 문서
- 인물의 장비, 세부 이력, 확장 전승

## 중단 조건

- 동일 대상에 정본 후보가 2개 이상인 경우
- 레거시와 현행 구조가 동시에 유효한 경우
- 관계 정의가 작품 철학과 충돌하는 경우

이 경우는 수정 대신 `audit/Open_Questions.md`에 남긴다.

## 기본 명령

```powershell
python scripts/export_reference_manifest.py `
  --name factions `
  --source "X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)" `
  --output "reference/manifests/factions_manifest.md"

python scripts/export_reference_manifest.py `
  --name heroes `
  --source "X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)" `
  --output "reference/manifests/heroes_manifest.md"

python scripts/audit_lore_tree.py `
  --section factions "X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-8. 세력 아카이브 (국가·조직 정리)" `
  --section heroes "X:\theforgottensummoner\THE FORGOTTEN SUMMONER\01. 아스트라리스 크로니클\01-14. 영웅 백과 (Hero Archive)" `
  --output "audit/reports/initial_inventory.md"
```

## 안전 규칙

- 원본 경로에서 `move`, `rename`, `delete`, `git add`, `git commit`를 하지 않는다.
- 원본 내용을 가져와야 할 때는 `reference/` 또는 `working/` 아래로만 복사한다.
- 원본 정리는 아이디어와 계획으로만 남기고, 실제 적용은 별도 승인 없이는 하지 않는다.

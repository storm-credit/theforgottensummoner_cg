# Race Species First Pass

이 문서는 종족 사이드트랙의 1차 판정 메모다.

이 단계에서는 `정본 확정`이 아니라
어떤 축이 강하고 어떤 축이 아직 얇은지 압축해서 본다.

## Strong Signals

### 1. 수인/야수인계는 강하다

- `정령연합`은 단일 종족국이 아니라 혼성 연합이지만,
  그 안의 `수인 부족`, `부족 영역`, `수인족 자치`는 분명한 people-scale 구조다.
- `그린스톰 부족`은 늑대수인, 곰수인, 여우수인과 자치권을 직접 말하므로
  `species + tribal polity` 신호가 강하다.

판정:

- `수인/야수인계`: `strong`
- `정령연합 전체`: `composite polity`, not a race

## Strong but Not Pure Species

### 2. 용계는 bloodline 쪽이 더 강하다

- `용의 후예`는 강한 조직/부족 축이지만,
  내부 서술은 `Dragonborn`, `용혈`, `반룡`, `용의 피`처럼 heritage 언어가 반복된다.

판정:

- `용계/비늘계`: `strong as bloodline/heritage`
- `독립 순혈 종족국`: `not yet proven`

### 3. 언데드는 state 기반 사회다

- `망자의 왕국`은 왕국, 군단, 계층, 정치 구조가 강하다.
- 하지만 그 기반은 기본 people-category라기보다 죽음 이후 상태/질서다.

판정:

- `언데드`: `strong as state/transformation`
- `독립 biological species`: `do_not_promote_yet`

## Medium Signals

### 4. 엘프/장생종은 개별 앵커는 강하지만 전역 표는 아직 없다

- `엘다라`의 `하이엘프`는 강한 개별 사례다.
- `정령연합` import에서도 숲 엘프, 하프엘프가 보인다.

판정:

- `엘프/장생종`: `medium`
- `대륙 공통 분포`: `not yet generalized`

### 5. 드워프는 반복되지만 아직 slot-bound 성격이 크다

- 프로스트와 에테르 import에 드워프 장인/전우 사례가 반복된다.
- 다만 아직 드워프 사회 전체를 정리한 정본 축은 없다.

판정:

- `드워프/장인종`: `medium`
- `독립 대륙권`: `not yet generalized`

## Thin or Reserved

### 6. 해양 종은 있다, 하지만 수중 문명은 아직 얇다

- 인어/merfolk, 바다 뱀, 수중 전력 신호는 보인다.
- `세레니아`에는 `인어의 쉼터`, `인어 공주`, `이종족 대표`가 보이고,
  `물의 정령 기사단`에는 인어 전사와 심해 순찰대가 직접 편제된다.
- 그러나 현재 문서 상태만으로는 `독립 해양 문명권`을 강하게 잠그기 어렵다.

판정:

- `수중/해양계`: `reserved_family with localized enclave signal`

### 7. 하피는 아직 몬스터/변이 쪽이 우세하다

- 현재까지 잡힌 하피 신호는 뮤턴트, 사이렌형, 이벤트성 개체 위주다.
- 공동체/언어/자치권 근거는 약하다.

판정:

- `하피/조익계`: `thin -> monster first`

### 8. 라미아/나가는 아직 근거가 부족하다

- `라미아`, `메두사`, `고르곤`, `serpentfolk` 계열은 안정적인 사회 구조 증거가 아직 없다.
- 현재 explicit humanoid-serpent 신호는 암약 조직 내부의 `나가족(반인반사)` 단일 개체 1건이 전부다.

판정:

- `라미아`: `open question`
- `나가`: `single-character signal only`

### 9. 거인, 요정, 오크는 존재 신호는 있으나 peoplehood 강도는 제각각이다

- `거인`은 고대 유해, 위협 개체, 전장 신화로는 반복되지만 현존 공동체 증거는 약하다.
- `요정`은 포획 대상과 자원 문맥도 많지만, `정령연합` 내부에서는 공동체/피난처/평의/정치 질서에 연결되는 사례가 반복된다.
- `오크 부락`은 people signal이 있으나 구조 설명이 아직 얇고, 전장 맥락이 우세하다.
- `고블린`은 오크보다 더 약하며, 현재는 `고블린혼혈` 같은 통합/혼혈 신호만 있고 독립 부족/정체/사회 구조는 안 보인다.

판정:

- `거인계`: `thin -> mythic/threat first`
- `요정계`: `composite_signal -> ally/community in Ether, hold globally`
- `오크`: `thin people signal`
- `고블린`: `integration/bloodline signal only`

## First Working Rule

당분간은 아래 순서를 고정한다.

1. 먼저 `species / bloodline / state / monster`를 가른다.
2. 그 다음에만 `왕국`, `부족`, `연합`, `길드` 같은 사회 앵커를 붙인다.
3. 사회 앵커가 있다고 바로 종족으로 읽지 않는다.
4. `하피`, `라미아`, `수중 문명`, `용인 순혈`, `거인족`은 `reserved` 또는 `open question`으로 유지한다.

## Next Read-Only Targets

- `해양` 문서에서 merfolk/sea-native civilization 증거가 실제로 얼마나 반복되는지 점검
- `오벨리스크` import에서 언데드 내부 계층이 `state`를 넘는 peoplehood를 갖는지 점검
- `요정`의 `정령연합 내부 공동체`가 전역 standalone species dossier로 확장 가능한지 점검
- `오크`, `고블린`, `라미아`, `나가`의 안정적 공동체 근거가 실제로 있는지 점검

# Species Framework Risk Register

이 문서는 종족 프레임을 도입할 때
어디서 세계관이 꼬일 수 있는지 미리 잠그는 리스크 장부다.

이 단계는 `해결`이 아니라 `금지선과 보류선`을 먼저 적는 단계다.

## Primary Risks

| Risk | Why It Is Dangerous | Current Signal | Handling Rule |
|---|---|---|---|
| `종족 vs 혈통 혼선` | 혼혈/계보를 독립 종족처럼 읽으면 가문/후계 문서가 무너진다 | `혈통`, `계보`, `후계`가 이미 별도 신호로 존재 | 기본값은 `bloodline/lineage` |
| `종족 vs 상태 혼선` | 언데드, 정령화, 저주 변이를 종족화하면 오벨리스크/봉인/심연 축이 재분류된다 | `정령화`, `언데드`, `변이` 계열 사례 다수 | 기본값은 `state/transformation` |
| `종족 vs 몬스터 혼선` | 하피, 라미아, 정령 개체, 거인, 괴수를 무조건 문명종으로 올리면 생태 문서가 흔들린다 | import층에 야생/사냥/재료 신호가 많다 | 사회 구조 없으면 `monster/ecological` |
| `대륙 전체 과대표` | 몇 사례만 보고 대륙 전체를 엘프권/드워프권으로 확정하면 세력 spine이 손상된다 | `엘다라`, `드워프 장인`, `수인 부족`은 모두 부분 사례다 | 개별 앵커만 인정, 대륙 일반화 금지 |
| `정령연합 오독` | 정령연합을 곧바로 정령 종족 국가로 읽으면 공동체/계약/부족층이 섞인다 | `Spirit Union`, `수인 부족`, `정령 계약`이 함께 나온다 | faction, contract, people을 분리 |
| `해양 종 성급 확정` | 바닷속 문명을 너무 빨리 정본화하면 해양 대륙의 기존 슬롯/항만 구조가 바뀐다 | 현재는 가능성만 높고 공식 표는 없다 | `reserved_family`로만 유지 |
| `하피/라미아 일괄 분류` | 판타지 전통상 몬스터와 문명종 양쪽 모두 가능하다 | 현재 직접 정본 근거 부족 | 개별 사례 전엔 `reserved_family` |

## Do Not Promote Yet

아래 항목은 이름만 보고 바로 `종족`으로 승격하지 않는다.

| Item | Default Reading | Reason |
|---|---|---|
| `언데드` | `state/transformation` | 죽음/부활/사령술 상태일 가능성이 더 큼 |
| `정령화` | `state/transformation` | 신체/영혼 변질 상태일 가능성이 큼 |
| `용의 피` | `bloodline/lineage` | 가문/혈통 신호에 더 가깝다 |
| `하프 엘프` | `bloodline/lineage` | 혼혈 분기선이므로 독립 종족화 금지 |
| `저주받은 하피/라미아` | `state` 또는 `monster` | 사회 구조가 없으면 종족 아님 |
| `야생 정령 개체` | `monster/ecological` 또는 `entity` | 공동체보다 자연 개체 신호가 강함 |

## Anchor Cases To Check First

- `엘다라`의 `하이엘프` 신호
- `푸른 폭풍 요새`의 `드워프 장인` 슬롯
- `정령연합`의 `수인 부족` 신호
- `오벨리스크` import층의 `언데드`와 `거인` 신화
- `해양` 문서에서 수중 문명/해양 적응 공동체가 있는지 여부

## Parallel Operation Rule

- 이 register는 메인 `14/15` workstream을 덮어쓰지 않는다.
- 메인선은 그대로 유지하고, 종족 쪽은 `parallel audit`로만 기록한다.
- 사례가 충분히 쌓이기 전에는 `OPEN INDEX`와 `workstream`에 side-track으로만 연결한다.

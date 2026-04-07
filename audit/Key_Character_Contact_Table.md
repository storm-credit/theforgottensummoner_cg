# Key Character Contact Table

이 문서는 핵심 인물들이 누구와 어떻게 얽히는지를
`관계 타입`, `세력 앵커`, `현재 상태`, `미래 가능성` 기준으로 정리하는 작업 시트다.

현재는 틀과 시드 행만 먼저 잡는다.

## Columns

| Character | Primary Anchor | Contact / Target | Relationship Type | Current Layer | Evidence Mode | Notes |
|---|---|---|---|---|---|---|

### Column Rules

- `Character`: 인물명
- `Primary Anchor`: 국가/가문/길드/협회/정보망/범대륙 조직 등 1차 소속
- `Contact / Target`: 관계 상대 또는 세력
- `Relationship Type`: `ally`, `former_ally`, `rival`, `enemy`, `rumor_only`, `crossed_paths`, `past_only`, `future_only`, `asymmetric_awareness`, `same_side_different_front`, `intermittent_alignment`
- `Current Layer`: 현재 서사 층위. 예: `direct`, `indirect`, `rumor`, `structural`
- `Evidence Mode`: 어떤 근거에서 이 접점이 보이는지. 예: `folder anchor`, `inline reference`, `orphan note`, `soft canon`
- `Notes`: 현재 판단 메모

## Seed Rows

| Character | Primary Anchor | Contact / Target | Relationship Type | Current Layer | Evidence Mode | Notes |
|---|---|---|---|---|---|---|
| `이리나 폰 루즈` | `그림자 첩보망` | `대륙 전역 정보망` | `same_side_different_front` | `structural` | `orphan note` | 직접 상대가 아직 비어 있지만, 정보망 중심 인물 후보로 읽힌다. |
| `칼리크 디트리히` | `철의 금융 연맹` | `대륙 무역 연맹` | `intermittent_alignment` | `indirect` | `orphan note` | 거래와 배신 구조에 묶인 인물로 읽히며, `침묵의 상회`와도 충돌 후보가 있다. |
| `칼리크 디트리히` | `철의 금융 연맹` | `그림자 첩보망` | `asymmetric_awareness` | `indirect` | `orphan note` | 감시 대상이거나 공모 대상일 수 있어 후속 확인 필요. |
| `에테르 영웅군` | `성국 / 왕국연합 / 자유도시연합 / 마법협회 / 정령 연합` | `국제 길드 연합` | `same_side_different_front` | `structural` | `inline reference` | 많은 인물 문서가 자격과 유통 규정을 이 축에 연결하고 있다. |
| `에테르 영웅군` | `각 대륙 세력 앵커` | `대륙 무역 연맹` | `crossed_paths` | `indirect` | `inline reference` | 직접 소속은 아니어도 거래, 후원, 유통 라인으로 반복 연결된다. |
| `에테르 영웅군` | `각 대륙 세력 앵커` | `그림자 첩보망` | `asymmetric_awareness` | `indirect` | `inline reference` | 상당수 문서가 관측/추적/암살률 구조와 연결된다. |
| `에테르 영웅군` | `각 대륙 세력 앵커` | `마도 공학 대공방 연합` | `same_side_different_front` | `indirect` | `inline reference` | 장비/특허/양산 체계와 연결되는 경우가 반복된다. |
| `레오니스 발레리우스` | `성국 (Saint Haven)` | `국제 길드 연합` | `same_side_different_front` | `structural` | `inline reference` | 자격과 유통 등급이 이 규정망 아래 관리된다고 직접 적혀 있다. |
| `레오니스 발레리우스` | `성국 (Saint Haven)` | `대륙 무역 연맹` | `intermittent_alignment` | `indirect` | `inline reference` | 직접 소속은 아니지만 유통권, 매점매석, 채무 구조와 결탁된다고 서술된다. |
| `레오니스 발레리우스` | `성국 (Saint Haven)` | `철의 금융 연맹` | `intermittent_alignment` | `indirect` | `inline reference` | 금융 지배 구조와 결탁되어 있다는 매크로 엔진 문구가 반복된다. |
| `레오니스 발레리우스` | `성국 (Saint Haven)` | `그림자 첩보망` | `asymmetric_awareness` | `indirect` | `inline reference` | 대륙 전역의 은폐 정보망 아래 귀속된다고 적혀 있어 감시/추적 대상 축이 강하다. |
| `레오니스 발레리우스` | `성국 (Saint Haven)` | `베네딕투스 테르시오` | `rival` | `direct` | `relationship block` | 성국 내부 온건파와 강경파의 교리 충돌이 직접 서술된다. |
| `레오니스 발레리우스` | `성국 (Saint Haven)` | `가브리엘 솔그리드` | `ally` | `direct` | `relationship block` | 폭주를 제어할 수 있는 유일한 무력 심복으로 적혀 있다. |
| `레오니스 발레리우스` | `성국 (Saint Haven)` | `제이더 블랙윈드` | `intermittent_alignment` | `direct` | `relationship block` | 몰살 욕망과 협상 필요가 동시에 존재하는 굴욕적 외교 관계다. |
| `레온하르트 카멜로스` | `왕국연합 (Allied Kingdoms)` | `국제 길드 연합` | `same_side_different_front` | `structural` | `inline reference` | 합법 관리와 등급 규정이 이 축에 연결된다. |
| `레온하르트 카멜로스` | `왕국연합 (Allied Kingdoms)` | `초국가 진리 연합 및 마탑` | `rival` | `indirect` | `inline reference` | 라이센스/학술 통제 구조가 왕권과 대립 축으로 서술된다. |
| `레온하르트 카멜로스` | `왕국연합 (Allied Kingdoms)` | `그림자 첩보망` | `asymmetric_awareness` | `indirect` | `inline reference` | 정보망 귀속 서술이 반복되어 감시 대상 축으로 읽힌다. |
| `레온하르트 카멜로스` | `왕국연합 (Allied Kingdoms)` | `제라르드 파브리스` | `ally` | `direct` | `relationship block` | 혐오와 의존이 공존하는 전략 파트너 관계다. |
| `레온하르트 카멜로스` | `왕국연합 (Allied Kingdoms)` | `도미닉 레가스` | `ally` | `direct` | `relationship block` | 차기 계승자 겸 칼집으로 아끼는 군사적 후계 축이다. |
| `레온하르트 카멜로스` | `왕국연합 (Allied Kingdoms)` | `레오니스 발레리우스` | `enemy` | `direct` | `relationship block` | 외교 회담에서 밥상을 엎을 정도의 철천지원수 라이벌로 적힌다. |
| `제이더 아테르` | `자유도시연합 (Crossroad Cities)` | `대륙 용병단` | `same_side_different_front` | `indirect` | `inline reference` | 청부와 외주 무력 생태계에 직간접 연결된다고 직접 나온다. |
| `제이더 아테르` | `자유도시연합 (Crossroad Cities)` | `대륙 무역 연맹` | `intermittent_alignment` | `indirect` | `inline reference` | 용병 의뢰와 자본을 통제하는 흑막으로 연결된다. |
| `제이더 아테르` | `자유도시연합 (Crossroad Cities)` | `국제 길드 연합` | `same_side_different_front` | `indirect` | `inline reference` | 자격/유통/등급이 이 시스템 아래 관리된다고 적혀 있다. |
| `제이더 아테르` | `자유도시연합 (Crossroad Cities)` | `그림자 첩보망` | `asymmetric_awareness` | `indirect` | `inline reference` | 은폐 정보망 귀속 서술이 직접 반복된다. |
| `제이더 아테르` | `자유도시연합 (Crossroad Cities)` | `베아트리스 녹튜아` | `rival` | `direct` | `relationship block` | 같은 그림자 계열이지만 서로를 혐오하는 암살자 대립축이다. |
| `제이더 아테르` | `자유도시연합 (Crossroad Cities)` | `칼렌 노이르` | `ally` | `direct` | `relationship block` | 정보는 칼렌, 처형은 제이더라는 비즈니스 파트너 관계다. |
| `제레시스 아르카디아` | `마법협회 (Arcane Society)` | `국제 길드 연합` | `same_side_different_front` | `indirect` | `inline reference` | 협회 소속 영웅도 규정망 아래 관리된다는 패턴을 공유한다. |
| `제레시스 아르카디아` | `마법협회 (Arcane Society)` | `초국가 진리 연합 및 마탑` | `ally` | `indirect` | `inline reference` | 학술 통제와 금서 규정의 핵심 수혜/강제 주체로 읽힌다. |
| `제레시스 아르카디아` | `마법협회 (Arcane Society)` | `크세노스 아르카디아` | `intermittent_alignment` | `direct` | `relationship block` | 혈통/후계/폭탄 각인이 함께 묶인 불신형 동맹이다. |
| `제레시스 아르카디아` | `마법협회 (Arcane Society)` | `마르쿠스 코르부스` | `intermittent_alignment` | `direct` | `relationship block` | 가장 강력한 체스말이지만 언제든 숙청할 수 있는 불안정한 충성축이다. |
| `실바리온 엘도라` | `정령 연합 (Spirit Union)` | `초국가 진리 연합 및 마탑` | `rival` | `indirect` | `inline reference` | 라이센스, 금서, 학술 통제 구조와 긴장 상태가 반복된다. |
| `실바리온 엘도라` | `정령 연합 (Spirit Union)` | `마도 공학 대공방 연합` | `same_side_different_front` | `indirect` | `inline reference` | 생산과 특허 구조에 걸리지만 정령 연합 결은 분명히 다르다. |
| `실바리온 엘도라` | `정령 연합 (Spirit Union)` | `그림자 첩보망` | `asymmetric_awareness` | `indirect` | `inline reference` | 관측/암살률 구조 아래 귀속된다는 문구가 반복된다. |
| `실바리온 엘도라` | `정령 연합 (Spirit Union)` | `아이샤 제피리스` | `ally` | `direct` | `relationship block` | 눈과 귀로 쓰는 적극 후원 관계다. |
| `실바리온 엘도라` | `정령 연합 (Spirit Union)` | `카엘라 테라니스` | `ally` | `direct` | `relationship block` | 생태계와 대지를 묶는 전장 듀오 관계다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `대륙 무역 연맹` | `same_side_different_front` | `structural` | `inline reference` | 자유도시 경제와 외교를 쥔 인물이라 상단/교역축과 구조적으로 겹친다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `철의 금융 연맹` | `intermittent_alignment` | `indirect` | `inline reference` | 채권, 전비, 협상 압박 구조와 간접 연결된다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `그림자 첩보망` | `asymmetric_awareness` | `indirect` | `inline reference` | 외교 기밀과 감청 위험 때문에 관측 대상으로 읽힌다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `레이나 브라이트헤븐` | `ally` | `direct` | `faction document` | 공식 경매장과 비공식 외교 채널을 함께 떠받치는 실무 축이다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `이사벨 카르도` | `ally` | `direct` | `faction document` | 외교와 물류가 서로를 떠받치는 자유도시 실무 동맹으로 읽힌다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `모이라 와일드웨이브` | `intermittent_alignment` | `indirect` | `organization mesh` | 합법 상업권과 밀수 중개망이 부딪히면서도 필요할 때는 거래할 가능성이 높다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `벤투라 모레티` | `intermittent_alignment` | `indirect` | `organization mesh` | 표면 아래의 익명 거래 질서를 필요할 때 활용하거나 견제할 축이다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `도미닉 발사노` | `enemy` | `indirect` | `organization mesh` | 도시의 합법 질서를 좀먹는 폭력 회수망이라 충돌 가능성이 높다. |
| `세실리아 메르카토르` | `자유도시연합 (Crossroad Cities)` | `로렌조 카르미네` | `enemy` | `indirect` | `organization mesh` | 인신매매와 노예 거래는 자유도시의 공적 얼굴과 정면 충돌한다. |

## First Pass Judgment

- 현재 핵심 접점은 `인물 대 인물`보다 `인물 대 조직망`에서 먼저 많이 드러난다.
- 즉 이 작품의 관계망 표는 처음부터 전부 1:1 감정선으로만 짜기보다,
  `조직망 접점 -> 개별 인물 접점` 순서로 확장하는 편이 더 안정적이다.

## Next Use

1. `14번` 핵심 인물 요약을 만들 때 이 표를 먼저 채운다.
2. `15번` 후보 인물을 회수할 때도 이 표의 `Primary Anchor`를 참조한다.
3. 나중에 액트별 관계 전환표를 만들 때 이 표를 기반으로 분기한다.
4. 같은 인물이 여러 범대륙 조직망에 반복 연결될 경우 `정상 분산`인지 `과설계 잔재`인지 별도 판정한다.
5. `자유도시연합`처럼 인간층이 풍부한 구역은 `세실리아 -> 상단/밀수/운송` 순서로 `15번` 후보를 회수한다.

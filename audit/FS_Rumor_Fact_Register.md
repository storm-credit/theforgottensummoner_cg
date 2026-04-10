# FS Rumor / Fact Register

이 문서는 소문과 사실을 분리해서 관리하는 장부다.

아스트라리스는 인물이 직접 만나지 않아도
소문만 들었거나,
잘못 알고 있거나,
미래/과거의 정보가 비대칭으로 얽힐 수 있는 구조다.

따라서 소문은 버릴 것이 아니라
정본과 분리해서 관리해야 한다.

## Information States

### `fact`

정본 사실.

- 상위 캐논과 충돌하지 않는다.
- 오케스트라가 실제 근거를 확인했다.

### `rumor`

작중 인물이나 대중에게 떠도는 말.

- 사실일 수도 있고 아닐 수도 있다.
- 소문을 들은 인물의 행동을 유발할 수 있다.

### `misread`

사실을 잘못 해석한 정보.

- 음모, 오해, 정치 선전, 종교 해석과 잘 맞는다.

### `forgery_claim`

진품/가품 논쟁.

- 아이템, 보물, 도감, 감정사, 경매장과 연결한다.

### `suppressed_record`

의도적으로 감춰진 기록.

- 세력의 금기, 실패한 실험, 몰락 왕가, 금서와 연결한다.

### `propaganda`

세력이 밖으로 내세우는 이야기.

- 완전한 거짓일 수도 있고 부분 진실일 수도 있다.

## Rumor Questions

소문을 등록할 때 묻는다.

1. 누가 처음 퍼뜨렸는가?
2. 누가 이 소문을 믿는가?
3. 누가 이 소문으로 이익을 보는가?
4. 실제 사실과 어느 부분이 다른가?
5. 어떤 인물 관계를 바꾸는가?
6. 회수될 복선인가, 분위기용 소문인가?

## Seed Entry Snapshot

| Rumor / Claim | State | Related Track |
|---|---|---|
| 어떤 보물은 멸실되었다는 도감 기록 | `rumor`, `forgery_claim` | 아이템 백과 / 경매장 |
| 검은 경매소의 진품 목록 | `suppressed_record` | 장물 감정 / 자산 장부 |
| 키르케 영약회의 약효 소문 | `rumor`, `misread` | 연금술 / 영약 |
| 자유도시 인물들의 영웅식 평판 | `rumor` | 14/15 검증 |
| 봉인 수호단의 공식 희생담 | `propaganda`, `public_legend` | 오벨리스크 / 기관 기억 |
| 네크로 우물 연락망 | `rumor`, `suppressed_record` | 사령 통신 / 음지 도시망 |

## Link Rule

- 사실로 확정할 때는 `FS_Canon_Tier_Register.md`와 연결한다.
- 관계 변화를 만들면 `FS_Relationship_Ledger.md`와 연결한다.
- 복선이면 `FS_Foreshadow_Payoff_Register.md`와 연결한다.

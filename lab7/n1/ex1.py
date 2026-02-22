from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

def main():
    with open(_path("n1/input.txt"), "rb") as f:
        data = f.read().split()

    money = int(data[0])
    k = int(data[1])
    coins = list(map(int, data[2:2 + k]))

    INF = 10**9
    dp = [INF] * (money + 1)
    dp[0] = 0

    # DPChange(money, coins) из лекции
    for m in range(1, money + 1):
        best = INF
        for c in coins:
            if m >= c:
                cand = dp[m - c] + 1
                if cand < best:
                    best = cand
        dp[m] = best

    with open(_path("n1/output.txt"), "w", encoding="utf-8") as f:
        f.write(str(dp[money]))


if __name__ == "__main__":
    main()
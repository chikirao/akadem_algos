from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

from array import array


def main():
    with open(_path("n2/input.txt"), "rb") as f:
        data = f.read().split()

    n = int(data[0])

    dp = array("I", [0]) * (n + 1) # dp[i] - минимум операций до i
    prev = array("I", [0]) * (n + 1) # prev[i] - откуда пришли в i

    for i in range(2, n + 1):
        best = dp[i - 1] + 1
        p = i - 1

        if i % 2 == 0:
            cand = dp[i // 2] + 1
            if cand < best:
                best = cand
                p = i // 2

        if i % 3 == 0:
            cand = dp[i // 3] + 1
            if cand < best:
                best = cand
                p = i // 3

        dp[i] = best
        prev[i] = p

    seq = []
    cur = n
    while True:
        seq.append(cur)
        if cur == 1:
            break
        cur = prev[cur]

    seq.reverse()

    out = [str(len(seq) - 1), " ".join(map(str, seq))]
    with open(_path("n2/output.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()
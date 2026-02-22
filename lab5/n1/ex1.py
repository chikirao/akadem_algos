from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

def sift_down(a, i, n, swaps):
    while True:
        min_i = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and a[l] < a[min_i]:
            min_i = l
        if r < n and a[r] < a[min_i]:
            min_i = r

        if min_i == i:
            break

        a[i], a[min_i] = a[min_i], a[i]
        swaps.append((i, min_i))
        i = min_i


def main():
    with open(_path("n1/input.txt"), "rb") as f:
        data = f.read().split()

    n = int(data[0])
    a = list(map(int, data[1:1 + n]))

    swaps = []
    for i in range(n // 2 - 1, -1, -1):
        sift_down(a, i, n, swaps)

    out_lines = [str(len(swaps))]
    out_lines.extend(f"{i} {j}" for i, j in swaps)

    with open(_path("n1/output.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(out_lines))


if __name__ == "__main__":
    main()
from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

import random

n = 3000
low = -10**9
high = 10**9

a = [random.randint(low, high) for _ in range(n)]

with open(_path("n3/input.txt"), "w", encoding="utf-8") as f:
    f.write(str(n) + "\n")
    f.write(" ".join(map(str, a)) + "\n")
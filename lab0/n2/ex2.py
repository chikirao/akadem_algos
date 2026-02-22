from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

with open(_path("n2/input.txt"), "r", encoding="utf-8") as f:
    n = int(f.read().strip())

with open(_path("n2/output.txt"), "w", encoding="utf-8") as f:
    f.write(str(fib(n)))
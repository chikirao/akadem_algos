from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

# Задача 1
print("Введите значения для суммы 1:")
a, b = map(int, input().split())
print(f"\n{a + b}\n")

# Задача 2
print("Введите значения для суммы 2:\n")
a, b = map(int, input().split())
print(f"\n{a + b * b}\n")

# Задача 3
with open(_path("input.txt"), "r", encoding="utf-8") as f:
    a, b = map(int, f.read().split())

with open(_path("output.txt"), "w", encoding="utf-8") as f:
    f.write(str(a + b))

print("Результат суммы файла 1 посчитан.")

# Задача 4
with open(_path("input2.txt"), "r", encoding="utf-8") as f:
    a, b = map(int, f.read().split())

with open(_path("output2.txt"), "w", encoding="utf-8") as f:
    f.write(str(a + b * b))

print("Результат суммы файла 2 посчитан.")

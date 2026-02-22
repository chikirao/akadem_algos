from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

def merge(left, right):
    i = 0
    j = 0
    res = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])
    return res


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


with open(_path("n1/input_worst.txt"), "r", encoding="utf-8") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

sorted_a = merge_sort(a)

with open(_path("n1/output2.txt"), "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, sorted_a)))

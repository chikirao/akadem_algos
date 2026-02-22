from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

def find_max_crossing_subarray(A, low, mid, high):

    left_sum = -10**30
    s = 0
    max_left = mid
    for i in range(mid, low - 1, -1):
        s += A[i]
        if s > left_sum:
            left_sum = s
            max_left = i

    right_sum = -10**30
    s = 0
    max_right = mid + 1
    for j in range(mid + 1, high + 1):
        s += A[j]
        if s > right_sum:
            right_sum = s
            max_right = j

    return max_left, max_right, left_sum + right_sum


def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]

    mid = (low + high) // 2

    left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)
    right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum


with open(_path("n3/input.txt"), "r", encoding="utf-8") as f:
    n = int(f.readline())
    A = list(map(int, f.readline().split()))

_, _, ans = find_maximum_subarray(A, 0, n - 1)

with open(_path("n3/output.txt"), "w", encoding="utf-8") as f:
    f.write(str(ans))
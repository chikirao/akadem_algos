import random
import sys

sys.setrecursionlimit(1_000_000)

def partition3(a, l, r):
    x = a[l]
    lt = l # граница < x
    i = l # текущий
    gt = r # граница > x

    while i <= gt:
        if a[i] < x:
            a[lt], a[i] = a[i], a[lt]
            lt += 1
            i += 1
        elif a[i] > x:
            a[i], a[gt] = a[gt], a[i]
            gt -= 1
        else:
            i += 1

    # итог:
    # a[l..lt-1] < x
    # a[lt..gt] = x
    # a[gt+1..r] > x
    return lt, gt

def randomized_quicksort3(a, l, r):
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m1, m2 = partition3(a, l, r)
        randomized_quicksort3(a, l, m1 - 1)
        randomized_quicksort3(a, m2 + 1, r)

def main():
    with open("n1/input_worst.txt", "r", encoding="utf-8") as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))

    randomized_quicksort3(a, 0, n - 1)

    with open("n1/output2_worst.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, a)))

if __name__ == "__main__":
    main()
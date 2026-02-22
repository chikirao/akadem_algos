import random
import sys

sys.setrecursionlimit(1_000_000)

def partition(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[j], a[i] = a[i], a[j]
    a[l], a[j] = a[j], a[l]
    return j

def randomized_quicksort(a, l, r):
    if l < r:
        k = random.randint(l, r)
        a[l], a[k] = a[k], a[l]
        m = partition(a, l, r)
        randomized_quicksort(a, l, m - 1)
        randomized_quicksort(a, m + 1, r)

def main():
    with open("n1/input_worst.txt", "r", encoding="utf-8") as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))

    randomized_quicksort(a, 0, n - 1)

    with open("n1/output1_worst.txt", "w", encoding="utf-8") as f:
        f.write(" ".join(map(str, a)))

if __name__ == "__main__":
    main()
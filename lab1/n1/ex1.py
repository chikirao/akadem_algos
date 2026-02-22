def insertion_sort(a, n):
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


with open("n1/input.txt", "r", encoding="utf-8") as f:
    n = int(f.readline())
    a = list(map(int, f.readline().split()))

insertion_sort(a, n)

with open("n1/output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(map(str, a)))

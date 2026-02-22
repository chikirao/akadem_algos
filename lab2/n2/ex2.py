def binary_search(a, x):
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        if a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1


with open("n2/input.txt", "r", encoding="utf-8") as f:
    data = list(map(int, f.read().split()))

n = data[0]
a = data[1:1 + n]
k = data[1 + n]
b = data[2 + n:2 + n + k]

ans = [str(binary_search(a, x)) for x in b]

with open("n2/output.txt", "w", encoding="utf-8") as f:
    f.write(" ".join(ans))

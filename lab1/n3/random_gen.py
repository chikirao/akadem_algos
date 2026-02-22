import random

n = 3000
low = -10**9
high = 10**9

a = [random.randint(low, high) for _ in range(n)]

with open("n3/input.txt", "w", encoding="utf-8") as f:
    f.write(str(n) + "\n")
    f.write(" ".join(map(str, a)) + "\n")
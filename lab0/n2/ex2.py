def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

with open("n2/input.txt", "r", encoding="utf-8") as f:
    n = int(f.read().strip())

with open("n2/output.txt", "w", encoding="utf-8") as f:
    f.write(str(fib(n)))
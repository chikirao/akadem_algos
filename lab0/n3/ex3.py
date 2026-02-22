def fib_last_digit(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10
    return a

with open("n3/input.txt", "r", encoding="utf-8") as f:
    n = int(f.read().strip())

with open("n3/output.txt", "w", encoding="utf-8") as f:
    f.write(str(fib_last_digit(n)))
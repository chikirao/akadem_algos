import time
import tracemalloc

def fib(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fib_last_digit(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, (a + b) % 10
    return a

def timer(fn, n: int, repeats: int = 5) -> float:
    best = float("inf")
    for _ in range(repeats):
        t0 = time.perf_counter()
        fn(n)
        t1 = time.perf_counter()
        best = min(best, t1 - t0)
    return best

def memory_counter(fn, n: int):
    tracemalloc.start()
    fn(n)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak

if __name__ == "__main__":
    print("Время (сек)")
    for n in [0, 1, 5, 10, 20, 45]:
        print(f"fib({n}) = {timer(fib, n):.6f}")

    for n in [10, 1000, 100_000, 1_000_000, 10_000_000]:
        print(f"last_digit_linear({n}) = {timer(fib_last_digit, n):.6f}")

    print("\nПамять")
    cur, peak = memory_counter(fib_last_digit, 1_000_000)
    print(f"пиковая загруженность в байтах = {peak}")

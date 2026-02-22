import time
import tracemalloc


def secretary_swap_sort_with_log(a, n, out):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j

        if min_idx != i:
            x, y = i + 1, min_idx + 1
            if x > y:
                x, y = y, x
            out.write(f"Swap elements at indices {x} and {y}.\n")
            a[i], a[min_idx] = a[min_idx], a[i]

    out.write("No more swaps needed.\n")


def bytes_to_mb(b):
    return b / (1024 * 1024)


if __name__ == "__main__":
    with open("n3/input.txt", "r", encoding="utf-8") as f:
        n = int(f.readline())
        a = list(map(int, f.readline().split()))

    tracemalloc.start()
    t0 = time.perf_counter()

    with open("n3/output.txt", "w", encoding="utf-8") as out:
        secretary_swap_sort_with_log(a, n, out)

        t1 = time.perf_counter()
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        elapsed = t1 - t0

        print(f"Time: {elapsed:.6f} sec\n")
        print(f"Peak memory: {peak} bytes ({bytes_to_mb(peak):.3f} MB)\n")

        print("Limits: 1 sec, 256 MB\n")
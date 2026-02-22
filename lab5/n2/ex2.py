class MinHeap:
    def __init__(self, arr):
        self.a = arr
        self.n = len(arr)
        for i in range(self.n // 2 - 1, -1, -1):
            self._sift_down(i)

    @staticmethod
    def _less(x, y):
        if x[0] != y[0]:
            return x[0] < y[0]
        return x[1] < y[1]

    def _sift_down(self, i):
        a = self.a
        n = self.n
        while True:
            min_i = i
            l = 2 * i + 1
            r = 2 * i + 2

            if l < n and self._less(a[l], a[min_i]):
                min_i = l
            if r < n and self._less(a[r], a[min_i]):
                min_i = r

            if min_i == i:
                break

            a[i], a[min_i] = a[min_i], a[i]
            i = min_i

    def top(self):
        return self.a[0]

    def replace_top(self, item):
        self.a[0] = item
        self._sift_down(0)


def main():
    with open("n2/input.txt", "rb") as f:
        data = f.read().split()

    n = int(data[0])
    m = int(data[1])
    times = list(map(int, data[2:2 + m]))

    heap = MinHeap([(0, i) for i in range(n)])

    out = []
    for t in times:
        free_time, thread_id = heap.top()
        out.append(f"{thread_id} {free_time}")
        heap.replace_top((free_time + t, thread_id))

    with open("n2/output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()
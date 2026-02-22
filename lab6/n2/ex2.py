from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

class HashMapOA:
    _EMPTY = None

    def __init__(self, cap):
        self.cap = cap
        self.keys = [self._EMPTY] * cap
        self.vals = [self._EMPTY] * cap
        self.states = bytearray(cap)  # 0 empty, 1 filled, 2 deleted
        self.size = 0

        # универсальная хеш-функция из лекции: h(x) = ((a*x + b) mod p) mod m
        self.p = (1 << 61) - 1
        self.a = 1000003
        self.b = 1000033

    def _h(self, x):
        x %= self.p
        return ((self.a * x + self.b) % self.p) % self.cap

    def _find_slot(self, k):
        j = self._h(k)
        first_del = -1

        for _ in range(self.cap):
            st = self.states[j]
            if st == 0:
                return (first_del if first_del != -1 else j, False)
            if st == 1 and self.keys[j] == k:
                return (j, True)
            if st == 2 and first_del == -1:
                first_del = j
            j += 1
            if j == self.cap:
                j = 0
        return (-1, False)

    def put(self, k, v):
        idx, exists = self._find_slot(k)
        if not exists:
            self.size += 1
            self.keys[idx] = k
            self.states[idx] = 1
        self.vals[idx] = v

    def remove(self, k):
        idx, exists = self._find_slot(k)
        if not exists:
            return
        self.states[idx] = 2
        self.size -= 1

    def get(self, k):
        idx, exists = self._find_slot(k)
        if not exists:
            return None
        return self.vals[idx]


def main():
    with open(_path("n2/input.txt"), "rb") as f:
        data = f.read().split()

    n = int(data[0])
    i = 1

    cap = 1
    need = n * 2 + 1
    while cap < need:
        cap <<= 1

    mp = HashMapOA(cap)
    out = []

    for _ in range(n):
        cmd = data[i].decode()

        if cmd == "add":
            number = int(data[i + 1])
            name = data[i + 2].decode()
            mp.put(number, name)
            i += 3
        elif cmd == "del":
            number = int(data[i + 1])
            mp.remove(number)
            i += 2
        else: # find
            number = int(data[i + 1])
            name = mp.get(number)
            out.append(name if name is not None else "not found")
            i += 2

    with open(_path("n2/output.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()

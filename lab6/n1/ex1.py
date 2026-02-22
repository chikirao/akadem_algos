class HashSetOA:
    _EMPTY = None

    def __init__(self, cap):
        self.cap = cap
        self.keys = [self._EMPTY] * cap
        self.states = bytearray(cap) # 0 empty, 1 filled, 2 deleted
        self.size = 0

        # универсальная хеш-функция из лекции: h(x) = ((a*x + b) mod p) mod m
        # p берем большим простым > всех ключей по модулю, чтобы работало стабильно
        self.p = (1 << 61) - 1
        self.a = 1000003
        self.b = 1000033

    def _h(self, x):
        # приводим к [0..p-1]
        x %= self.p
        return ((self.a * x + self.b) % self.p) % self.cap

    def _find_slot(self, x):
        j = self._h(x)
        first_del = -1

        for _ in range(self.cap):
            st = self.states[j]
            if st == 0:
                return (first_del if first_del != -1 else j, False)
            if st == 1 and self.keys[j] == x:
                return (j, True)
            if st == 2 and first_del == -1:
                first_del = j
            j += 1
            if j == self.cap:
                j = 0
        return (-1, False)

    def add(self, x):
        idx, exists = self._find_slot(x)
        if exists:
            return
        self.keys[idx] = x
        self.states[idx] = 1
        self.size += 1

    def discard(self, x):
        idx, exists = self._find_slot(x)
        if not exists:
            return
        self.states[idx] = 2
        self.size -= 1

    def contains(self, x):
        _, exists = self._find_slot(x)
        return exists


def main():
    with open("n1/input.txt", "rb") as f:
        data = f.read().split()

    n = int(data[0])
    i = 1

    cap = 1
    need = n * 2 + 1
    while cap < need:
        cap <<= 1

    hs = HashSetOA(cap)
    out = []

    for _ in range(n):
        op = data[i].decode()
        x = int(data[i + 1])
        i += 2

        if op == "A":
            hs.add(x)
        elif op == "D":
            hs.discard(x)
        else: # "?"
            out.append("Y" if hs.contains(x) else "N")

    with open("n1/output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()

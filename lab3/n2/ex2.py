def main():
    with open("n2/input.txt", "r", encoding="utf-8") as f:
        n = int(f.readline().strip())

    a = list(range(1, n + 1))

    for i in range(2, n):
        j = i // 2
        a[i], a[j] = a[j], a[i]

    with open("n2/output.txt", "w", encoding="utf-8") as out:
        chunk = 20000
        first = True
        for start in range(0, n, chunk):
            part = a[start:start + chunk]
            s = " ".join(map(str, part))
            if first:
                out.write(s)
                first = False
            else:
                out.write(" " + s)

if __name__ == "__main__":
    main()
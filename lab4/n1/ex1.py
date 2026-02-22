def main():
    with open("n1/input.txt", "r", encoding="utf-8") as f:
        m = int(f.readline())

        q = [0] * m
        head = 0
        tail = 0
        size = 0

        out_lines = []

        for _ in range(m):
            line = f.readline().strip()

            if line[0] == '+':
                x = int(line[1:].strip())
                q[tail] = x
                tail += 1
                if tail == m:
                    tail = 0
                size += 1
            else:
                # "-"
                x = q[head]
                out_lines.append(str(x) + "\n")
                head += 1
                if head == m:
                    head = 0
                size -= 1

    with open("n1/output.txt", "w", encoding="utf-8") as out:
        out.write("".join(out_lines))


if __name__ == "__main__":
    main()
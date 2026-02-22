SERVICE = 10 # минут на одного

def main():
    with open("n4/input.txt", "r", encoding="utf-8") as f:
        n = int(f.readline())
        customers = []
        for _ in range(n):
            h, m, p = map(int, f.readline().split())
            t = h * 60 + m
            customers.append((t, p))

    end_times = [] # времена окончания обслуживания тех, кто остался
    head = 0

    out_lines = []

    for t, p in customers:
        # убираем всех, кто успел закончить к моменту t
        while head < len(end_times) and end_times[head] <= t:
            head += 1

        if head == len(end_times):
            end_times = []
            head = 0

        in_system = len(end_times) - head

        if in_system > p:
            leave = t
        else:
            if in_system == 0:
                start = t
            else:
                start = end_times[-1]
            leave = start + SERVICE
            end_times.append(leave)

        out_lines.append(f"{leave // 60} {leave % 60}\n")

    with open("n4/output.txt", "w", encoding="utf-8") as out:
        out.write("".join(out_lines))


if __name__ == "__main__":
    main()
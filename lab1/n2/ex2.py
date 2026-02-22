with open("n2/input.txt", "r", encoding="utf-8") as f:
    lines = [line.rstrip("\n") for line in f.readlines()]

a = list(map(int, lines[0].split())) if len(lines) > 0 and lines[0].strip() else []
v = int(lines[1].strip()) if len(lines) > 1 else 0

idx = []
for i, x in enumerate(a, start=1):
    if x == v:
        idx.append(i)

with open("n2/output.txt", "w", encoding="utf-8") as f:
    if len(idx) == 0:
        f.write("-1")
    elif len(idx) == 1:
        f.write(str(idx[0]))
    else:
        f.write(str(len(idx)) + "\n")
        f.write(",".join(map(str, idx)))

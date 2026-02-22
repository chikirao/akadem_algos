def main():
    with open("n3/input.txt", "rb") as f:
        data = f.read().split()

    votes = {}
    i = 0
    n = len(data)

    while i + 1 < n:
        name = data[i].decode()
        cnt = int(data[i + 1])
        votes[name] = votes.get(name, 0) + cnt
        i += 2

    keys = sorted(votes.keys())
    out = [f"{k} {votes[k]}" for k in keys]

    with open("n3/output.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()
def h_index(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations, start=1):
        if c >= i:
            h = i
        else:
            break
    return h

def main():
    with open("n3/input.txt", "r", encoding="utf-8") as f:
        s = f.read().strip()

    s = s.replace(",", " ")
    citations = [int(x) for x in s.split()] if s else []

    ans = h_index(citations)

    with open("n3/output.txt", "w", encoding="utf-8") as f:
        f.write(str(ans))

if __name__ == "__main__":
    main()
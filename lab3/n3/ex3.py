from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

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
    with open(_path("n3/input.txt"), "r", encoding="utf-8") as f:
        s = f.read().strip()

    s = s.replace(",", " ")
    citations = [int(x) for x in s.split()] if s else []

    ans = h_index(citations)

    with open(_path("n3/output.txt"), "w", encoding="utf-8") as f:
        f.write(str(ans))

if __name__ == "__main__":
    main()
from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

def main():
    with open(_path("n3/input.txt"), "rb") as f:
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

    with open(_path("n3/output.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(out))


if __name__ == "__main__":
    main()
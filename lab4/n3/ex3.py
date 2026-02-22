from pathlib import Path

_LAB_DIR = Path(__file__).resolve().parent.parent
_TASK_DIR = Path(__file__).resolve().parent


def _path(rel_path: str) -> Path:
    if "/" in rel_path or "\\" in rel_path:
        return _LAB_DIR / rel_path
    return _TASK_DIR / rel_path

def main():
    with open(_path("n3/input.txt"), "r", encoding="utf-8") as f, open(_path("n3/output.txt"), "w", encoding="utf-8") as out:
        n_line = f.readline()
        if not n_line:
            return
        n = int(n_line)

        st = []
        mx = []

        buf = []
        FLUSH = 50000

        for _ in range(n):
            line = f.readline().strip()
            if not line:
                continue

            parts = line.split()
            cmd = parts[0]

            if cmd == "push":
                v = int(parts[1])
                st.append(v)
                if not mx:
                    mx.append(v)
                else:
                    mx.append(v if v > mx[-1] else mx[-1])

            elif cmd == "pop":
                st.pop()
                mx.pop()

            else: # "max"
                buf.append(str(mx[-1]) + "\n")
                if len(buf) >= FLUSH:
                    out.write("".join(buf))
                    buf.clear()

        if buf:
            out.write("".join(buf))


if __name__ == "__main__":
    main()
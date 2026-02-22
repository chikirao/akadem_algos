def main():
    with open("n2/input.txt", "r", encoding="utf-8") as f:
        s = f.readline()
        if s is None:
            s = ""
        s = s.rstrip("\n")

    open_set = {'(', '[', '{'}
    match = {')': '(', ']': '[', '}': '{'}

    stack = [] # скобка

    for pos, ch in enumerate(s, start=1):
        if ch in open_set:
            stack.append((ch, pos))
        elif ch in match:
            if not stack:
                with open("т2/output.txt", "w", encoding="utf-8") as out:
                    out.write(str(pos))
                return
            top_ch, top_pos = stack.pop()
            if top_ch != match[ch]:
                with open("n2/output.txt", "w", encoding="utf-8") as out:
                    out.write(str(pos))
                return

    if stack:
        # первая открывающая без закрывающей
        with open("n2/output.txt", "w", encoding="utf-8") as out:
            out.write(str(stack[0][1]))
    else:
        with open("n2/output.txt", "w", encoding="utf-8") as out:
            out.write("Success")


if __name__ == "__main__":
    main()
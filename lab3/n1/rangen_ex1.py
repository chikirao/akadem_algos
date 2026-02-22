import random

random.seed("chikirao")

def write_case(filename, a):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(len(a)) + "\n")
        f.write(" ".join(map(str, a)) + "\n")

n = 10000

a_best = list(range(n))
a_worst = list(range(n, 0, -1))

a_avg = list(range(n))
random.shuffle(a_avg)

few_vals = [1, 2, 3, 4, 5]
a_few_unique = [random.choice(few_vals) for _ in range(n)]

write_case("n1/input_best.txt", a_best)
write_case("n1/input_avg.txt", a_avg)
write_case("n1/input_worst.txt", a_worst)
write_case("n1/input_few_unique.txt", a_few_unique)
import itertools

p = [0.05, 0.15, 0.20, 0.25, 0.35]

def Q(n):
    total = 0.0

    for r in range(6):
        for I in itertools.combinations(range(5), r):

            s = sum(p[i] for i in I)

            total += (-1)**r * (1 - s)**n

    return total
n = 1

while Q(n) < 0.90:
    n += 1
print("smallest n =", n)
print("Q_{} = {:.10f}".format(n - 1, Q(n - 1)))
print("Q_{} = {:.10f}".format(n, Q(n)))
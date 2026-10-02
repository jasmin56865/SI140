import math
import matplotlib.pyplot as plt

# Uniform case: p_i = 0.2
def Q_equal(n):
    return sum(
        (-1)**k * math.comb(5, k) * (1 - k/5)**n
        for k in range(6)
    )

# Unequal case
def Q_unequal(n):
    p = [0.05, 0.15, 0.20, 0.25, 0.35]
    total = 0

    # Enumerate all subsets of {1,2,3,4,5}
    for mask in range(1 << 5):
        s = 0
        k = 0

        for i in range(5):
            if mask & (1 << i):
                s += p[i]
                k += 1

        total += (-1)**k * (1 - s)**n

    return total


# Find the smallest n in the uniform case
n = 1
while Q_equal(n) < 0.90:
    n += 1

print("Uniform case:")
print("smallest n =", n)
print("Q_{} = {:.10f}".format(n - 1, Q_equal(n - 1)))
print("Q_{} = {:.10f}".format(n, Q_equal(n)))


# Plot Q_n
ns = range(1, 61)

q_equal = [Q_equal(n) for n in ns]
q_unequal = [Q_unequal(n) for n in ns]

plt.plot(ns, q_equal, label="Uniform: p_i = 0.2")
plt.plot(
    ns,
    q_unequal,
    label="Unequal: (0.05, 0.15, 0.20, 0.25, 0.35)"
)

plt.axhline(0.90, linestyle="--", label="Q_n = 0.90")

plt.xlabel("n")
plt.ylabel("Q_n")
plt.title("Q_n for Uniform and Unequal Card Probabilities")

plt.legend()
plt.grid(True)

plt.show()
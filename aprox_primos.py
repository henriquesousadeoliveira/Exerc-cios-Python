import math

n = int(input())

n / (math.log(n)) < math.pi *n < 1.25506 * (n / math.log(n))

p = n / (math.log(n))
m = 1.25506 * (n / math.log(n))

print(f"{p:.1f} {m:.1f}")


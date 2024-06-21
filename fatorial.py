import math
n = int(input())
if (n <= 1):
    print(1)
else:
    print(n * math.factorial(n-1))

import math

n = int(input())

menor_1 = math.inf
menor_2 = math.inf
for i in range(n)
    x = int(input())
    if x < menor_1:
        menor_2 = menor_1
        menor_1 = x
    elif x < menor_2:
        menor_2 = x
print(menor_2)
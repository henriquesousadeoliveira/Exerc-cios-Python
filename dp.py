import math
n = int(input())
valores = [float(input()) for _ in range(n)]
media = sum(valores) / n
soma = 0
for x in valores:
    soma += ( x-media)**2
    
dp = soma / n - 1
print(dp)
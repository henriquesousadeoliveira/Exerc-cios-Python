notas = [float(x) for x in input().split()]
notas.sort()
del notas[0]
del notas[-1]
soma = 0
for i in notas:
    soma += i
print(f"{soma:.1f}")

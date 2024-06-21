numero = input()
peso = len(numero)
soma = 0
for i in range(peso - 1):
    soma += int(numero[i]) * peso
    peso -= 1
dv = 11  - soma % 11
if dv >= 10:
    dv = 0
print(dv == int(numero[-1]))
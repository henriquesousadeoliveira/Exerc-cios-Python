qtd_valores = int(input())
numeros = [float(input()) for i in range(qtd_valores)]
soma = 0
produto = 1
for i in numeros:
    produto *= i
media = produto ** (1 / qtd_valores)
print(media)
n = int(input())
for _ in range(n):
    num_alunos, segredo = [int(x) for x in input().split()]
    numeros = [int(x) for x in input().split()]

    diferencas = [abs(x - segredo) for x in numeros]
    ganhador = diferencas.index(min(diferencas)) + 1
    print(ganhador)

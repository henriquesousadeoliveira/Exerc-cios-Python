while True:
    qtd_comprimentos = int(input())
    if qtd_comprimentos == 0:
        break
    qtd_comprimentos = int(input())
    soma = 0
    for _ in range(qtd_comprimentos):
        comprimento,qtd_varetas = [int(x) for x in input().split()]
        soma += qtd_varetas // 2 * 2
    num_retangulos = soma // 4
    print(num_retangulos)

qtd_testes = int(input())
for lista in range(qtd_testes):
    lista = input().split()
    lista_nova = []
    for item in lista:
        if item not in lista_nova:
            lista_nova.append(item)
    lista_nova.sort()
    print(" ".join(lista_nova))

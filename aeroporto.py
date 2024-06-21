teste = 0
while True:
    num_aeroportos, num_voos = [int(x) for x in input().split()]
    if num_aeroportos == 0 and num_voos == 0:
        break
    aeroportos = list(range(1, num_aeroportos + 1))
    mapeamento = {aeroporto: 0 for aeroporto in aeroportos}
    for _ in range(num_voos):
        voos = [int(x) for x in input().split()]
        for voo in voos:
            if voo in mapeamento:
                mapeamento[voo] += 1
    maior_valor = max(mapeamento.values())
    chaves_maximas = [chave for chave, valor in mapeamento.items() if valor == maior_valor]
    teste += 1
    print(f"Teste {teste}")
    for chave in chaves_maximas:
        print(chave)
    print()
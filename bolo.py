a, b, c = [int(w) for w in input().split()]

quantidade_trigo = a // 2
quantidade_ovo = b // 3
quantidade_leite = c // 5

ingredientes = [quantidade_trigo, quantidade_ovo, quantidade_leite]

quantidade_bolo = min(ingredientes)

print(quantidade_bolo)
qtd_jogador, qtd_jogos = [int(x) for x in input().split()]
fizeram_gol = 0
for i in range(qtd_jogador):
    jogador = [int(x) for x in input().split()]
    for gol in jogador:
        if gol == 0:
            fez_gol = False
            break
        fez_gol = True
    if fez_gol:
        fizeram_gol += 1
print(fizeram_gol)

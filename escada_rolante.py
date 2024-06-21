while True:
    qtd_pessoas = int(input())
    if qtd_pessoas == 0:
        break
    tempo_pessoas = [int(x) for x in input().split()]
    tempo_ativo = 0
    for pessoa in range(qtd_pessoas-1):
        if abs(tempo_pessoas[pessoa] - tempo_pessoas[pessoa+1]) < 10:
            tempo_ativo += abs(tempo_pessoas[pessoa] - tempo_pessoas[pessoa+1])
        else:
            tempo_ativo += 10
    tempo_ativo += 10
    print(tempo_ativo)

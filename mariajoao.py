jogos = 1
while True:
    jogos = int(input())
    if jogos == 0:
        break
    partidas = input()
    m_w = 0
    j_w = 0
    partida_limpa = partidas.replace(' ', '')
    for carac in(partida_limpa):
        if carac == "0":
            m_w += 1
        else:
            j_w +=1
    print(f"Mary won {m_w} times and John won {j_w} times")
    
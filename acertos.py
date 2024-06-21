respostas = input()
gabarito = input()
posição_carac = 0
acertos = 0
for caracter in respostas:
    if caracter == gabarito[posição_carac]:
        acertos += 1
    posição_carac += 1
print(acertos)


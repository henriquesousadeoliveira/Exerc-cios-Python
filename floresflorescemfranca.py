teste = ''
while True:
    teste = input()
    if teste == '*':
        break
    separacoes = teste.count(' ')
    partes = teste.split(' ', separacoes + 1)
    for i in range(len(partes))
        partes[i] = partes[i][0].lower() + partes[i][1:]
    primeira_letra = partes[0][0]
    iguais = all(p[0] == primeira_letra for p in partes)
    if iguais == True:
        print('Y')
    else:
        print('N')
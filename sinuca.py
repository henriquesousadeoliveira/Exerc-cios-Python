lista_regras = []
while True:
    regra = input().split() #entrada da regra
    if int(regra[0]) == 0 and int(regra[1]) == 0:
        ordem = regra[3].split(';') #separa a ordem de seleção por ponto e vírgula
    lista_regras.append(regra)
vagas = {}
categoria = lista_regras[0][3].split(',')
for ordem_selecao in categoria:
    vagas[ordem_selecao] = int(input(0)) #cria o dicionario vagas com o numero das mesmas em cada categoria
n_candidatos = int(input())
lista_candidatos = []
for i in range(n_candidatos):
    candidato = input().split()
    lista_candidatos.append(candidato)
    print(vagas)
  
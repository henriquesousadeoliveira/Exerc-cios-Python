n_candidatos = int(input())
lista_candidatos = []
for i in range(n_candidatos):
    candidato = input().split()
    candidato_conj = [candidato[0], candidato[1], set([candidato[2]])]
    lista_candidatos.append(candidato_conj)
print(lista_candidatos)
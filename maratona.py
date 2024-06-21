num_postos_de_agua, distancia = [int(x) for x in input().split()]
postos = [int(x) for x in input().split()]
termina = False
for i in range(1, len(postos)):
    if postos[int(i)] - postos[int(i-1)] <= distancia:
        termina = True
    else:
        termina = False
        break
if termina: 
    print("S")
else:
    print("N")
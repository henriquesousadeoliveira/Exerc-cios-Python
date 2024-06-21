# ler o tamanho do pulo do sapo e a quantidade de canos em uma lista
# ler as alturas do cano com um for(qtd canos) em uma lista
# verificar se abs(cano inicial - cano final) <= tamanho do pulo
alt_max, num_canos = [int(x) for x in input().split()]
canos = [int(x) for x in input().split()]
chegou_final = True
for i in range(num_canos -1):
    if abs(canos[i] - canos[i+1]) > alt_max:
        chegou_final = False
        break
if chegou_final == True:
    print("YOU WIN")
else:
    print("GAME OVER")

        

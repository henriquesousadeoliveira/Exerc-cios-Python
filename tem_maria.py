testes = int(input())
tem_maria = 0
for i in range(testes):
    nome = input()
    if testes == 1 and "Mariana" in nome:
        tem_maria = 0
        break
    if  "Mariana" in nome:
        tem_maria == tem_maria
    elif "Maria" in nome:
        tem_maria +=  1
print(tem_maria)
        
        
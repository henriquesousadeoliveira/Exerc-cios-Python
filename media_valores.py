tamanho_seq = int(input())
soma = 0
for n in range (tamanho_seq):
    n = float(input())
    soma += n
    media = soma / tamanho_seq
    
print(media)
comprimento = float(input()) #em metros
largura_da_mesa = float(input())#em metros
numero_de_gavetas = int(input())
tipo_de_madeira = input()

m2 = comprimento * largura_da_mesa

preco_mesa = m2 * 100 + numero_de_gavetas * 30

if m2 > 2:
    preco_mesa= preco_mesa + 50
    
if tipo_de_madeira == "mogno":
    preco_mesa1 = preco_mesa + 150
elif tipo_de_madeira == "carvalho"
    preco_mesa1 = preco_mesa  + 125
else
    preco_mesa1 = preco_mesa1

print(f"{preco_mesa1:.1f}")



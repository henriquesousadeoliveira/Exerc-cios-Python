num_carros, num_voltas = [int(x) for x in input().split()]
voltas = dict()
for carro in range(1,num_carros+1):
    voltas[carro] = sum([int(x) for x in input().split()] )
voltas_ordenado = dict(sorted(voltas.items(),key= lambda item:item[1]))
chaves = list(voltas_ordenado.keys())[:3]
for chave in chaves:
    print(chave)
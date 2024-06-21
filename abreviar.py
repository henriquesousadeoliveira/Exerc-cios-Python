#Separar as palavras da string dentro de uma lista
#Filtrar as palavras deixando apenas as que tem + do que 3 caracteres
#Manter a primeira e ultima palavra
#pegar as palavras restantes e resumilás a primeira letra + '.' 
nome = input() 
partes = nome.split()
for i in range(1, len(partes)-1):
    parte = partes[i]
    if len(parte) > 3: 
        partes[i] = parte[0] + '.' 
nome_abreviado = ' ' .join(partes)
print(nome_abreviado)

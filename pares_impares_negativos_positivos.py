valores_positivos = ' '
valores_negativos = ' '
valores_pares = ' '
valores_impares = ' '
for n in range (5):
    n = int(input())
    if n >= 0:
        valores_positivos += str(n) + ' '
    else:
        valores_negativos += str(n) + ' '
    if n % 2 == 0:
        valores_pares += str(n) + ' '
    else:
        valores_impares += str(n) + ' '
        
print(valores_positivos)
print(valores_negativos)
print(valores_pares)
print(valores_impares)
    
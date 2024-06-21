contador_pares = 0
contador_impares = 0
contador_positivos = 0
contador_negativos = 0
for n in range(5):
    n = int(input())
    if n < 0:
        contador_negativos += 1
    elif n > 0:
        contador_positivos += 1
    if n % 2 == 0:
        contador_pares += 1
    else:
        contador_impares += 1

print(str(contador_pares),"valor(es) par(es)")
print(str(contador_impares),"valor(es) impar(es)")
print(str(contador_positivos),"valor(es) positivo(s)")
print(str(contador_negativos),"valor(es) negativos(s)")
n1 = int(input())
n2 = int(input())
multiplos = ''
for numeros in range (1,n2+1):
    if numeros % n1 == 0:
        multiplos += str(numeros) + ' ' 
print(multiplos, end=' ')
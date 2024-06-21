numeros = [int(input()) for i in range(4)]
conjunto = set(numeros)
if len(conjunto) == 1:
    print(1)
elif len(conjunto) == 2:
    print(2)
elif len(conjunto) == 3:
    print(3)
else: 
    print(4)
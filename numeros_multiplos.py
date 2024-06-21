n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

primeiro_multiplo = True

for numeros in range(1, n2+1):
    if numeros % n1 == 0:
        if primeiro_multiplo:
            print(numeros, end='')
            primeiro_multiplo = False
        else:
            print(' ' + str(numeros), end='')

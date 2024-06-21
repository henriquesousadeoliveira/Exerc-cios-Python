a, b = [int(w) for w in input().split()]

resultado = "Sao multiplos" if a % b == 0 or b % a == 0 else "Nao sao Multiplos"
print(resultado)
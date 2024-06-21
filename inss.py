salario = float(input())

if salario < 720:
    inss = salario * 0.0765
elif 720 < salario < 1200:
    inss = salario * 0.09
elif 1200 < salario < 2400:
    inss = salario * 0.11
elif salario > 2400:
    inss = 2400 * 0.11
print(inss)
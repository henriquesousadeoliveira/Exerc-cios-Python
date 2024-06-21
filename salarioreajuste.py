salario_fun = float(input())
salario_min = float(input())

salariomin3 = salario_min * 3
salariomin5 = salario_min * 5

if salario_fun <= salariomin3:
    salario = salario_fun + (2/10 * salario_fun)
elif salario_fun <= salariomin5:
    salario = salario_fun + (15/100 * salario_fun)
else :
    salario = salario_fun + (1/10 * salario_fun)
    
if salario < salario_min * 1.5:
    print(salario_min * 1.5)
elif salario > 20 * salario_min:
    print(salario_min * 20)
else :
    print(salario)
    
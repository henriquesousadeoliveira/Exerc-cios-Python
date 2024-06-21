def todos_digitos_iguais(cpf):
    return len(set(cpf)) == 1

cpf = input()
if len(cpf) == 14:
    cpf_so_numeros = ''.join(filter(str.isdigit, cpf))
else:
    cpf_so_numeros = cpf
if todos_digitos_iguais(cpf_so_numeros):
    print(False)
else:
    peso = 10
    soma = 0
    for i in range(len(cpf_so_numeros) - 2):
        soma += int(cpf_so_numeros[i]) * peso
        peso -= 1

    dv1 = 11 - (soma % 11)
    if dv1 >= 10:
        dv1 = 0

    soma = 0
    peso = 11
    for i in range(len(cpf_so_numeros) - 1):
        soma += int(cpf_so_numeros[i]) * peso
        peso -= 1

    dv2 = 11 - (soma % 11)
    if dv2 >= 10:
        dv2 = 0

    print(dv1 == int(cpf_so_numeros[-2]) and dv2 == int(cpf_so_numeros[-1]))

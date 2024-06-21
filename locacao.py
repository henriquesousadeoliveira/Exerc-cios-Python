dias = int(input())
km_rodados = int(input())
km_rodados_dia = km_rodados / dias
if km_rodados_dia > 60:
    km_cobrado = km_rodados_dia - 60
    custo_de_locacao = 45 * dias + 0.5 * km_cobrado * dias
else:
    custo_de_locacao= 45 * dias
print(custo_de_locacao)
    
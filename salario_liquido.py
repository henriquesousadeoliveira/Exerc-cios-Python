hora_normal = int(input())
hora_extra = int(input())

salario_bruto = (hora_normal*12.5) + (hora_extra*15)
imposto_de_renda = (salario_bruto) * (13/100)
inss = (salario_bruto) * (9/100)
salario_liquido = salario_bruto - (imposto_de_renda + inss)

print(f"- Salário Bruto : R$ {salario_bruto:.2f}")
print(f"- IR (13%) : R$ {imposto_de_renda:.2f}")
print(f"- INSS (9%) : R$ {inss:.2f}")
print(f"- Salário Líquido : R$ {salario_liquido:.2f}")
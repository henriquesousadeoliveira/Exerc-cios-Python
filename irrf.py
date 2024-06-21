salario_bruto = float(input())
dependentes = int(input())

c_dependentes = dependentes * 137.99


if salario_bruto <= 720.00:
    inss = salario_bruto * 0.0765
elif salario_bruto <= 1200.00:
    inss = salario_bruto * 0.09
elif salario_bruto <= 2400:
    inss = salario_bruto * 0.11
elif salario_bruto >= 2400:
    inss = 2400 * 0.11
    
    
if salario_bruto <= 1372.81:
    irrf = (salario_bruto - c_dependentes) - inss
elif 1372.82 <= salario_bruto < 2743.25:
    irrf = ((salario_bruto - c_dependentes)-inss) * 0.15 - 205.92
elif salario_bruto > 2743.25:
    irrf = ((salario_bruto - c_dependentes)-inss) * 0.275 - 548.82

print(f"{irrf:.2f}")

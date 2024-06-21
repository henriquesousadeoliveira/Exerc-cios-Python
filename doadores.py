num_calouros = int(input())
calouros = []
for calouro in range(num_calouros):
    calouro = input()
    calouros.append(calouro)

num_doadores = int(input())
doadores = []
for doador in range(num_doadores):
    doador = input()
    doadores.append(doador)  # Correção aqui

calouros1 = set(calouros)
doadores1 = set(doadores)
calouros_doadores = calouros1.intersection(doadores1)
proporcao = len(calouros_doadores) / len(calouros)

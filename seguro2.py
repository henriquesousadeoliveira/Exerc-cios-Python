valor_do_veiculo = float(input())
sexomf = input()
idade = int(input())

seguro = valor_do_veiculo * 0.1

if sexomf == "M":
    if idade <= 24:
        valor_seguro = seguro
    elif 24 <= idade <= 33:
        valor_seguro = seguro * 0.1
    elif idade > 33:
        valor_seguro = seguro * 0.2
        if idade <= 24:
            print(seguro)
        else:
            print(seguro - valor_seguro)

elif sexomf == "F" :
    if idade <= 24:
        valor_seguro = seguro * 0.95
    elif 24 <= idade <= 33:
        valor_seguro = seguro * 0.2
    elif idade > 33:
        valor_seguro = seguro * 0.35
if idade <= 24:
    print(valor_seguro)
else:
    print(seguro - valor_seguro)
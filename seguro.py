valor_veiculo = float(input())
classe = input()
procedencia = input()
idade_segurado = int(input())
if procedencia == "nacional":
    desconto = valor_veiculo * 0.1
    
    
    if classe == "A":
        desc_ = desconto * 0.7
    elif classe == "B":
        desc_ = desconto * 0.8
    elif classe == "C":
        desc_ = desconto * 0.9
    elif classe == "D":
        desc_ = desconto * 0.95
    elif classe == "E":
        desc_ = desconto
    
    if idade_segurado > 24:
        desc_2 = desconto * 0.1
        print(desc_ - desc_2)
    else:
        print(desc_)

elif procedencia == "estrangeira":
    desconto2 = valor_veiculo * 0.15

    
    if classe == "A":
        desc_ = desconto2 * 0.7
    elif classe == "B":
        desc_ = desconto2 * 0.8
    elif classe == "C":
        desc_ = desconto2 * 0.9
    elif classe == "D":
        desc_ = desconto2 * 0.95
    elif classe == "E":
        desc_ = desconto2
    
    if idade_segurado > 24:
        desc_2 = desconto2 * 0.1
        print(desc_ - desc_2)
    else:
        print(desc_)
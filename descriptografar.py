alfabeto_normal = input()
alfabeto_cifragem = input()
deciframento = dict(zip(alfabeto_cifragem,alfabeto_normal))
msg_cifrada = input()
msg_normal = ''
for letra in msg_cifrada:
    if letra in deciframento:
        msg_normal += deciframento[letra]
    else:
        msg_normal += letra
print(msg_normal)
numero = float(input())
if numero > 0:
    notacao = "{:+.4E}".format(numero)
else:
        notacao = "{:-.4E}".format(numero)
print(notacao)
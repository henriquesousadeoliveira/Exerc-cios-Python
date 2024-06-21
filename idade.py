dias = int(input())

anos = dias // 365
dias %= 365
meses = dias // 30
dias %= 30
numero_de_dias = dias

print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{numero_de_dias} dia(s)")

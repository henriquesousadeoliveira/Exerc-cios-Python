compra = float(input())
preco1 = compra * 0.8

if 1000 >= compra >= 500:
    desconto1 = compra * 0.1
elif compra >= 1000:
    desconto1 = compra * 0.1 + (compra - 1000) * 0.15
else:
    desconto1 = 0

print(f"{preco1 - desconto1:.2f}")
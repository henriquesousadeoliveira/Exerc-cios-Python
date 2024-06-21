a = float(input())
b = float(input())
c = float(input())

verificar = abs(a-b) > c or abs(a-c) > b or abs(b-c) > a
print(verificar)





cartas = [int(x) for x in input().split()]
for i in range(0, len(cartas)):
    if int(cartas[i]) > int(cartas[i+1]):
        ordem = "D"
    elif  int(cartas[i]) > int(cartas[i+1]):
        ordem = "C"
    else:
        ordem = "N"
print(ordem)
    
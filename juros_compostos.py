import math
capital = float(input())
meses = float(input())
taxa = float(input())

montante = capital * ((1 + (taxa/100))**meses)

print(round(montante,2))

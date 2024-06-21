energia = int(input())
energia_30 = 0.09556
energia_100 = 0.16698
energia_200 = 0.25052
energia_201 = 0.27836
if energia <= 30:
    custo = energia * energia_30
elif 31 <= energia <= 100:
    resto = energia - 30
    custo = (30 * energia_30) + (resto * energia_100)
elif 101 <= energia <= 200:
    resto = energia - 100
    custo = (30 * energia_30) + (70 * energia_100) + (resto * energia_200)
elif energia > 200:
    resto = energia - 200
    custo = (30 *energia_30) + (70 * energia_100) + (100 * energia_200) + (resto * 0.27836)

print(f"{custo:.2f}")


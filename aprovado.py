nota1 = float(input())
nota2 = float(input())
nota3 = float(input())
peso1 = float(input())
peso2 = float(input())
peso3 = float(input())

media= nota1 * peso1 + nota2 * peso2 + nota3 * peso3
peso = peso1 + peso2 + peso3

media_final =(media / peso)

print(media_final >= 6)

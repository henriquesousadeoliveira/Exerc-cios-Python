palavra1 = input()
palavra2 = input()
if palavra1 == palavra2:
    print(False)

palavra1_ordenada = "" .join(sorted(palavra1))
palavra2_ordenada = "" .join(sorted(palavra2))


if palavra1_ordenada == palavra2_ordenada:
    print(True)
else:
    print (False)
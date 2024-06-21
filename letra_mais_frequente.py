#Hoje acordei com vontade de tomar sorvete  de cereja
frase = input().lower()
conjunto_f =set(frase)
letra_mais_freq = 0
letra_freq = ''
for letra in conjunto_f:
    if frase.count(letra) > letra_mais_freq:
        letra_mais_freq = frase.count(letra)
        letra_freq = letra
print(letra_freq)
        
#O romance todo é bem lido


lista1 = int(input())
lista1_ = [input() for i in range(lista1)]
lista2 = int(input())
lista2_ = [input() for i in range(lista2)]
nova_lista = lista1_ + lista2_
nova_lista.sort()
for i in range(len(nova_lista)):
    print(nova_lista[i])
c, p , f = [float(w) for w in input().split()]

papel_comp = p/c

if papel_comp >= f:
    print("S")
else:
    print("N")
5        ingressos = [int(x) for x in input().split()]
        for i in range(0, len(ingressos)):
            if i+1 == int(ingressos[i]):
                print(f"Teste:{teste}")
                print(i+1)
                break
        teste += 1

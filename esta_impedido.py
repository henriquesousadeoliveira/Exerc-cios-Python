while True:    
    num_atac, num_def = [int(x) for x in input().split()]
    if num_def == 0 and num_atac == 0:
        break
    atacantes = [int(x) for x in input().split()]
    defensores = [int(x) for x in input().split()]
    menor_dist_atac = min(atacantes)
    defensores.sort()
    seg_dist_def = defensores[1]
    esta_impedido = 'Y' if menor_dist_atac < seg_dist_def else 'N'
    print(esta_impedido)

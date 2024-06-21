distancia, d_e_pedagios  = [int(w) for w in input().split()]
custo_km, valor_pedagio = [int(w) for w in input().split()]

numero_de_pedagios = distancia // d_e_pedagios
custo_por_km = distancia * custo_km
valor_t_pedagios = numero_de_pedagios * valor_pedagio

custo_t_viagem = valor_t_pedagios + custo_por_km

print(custo_t_viagem)

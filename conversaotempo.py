tempo_em_segundos = int(input())

horas = tempo_em_segundos // 3600
tempo_em_segundos %= 3600
minutos = tempo_em_segundos // 60
tempo_em_segundos %= 60
segundos = tempo_em_segundos

print("{:01d}:{:01d}:{:01d}".format(horas, minutos, segundos))
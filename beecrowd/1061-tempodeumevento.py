# Lê o dia inicial (ex: "Dia 5" -> extrai o 5)
inicio_dia = int(input().split()[1])

# Lê o horário inicial (ex: "08 : 12 : 23" -> [8, 12, 23])
inicio_tempo = list(map(int, input().split(" : ")))

# Lê o dia final (mesmo formato do dia inicial)
fim_dia = int(input().split()[1])

# Lê o horário final (mesmo formato do horário inicial)
fim_tempo = list(map(int, input().split(" : ")))

# Converte tudo para segundos para facilitar os cálculos
# Dias convertidos para segundos + horas convertidas para segundos + minutos convertidos + segundos
inicio_segundos = (inicio_dia * 24 * 3600) + (inicio_tempo[0] * 3600) + (inicio_tempo[1] * 60) + inicio_tempo[2]
fim_segundos = (fim_dia * 24 * 3600) + (fim_tempo[0] * 3600) + (fim_tempo[1] * 60) + fim_tempo[2]

# Calcula a diferença total em segundos
duracao_segundos = fim_segundos - inicio_segundos

# Converte os segundos de volta para dias, horas, minutos e segundos
duracao_dias = duracao_segundos // (24 * 3600)  # Dias completos
duracao_segundos %= (24 * 3600)  # Segundos restantes após extrair os dias

duracao_horas = duracao_segundos // 3600  # Horas completas
duracao_segundos %= 3600  # Segundos restantes após extrair as horas

duracao_minutos = duracao_segundos // 60  # Minutos completos
duracao_segundos %= 60  # Segundos restantes

# Exibe os resultados formatados
print(f"{duracao_dias} dia(s)")
print(f"{duracao_horas} hora(s)")
print(f"{duracao_minutos} minuto(s)")
print(f"{duracao_segundos} segundo(s)")
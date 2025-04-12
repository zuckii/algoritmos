# Recebe o tempo em segundos como um número inteiro
segundos = int(input())

# Calcula as horas completas (1 hora = 3600 segundos)
horas = segundos // 3600

# Calcula o restante de segundos após extrair as horas
resto = segundos % 3600

# Calcula os minutos completos do restante (1 minuto = 60 segundos)
minutos = resto // 60

# Os segundos restantes após extrair os minutos
segundos = resto % 60

# Exibe no formato HH:MM:SS
print(f"{horas}:{minutos}:{segundos}")
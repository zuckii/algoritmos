# Lê quatro valores inteiros da entrada, representando:
# hora_inicial, minuto_inicial, hora_final, minuto_final
hora_inicial, minuto_inicial, hora_final, minuto_final = map(int, input().split())

# Converte o horário inicial para minutos totais desde 00:00
inicio = (hora_inicial * 60) + minuto_inicial

# Converte o horário final para minutos totais desde 00:00
fim = (hora_final * 60) + minuto_final

# Verifica se o horário final é maior que o inicial (mesmo dia)
if fim > inicio:
    # Calcula a duração em minutos (caso simples, mesmo dia)
    duracao_min = fim - inicio
else:
    # Caso o horário final seja no dia seguinte:
    # Calcula o tempo restante do dia inicial + tempo do dia final
    duracao_min = ((24 * 60) - inicio) + fim

# Trata o caso especial onde início e fim são iguais (24 horas completas)
if duracao_min == 0:
    duracao_min = 24 * 60

# Converte a duração total em minutos para horas e minutos separados
duracao_hora = duracao_min // 60  # Divisão inteira para obter as horas
duracao_min = duracao_min % 60    # Resto da divisão para obter os minutos

# Exibe o resultado no formato especificado
print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_min} MINUTO(S)")
# Recebe a idade em dias como um número inteiro
idade_em_dias = int(input())

# Calcula os anos completos (considerando 1 ano = 365 dias)
anos = idade_em_dias // 365

# Calcula os dias restantes após remover os anos completos
dias_restantes = idade_em_dias % 365

# Calcula os meses completos nos dias restantes (considerando 1 mês = 30 dias)
meses = dias_restantes // 30

# Calcula os dias restantes após remover os meses completos
dias = dias_restantes % 30

# Exibe os resultados no formato especificado
print(f"{anos} ano(s)")
print(f"{meses} mes(es)")
print(f"{dias} dia(s)")
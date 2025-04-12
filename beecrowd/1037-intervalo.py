# Solicita ao usuário que insira um valor numérico e converte para float
valor = float(input())

# Verifica em qual intervalo o valor se encontra e imprime a mensagem correspondente:

# Se o valor estiver entre 0 e 25 (inclusive)
if valor >= 0 and valor <= 25:
    print('Intervalo [0,25]')

# Se o valor estiver entre 25 (exclusivo) e 50 (inclusive)
elif valor > 25 and valor <= 50:
    print('Intervalo (25,50]')

# Se o valor estiver entre 50 (exclusivo) e 75 (inclusive)
elif valor > 50 and valor <= 75:
    print('Intervalo (50,75]')

# Se o valor estiver entre 75 (exclusivo) e 100 (inclusive)
elif valor > 75 and valor <= 100:
    print('Intervalo (75,100]')

# Se o valor estiver fora do intervalo [0, 100]
else:
    print('Fora de intervalo')
    
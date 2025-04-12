# Lê o valor do salário como um número de ponto flutuante
salario = float(input())

# Verifica em qual faixa salarial o valor se encaixa e calcula o reajuste correspondente
if 0 < salario <= 400:
    # Calcula 15% de reajuste para salários até R$ 400
    reajuste_ganho = salario * 0.15
    novo_salario = reajuste_ganho + salario
    percentual = 15

elif 400 < salario <= 800:
    # Calcula 12% de reajuste para salários entre R$ 400.01 e R$ 800
    reajuste_ganho = salario * 0.12
    novo_salario = reajuste_ganho + salario
    percentual = 12

elif 800 < salario <= 1200:
    # Calcula 10% de reajuste para salários entre R$ 800.01 e R$ 1200
    reajuste_ganho = salario * 0.10
    novo_salario = reajuste_ganho + salario
    percentual = 10

elif 1200 < salario <= 2000:
    # Calcula 7% de reajuste para salários entre R$ 1200.01 e R$ 2000
    reajuste_ganho = salario * 0.07
    novo_salario = reajuste_ganho + salario
    percentual = 7

else:
    # Calcula 4% de reajuste para salários acima de R$ 2000
    reajuste_ganho = salario * 0.04
    novo_salario = reajuste_ganho + salario
    percentual = 4

# Imprime os resultados formatados com duas casas decimais para os valores monetários
print(f"Novo salario: {novo_salario:.2f}\n" f"Reajuste ganho: {reajuste_ganho:.2f}\n" f"Em percentual: {percentual} %")
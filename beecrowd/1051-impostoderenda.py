salario = float(input())

# Verifica se o salário está na faixa isenta (até R$ 2000)
if salario <= 2000.00:
    print("Isento")
else:
    # Inicializa o valor do imposto como 0.0
    imposto = 0.0

    # Calcula imposto para a faixa entre R$ 2000.01 e R$ 3000 (8%)
    if salario > 2000.00:
        # Calcula o valor tributável nessa faixa (o menor entre o salário e R$ 3000, menos R$ 2000)
        faixa = min(salario, 3000.00) - 2000.00
        imposto += faixa * 0.08

    # Calcula imposto para a faixa entre R$ 3000.01 e R$ 4500 (18%)
    if salario > 3000.00:
        # Calcula o valor tributável nessa faixa
        faixa = min(salario, 4500.00) - 3000.00
        imposto += faixa * 0.18

    # Calcula imposto para valores acima de R$ 4500 (28%)
    if salario > 4500.00:
        # Calcula o valor tributável acima de R$ 4500
        faixa = salario - 4500.00
        imposto += faixa * 0.28

    # Imprime o valor do imposto formatado com 2 casas decimais
    print(f"R$ {imposto:.2f}")
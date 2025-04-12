# Recebe o nome do vendedor como uma string (texto)
vendedor = input()  # Armazena o nome do funcionário

# Recebe o salário fixo como float (permite valores decimais)
salario_fixo = float(input())  # Valor base do salário sem comissões

# Recebe o total de vendas realizadas como float (permite valores decimais)
total_vendas = float(input())  # Valor total das vendas do mês

# Calcula o salário final com bônus:
# - Bônus de 15% sobre o total de vendas (total_vendas * 0.15)
# - Equivalente a: total_vendas / (100 / 15) = total_vendas * 0.15
salario_com_bonus = salario_fixo + (total_vendas * 0.15)

# Exibe o valor total formatado:
# - Prefixo "TOTAL = R$ " indicando a moeda (Real brasileiro)
# - Valor com exatamente 2 casas decimais (padrão monetário)
print(f'TOTAL = R$ {salario_com_bonus:.2f}')
# Recebe o número do funcionário como um valor inteiro
numero_funcionario = int(input())  # Identificação única do funcionário

# Recebe a quantidade de horas trabalhadas como valor inteiro
horas_trabalhadas = int(input())  # Total de horas trabalhadas no mês

# Recebe o valor da hora trabalhada como float (permite valores decimais)
valor_por_hora = float(input())  # Valor monetário por hora de trabalho

# Calcula o salário multiplicando horas trabalhadas pelo valor de cada hora
salario = valor_por_hora * horas_trabalhadas  # Fórmula básica de cálculo salarial

# Exibe o número do funcionário (sem formatação especial)
print(f'NUMBER = {numero_funcionario}')

# Exibe o salário formatado:
# - Valor com exatamente 2 casas decimais (:.2f) para representação monetária
print(f'SALARY = U$ {salario:.2f}')
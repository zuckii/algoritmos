# Recebe um valor inteiro de dinheiro (em reais) do usuário
dinheiro = int(input())

# Exibe o valor total informado
print(dinheiro)

# Lista de valores das notas disponíveis, em ordem decrescente
valores = [100, 50, 20, 10, 5, 2, 1]

# Itera sobre cada valor de nota disponível
for valor in valores:
    # Calcula quantas notas do valor atual são necessárias
    quantidade = dinheiro // valor  # Divisão inteira
    
    # Exibe a quantidade de notas necessárias para o valor atual
    print(f"{quantidade} nota(s) de R$ {valor},00")
    
    # Atualiza o valor restante de dinheiro após usar as notas calculadas
    dinheiro %= valor  # Resto da divisão (equivalente a: dinheiro = dinheiro % valor)
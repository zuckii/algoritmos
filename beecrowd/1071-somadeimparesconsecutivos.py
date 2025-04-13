x = int(input())
y = int(input())

# Determina o menor e o maior valor para definir o intervalo
inicio = min(x, y) + 1  # Começa do menor valor +1 (para ser exclusivo)
fim = max(x, y)         # Termina no maior valor (também exclusivo)

# Variável para acumular a soma dos ímpares
soma_impares = 0

# Percorre todos os números no intervalo (exclusive)
for numero in range(inicio, fim):
    # Verifica se o número é ímpar (resto da divisão por 2 é 1)
    if numero % 2 == 1:
        soma_impares += numero  # Acumula o número ímpar na soma

# Imprime o resultado da soma
print(soma_impares)
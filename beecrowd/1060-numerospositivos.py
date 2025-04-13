numero1 = float(input())
numero2 = float(input())
numero3 = float(input())
numero4 = float(input())
numero5 = float(input())
numero6 = float(input())

# Armazena todos os números em uma lista
numeros = [numero1, numero2, numero3, numero4, numero5, numero6]

# Lista vazia para armazenar apenas os números positivos
numeros_positivos = []

# Percorre cada número na lista original
for numero in numeros:
    # Verifica se o número é positivo (maior que zero)
    if numero > 0:
        # Se for positivo, adiciona à lista de positivos
        numeros_positivos.append(numero)

# Conta quantos números positivos foram encontrados
quantidade = len(numeros_positivos)

# Imprime o resultado formatado
print(f"{quantidade} valores positivos")
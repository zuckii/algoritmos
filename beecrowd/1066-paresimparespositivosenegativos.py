numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numero5 = int(input())

# Armazena todos os números em uma lista
numeros = [numero1, numero2, numero3, numero4, numero5]

# Listas para armazenar os números classificados
valores_pares = []
valores_impares = []
valores_positivos = []
valores_negativos = []

# Classifica cada número nas categorias apropriadas
for numero in numeros:
    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        valores_pares.append(numero)
    else:
        valores_impares.append(numero)
    
    # Verifica se o número é positivo ou negativo
    if numero > 0:
        valores_positivos.append(numero)
    elif numero < 0:
        valores_negativos.append(numero)

# Conta quantos números há em cada categoria
quantidade_pares = len(valores_pares)
quantidade_impares = len(valores_impares)
quantidade_positivos = len(valores_positivos)
quantidade_negativos = len(valores_negativos)

# Exibe os resultados formatados
print(f"{quantidade_pares} valor(es) par(es)")
print(f"{quantidade_impares} valor(es) impar(es)")
print(f"{quantidade_positivos} valor(es) positivo(s)")
print(f"{quantidade_negativos} valor(es) negativo(s)")
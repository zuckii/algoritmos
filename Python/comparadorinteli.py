
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
num3 = float(input("Digite outro número: "))

numeros = [num1, num2, num3]
numeros.sort()  # Ordena a lista em ordem crescente

# Verifica se há números repetidos
if len(set(numeros)) < 3:
    print("Os números são iguais ou há números repetidos.")
else:
    print(f"{numeros[0]} < {numeros[1]} < {numeros[2]}")
numero1 = float(input())
numero2 = float(input())
numero3 = float(input())
numero4 = float(input())
numero5 = float(input())
numero6 = float(input())

numeros = [numero1, numero2, numero3, numero4, numero5, numero6]

numeros_positivos = []

for numero in numeros:
    if numero > 0:
        numeros_positivos.append(numero)
        soma = sum(numeros_positivos)
        media = soma / len(numeros)

quantidade_positivos = len(numeros_positivos)

soma = sum(numeros_positivos)
media = soma / quantidade_positivos

print(f"{quantidade_positivos} valores positivos")
print(f"{media:.1f}")
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())
numero4 = int(input())
numero5 = int(input())

numeros = [numero1, numero2, numero3, numero4, numero5]
valores_pares = []


for i in numeros:
    if (i % 2) == 0:
        valores_pares.append(i)

quantidade_pares = len(valores_pares)

print(f"{quantidade_pares} valores pares")
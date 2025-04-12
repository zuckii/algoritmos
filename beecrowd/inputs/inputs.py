# Caso simples
a = int(input())

# Mais de um valor na mesma linha:
    #Jeito 1 
linha = input().split()
valor1 = int(linha[0])
valor2 = str(linha[1])
valor3 = float(linha[2])

    # Jeito 2
valor1, valor2, valor3 = input().split()
valor1 = int(valor1)
valor2 = int(valor2)
valor3 = float(valor3)

    # Jeito 3 (caso todos os dados sejam iguais)
valor1, valor2, valor3 = map(float, input().split())

    # Jeito 4 (caso 2 ou + dados sejam iguais)
a, b, c = map(float, input().split())
c = int(c)
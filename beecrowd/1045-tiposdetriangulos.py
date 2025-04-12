A, B, C = map(float, input().split())

# Ordena os valores em ordem decrescente e reatribui às variáveis A, B, C
# (A será o maior lado, seguido por B e C)
A, B, C = sorted([A, B, C], reverse=True)

# Verifica se o maior lado (A) é maior ou igual à soma dos outros dois lados (B + C)
# Se verdadeiro, não forma um triângulo (desigualdade triangular)
if A >= (B + C):
    print("NAO FORMA TRIANGULO")
else:
    # Verifica se satisfaz o Teorema de Pitágoras (triângulo retângulo)
    if (A ** 2) == ((B ** 2) + (C ** 2)):
        print("TRIANGULO RETANGULO")
    
    # Verifica se o quadrado do maior lado é maior que a soma dos quadrados dos outros (obtusângulo)
    elif (A ** 2) > ((B ** 2) + (C ** 2)):
        print("TRIANGULO OBTUSANGULO")
    
    # Caso contrário, o triângulo é acutângulo (A² < B² + C²)
    elif (A ** 2) < ((B ** 2) + (C ** 2)):
        print("TRIANGULO ACUTANGULO")
    
    # Verifica se todos os lados são iguais (equilátero)
    if A == B == C:
        print("TRIANGULO EQUILATERO")
    
    # Verifica se pelo menos dois lados são iguais (isósceles)
    elif A == B or B == C or A == C:
        print("TRIANGULO ISOSCELES")
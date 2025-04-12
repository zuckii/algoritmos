# Lê três valores float digitados pelo usuário e atribui às variáveis a, b e c
a, b, c = map(float, input().split())

# Calcula o discriminante (delta) da equação quadrática
delta = (b * b) - (4 * a * c)

# Verifica duas condições que tornam o cálculo impossível:
# 1. Se 'a' é zero (não é equação quadrática)
# 2. Se delta é negativo (raízes complexas)
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    # Calcula a raiz quadrada do delta
    raiz_delta = delta ** 0.5
    
    # Calcula a primeira raiz usando a fórmula de Bhaskara
    bhaskara1 = (-b + raiz_delta) / (2 * a)
    
    # Calcula a segunda raiz usando a fórmula de Bhaskara
    bhaskara2 = (-b - raiz_delta) / (2 * a)
    
    # Imprime as raízes com 5 casas decimais
    print(f'R1 = {bhaskara1:.5f}')
    print(f'R2 = {bhaskara2:.5f}')
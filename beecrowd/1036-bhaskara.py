# Recebendo os valores em uma única linha e separando-os
a, b, c = map(float, input().split())

# Calculando o delta
delta = (b * b) - (4 * a * c)

# Verificando se é possível calcular Bhaskara
if a == 0 or delta < 0:
    print("Impossivel calcular")
else:
    raiz_delta = delta ** 0.5  
    bhaskara1 = (-b + raiz_delta) / (2 * a)
    bhaskara2 = (-b - raiz_delta) / (2 * a)
    
    print(f'R1 = {bhaskara1:.5f}')
    print(f'R2 = {bhaskara2:.5f}')

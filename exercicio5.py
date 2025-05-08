# inicializa a constante (poli) que tem a seguinte equação 2x³ - 3x² - 3x + 2
from random import randint
# incializa lista vazia para guardar as raizes
listaR = []

# para i de 0 até 100.000 faça:
for i in range(100000 + 1):
    # x recebe um numero aleatorio
    x = randint(-50000, 50000)
    # realize a operação matematica de poli, utilizando (x)
    poli = (2 * (x ** 3)) - (3 * (x ** 2)) - (3 * x) + 2
    # se o resultado = 0
    
    if poli == 0:
        # armazena o valor de x na lista
        listaR.append(x)

print(listaR)


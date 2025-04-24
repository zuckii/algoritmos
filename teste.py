lista = []


for i in range(11):   
    numero = int(input("Digite um numero: "))
    if numero == 0:
        break
    lista.append(numero)
    maximo = float('-inf')
    segundo_maximo = float('-inf')

    for numero in lista:
        if numero > maximo:
            segundo_maximo = maximo
            maximo = numero
        elif numero > segundo_maximo:
            segundo_maximo = numero
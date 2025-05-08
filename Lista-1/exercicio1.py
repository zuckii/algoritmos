lista = []


for i in range(11):   
    numero = int(input("Digite um numero: "))
    if numero == 0:
        break
    lista.append(numero)

    maior1 = 0
    maior2 = 0
    for numero in lista:
        if numero > maior1:
            maior2 = maior1
            maior1 = numero
        elif numero > maior2:
            maior2 = numero
    
    soma = maior1 + maior2

print("A soma dos dois maiores números é:", soma)
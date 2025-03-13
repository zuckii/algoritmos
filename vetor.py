lista = []

tam_lista = int(input("Digite o tamanho da lista: "))


def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

for i in range(tam_lista):
    numero = int(input("Digite um numero: "))
    lista.append(numero)

bubble_sort(lista)

print("Lista ordenada: ", lista)
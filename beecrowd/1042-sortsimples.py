valor1, valor2, valor3 = map(int, input().split())

# Lista com os valores na ordem original
lista_original = [valor1, valor2, valor3]

# Cria uma cópia da lista original e ordena em ordem crescente
lista_ordenada = sorted(lista_original)

# Imprime os valores em ordem crescente
for i in lista_ordenada:
    print(i)

# Linha em branco
print()

# Imprime os valores na ordem original
for i in lista_original:
    print(i)
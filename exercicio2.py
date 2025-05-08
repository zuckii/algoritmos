#Abrir o arquivo
with open("gabriel.txt", "r") as arquivo:
    #ler os valores do arquivo e armazenar em (c)
    c = arquivo.read()
    # transformar o conteúdo de (c) em uma lista de números (n)
    listaN = [int(valor) for valor in c.split()]
    
# inicializa duas variaveis ambas com o primeiro valor da lista (maior), (menor)
maior = listaN[0]
menor = listaN[0]

# percorrer os valores da (listaN)
for valor in listaN:
    # se valor > maior
    if valor > maior:
        # se valor < menor
        maior = valor
    
    if valor < menor:
        # salva em menor
        menor = valor

# salvar o valor maior e menor em outro arquivo
with open("victor.txt", "w") as arquivo:
    arquivo.write(f"{menor}, {maior}")



# Exercícios

## Questão 1

inicializa lista que vai conter os valores digitados diferentes de zero (lista)



repetir 10 vezes:
    pedir um numero (n)
    se n for diferente de 0 
        coloque n na lista
    senao
        pare a repetição

maximo = 0

for numero in lista:
    if numero > maximo:
        segundo_maximo = maximo
        maximo = numero
    elif numero > segundo_maximo:
        segundo_maximo = numero

inicializar a variavel máximo 

repetir a quantidade de valores na lista, incrementando em n
    se n > maximo

verificar o segundo valor mais alto da lista

soma-los

mostrar na tela
# Exercícios

## Questão 1

inicializa lista que vai conter os valores digitados diferentes de zero (lista)

repetir 10 vezes:
    pedir um numero (n)
    se "n" for diferente de 0 
        coloque n na lista
    senao
        pare a repetição

    inicializar a variavel maior1 e maior2, ambas valendo zero

    percorrer os numeros da lista (elemento atual = numero)
        se numero > maior1
            maior2 = maior1
            maior1 = numero
        se numero > maior2
            maior2 = numero

somar maior1 e maior2 (soma)

mostrar uma mensagem na tela ("A soma dos dois maoires numeros é (soma)")


## Questão 2 

Abrir o arquivo
Ler os valores do arquivo e armazenar em (c)

Transformar o conteúdo de (c) em uma lista de números (n)

Inicializar:
    maior = n[0]
    menor = n[0]

Para cada valor i em n:
    Se i > maior:
        maior = i
    Senão se i < menor:
        menor = i

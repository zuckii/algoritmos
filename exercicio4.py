# pedir ao usuario dois valores (base), (altura-2)
base = int(input("Digite o valor da base: ")) 
altura = int(input("Digite o valor da altura: ")) - 2

# criar a variavel (espacos = base - 2)
espacos = base - 2

# escreva (base vezes "*")
print(base * "*")

# para i de 0 até altura - 1 faça:
for i in range(altura):
    # escreva "*" + (espacos vezes " ") + "*"
    print("*" + espacos * " " + "*")

# escreva (base vezes "*")
print(base * "*")
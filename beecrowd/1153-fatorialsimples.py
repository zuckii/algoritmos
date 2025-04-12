# Inicializa a variável 'm' com o valor 1, que armazenará o resultado do fatorial
m = 1 

# Solicita ao usuário um número inteiro e armazena em 'n'
n = int(input())

# Loop que itera de 1 até 'n' (inclusive)
for i in range(1, n+1):
    m = m * i

# Imprime o resultado do fatorial (n!)
print(m)    
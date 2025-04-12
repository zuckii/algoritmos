# Recebe três valores inteiros separados por espaço e os atribui às variáveis a, b, c
a, b, c = map(int, input().split())

# Encontra o maior entre a e b usando a fórmula matemática:
# (a + b + abs(a - b)) // 2
# Isso funciona porque:
# - Se a > b: (a + b + (a - b)) // 2 = (2a) // 2 = a
# - Se b > a: (a + b + (b - a)) // 2 = (2b) // 2 = b
maior = (a + b + abs(a - b)) // 2

# Agora compara o maior encontrado (entre a e b) com c
# usando a mesma fórmula para encontrar o maior dos três
maior = (maior + c + abs(maior - c)) // 2

# Exibe o resultado formatado com a mensagem indicando o maior valor
print(f'{maior} eh o maior')
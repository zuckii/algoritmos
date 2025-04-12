# Solicita ao usuário que insira o valor do raio e converte para float
raio = float(input())

# Define o valor de π (pi) como 3.14159
π = 3.14159

# Calcula a área do círculo usando a fórmula: área = raio² * π
area = (raio ** 2) * π 

# Exibe o resultado formatado com 4 casas decimais
print(f"A={area:.4f}")
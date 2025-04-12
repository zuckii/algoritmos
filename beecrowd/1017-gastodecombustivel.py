# Lê o tempo gasto na viagem (em horas) como valor inteiro
tempo_gasto = int(input())

# Lê a velocidade média durante a viagem (em km/h) como valor inteiro
velocidade_media = int(input())

# Calcula a quantidade de combustível gasto:
# Fórmula: (velocidade_media × tempo_gasto) / autonomia_veiculo
# Onde 12 km/l é a autonomia fixa do veículo
combustivel_gasto = (velocidade_media * tempo_gasto) / 12

# Exibe o resultado com 3 casas decimais
print(f'{combustivel_gasto:.3f}')
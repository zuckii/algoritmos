from math import dist

# Lê as coordenadas dos pontos
p = tuple(map(float, input().split()))  # ponto p (x1, y1)
q = tuple(map(float, input().split()))  # ponto q (x2, y2)

# Calcula a distância usando math.dist()
distancia = dist(p, q)

# Exibe com 4 casas decimais
print(f'{distancia:.4f}')
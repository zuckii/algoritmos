A, B, C = map(float, input().split())

π = 3.14159

area_triangulo = (A * C) / 2
area_circulo = π * (C * C)
area_trapezio = ((A + B) * C) / 2
area_quadrado = B * B
area_retangulo = A * B  

print(f'TRIANGULO: {area_triangulo:.3f}')
print(f'CIRCULO: {area_circulo:.3f}')
print(f'TRAPEZIO: {area_trapezio:.3f}')
print(f'QUADRADO: {area_quadrado:.3f}')
print(f'RETANGULO: {area_retangulo:.3f}')

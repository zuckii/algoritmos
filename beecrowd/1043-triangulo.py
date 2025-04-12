A, B, C = map(float, input().split())



if A + B >= C and A + C > B and B + C > A:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")

else:
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}")

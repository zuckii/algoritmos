x1, y1 = map(float, input().split())

if x1 == 0 and y1 == 0:
    print("Origem")

elif x1 > 0 and y1 > 0:
    print("Q1")

elif x1 < 0 and y1 > 0:
    print("Q2")

elif x1 < 0 and y1 < 0:
    print("Q3")

elif x1 > 0 and y1 < 0:
    print("Q4")

elif x1 == 0 and y1 != 0:
    print("Eixo Y")

else:
    print("Eixo X")
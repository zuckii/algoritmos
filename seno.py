from math import sin, radians

delta = 80

for angulo_graus in range(0, 361):
    angulo_radianos = radians(angulo_graus)
    y = sin(angulo_radianos) * delta + delta

    print(round(y) * " " + "*") 

from math import sin, radians

delta = 80  # valor central

for angulo_graus in range(0, 361):
    angulo_radianos = radians(angulo_graus)
    y = sin(angulo_radianos) * delta + delta
    y_int = round(y)  # usa round ao invés de int

    linha = [" "] * (2 * delta + 1)
    linha[delta] = "|"  # marca o centro

    if y_int == 0 or y_int == 2 * delta:
        linha[y_int] = "#"  # caractere especial nos extremos
    else:
        linha[y_int] = "*"  # caractere normal

    print("".join(linha))

codigo, quantidade = map(int, input().split())

cardapio = [
    (1, 4.00),
    (2, 4.50),
    (3, 5.00),
    (4, 2.00),
    (5, 1.50),
]

for item in cardapio:
    if item[0] == codigo:
        total = item[1] * quantidade
        print(f"Total: R$ {total:.2f}")
        break
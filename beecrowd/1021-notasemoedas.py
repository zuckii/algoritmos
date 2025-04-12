dinheiro = float(input())

NOTAS = (100, 50, 20, 10, 5, 2)
print('NOTAS:')

for valor in NOTAS:
    quantidade = dinheiro // valor
    print(f"{quantidade:.0f} nota(s) de R$ {valor}.00")
    dinheiro %= valor 

dinheiro = round(dinheiro * 100)

MOEDAS = (100, 50, 25, 10, 5, 1) 
print('MOEDAS:')
for valor_moeda in MOEDAS:
    quantidade = dinheiro // valor_moeda 
    print(f"{quantidade:.0f} moeda(s) de R$ {valor_moeda / 100:.2f}")
    dinheiro %= valor_moeda 

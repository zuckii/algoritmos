linha = 'João da Silva,josilva@gmail.com,47 9 9234 5678'

partes = linha.split(",")

for p in partes:
    print(p)
    
print(f'Email: {partes[1]}')

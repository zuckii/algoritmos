# Recebe e divide a entrada do usuário em uma lista de strings
dados_peca1 = input().split()  
# Converte e armazena os dados da peça 1:
codigo1 = int(dados_peca1[0])          # Código único da peça (inteiro)
quantidade1 = int(dados_peca1[1])      # Quantidade comprada (inteiro)
valor_unitario1 = float(dados_peca1[2])  # Preço unitário (decimal)

# Recebe e divide a entrada do usuário em uma lista de strings
dados_peca2 = input().split()  
# Converte e armazena os dados da peça 2:
codigo2 = int(dados_peca2[0])          # Código único da peça (inteiro)
quantidade2 = int(dados_peca2[1])      # Quantidade comprada (inteiro)
valor_unitario2 = float(dados_peca2[2])  # Preço unitário (decimal)

# Cálculo do valor total 
total = (quantidade1 * valor_unitario1) + (quantidade2 * valor_unitario2)


# Exibe o resultado com
print(f'VALOR A PAGAR: R$ {total:.2f}')
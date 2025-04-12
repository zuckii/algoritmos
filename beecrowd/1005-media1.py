# Recebe o primeiro valor numérico do usuário e converte para float (permite decimais)
nota1 = float(input())

# Recebe o segundo valor numérico do usuário e converte para float (permite decimais)
nota2 = float(input())

# Calcula a média ponderada onde:
# - 'a' tem peso 3.5
# - 'b' tem peso 7.5
# A soma dos pesos é 11 (3.5 + 7.5)
media = (nota1 * 3.5 + nota2 * 7.5) / 11

# Exibe o resultado formatado com:
# - O texto "MEDIA = "
# - O valor da média com 5 casas decimais
print(f"MEDIA = {media:.5f}")
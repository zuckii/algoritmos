# Recebe três valores numéricos do usuário e converte para float (permite decimais)
nota1 = float(input())  # Primeiro valor com peso 2
nota2 = float(input())  # Segundo valor com peso 3
nota3 = float(input())  # Terceiro valor com peso 5

# Calcula a média ponderada onde:
# - A tem peso 2
# - B tem peso 3
# - C tem peso 5
# A soma dos pesos é 10 (2 + 3 + 5)
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

# Exibe o resultado formatado com:
# - O texto 'MEDIA = '
# - O valor da média com 1 casa decimal
print(f'MEDIA = {media:.1f}')
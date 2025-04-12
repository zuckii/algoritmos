# Recebe as quatro notas do aluno como valores float separados por espaço
n1, n2, n3, n4 = map(float, input().split())

# Calcula a média ponderada conforme os pesos especificados:
# n1 (peso 2), n2 (peso 3), n3 (peso 4), n4 (peso 1)
media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10 

# Exibe a média com uma casa decimal
print(f"Media: {media:.1f}")

# Verifica a situação do aluno
if media >= 7:
    print("Aluno aprovado.")
elif 5 <= media <= 6.9:  # Forma mais idiomática do Python para intervalos
    print("Aluno em exame.")
    nota_exame = float(input())  # Recebe a nota do exame de recuperação
    print(f"Nota do exame: {nota_exame}")
    
    # Recalcula a média final (média aritmética entre a média original e o exame)
    media_final = (media + nota_exame) / 2
    
    # Verifica o resultado final
    if media_final >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print(f"Media final: {media_final:.1f}")  # Exibe com uma casa decimal
else:  # media < 5
    print("Aluno reprovado.")
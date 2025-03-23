frase = "Olá tudó bem com você"
for i in frase:
    print(i)

frase = frase.replace("á", "a")
frase = frase.replace("ê", "e")
frase = frase.replace("ó", "o")

print(frase)
# Dicionário que mapeia combinações de características para animais correspondentes
animais = {
    # Vertebrados - Aves
    ("vertebrado", "ave", "carnivoro"): "aguia",
    ("vertebrado", "ave", "onivoro"): "pomba",
    
    # Vertebrados - Mamíferos
    ("vertebrado", "mamifero", "onivoro"): "homem",
    ("vertebrado", "mamifero", "herbivoro"): "vaca",
    
    # Invertebrados - Insetos
    ("invertebrado", "inseto", "hematofago"): "pulga",
    ("invertebrado", "inseto", "herbivoro"): "lagarta",
    
    # Invertebrados - Anelídeos
    ("invertebrado", "anelideo", "hematofago"): "sanguessuga",
    ("invertebrado", "anelideo", "onivoro"): "minhoca",
}

# Lê três características do animal (categoria, classe e alimentação)
palavra1 = input()  
palavra2 = input()  
palavra3 = input()  

# Busca no dicionário usando as três características como chave e imprime o animal correspondente
print(animais[(palavra1, palavra2, palavra3)])
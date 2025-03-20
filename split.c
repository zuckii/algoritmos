
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <locale.h>

int main() {
    char frase[500];

    strcpy(frase, "A legítima lingüiça, cuidadosamente frita, exibia um gosto único e freqüente nas reuniões de ürsula e suas amigas.");
    int len = strlen(frase);
    printf("Ta aqui a frase: %s\n", frase);

    for (int i = 0; (i < len-1); i++){
        // printf("%c\n", frase[i]);
        if (frase[i] == 'ü'){
            frase[i] = 'u';
            frase[i+1] = ' ';
        }
    }


    printf("Ta aqui a frase: %s", frase);
    return 0;
}
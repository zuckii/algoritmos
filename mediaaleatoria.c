#include <stdio.h>
#include <stdlib.h>

int main() {
    float s = 0;
    int i;
    srand(time(NULL));

    for (i=0; i<10; i++){
        float n = rand() % 11;
        printf("%.1f\n", n);
        s += n;
    }
    float m = s / 10;
    printf("A média é: %.1f\n", m);
    return 0;
}
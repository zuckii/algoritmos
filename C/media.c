#include <stdio.h>


int main(){
    int i=1;
    int s = 0;

    for(i; i<=10; i++) {
        printf("Digite o n%d\n", i);
        int n;
        scanf("%d", &n);
        s += n;
        printf("A soma e igual a: %d\n", s);
    }
    int m = s/10;
    printf("A media e: %d\n", m);
    return 0;
}
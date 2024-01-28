#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
    int nombre1 , nombre2 , resultat= 0;

    printf("Choisissez un premier nombre entier:\n");
    scanf("%d", &nombre1);

    printf("Merci !Maintenant choisissez un deuxième nombre entier:\n");
    scanf("%d", &nombre2);

    resultat = nombre1 + nombre2;

    printf("%d + %d = %d\n", nombre1, nombre2, resultat);

    return resultat;
}


#include <stdlib.h>
#include <stdio.h>

int menu()
{
    int choix = 0;

    while(choix < 1 || choix > 4)
    {
        printf("Menu :\n");
        printf("1 : Poulet de dinde aux escargots rotis a la sauce bearnaise\n");
        printf("2 : Concombres sucres a la sauce de myrtilles enrobee de chocolat\n");
        printf("3 : Escalope de kangourou saignante et sa gelee aux fraises poivree\n");
        printf("4 : La surprise du Chef (j'en salive d'avance...)\n");
        printf("Votre choix ? ");
        scanf("%d",&choix);
    }

    return choix;
}

int main(int argc, char *argv[])
{
    switch(menu())
    {
        case 1:

            printf("Vous avez choisi le poulet de dinde aux escargots rotis a la sauce bearnaise\n");
            break;

        case 2:

            printf("Vous avez choisi le concombres sucres a la sauce de myrtilles enrobee de chocolat\n");
            break;

        case 3:

            printf("Vous avez choisi le escalope de kangourou saignante et sa gelee aux fraises poivree\n");
            break;

        case 4:

            printf("Vous avez choisi la surprise du Chef (j'en salive d'avance...)\n");
            break;
    }

    return 0;
}

/*
int nombredemande = 0;

while (nombredemande != 3)
{
    printf("tapez 3");
    scanf("%d", &nombredemande);
}
*/
/*
int triple(int nombre)
{
    return 3 * nombre;
}

int main(int argc, char *argv[])
{
    int nombre = 0, nombretriple = 0;
    printf("Choisi un nombre : ");
    scanf("%d", &nombre);

    printf("Le triple du nombre choisi est : %d", triple(nombre));

    return 0;
}
*/

/*
double airerectangle(double largeur ,double longueur)
{
    double aire = 0;

    aire = largeur * longueur;
    printf("Rectangle de largeur %f et hauteur %f. Aire = %f\n", largeur,longueur,aire);


}

int main(int argc, char *argv[])
{
    airerectangle(5, 10);
    airerectangle(2.5, 3.5);
    airerectangle(4.2, 9.7);

    return 0;
}
*/
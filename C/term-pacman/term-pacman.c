#include <curses.h>
#include <stdlib.h>

// constantes graphisme
#define PACMAN 'C'
#define FANTOME 'M'
#define PASTILLE '·'
#define MUR '#'
#define VIDE ' '

// constantes labyrinthe
#define LARGEUR 60
#define HAUTEUR 20

// variables globales
char labyrinthe[HAUTEUR][LARGEUR];
int joueur_x; 
int joueur_y;

void init_jeu(void)
{
    // murs extérieurs du labyrinthe
    for (int i = 0; i < HAUTEUR; i++)
    {
        for (int j = 0; j < LARGEUR; j++)
        {
            if (i == 0 || i == HAUTEUR - 1 || j == 0 || j == LARGEUR - 1)
            {
                labyrinthe[i][j] = MUR;
            }
            else
                labyrinthe[i][j] = VIDE;
        }
    }

    // position de départ du joueur
    joueur_x = LARGEUR / 2; // c’est la hauteur qui correspond aux lignes (position x)
    joueur_y = HAUTEUR / 2; // c’est la largeur qui correspond aux colonnes (position y)
    labyrinthe[joueur_y][joueur_x] = PACMAN;
 } 


void update(int t)//char t)
{
    int dx = 0;
    int dy = 0;
    int test_x;
    int test_y;

    switch (t)
    {
        case KEY_UP://'A':
            dy = -1;
            break;
        case KEY_DOWN://'B':
            dy = 1;
            break;
        case KEY_RIGHT://'C':
            dx = 1;
            break;
        case KEY_LEFT://'D':
            dx = -1;
            break;
    }

    labyrinthe[joueur_y][joueur_x] = VIDE;
    
    test_x = joueur_x + dx;
    test_y = joueur_y + dy; 

    if (test_x > 0 && test_x < LARGEUR - 1)
    {
        joueur_x = test_x;
    }
    if (test_y > 0 && test_y < HAUTEUR - 1)
    {
        joueur_y = test_y;
    }

    labyrinthe[joueur_y][joueur_x] = PACMAN;
}


 void draw(void)
 {
    clear();
    for (int i=0; i < HAUTEUR; i++)
    {
        for (int j=0; j < LARGEUR; j++)
        {
            printw("%c", labyrinthe[i][j]);
        }
        printw("\n");
    }
 }


 int main(void)
 {
    int touche; //char touche;

    initscr();
    noecho(); // pour ne pas afficher les touches quand elles sont pressées
    keypad(stdscr, TRUE); // pour accéder directement aux codees des touches spéciales (flèches notamment)
    init_jeu();
    printw("Presser la touche j pour lancer le jeu.\nAppuyez sur une autre touche pour quitter immédiatement.\n");
    touche = getch();
    printw("%c", touche);
    if (touche != 'j' && touche != 'J')
    {
        endwin();
        return EXIT_SUCCESS;
    }

    while(1)
    {
        draw();
        touche = getch();

        if (touche == 'q') 
        {
            printw("\nAbandon : appuyez sur une touche pour quitter définitivement");
            getch();
            endwin();
            return EXIT_SUCCESS;
        }
        else
            update(touche);
    }
 }
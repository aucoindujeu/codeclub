#include <ncurses.h>
#include <stdlib.h>

int main(void)
{
    initscr(); // initialise la structure WINDOW et autres paramètres
    
    printw("Test : ncurses fonctionne !\nAppuyer sur une touche pour quitter"); // écrit à la position du curseur logique

    refresh(); // rafraichit la fenêtre courante (pour voir le message)

    getch(); // attent l’appui sur une touche 

    endwin(); // restaure les paramètres par défaut du terminal

    return EXIT_SUCCESS; // on quitte sans erreur
}
# Game of Life

Le Game of Life (jeu de la vie) est un jeu un peu particulier dans le sens où il n'y a ni perdant, ni gagnant. Le but est simplement de prendre du plaisir à voir la vie évoluer.

## Rules of Life

Dans ce jeu, le monde est divisé en un damier régulier de cellules. Chaque cellule peut être dans deux état différents : vivante ou morte. Une cellule vivante peut mourir, mais elle peut aussi se propager à d'autres cellules. Cette évolution se fait en fonction de l'état des 8 cellules voisines. (situées au-dessous, en dessous, à gauche, à droite et en diagonale). Chaque changement d'état se fait selon les règles suivantes :

1. Toute cellule vivante ayant moins de deux voisines vivantes meurt (de sous-population).
2. Toute cellule vivante ayant deux ou trois voisines vivantes continue à vivre.
3. Toute cellule vivante ayant plus de trois voisines vivantes meurt (de sur-population).
4. Toute cellule morte ayant exactement trois voisines vivantes devient vivante (par reproduction).

## Préambule

En suivant les règles du jeu de la vie, est-ce que vous pouvez prédire quelle est l'évolution des structures suivantes ? (blanc=vivant, noir=mort).

Barre verticale de taille 3 :

    ⬛⬛⬛
    ⬛⬜⬛
    ⬛⬜⬛
    ⬛⬜⬛
    ⬛⬛⬛

Barre horizontale de taille 3 :

    ⬛⬛⬛⬛⬛
    ⬛⬜⬜⬜⬛
    ⬛⬛⬛⬛⬛

Carré 2x2 :

    ⬛⬛⬛⬛
    ⬛⬜⬜⬛
    ⬛⬜⬜⬛
    ⬛⬛⬛⬛

C'est compris ? Allez on enchaîne.

## C'est parti

### Installation de Python (sous Windows)

Téléchargez le fichier suivant et exécutez-le : https://www.python.org/ftp/python/3.12.6/python-3.12.6-amd64.exe

Lors de l'installation, cochez bien la case "Add Python to PATH".

Une fois que l'installation est terminée, ouvrez une invite de commande (cmd). Exécutez la commande suivante :

    python --version

Cela devrait afficher "Python 3.12.6".

### Création d'un environnement virtuel (virtualenv)

Dans votre invite de commande (aussi appelée : terminal), changez de répertoire pour vous placer à un endroit sur le disque où vous mettrez le code source de votre jeu. Pour faire cela, vous allez devoir faire un copieux usage de la commande "cd" et de la touche "TAB" (les deux flèches à gauche du clavier).

Une fois que vous êtes dans le bon répertoire, créez un environnement virtuel avec la commande :

    python -m venv venv

Puis activez cet environnement virtuel avec:

    venv\Scripts\activate.bat

(encore une fois, un copieux usage de TAB est recommandé)

**A quoi ça sert ?** Un environnement virtuel va nous permettre d'installer tout un tas de logiciels sans affecter le reste du système d'exploitation. Pour être plus précis, ça va nous permettre d'installer des _packages_ Python, qui sont des bouts de code réutilisables par d'autres logiciels. On appelle ça aussi des "librairies" ou des "modules". Dans notre cas particulier, on va utiliser notre environnement virtuel pour installer [Pygame (https://www.pygame.org)](https://www.pygame.org) et [Pygame-Zero (https://pygame-zero.readthedocs.io/)](https://pygame-zero.readthedocs.io/). Pygame est un moteur de jeu pour Python, et Pygame-Zero est une surcouche (facultative) de Pygame qui permet de l'utiliser de manière un peu plus simple.

### Installation de pygame-zero

Toujours dans votre terminal, exécutez la commande :

    python -m pip install pgzero

(vous aurez besoin d'un accès à Internet pour que cette commande fonctionne.)

Créez un fichier vide nommé "gameoflife.py" dans ce répertoire. Puis exécutez la commande :

    pgzrun gameoflife.py

Si tout se passe bien, vous devriez voir une fenêtre toute noire intitulée "Pygame Zero Game". A ce stade, vous n'êtes pas encore Game Dev, mais vous êtes vraiment plus très loin.

Dans la suite, on va beaucoup utiliser ce moteur de jeu qui s'appelle "Pygame Zero". Et donc vous allez avoir bien besoin de sa [documentation : https://pygame-zero.readthedocs.io/en/stable/index.html](https://pygame-zero.readthedocs.io/en/stable/index.html).

### You're gonna need a bigger window

Dans ce fichier gameoflife.py, on va mettre le code source de notre jeu. Ouvrez ce fichier dans votre éditeur de texte favori (en espérant que ça ne soit pas Word). On vous recommande [VSCodium (https://vscodium.com)](https://vscodium.com) ou [Zed (https://zed.dev)](https://zed.dev).

Dans ce fichier, créez deux variables `WIDTH` et `HEIGHT` : donnez-leur des valeurs entières (éventuellement différentes) comprises entre 10 et 1000.

Exécutez à nouveau votre jeu. Félicitations ! Vous êtes maintenant Game Dev (junior).

### La vie en couleur

Créez une fonction nommé `draw`. Cette fonction ne prend aucun argument. A l'intérieur de cette fonction, faites appel à la fonction [`screen.fill`](https://pygame-zero.readthedocs.io/en/stable/builtins.html#Screen.fill). Cette fonction prend comme argument un tuple composé de trois valeurs entières. Chaque valeur est comprise entre 0 et 255. En faisant varier ces valeurs, et en exécutant à chaque fois votre code, essayez de comprendre à quoi elles correspondent.

### Le monde se divise en deux catégories

Toujours à l'intérieur de votre fonction `draw`, mais après l'appel à `screen.fill`, ajoutez un appel à la fonction [`screen.draw.line`](https://pygame-zero.readthedocs.io/en/stable/builtins.html#Screen.draw.line), comme ceci :

    screen.draw.line((WIDTH/2, 0), (WIDTH/2, HEIGHT), (0, 0, 0))

Un carambar lorque vous comprenez à quoi correspond chaque argument de cette fonction.

Blague à part, vous devriez commencer à comprendre le système de coordonnées utilisé par Pygame (et tous les moteurs de jeu du monde en fait). C'est très important pour la suite de comprendre quels sont l'abscisse et l'ordonnée de notre repère de travail.

### Le monde se divise en `WIDTH*HEIGHT/CELL_SIZE**2` catégories

Créez une variable globale `CELL_SIZE` avec une valeur entière de votre choix. Tracez des lignes pour que votre fenêtre soit divisée en rangées verticales toutes de largeur `CELL_SIZE`. Puis dessinez les lignes horizontales, de sorte à obtenir un quadrillage régulier de taille `CELL_SIZE`.

(moins de cellules ne voudra pas dire moins de travail pour vous)

Créez deux variables `CELL_COUNT_X` et `CELL_COUNT_Y` égales au nombre de cellules sur l'axe x et sur l'axe y.

### Colorier sans dépasser les traits

Prenez une case au hasard. Coloriez-la avec la couleur que vous voulez. Pour cela, vous allez devoir utiliser la fonction [`screen.draw.filled_rect`](https://pygame-zero.readthedocs.io/en/stable/builtins.html#Screen.draw.filled_rect). Son premier argument est un objet de type `Rect` (un rectangle). On crée un rectangle comme ça :

    Rect((x, y), (w, h))

Où `(x, y)` sont les coordonnées du coin en haut à gauche du rectangle, `w` la largeur du rectangle, et `h` sa hauteur.

Le second argument de `screen.draw.filled_rect` est une couleur, comme pour `screen.fill` et `screen.draw.line`.

### Life... finds a way

Créez une variable `CELLS` de type dictionnaire. Cette variable va contenir le statut (vivant ou mort) de chacune des cellules. Au début, toutes les cellules seront mortes. Pour `x` compris entre 0 et `CELL_COUNT_X` (exclu) et `y` compris entre 0 et `CELL_COUNT_Y` (exclu), on va écrire :

    CELLS[(x, y)] = 0

Faites ceci pour toutes les valeurs possibles de x, y. Indice : vous allez (probablement) devoir utiliser une double boucle `for`.

Choisissez une cellule, à peu près vers le milieu du damier, et donnez-lui la vie :

    CELLS[(votre_valeur_de_x, votre_valeur_de_y)] = 1

### Living pixels

Utilisez le bout de code que vous avez écrit dans "Colorier sans dépasser les traits" pour afficher à l'écran toutes les cellules vivantes. Pour cela, vous allez devoir :

1. Parcourir toutes les valeurs possibles de x, y.
2. Lire la valeur de `CELLS[(x, y)]`.
3. Si cette valeur est 1, alors afficher un rectangle vivant à l'emplacement correspondant à celui de la cellule. Sinon, afficher un rectangle mort.

### Smoke check

Vérifiez que votre code fonctionne correctement en donnant la vie à huit cellules alignées verticalement vers le milieu de l'écan :

    ⬛⬛⬛⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬛⬛⬛

## gg

OK c'est parti pour le morceau de résistance ! Dans cette section on va implémenter l'algorithme de la vie de Conway décrit dans l'introduction.

Pour chacune des cellules, on va compter le nombre de voisins vivants. En fonction du résultat, on va changer (ou pas) le statut de la cellule.

Pour ça, on va créer une fonction `update`. Cette fonction sera automatiquement appelée à chaque frame, juste avant `draw`. C'est dans cette fonction qu'on va mettre tout le code qui suit.

On va commencer par créer une copie de `CELLS` : `new_cells = CELLS.copy()`.

C'est entre ces deux lignes de code qu'on va examiner toutes les cellules une par une et modifier `new_cells`.

On va commencer par ignorer les cellules sur le bord, qui vont nous causer un peu de fil à retordre (vous voyez pourquoi ?). Donc on va regarder toutes les cellules `(x, y)` pour x dans `[0, CELL_COUNT_X-1[` et y dans `[0, CELL_COUNT_Y-1[`.

Pour chacune de ces cellules, on va regarder ses huit voisins et compter le nombre de cellules vivantes. Là aussi vous allez devoir utiliser une (ou deux) boucles `for`. Puis, en fonction du nombre de cellules voisines vivantes et de la valeur `CELLS[(x, y)]`, vous allez définir la valeur de `new_cells[(x, y)]`.

Pour terminer, tout à la fin de notre fonction `update`, on va copier les nouvelles valeurs dans `CELLS` avec : `CELLS.update(new_cells)`.

Voilà, c'est tout :) Si vous avez correctement écrit votre code, vous devriez voir les cellules naître et mourir.

**Question bonus fastoche** : l'affichage change au rythme de 60 frames par seconde, ce qui est beaucoup trop rapide pur voir quoi que ce soit. Vous pouvez changer la vitesse d'affichage en forçant Python à faire une pause au début de votre fonction `update`. Par exemple grâce à la fonction `sleep` du module `time` de Python.
**Question bonus chouïa plus dure** : est-ce que vous voyez pourquoi est-ce qu'on ne peut pas modifier directement `CELLS` plutôt que de s'enquiquiner avec la variable `new_cells` ?
**Question giga bonus** : dans cette implémentation, les cellules sur le bord ne peuvent jamais être vivantes. Est-ce que vous voyez comment faire autrement ? Indice : la Terre est ronde. Indice 2 : `94 % 80 == 14`.

### Let's play

Ce jeu de la vie est bien beau, mais il ne permet pas d'interaction avec les joueurs, ce qui est tout de même dommage. Nous vous proposons d'ajouter les fonctionnalités suivantes :

1. Lorsque la touche "espace" est pressée, le jeu est mis en pause. Et quand on appuie à nouveau sur cette touche, on relance le jeu.
2. Lorsque l'on clique sur une cellule vivante, alors cette cellule est tuée (et inversement).

Pour implémenter ces fonctionnalités, vous aurez besoin d'utiliser les fonctions suivantes :

1. [`on_key_down`](https://pygame-zero.readthedocs.io/en/stable/hooks.html#on_key_down) : lorsque le premier argument passé à cette fonction est égal à `keys.SPACE` alors il faut modifier une variable globale booléenne `PAUSE_GAME`. Et quand cette variable globale est égale à vraie, alors il ne faut pas exécuter le contenu de la fonction `update`.
2. [`on_mouse_down`](https://pygame-zero.readthedocs.io/en/stable/hooks.html#on_mouse_down) : le premier argument passé à cette fonction est la position de la souris, qu'il va falloir convertir en position `(x, y)` de cellule. Puis, changer la valeur de `CELLS[(x, y)]`.

### Die Hard : 1103 générations pour vivre

Le schéma suivant s'appelle "r-penthomino" et fait partie de la catégorie des "Mathusalem". Savez-vous pourquoi ?

    ⬛⬛⬛⬛⬛
    ⬛⬛⬜⬜⬛
    ⬛⬜⬜⬛⬛
    ⬛⬛⬜⬛⬛
    ⬛⬛⬛⬛⬛

### Voilà

C'est tout.

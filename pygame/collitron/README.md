# Collitron

Dans ce petit atelier conçu pour une séance courte, on va découvrir les concepts suivants :

* 🍎 Le modèle physique de la chute des corps
* 💥 Détection de collisions avec les bords
* 🔀 Génération de nombres aléatoires

Le but de l'atelier est d'afficher des balles colorées qui rebondissent sur les quatre bords de l'écran.

## C'est de la balle

On commence doucement en créant une balle qui a une position, une vitesse, un rayon et une couleur. Ces valeurs sont stockées dans une liste :

    BALLE = [...]

Au début, la balle est au centre de l'écran, avec une vitesse nulle et une couleur de votre choix. A vous de décider comment stocker ces valeurs.

N'oubliez pas que pour créer un écran, il faut créer deux variables `WIDTH` et `HEIGHT` !

## I'm having a ball

Maintenant qu'on a une balle, on va l'afficher. Pour ça, on créer la fonction `draw`, qui ne prend aucun argument. Cette fonction va devoir appeler la fonction [screen.draw_filled_circle](https://pygame-zero.readthedocs.io/en/stable/builtins.html#Screen.draw.filled_circle) qui prend trois arguments:

     screen.draw.filled_circle(
        (x, y),     # position
        rayon,      # rayon
        (r, g, b)   # couleur
    )

Notez que vous allez avoir besoin plus tard du rayon de la balle, donc autant le stocker dans une variable `RAYON` dédiée.

A ce stade, vous devriez avoir votre balle qui s'affiche à l'écran 🥳 Prenez un moment pour vous auto-congratuler.

## Laisse tomber

Dans le monde réel, sur Terre, une balle lâchée avec une vitesse nulle tombe. C'est ce qu'on va faire dans cette étape : la position et la vitesse de la balle vont changer en fonction de la gravité et de la masse de la balle, qu'on va définir à l'aide de ces variables :

    GRAVITE = 9.81
    MASSE = 1

On va créer la fonction `update` qui prend un argument `dt`. Cette fonction est appelée en continue par Pygame, juste avant la fonction `draw`. L'argument `dt` indique la durée qui s'est écoulée depuis la dernière fois que la fonction `update` a été appelée.

Avec ces informations, comment modifier la composante `y` de la position et de la vitesse de la balle en fonction du temps écoulé `dt`, de la gravité et de la masse ?

Si vous n'avez jamais fait de mécanique en physique, alors n'hésitez pas à demander des infos autour de vous.

## C'est dans la boîte

A ce stade, vous avez une balle qui tombe, mais le problème c'est qu'elle quitte l'écran. On va donc la faire rebondir sur le bord inférieur, en appliquant l'algorithme suivant.

Quand le bord inférieur de la balle dépasse le bord inférieur de l'écran, alors :

1. On remonte la balle de sorte qu'elle ne touche pas le bord inférieur.
2. On transforme la composante `y` de son vecteur vitesse en son opposé.

## What happens in the box stays in the box

En suivant la même méthode, faire en sorte de faire rebondir la balle sur les trois autres bords de l'écran. Attention : cuand la balle touche le bord gauche ou droit, c'est la composante `x` de sa vitesse dont il faut prendre la valeur opposée.

Vérifiez que votre balle rebondit bien sur les côtés en donnant une valeur non nulle à la composante `x` de la vitesse initiale.

## And now for something completely different

Modifiez votre code de sorte que la balle soit initalisée, au début de la partie, avec des valeurs aléatoires de position, vitesse et couleur.

Pour cela, vous aurez besoin du module [`random`](https://docs.python.org/3/library/random.html) de Python, et en particulier des fonctions suivantes :

    import random

    random.random()         # retourne une valeur aléatoire dans [0, 1[
    random.randint(0, 100)  # retourne un entier aléatoire dans [0, 100]

## Extra ball

Modifiez votre code pour faire apparaître 100 balles différentes, toutes initialisées avec des valeurs aléatoires différentes.

# Atelier 2 : Déplacer une image

Nous avons vu dans le premier atelier comment afficher des éléments (textes, formes, images) à l’écran, à des positions précises. Ces images étaient figées, alors que dans un jeu vidéo, elles bougent (animation), parfois très rapidement.

En fait ce n’est pas une grosse difficulté : une animation n’est jamais qu’une succession d’image figées, à un rythme élevée avec un léger décalage des éléments mobiles sur chaque image qui donne alors l’illusion du mouvement. Traditionnellement 24 images par seconde au cinéma, 12 images/s. pour beaucoup de dessins animés, mais plutôt autour de 60 images/s. dans les jeux vidéos (voire plus selon la puissance de la machine).

Nous savons afficher des images figées. Nous savons indiquer la position des éléments et la faire varier si besoin grâce à des calculs sur des… variables (précisément). Il suffit de trouver comment afficher cette succession d’image en quelques fractions de seconde. Pas de soucis, c’est prévu “par construction” dans Löve 2D, et c’en est en fait c’est le principal intérêt de ce type de framework : rendre “transparente” la programmation de ce genre de mécanisme.

C’est facile à faire, mais c’est un peu plus difficile à comprendre : prends bien le temps d’assimiler cet atelier il est très important pour la suite.

## La fonction love.update()

En fait la fonction love.draw() affiche déjà les images à l’écran un certain nombre de fois par seconde (et elles s’effacent entre temps). On peut donc se dire que si on affiche un rond en décalant petit à petit son centre, on aurait l’impression qu’il se déplace.

Mais si on fait ça :

```lua
function love.draw()
  centreX = 10
  centreY = 10
  love.graphics.circle(centreX, centreY, 10)
  centreX = centreX + 5 -- on décale horizontalement le centre du rond
  love.graphics.circle(centreX, centreY, 10)
end
```

Qu’obtient-on ? Un rond qui se déplace ou autre chose ? Pourquoi ? (réfléchis bien…)

En fait comme on l’a dit dans l’atelier précédent, à l’intérieur de love.draw() on ne peut que donner des indications sur l’affichage d’un image ou d’éléments, mais on ne peut pas faire évoluer ces éléments. Dans l’exemple ci-dessus on donne en fait des instructions pour afficher 2 cercles, et pas un cercle qu’on va modifier.

En fait il faudrait modifier la position du rond en dehors de love.draw(). Mais pas n’importe où : il faut que ça soit juste avant que love.draw() soit exécutée, et pour ça on a la fonction love.update(). C’est une fonction qui est exécutée des dizaines de fois chaque seconde (selon la puissance de l’ordinateur) et qui est conçue pour permettre des modifications des éléments du jeux avant qu’ils ne soient affichés. Il ne reste plus qu’à afficher une seule fois notre rond dans love.draw()

Essayons :

```lua
function love.update()
  centreX = 10
  centreY = 10
  
  centreX = centreX + 5 --  on décale horizontalement le centre du rond
end
  
function love.draw()
  love.graphics.circle("fill", centreX, centreY, 10)
end
```

Mais ça ne marche pas ! As-tu une idée de pourquoi ? (un indice : l’ensemble de la fonction .update() est exécutée des dizaines de fois par seconde… regarde bien toutes les instructions, que se passe-t-il alors ?)

Essayons comme ça :

```lua
centreX = 10
centreY = 10

function love.update(dt)
  centreX = centreX + 5 --  on décale horizontalement le centre du rond
end
  
function love.draw()
  love.graphics.circle("fill", centreX, centreY, 10)
end
```

Pourquoi ça marche (à peu près) cette-fois ci ? Que déduis-tu de ce qu’il se passe pour les instructions qui sont en dehors de .update() et de .draw() ? Combien de fois sont-elle exécutées ?

Par contre quel est le problème ?

Oui, ça va trop vite !

Comment ralentir la balle ? Essaye de proposer une solution.

En fait il y a une technique “propre”, mais propose ta solution d’abord, ça peut marcher.

Quelle est la technique qu’il faut employer de préférence ? Il s’agit d’utiliser un paramètre qu’on appelle “deltatime”. C’est le “dt” que tu vois en paramètre de la fonction .update(dt). Mais qu’est-ce que ça peut bien être ?

## Le deltatime (dt)

Attention, c’est compliqué, pas toujours très intuitif, mais essentiel ! Prends le temps de lire lentement, et fait des schémas au besoin.

Nous avons dit que les fonctions .update() et .draw() sont exécutées de nombreuses fois par seconde. Mais on ne sait pas exactement combien, car ça dépend de la puissance de la machine.

Afin de donner une indication à ce sujet au programmeur, Löve donne **la valeur deltatime qui est simplement le temps écoulé entre chaque affichage.**

Si par exemple l’ordinateur affiche avec .draw ou exécute .update() 60 fois par seconde, alors on a :

dt = 1 seconde / 60 =  0.016666666… secondes

Si l’affichage est de 30 images par secondes (2 fois plus lent) :

dt = 1 seconde / 30 = 0.03333333… secondes (ce qui fait 2 fois plus).

Donc si l’on veut que sur n’importe quel ordinateur le rond se déplace de par exemple 50 pixels chaque seconde (donc la même vitesse de déplacement sur tous les ordinateurs), dans .update() on va simplement dire qu’on décale la position du centre du rond de 50 * dt :

```lua
function love.update(dt)
  centreX = centreX + 50 * dt --  on décale horizontalement le centre du rond
end
```

En effet, à chaque affichage, de combien de pixel se sera décalé le rond sur un ordinateur à 60 images/s. ?

C’est facile, le rond sera affiché 50 * 0.016666666… = 0.833333… pixels plus loin

Mais au bout d’une seconde, à ce rythme, combien de pixels le rond aura-t-il parcouru ? Et bien : 0.8333333 * 60 soit 50 pixels !

Fait les mêmes calculs pour un ordinateur qui est deux fois moins rapide (dt = 0.03333333…) :

De combien de pixel le rond sera décalé à chaque affichage ?

Combien de pixels le rond aura parcouru au bout d’une seconde ?

Ainsi sur un ordinateur deux fois moins puissant, le rond aura parcouru la même “distance” en 1 seconde, mais comme il y a deux fois moins d’étapes, la distance parcouru à chaque étape est deux fois plus longue.

L’animation aura donc lieu à la même “vitesse” sur les deux machines, mais sera plus fluide sur la machine la plus rapide.

Programme le déplacement de plusieurs formes ou images, à différentes vitesses, dans différentes direction (par exemple un triangle verticalement à 20 pixels/seconde, un rectangle en diagonale à 100 pixels secondes, un cercle horizontalement à 3, etc.)

Tu peux aussi faire varier les paramètres d’autres fonctions graphiques pour avoir des effets sympa, par exemple avec la fonction .setColor() :

```lua
centreX = 10
centreY = 20
rouge = 0
vert = 0
bleu = 1

function love.update(dt)
  centreX = centreX + dt*60 --  on décale horizontalement le centre du rond
  rouge = rouge + dt * 0.1 -- on change doucement les composantes de couleur
  vert = vert + dt * 0.05
  bleu = bleu - dt * 0.08
end

function love.draw()
  love.graphics.setColor(rouge, vert, bleu)
  love.graphics.circle("fill", centreX, centreY, 10) 
end
```

Par exemple, modifie aussi le paramètre alpha de .setColor(), ou .setBackground(), le paramètre rotation ou zoom d’une image (et ça permet de réviser comment on affiche un fichier image), etc.

Entraîne-toi ! Penser à utiliser dt dès que tu déplaces ou modifie une image (et que tu veux que ce soit fait dans un temps prédéfini) doit devenir un réflexe !

## Les conditions

Tu auras remarqué que notre rond dans l’exemple précédent file dans une direction jusqu’à sortir de l’écran… puis notre programme continue de tourner sans plus rien afficher.

C’est parce que nous indiquons qu’il faut augmenter la valeur de la coordonnée x par exemple, sans dire quand arrêter : l’ordinateur le fera donc jusqu’à l’infini (en général jusqu’à ce que la mémoire soit pleine).

Pour lui dire d’arrêter, ou de faire autre chose (par exemple changer la direction de la balle) il faut poser une condition. Par exemple dire : on arrête d’avancer le rond dès qu’il a parcouru 300 pixels.

Une manière de faire serait :

```lua
centreX = 10
centreY = 20

function love.update(dt)
  if centreX < 300 then
    centreX = centreX + dt*60 --  on décale horizontalement le centre du rond
  end
end

function love.draw()
  love.graphics.circle("fill", centreX, centreY, 10) 
end
```

Quelle condition faudrait-il mettre pour que la balle s’arrête *exactement* au bord de l’écran (le bord de la balle touche le bord de la fenêtre, pas plus, pas moins ) ?

Indice : tu peux connaître les dimensions de la fenêtre avec les fonctions love.graphics.getWidth() et love.graphics.getHeight()

## Défis

- Tu peux imaginer des trajectoires plus intéressantes que des trajectoires linéaires, en utilisant plus d’une seule variable et des équations ou des fonctions mathématiques (cercle, ellipse, sinusoïde…) ou des équation de physique pour des objets qui tombent, avec une inertie, une accélération/décélération, etc.
- Essaye d’imaginer un effet “démo” pour faire rebondir les lettres d’un texte par exemple et des changements de couleurs cycliques, ou de zoom, des rotations…
- On a vu comment faire s’arrêter une balle quand elle arrive au bord de la fenêtre. Pourrais-tu imaginer un moyen de la faire partir dans une autre direction quand elle touche le bord de la fenêtre ? Si tu y arrives, tu auras déjà fait une partie de l’atelier collision !

## Prochaine étape

Comme on l’a vu sur le dernier défi, en matière de jeux vidéo, si on déplace des éléments, on a envie de gérer leurs interactions. Mais avant ça, c’est peut-être plus fun d’interagir en tant que joueur-euse avec ces éléments ! Voyons donc d’abord comment on peut contrôler ce qu’il se passe dans notre programme avec le clavier, la souris ou une manette, de manière interactive !

[Atelier 3 : Contrôles](Atelier%203%20Contro%CC%82les.md)

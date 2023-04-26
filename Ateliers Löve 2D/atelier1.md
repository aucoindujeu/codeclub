# Atelier 1 : Affichage avec Löve

La première chose que nous allons apprendre à faire est d’afficher des choses (textes, graphismes) à l’écran, car un jeu vidéo est presque tout le temps basé sur un affichage.

## La fonction love.draw()

Toutes les instructions pour afficher quelque chose à l’écran (image, texte, etc.) doivent apparaître dans cette fonction.

Pour créer une fenêtre, crée un dossier de ton choix (par exemple Atelier_Affichage/) puis dans ce dossier un fichier main.lua avec un éditeur de texte.

La fonction love.draw() se présente comme suit :

```lua
function love.draw()

 -- <instructions pour afficher des trucs>

end
```

Si tu lances ce programme (dans le gestionnaire de fichier : glisser/déposer le répertoire sur un raccourci vers Löve, soit dans un terminal en tapant : “> love <nom_du_dossier>” , tu devrais voir apparaître une fenêtre, avec une dimension par défaut (800x600) et le titre “Untitled” (nous verrons plus tard comment changer ces paramètres).

En fait même sans .draw(), avec un fichier main.lua vide, le programme créerait une fenêtre.

Bien sûr, pour le moment il n’y a rien dans cette fenêtre : on n’a rien demandé à afficher !  Mais voyons comment afficher des trucs dans cette fenêtre.

## Afficher du texte

Modifie le fichier main.lua pour avoir le code suivant :

```lua
function love.draw()

  love.graphics.print("Texte à afficher.")

end
```

Si tu exécutes ce code, tu devrais voir une fenêtre apparaître avec le texte “Texte à afficher”.

Maintenant essaye :

```lua
function love.draw()

  love.graphics.print("Texte à afficher.", 10, 20)

end
```

Modifie les paramètres de la fonction .print() pour voir comment l’affichage est impacté, notamment les valeurs chiffrées. Après expérimentation, que peux-tu en déduire sur la manière donc on positionne un objet à afficher dans la fenêtre ?

### Couleurs

Apportons un peu de couleur avec la fonction .setColor() :

```lua
function love.draw()
  love.graphics.setColor(1, 0, 0)
  love.graphics.print("Texte en rouge.", 10, 0)

  love.graphics.setColor(0, 1, 0)
  love.graphics.print("Texte en vert.", 10, 15)

  love.graphics.setColor(0, 0, 1)
  love.graphics.print("Texte en bleu.", 10, 30)

  love.graphics.setColor(1, 1, 1)
  love.graphics.print("Texte en blanc.", 10, 45)

  love.graphics.setColor(.2, .2, .2)
  love.graphics.print("Texte en gris foncé.", 10, 60)

  love.graphics.setColor(.8, .8, .8)
  love.graphics.print("Texte en gris clair.", 10, 75)

  love.graphics.setColor(.3, 0, 0)
  love.graphics.print("Texte en rouge foncé.", 10, 90)

  love.graphics.setColor(0, 0, .8)
  love.graphics.print("Texte en bleu clair.", 10, 105)

end
```

Expérimente encore pour voir comment on modifie les couleurs.

Attention ! une fois que tu as modifié la couleur d’affichage, tout ce qui suit sera affiché dans cette couleur ! Si tu modifies une couleur, il faut penser à remettre les couleurs d’origine après.

On peut aussi expérimenter la modification de la couleur de fond avec :

```lua
love.graphics.setBackgroundColor(valeurR, valeurV, valeurB)
```

Avant d’aller plus loin voyons comment deux concepts très importants en programmation peuvent nous faciliter la vie : les variables et les boucles

### Des variables et des boucles pour se faciliter la vie

Tu vois que quand on envoie des valeurs à une fonction (paramètres) c’est plus pratique de leur donner un nom : ça permet de les désigner plus facilement.

Les noms peuvent aussi servir à désigner des contenants, qui vont contenir des valeurs données.

Par exemple si on écrit :

```lua
x = 10
y = 20
```

Si on fait 

```lua
love.graphics.print(”Texte”, x, y)
```

C’est comme si on faisait :

```lua
love.graphics.print(”Texte”, 10, 20)
```

Mais ce qui est intéressant c’est que si on fait :

```lua
love.graphics.print(”Texte”, x, y)
y = y + 15
love.graphics.print(”Texte”, x, y)
```

Que se passe-t-il ? Comment l’expliquer ?

Vois comment cela peut modifier l’écriture du long programme de la section précédente (avec les couleurs). C’est plus lisible et moins fastidieux, non ?

Autre chose : dans une variable on peut mettre autre chose que des nombres. Par exemple :

```lua
x = 10
texte = "Texte à afficher"

love.graphics.print(texte, x, y)
y = y + 15
love.graphics.print(texte, x, y)
```

On peut faire mieux : on voit qu’on fait n fois la même opération… on peut peut-être faire plus simple ? Ici un type de boucle va nous aider !

```lua
love.draw()
  x = 10
  for y = 0, 105, 15 do
    love.graphics.print(”Texte”, x, y)
  end
end
```

C’est quand même plus court ! Tu as une idée de comment fonctionne la boucle “for” ? N’hésite pas à modifier les nombres sur la ligne qui commence par “for” pour essayer de comprendre.

Imagine des manières d’utiliser des boucles “for” (attention, n’oublie pas le “end” à la fin) et des variables pour afficher du textes en différents endroits et en changeant la couleur à chaque fois.

Note : on peut aussi mettre une boucle “for” à l’intérieur d’une autre boucle “for” ! (expérimente)

### Fontes

Pour plus de fantaisie, on peut aussi changer la fonte du texte affiché.

Dans le dossier de l’atelier, crée un dossier Fontes/ et télécharge dedans la fonte “Press Start 2P” (facile à trouver sur le net, pense à la décompresser si c’est un zip)

Essaye ce code en remplaçant <nom du fichier> par le nom du fichier de la fonte que tu as téléchargée :

```lua
function love.draw()
  

  font = love.graphics.newFont("Fontes/<nom du ficher>")
  love.graphics.setFont(font)
  love.graphics.print("Texte avec la fonte Press Start 2P.", 10, 10)

  font = love.graphics.newFont("Fontes/<nom du ficher>", 30)
  love.graphics.setFont(font)
  love.graphics.print("Texte avec la fonte Press Start 2P.", 10, 100)

end
```

Expérimente avec le paramètre numérique de la fonction .newFont() (et avec des variables, et des boucles…)

Tu constates qu’utiliser une fonte se fait en deux étapes :

- on charge d’abord la fonte dans un objet auquel on donne un nom (variable)
- on utilise une fonction pour changer/afficher la fonte en lui donnant le nom d’objet (variable) qu’on a choisi

Tu retrouveras ce mécanisme en deux étapes pour d’autres objets, par exemple les images (patience, on voit comment afficher une image plus bas).

On peut utiliser la fonction .setNewFont() pour changer la taille d’une fonte déjà chargée. À ton avis, quel paramètre faut-il donner à cette fonction ? (expérimente)

Comment réécrirais-tu le code ci-dessus pour éviter des répétitions alors ?

## Afficher des formes

### Formes (primitives)

On peut utiliser des fonctions pour afficher des formes simples : point, ligne, triangle, rectangle, cercle, polygone…

Voici quelques exemples. Expérimente pour voir à quoi correspondent les paramètres indiqués à chaque fois. 

Note : certains paramètres sont optionnels (tu peux ne pas les mettre) et le paramètre “mode” ne prend pas une valeur numérique (c’est soit “fill”, soit “line”).

```lua
love.graphics.rectangle(mode, x, y, width, height, rx, ry, segments)
love.graphics.circle(mode, x, y, radius)
love.graphics.polygon(mode, x1, y1, x2, y2, x3, y3, …)
love.graphics.line (x1, y1, x2, y2, x3, y3, …)
love.graphics.point(x1, y1)
love.graphics.points(x1, y1, x2, y2, x3, y3, …)
```

Tu peux trouver la liste complète des primitives ici (section “Drawing”) : 

[love.graphics - LOVE](https://love2d.org/wiki/love.graphics)

N’hésite pas à expérimenter des fonctions indiquées à cet endroit.

### Des listes pour se faciliter la vie

Pour certaines primitives, notamment .line() ou .points() ou encore .polygons(), il peut être fastidieux de rentrer les coordonnées dans l’appel de la fonction. On peut se simplifier la vie en créant une variable de type “liste” :

```lua
listePoints = {100, 200, 300,400, 10, 400, 5, 10)
love.graphics.points(listePoints)
```

Peux-tu imaginer comment utiliser des boucles et des variables  - puis des listes si tu as du courage - pour dessiner des formes automatiquement ? 

Important : pour accéder à un élément d’une liste, par exemple le 1er, il faut écrire listePoints[1], pour accéder au 4e il faut écrire listePoints[4]… et chacun de ces éléments peut-être traité comme une variable (on peut le modifier, ou lire sa valeur - selon les opérations qu’on indique).

Tu remarques que si on dessine une forme par dessus une autre, c’est la dernière dessinée qui est “au dessus”.

Note : la fonction .setColor() dispose d’un 4e paramètre : alpha ! Expérimente pour voir à quoi il sert, il est intéressant quand on dessine une forme par dessus les autres…

## Afficher une image

Là ça devient intéressant !

Avec tout ce qu’on a vu avant tu devrais pouvoir t’en sortir seul-e avec quelques indices.

La marche à suivre : 

- télécharge une image (assez petite pour rentrer dans la fenêtre)
- charge l’image avec la fonction .newImage() → quel est le paramètre à ton avis ? faut-il utiliser une variable sur cette ligne ?
- affiche la avec la fonction .draw(<nom_de_l’image>, x, y) → ATTENTION : la fonction draw ici est différente de love.draw() !!!!!!!

Une fois que tu as réussi, voilà la liste complète des paramètres de la fonction .draw() :

```lua
love.graphics.draw(img, x, y, r, sx, sy, ox, oy)
```

Note : ajoute les nouveaux paramètres l’un après l’autre ! Les deux derniers ne sont pas faciles à deviner…

## Défis

- Affiche des images avec différentes orientation, grosseur, plusieurs fois… (utiliser les variables et les boucles)
- Crée un écran (minimaliste) de jeu : par exemple une zone avec les informations pour le joueur : le nombre de vie, la santé, les armes ou la magie (ça peut être des petites icônes, du texte, des jauges…), etc., et une zone de jeu, avec une image de fond, et des personnages par dessus. Tu peux délimiter les zones avec des formes simples (des traits de couleurs, etc.)

Bien sûr ça ne bouge pas encore, mais c’est un début ! On pourra réutiliser ces éléments dans la suite. 

## Prochaine étape

Déplacer ces choses qu’on affiche (texte, formes, images…) grâce à la fonction love.update() :

[Atelier 2 : Déplacer une image](./atelier2.md)

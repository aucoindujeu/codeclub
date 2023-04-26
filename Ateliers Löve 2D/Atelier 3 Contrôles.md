# Atelier 3 : Contrôles

On ne peut pas avoir de jeu si on ne peut pas avoir une influence sur les évènements en jeu, par exemple contrôler le personnages que l’on incarne, ou plus généralement sélectionner des actions grâce aux touches du clavier, aux mouvements ou aux boutons de la souris ou aux boutons d’une manette de jeu. Nous avons vu comment déplacer des images en codant ce déplacement “en dur” dans nos programme, ce serait bien de pouvoir contrôler ces déplacement de manière interactive. Voyons comment on fait ! 

## Clavier

Löve propose deux familles de fonction pour gérer chaque type de contrôle (clavier, souris, manette…), en fonction de la manière dont on va utiliser l’appui sur un bouton ou une touche : l’appui en continu, ou l’appui “unique” ou “simple”. En gros : quand on laisse le bouton appuyé est-ce que l’effet va être continu (par exemple le personnage ne va pas arrêter de tirer) ou unique  (le personnage ne tire qu’une seule fois, quelle que soit la durée pendant laquelle on appuie sur le bouton.

### Appui unique

La fonction en jeu ici est love.keypressed(key). C’est une fonction qu’on appelle en dehors de love.draw() (évidemment !) mais aussi de love.update().

Par exemple, si on dessine un rond à l’écran et qu’on veut le faire bouger de quelques pixels vers la droite ou vers la gauche en fonction des flèches du clavier :

```lua
centreX = love.graphics.getWidth()/2
centreY = love.graphics.getHeight()/2

function love.draw()

  love.graphics.circle("fill", centreX, centreY, 10)

end

function love.keypressed(key)

  if key == "left" then
    centreX = centreX - 10
  elseif key == "right" then
    centreX = centreX + 10
  end

end
```

Que se passe-t-il si tu appuies sur les flèches gauche ou droite du clavier ? Et si tu laisses appuyé ?

As-ton avis à quoi sert le “elseif” au sein du bloc “if” ?

Peux-tu faire réagir le rond également aux directions “haut” et “bas” ?

Comment ferais-tu pour empêcher le rond de sortir de la fenêtre, même si on continue à appuyer sur les flèches ?

Pour t’aider, voici le nom donné aux touches par Löve2D : 

[KeyConstant - LOVE](https://love2d.org/wiki/KeyConstant)

C’est une méthode qui est pratique dans les jeux où un seul appui sur une touche provoque le déplacement comme Sokoban, 

Mais en fait, c’est une méthode que personnellement je n’aime pas trop utiliser pour diriger les personnages dans un jeu : il vaut mieux, pour un code “plus propre”, mettre tout ce qui concerne l’évolution du jeu dans love.update(), il y a des techniques pour cela, que nous verrons plus loin.

.keypressed() a un intérêt, mais plutôt pour des fonctionnalités “hors-jeu” : quitter le jeu, faire une copie d’écran, éventuellement afficher un menu… Notons également que .keypressed() a son pendant : keyreleased(), si on veut détecter le relâchement d’une touche.

Par exemple voilà un bout de code que je mets dès que je programme quelque chose avec Löve2D (un jeu, une simple démo, un test avec Löve2D) car c’est très pratique :

```lua
love.keypressed(key)
  
  if key == "escape" then
    love.event.quit()
  end

end
```

→ l’appui sur “échap” (”escape”) fait quitter le jeu

→ on peut aussi programmer une capture d’écran à déclencher en appuyant sur une touche, regarder dans la section [Bouts de code](Bouts%20de%20code.md) car ça fait intervenir des concepts plus compliqué (Lua n’est pas très pratique pour manipuler des fichiers dans le système).

### Appui en continu

Cette fois-ci, nous allons utiliser une fonction au sein de .update(). En effet, cette nouvelle fonction nous permettra de tester à chaque fois que le jeu se réactualisera quel est l’état de la touche (pressée, ou relevée). Il s’agit de love.keyboard.isDown(<touche_à_tester>)

Dans notre exemple précédent, cela donne :

```lua
centreX = love.graphics.getWidth()/2
centreY = love.graphics.getHeight()/2

function love.update(dt)

  if love.keyboard.isDown("right") then
    centreX = centreX + 10
  end

end

function love.draw()

  love.graphics.circle("fill", centreX, centreY, 10)

end
```

Que se passe-t-il si on appuie sur la flèche de droite ?

Pourquoi ? Que se passe-t-il dans le programme quand on appuie sur la flèche de droite ? (pense que nous sommes dans .update() qui a une caractéristique bien particulière…)

Comment pourrait-on corriger ça ?

Voilà le code qui fonctionne :

```lua
centreX = love.graphics.getWidth()/2
centreY = love.graphics.getHeight()/2

function love.update(dt)

  if love.keyboard.isDown("right") then
    centreX = centreX + 10 * dt * 60
  end

end

function love.draw()

  love.graphics.circle("fill", centreX, centreY, 10)

end
```

→ Change une valeur pour obtenir la vitesse qui te convient (tu peux utiliser une variable pour faire un code plus propre et plus lisible)

→ Modifie le programme pour que la balle puisse être dirigée dans toutes les directions

→ Essaye les autres fonctions qui testent l’état des touches du clavier 

### Appui unique dans .update() (optionnel)

Attention, dans cette partie on voit quelque chose de compliqué, si tu n’en vois pas l’intérêt, ce n’est pas grave, tu pourras y revenir plus tard. Nous avons vu qu’il valait mieux, pour rendre le code plus compréhensible, mettre tout ce qui concerne l’actualisation et les interactions avec le jeu dans .update(). Mais alors, si on ne peut utiliser que love.keyboard.isDown() dans .update(), comment teste-t-on un appui unique avec cette fonction ?

On va faire intervenir une variable particulière. C’est une variable qui n’a que deux états, un peu comme un interrupteur (allumé/éteint ou on/off, ou encore pile/face ou vrai/faux). Pour généraliser, on dit qu’elle a la valeur soit vraie, soit fausse. On appelle ces variables des variables booléennes. Comment une telle variable peut nous aider ?

Observe le code suivant :

```lua
centreX = love.graphics.getWidth()/2
centreY = love.graphics.getHeight()/2

pressed = false

function love.update(dt)

  if love.keyboard.isDown("right") then
    if pressed == false then
      pressed = true  
      centreX = centreX + 10 * dt * 60
    end
  else
    pressed = false
  end

end

function love.draw()

  love.graphics.circle("fill", centreX, centreY, 10)

end
```

Prends bien le temps de dérouler ce que fait le code pas à pas, et comment les valeurs de “pressed” changent, et comment cela affecte le programme.

Que se passe-t-il quand on laisse la touche enfoncée ? Quelle est la valeur de “pressed” alors ?

Et que se passe-t-il quand on la relâche ? Que devient la valeur de “pressed” ?

Et que se passe-t-il quand on appuie à nouveau ? Et quelle est encore la valeur de “pressed” ?

Pourquoi écrit-on au début du programme “pressed = false” ?

## Souris

Il y a deux informations à récupérer dans un contrôle via la souris : 

- la position du pointeur (une paire de coordonnées x et y à l’écran)
- l’appui sur un des boutons de la souris (et la molette).

Maintenant qu’on a vu comment ça se passait avec le clavier, on peut aller plus vite pour la souris car c’est presque la même chose !

### Récupérer la position du pointeur

On a 3 manière de le faire :

1. on a une fonction indépendante (qui s’emploie en dehors de .update()) qui nous permet de récupérer toutes les infos concernant la souris (position du pointeur, bouton(s) pressé(s) en click simple) : love.mousepressed(x, y, button)

```lua
function love.mousepressed(x, y, button)
  if button == 2 then
    centreX = x
    centreY = y
  end
end
```

En t’inspirant des programmes vu précédemment, utilise ce bout de code pour faire en sorte que le rond se déplace avec la souris lorsque tu appuies sur un bouton de la souris (lequel ?)

N’hésite pas à regarder la doc de Löve pour bien comprendre : 

[love.mousepressed - LOVE](https://love2d.org/wiki/love.mousepressed)

Explore aussi la doc concernant les fonctions du même style : love.mousereleased(), love.mousemoved(), etc.

1. autre méthode : au sein de .update() cette fois, les fonctions love.mouse.getX et love.mouse.getY peuvent, l’une récupérer la position x, l’autre la position y du pointeur sur l’écran

```lua
centreX = love.mouse.getX
centreY = love.mouse.getY
```

1. Enfin, toujours au sein de .update(), la fonction love.mouse.getPosition() permet de récupérer en un seul appel les deux composantes des coordonnées du pointeur

```lua
centreX, centreY = love.mouse.getPosition()
```

Réécris le programme où l’on contrôle les mouvement du rond avec la souris en utilisant ces méthodes.

### Click continu

Pour repérer un appui continu sur les boutons de la souris, nous disposons de la fonction love.mouse.isDown(<numéro_de_bouton>). Dans le programme, remplace la fonction love.update(dt) par celle-ci :

```lua
function love.update(dt)

	if love.mouse.isDown(1) then
		centreX = love.mouse.getX()
		centreY = love.mouse.getY()
	end

end
```

Que fait ce programme ? Quel bouton est testé ? Que se passe-t-il quand on relâche ce bouton ? Et quand on le maintien enfoncé ?

Plus difficile : pourquoi n’utilise-t-on pas dt ?

Comment modifierais-tu ce programme pour, en utilisant également love.mouse.isDown(), ne réagir qu’à un simple click ? (par exemple quand on clique et qu’on maintient appuyé, le rond ne suis pas les déplacements du pointeur).

## Manette

La manette est plus compliqué à gérer. Déjà parce qu’il y a plusieurs modèles de manettes, qui n’ont pas toutes les mêmes configurations (nombre de boutons, nom des boutons, bouton multidirectionnelle ou sticks analogiques…)

Ensuite, si on peut raisonnablement penser qu’un clavier et qu’une souris (à défaut, un touchpad) sont tout le temps connectés à l’ordinateur (sinon il est juste inutilisable), il n’en est pas de même d’une manette de jeu. Non seulement il n’est pas toujours sûr qu’une manette soit connectée, mais en plus plusieurs manettes peuvent être connectées ! Il faut donc être capable de détecter si une ou des manettes sont branchées, et ensuite être capable de surveiller une manette en particulier, donc de l’identifier. Cela va devenir un peu technique car il va falloir utiliser des listes.

### Détecter la présence des manettes

Voilà un bout de code qui permet de tester si des manettes sont branchées, à l’aide de la fonction love.joystick.getJoysticks() (les chiffres entre crochets renvoient à des notes).

```lua
**[1]** joysticks = love.joystick.getJoysticks()
**[2]** if #joysticks > 0 then
**[3]**   areJoysticks = true
    else
      areJoysticks = false
```

[1] : la fonction .getJoysticks() retourne une liste d’objets dont chacun correspond à une manette branchée (liste de 1 éléments : 1 manette branchée, 2 éléments si 2 manettes branchées, etc.)

[2] : # est un opérateur qui permet d’obtenir la longueur d’une liste. Par exemple si une liste appelée Liste contient 1 élément, alors #Liste retournera 1. Si Liste contient 2 éléments alors #Liste retourne 2. Donc pour savoir si notre liste joysticks contient au moins 1 élément, alors il faut que sa longueur soit au moins de 1. C’est pourquoi on teste #joysticks > 0

[3] : on crée une variable booléenne (soit à “vraie”, soit à “fausse”) qui nous indiquera s’il y a au moins une manette branchée. Donc s’il est vrai que la longueur de la liste joysticks est supérieure à 0 (donc au moins égale à 1, ou plus) c’est qu’une manette est branchée, on met donc la variable areJoystics à “true”. Dans le cas contraire, elle sera égale à “false” pour indiquer qu’aucun joystick n’est branché.

Si l’on a détecté des manettes branchées, il peut être intéressant de créer des variables qui permettent de bien les identifier, plutôt que de se référer à leur place dans la liste retournée par .getJoysticks() : il est plus lisible de se référer à joystick1 plutôt qu’à joysticks[1]. Il suffit de faire :

```lua
if areJoysticks == true then
  joystick1 = joysticks[1]
```

### Identifier les boutons

Löve2D dispose d’une méthode qui ressemble beaucoup à .keyboard.isDown(<nom_de_la_touche>) pour identifier les boutons enfoncés des manettes, mais la syntaxe est un peu différente :

```lua
  joystick1:isGamepadDown("dpright') -- teste la croix directionnelle vers la droite
  joystick1:isGamepadDown("a") -- teste le bouton "a" de joystick1 = joysticks[1]
```

ATTENTION : il peut y avoir des petits problèmes ici. Le modèle que Löve se fait d’une manette est une manette type X-Box. Néanmoins, en fonction des constructeurs, des modèles, etc. il se peut que les noms des boutons dans love, et ceux inscrits sur la manette ne correspondent pas. Par exemple j’ai une manette type SNES dont le bouton ‘b’ correspond au bouton ‘a’ selon Löve2D et ‘x’ à ‘y’ (et vice-versa). 

![https://love2d.org/w/images/d/d4/360_controller.png](https://love2d.org/w/images/d/d4/360_controller.png)

Voir sur cette page le mapping d’une manette par Löve2D : 

[Joystick:isGamepad - LOVE](https://love2d.org/wiki/Joystick:isGamepad)

OPTIONNEL (SEULEMENT SI TU ES À L’AISE ET VEUX ALLER PLUS LOIN)

Une autre solution est de mapper soi-même la manette. Attention ça va être un peu abstrait, mais c’est intéressant pour comprendre avec quelle logique on accède à une interface ou un «objet». 

1. D’abord on va créer une liste qui va stocker les différents boutons possibles
2. On vérifie si un joystick est branché et on récupère «l’objet» joystick
3. On parcours tous les boutons de l’objet «joystick»
4. On stocke l’état de chaque bouton dans la liste «buttons»

Essaye les fonction .update() et .draw() ci-dessous :

```lua
   function love.update(dt)
     local joysticks = love.joystick.getJoysticks()
[1]  buttons = {}
[2]  if #joysticks > 0 then
       local joystick1 = joysticks[1]
[3]    for b = 1, joystick1:getButtonCount() do
[4]      buttons[b] = joystick1:isDown(b)
       end
     end
   end
  
   function love.draw()
     for i, state in ipair(buttons) do
       love.graphics.print(tostring(i)..' state....'..tostring(state))
     end
   end
```

Il y a plusieurs nouvelles choses dans ce code :

1. D’abord, fais-toi expliquer le sens de ce nouveau mot clé : ‘local’
2. Fais toi expliquer aussi la forme un peu différente de la boucle ‘for’ avec le mot clé ‘ipairs()’
3. Quel est le type des variables stockées dans la table ‘buttons’ ?
4. Ensuite comprends-tu ce que ce programme affiche, et comment ?
5. Essaye de rajouter le mapping pour la croix directionnelle en étudiant cette page de la doc : 

[love.joystick.getJoysticks - LOVE](https://love2d.org/wiki/love.joystick.getJoysticks)

### Les sticks analogiques

Jusqu’à présent les valeurs que nous avons utilisées étaient majoritairement booléenne (true/false) car un bouton est soit enfoncé, soit relâché. Seule exception : la position du pointeur de la souris (getX/getY, …) qui elle renvoyait un nombre plus ou moins important selon la position de la souris dans la fenêtre. Il en est de même avec les sticks analogiques. À la différence de la croix multidirectionnelle, ceux-ci renvoient un nombre à virgule dont la valeur dépend de comment ils sont inclinés. Ce nombre est compris entre -1 (à fond à gauche) et +1 (à fond à droite) en passant par 0 (au milieu).

L’intérêt est que l’on peut avoir un effet sur le jeu qui soit proportionnel à l’inclinaison du stick. Le plus classique est de rendre une accélération. Ici par exemple, si nous revenons au programme qui déplace notre rond (réécris le programme en entier), on peut imprimer une vitesse plus ou moins importante au rond en bougeant le stick de droite :

```lua
function love.update(dt)
  
  xAxis = joystick1:getGamepadAxis('rightx')
  yAxis = joystick1:getGamepadAxis('righty')

  if math.abs(xAxis) > 0.25 then
    vX = xAxis*100*dt
  end
  if math.abs(yAxis) > 0.25 then
    vY = yAxis*100*dt
  end

  centreX = centreX + vX
  centreY = centreY + vY

end
```

Si les sticks sont poussés à fond, le rond se déplacera de 100 pixels par seconde. Si les sticks sont à 45° le rond n’avancera que de 50 pixels par seconde.

Pourquoi teste-t-on si la position du stick est supérieur à 0.25, et pas juste différente de 0 ?

Que fais la fonction math.abs() ? Comment aurais-tu écrit les conditions de tests si tu ne faisais pas appel à elle (soit parce que tu ne la connais pas ou que tu ne comprends pas ce qu’elle fait) ?

## Prochaine étape

Maintenant qu’on sait contrôler des éléments de notre programme, il reste à gérer les collisions entre ces éléments ! C’est primordial dans un jeu vidéo. Nous disposons déjà de tous les outils ou méthode pour le faire. Après ça, on pourra d’ores et déjà programmer nos premiers jeux vidéos !

[Atelier 4 : Gérer les collisions](Atelier%204%20Ge%CC%81rer%20les%20collisions.md)

## 012 Avec des "if" on met Löve en bouteille

Ici on va découvrir les conditions "if", qui sont super importantes en programmation.

0. Qu'est-ce que "if" veut dire en anglais ?
1. Crée une variable `position = 0`.
2. Affiche ton pseudonyme à la position `position`.
3. Dans la fonction `love.keypressed` ajoute le code suivant :

    if key == "right" then
        position = position + 10
    end

4. Est-ce que ta touche flèche droite fonctionne ?
5. Fais en sorte que ta touche flèche gauche ("left") fonctionne aussi.

Questions bonus :

6. Fais en sorte que ta touche flèche en haut ("up") fonctionne aussi.
7. Fais en sorte que ta touche flèche en bas ("down") fonctionne aussi.

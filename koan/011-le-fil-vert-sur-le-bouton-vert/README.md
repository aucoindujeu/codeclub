# 011 Le fil vert sur le bouton vert...

Voyons encore une nouvelle fonction de Löve 2D. Ajoute ceci à ton code :

    touche = ""

    function love.keypressed(key)
        touche = key
    end

La fonction `love.keypressed` est appelée à chaque fois qu'on appuie sur une touche du clavier. La variable `key` représente le nom de la touche.

1. Affiche la valeur de la variable `touche`.
2. Qu'est-ce qui se passe quand tu tapes au clavier ?


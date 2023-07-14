## 007 Oh ! Une variable

Crée un nouveau fichier main.lua. À l'intérieur, ajoute le code suivant :

    function love.draw()
        sourisX = love.mouse.getX()
        sourisY = love.mouse.getY()

        love.graphics.print("salut <ton pseudonyme> !",  sourisX, sourisY)
    end

1. À ton avis, qu'est-ce qui va se passer ?
2. Vérifie ta théorie en exécutant ton programme.

Dans ce programme, "sourisX" et "sourisY" sont ce qu'on appelle des "variables". Ce sont des symboles qui représentent des valeurs. On va faire énormément usage dans les programmes qui suivent...

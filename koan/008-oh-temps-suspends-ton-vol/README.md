## 008 Oh temps ! Suspends ton vol

On va faire appel à une nouvelle fonctionnalité de Löve2D. Ajoute à ton programme le code suivant :

    t = 0

    function love.update(dt)
        t = t + dt
    end

Le code qui est à l'intérieur de la fonction `love.update` est appelé à chaque rafraîchissement du jeu. La variable `dt` représente le temps écoulé depuis le dernier appel de la fonction.

1. À ton avis, que représente la variable `t` ?
2. Vérifie ta théorie en affichant la valeur de la variable `t` (dans `love.draw`).


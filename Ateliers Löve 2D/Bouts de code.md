# Bouts de code

## Squelette d’un programme Löve

```lua
function love.load()
  love.filesystem.setIdentity("screenshot")
end

function love.update()

end

function love.draw()

end

function love.keypressed(key)

  if key == "escape" then
	  love.event.quit()
  elseif key == "c" then
    love.graphics.captureScreenshot(os.time() .. ".png")
  end

end
```

→ l’appui sur la touche “c” fait une capture d’écran du jeu (l’image est stockée dans le répertoire par défaut de Löve, dans le répertoire du jeu qu’on renomme “screenshot” dans load()). Le répertoire par défaut de Löve est dans un emplacement différent selon le système utilisé, voir 

[love.filesystem - LOVE](https://love2d.org/wiki/love.filesystem)
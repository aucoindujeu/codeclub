# Ressources pour la création de jeux vidéos

## Apprendre (tuto, cours, etc.)

### Livres (en français)

- *Initiation à la création de jeux vidéo avec LÖVE2D*, par Anthony Cardinale - [Éditions D-Booker](https://www.d-booker.fr/developpement-de-jeux-video/654-1194-initiation-a-la-creation-de-jeux-video-en-lua-avec-love2d.html). Création d’une base de RPG avec Löve2D. La maison d’édition propose le seul ouvrage de référence en français sur le Lua (en deux tomes). Elle propose aussi des ouvrages du même auteur sur Godot et Unity.

- *Codex Ludorum, programmer des jeux vidéo en C++*, par [Gaëtan Blaise-Cazalet](https://github.com/Gaetz) (auto-édité, en vente sur [Amazon](https://www.amazon.fr/Programmer-jeux-vid%C3%A9o-Codex-Ludorum/dp/2958679217))

### Sites / cours en ligne (en français)

- [MicroStudio](https://microstudio.dev/fr/) une plateforme extraordinaire pour apprendre à programmer des jeux vidéos. Tout se fait en ligne, une implémentation très proche du Lua, une série de tuto extrêmement bien faite
- [GameCodeur](https://www.gamecodeur.fr/), des cours de programmation de jeux vidéos en ligne, payants, mais l’introduction au Lua est gratuite. C’est aussi une [chaîne YouTube](https://www.youtube.com/@gamecodeur) en français avec un contenu varié (tutos, actualités, interviewes)  
- [https://fairedesjeux.fr](https://fairedesjeux.fr) site collaboratif créé par l’association [Game Dev Alliance](https://gamedevalliance.fr/), on y trouve des explications pour faire son jeu sous [Pico-8](https://www.lexaloffle.com/pico-8.php) (une console virtuelle qui se programme en Lua), en [Ren’Py](https://www.renpy.org/) (moteur pour faire des visual novels), etc. et même pour faire du Pixel Art, et d’autres choses (concepts de base de la programmation, Krita, RPG Maker). Très didactique et adapté aux débutant-e-s complet-e-s

### Livres et sites en anglais
- La chaîne YouTube [CS50](https://www.youtube.com/@cs50) compile des cours d’introduction à la *Computer Science* d’Harvard. Il y a plusieurs cycles consacrés à la programmation de jeux vidéos

### Généralités

Faire un jeu vidéo ne se résume pas au code ! Gameplay, concept, financement, etc. Les chaînes YouTube suivantes proposent des dossiers ou des conférences sur tel ou tel aspect de l’industrie du jeu vidéo, avec des interviews de créateurs pro qui reviennent sur le développement de leurs jeux.

- [Game Dev Alliance](https://www.youtube.com/@GameDevAlliance) la chaîne de [l’association](https://gamedevalliance.fr/) du même nom

- [Toulouse Game Dev](https://www.youtube.com/@toulousegamedev/) la chaîne de [l’association](http://toulousegamedev.fr/) du même nom

- [AFJV](https://www.youtube.com/@Afjv-jeuxvideo/) la chaîne de [l’Agence française pour le jeu vidéo](https://www.afjv.com/), on trouve sur son site d’autres dossiers et interview, et des offres d’emploi et de stages

- Les [conférences de l’ADDON](https://www.youtube.com/@Atlangames/videos) sur la chaîne YouTube d’[Atlangames](https://www.atlangames.com/), groupement des professionnel-le-s du jeu vidéo de la région Ouest

## Outils / Collection d’*assets*

### Graphismes

- [Universal LPC Spritesheet Generator](https://sanderfrenken.github.io/Universal-LPC-Spritesheet-Character-Generator/) un site qui permet de créer rapidement des personnages animés. Idéal pour le prototypage.

- [Tiled](https://www.mapeditor.org/download.html) pour générer des niveaux et les *tilemaps* associées (export possible en de nombreux formats, dont Lua).

- [Pyxel Edit](https://www.pyxeledit.com/get.php) (la version gratuite n’est plus supportée, mais toujours disponible)

- [GrafX2](http://pulkomandy.tk/projects/GrafX2) pour les amateur-ice-s du légendaire [Deluxe Paint](https://fr.wikipedia.org/wiki/Deluxe_Paint), on ne fait pas plus rétro !

- [Pixilart](https://www.pixilart.com) outil de *pixel art* en ligne et téléchargeable

- [Piskel](https://www.piskelapp.com/) outil de *pixel art* en ligne et téléchargeable

- [Krita](https://krita.org/fr/) l’outil de référence open-source pour la peinture numérique

### Sons

- [rFXGen](https://github.com/raysan5/rfxgen), basé sur [sfxr](http://www.drpetter.se/project_sfxr.html) par l’auteur de Raylib, un synthétiseur qui permet de créer des sons typiques « 8-bits ». L’appli est aussi disponible [en ligne](https://raylibtech.itch.io/rfxgen) (web-assembly)

- [sfxr](http://www.drpetter.se/project_sfxr.html) par DrPetter, créé dans le cadre de la célèbre GameJam [Ludum Dare](https://ludumdare.com/), pour faciliter la création rapide de sons pour les jeux rétro

- [jsfxr](https://sfxr.me/) portage en ligne de [sfxr](http://www.drpetter.se/project_sfxr.html)

- [Audacity](https://www.audacityteam.org/) l’outil de référence open-source de traitement du son

### Collection d’assets

- [opengameart.org](https://opengameart.org/) des tonnes de graphismes et de sons libres de droit (attention de respecter néanmoins les diverses licences et demandes des créateur-ice-s)

- on peut trouver des collections d’assets gratuites ou à petits prix sur [itch.io](https://itch.io/), le site de référence des développeur-euse-s indépendant-e-s ou amateur-ice-s

- [freesound.org](https://freesound.org/) pour télécharger des échantillons de son gratuits

### Editeurs

- [Zero Brane Studio](https://studio.zerobrane.com/) pour le Lua et [Löve2D](https://love2d.org/) : un éditeur dédié très léger qu’on peut (sous Windows) installer en version portable sur une clé USB à côté de Löve2D pour coder son jeu partout où on a accès à un ordinateur sous Windows (voir notre [atelier 0](./atelier0.md))

- [VS Code](https://code.visualstudio.com/) l’éditeur star de Microsoft, installable également en version portable, même si assez lourd (>300Mo)

- [Notepad++](https://notepad-plus-plus.org/) un autre éditeur léger et populaire installable en version portable

## Framework / Moteurs

Dans l’ordre (conseillé) :

- [Love2D](https://love2d.org/) (Lua), que l’on présente dans nos [ateliers](https://github.com/aucoindujeu/codeclub)

- [RayLib](https://www.raylib.com/) (en C, des *bindings* sont diponibles pour la plupart des autres langages), très simple d’emploi

- [Monogame](https://www.monogame.net/) (C#) un *framework* multi-plateforme où portabilité est le maître mot (Windows, macOS, Linux, iOS/iPadOS, Android, PlayStation 4, PlayStation 5, Xbox, et Nintendo Switch)

- [Godot](https://godotengine.org/) (supporte C++, C#, Python et GDScript) un moteur open-source

- [Pygame Zero](https://pygame-zero.readthedocs.io/en/stable/index.html) (Python) nettement plus facile à utiliser que [Pygame](https://www.pygame.org/), avec des fonctions *draw(), update()*, etc. comme en [Love2D](https://love2d.org/). Propose un excellent tuto pour la prise en main

- [Pygame](https://www.pygame.org/) (Python)

- [SDL2](https://www.libsdl.org/) (en C), pour les courageux-ses seulement

## Ressources générales pour la programmation

- [https://adventofcode.com/] un célèbre défi de programmation, tous les ans chaque jour du mois de décembre avant Noël (calendrier de l’avent de la programmation). Concourrez dans le langage que vous désirez, les défis sont accessible aux débutant-e-s les premiers jours. Révisez ou découvrez des algorithmes classiques ! (en anglais).

- [Learn X in Y minutes](https://learnxinyminutes.com/) un site pour découvrir rapidement les fondamentaux de nombreux langages (en anglais pour la plupart, certaines pages sont traduites en français, notamment pour le [Lua](https://learnxinyminutes.com/docs/fr-fr/lua-fr/), le [C#](https://learnxinyminutes.com/docs/fr-fr/csharp-fr/), le [C++](https://learnxinyminutes.com/docs/fr-fr/c++-fr/) et le [Python](https://learnxinyminutes.com/docs/fr-fr/python-fr/), mais aussi pour des outils comme [git](https://learnxinyminutes.com/docs/fr-fr/git-fr/), [bash](https://learnxinyminutes.com/docs/fr-fr/bash-fr/), [make](https://learnxinyminutes.com/docs/fr-fr/make-fr/), [tmux](https://learnxinyminutes.com/docs/fr-fr/tmux-fr/), etc.) 
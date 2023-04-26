# Ateliers Löve 2D

Le but de ces fiches d’atelier n’est pas de proposer un cours détaillé et structuré de programmation ou de création de jeux avec Love 2D. Les explications théoriques sont donc très succinctes car les animateurs de l’atelier sont là pour montrer, expliquer, répondre aux questions en direct.

Pour créer un jeu vidéo, il faut :

- afficher des informations et des images à l’écran,
- les déplacer et les animer, et montrer leurs interactions (p. ex. une balle qui rebondit sur les bords de l’écran ou un ennemi qui explose quand il est touché par un tir),
- faire réagir le jeu aux actions sur le clavier, la souris ou la manette (contrôles),
- mettre à jour les informations dans le jeu (position des différents personnages, nombre de vies, niveau, etc.)
- jouer des sons

Löve 2D est une boîte à outil qui facilite la programmation d’un jeu en langage Lua avec des fonctions toutes prêtes pour réaliser ces actions de base, tout en laissant beaucoup de choses à programmer, laissant beaucoup de liberté dans la conception du jeu. Le Lua c’est un vrai langage de programmation très léger qui fonctionne sur beaucoup de plateformes et qui sert à faire des applications professionnelles, il est très utilisé dans le monde du jeu vidéo. Et surtout, « facile », il est idéal  pour apprendre à programmer.

[https://love2d.org/](https://love2d.org/)

## Installation de Löve2D sur une clé USB

Si tu disposes d’une clé USB, tu peux te créer (sous Windows) un environnement de développement de jeu nomade : tu pourras programmer n’importe où tu trouveras un ordinateur sous Windows, sans avoir rien à installer sur cet ordinateur.

Voilà la procédure. Ne t’inquiète pas, elle est longue à décrire, mais très facile et surtout plus rapide à faire en vrai ! Tu la feras avec un animateur, je la décris là pour que tu puisses t’en rappeler si tu veux la refaire tout-e seul-e :

1. Branche ta clé USB, et assure-toi d’avoir assez d’espace. Tu n’as pas besoin de beaucoup : Löve2D demande 11Mo d’espace, un éditeur comme Notepad++ 21Mo. Pour comparaison, installer un éditeur comme VS Code demandera 370Mo. Il faut penser aussi à l’espace que prendront les projets ou les jeux que tu vas programmer, les images et les sons ça prend vite de la place. Mais dans tous les cas, acheter pour quelques euros une clé neuve de 8 ou 16Go (les plus petites que l’on trouve aujourd’hui) ou en récupérer une ancienne inutilisée couvrira largement tous tes besoins.
2. Rends toi sur le site de Löve2D : [love2d.org/](http://love2d.org/) et télécharge le fichier « 64-bit zipped » pour Windows (sauf exception il fonctionnera sur la plupart des machines actuelles) :

![Love_telecharger.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love_telecharger.png)

1. Sauve le fichier sur ta clé USB :

![Love1_sauver.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love1_sauver.png)

1. Le fichier que tu as téléchargé est compressé. Pour le rendre utilisable, rends-toi sur ta clé [1] , fais un clic droit sur le fichier qui commence par « love » et fini par quelque chose comme « win64.zip » [2] et sélectionne « extract to … » [3] :

![Love3_extraire.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love3_extraire.png)

1. Un dossier (un espace qui contient plusieurs fichiers) symbolisé par une icône jaune, devrait apparaître, dont le nom est presque identique au fichier que tu as téléchargé (le nom ne finit juste pas par « .zip ». Va à l’intérieur de ce dossier (double clic gauche) [1]. Le programme qui permettra de lancer les jeux que nous allons programmer s’appelle « love.exe ». Pour pouvoir l’utiliser rapidement on va faire un raccourci vers ce fichier. Fais un clic droit sur « love.exe » [2] et sélectionne « créer un raccourci » [3].

![Love2_raccourci.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love2_raccourci.png)

1. Nous allons simplement mettre ce raccourci à la « racine » (la base) de la clé USB pour pouvoir accéder au programme facilement. Dans le dossier [1] fais un clic droit sur le nouveau raccourci [2] , sélectionne « couper » [3].

![Love4_couperRaccourci.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love4_couperRaccourci.png)

1. Remonte à la base de la clé USB (la « racine ») [1], fais un clic droit dans le fond de la fenêtre (surtout pas sur un fichier ou un dossier !) [2] et sélectionne « copier le raccourci » [3]. C’est bientôt fini ! Le raccourci devrait apparaître dans la fenêtre [4].

![Love5_collerRaccourci.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love5_collerRaccourci.png)

1. Pour vérifier que tout s’est bien passé, double clic gauche sur le raccourci, tu devrais voir cette fenêtre s’ouvrir, qui indique que Löve2D fonctionne :

![Love_ItWorks.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love_ItWorks.png)

## Installer un éditeur de texte sur la clé USB

Un programme est en fait un simple fichier texte. Il te faut donc un logiciel pour créer ce type de fichier. Il y a beaucoup de choix, mais il existe des éditeurs spécialisés pour la création de fichiers programmes. Il faut donc en installer un sur la clé. Pour les installer, la procédure est identique que ci-dessus : télécharger un fichier compressé, le décompresser sur la clé, créer un raccourci vers le fichier qui fini par « .exe » et le copier à la racine de la clé. Essaye de le faire seul si tu as bien compris l’installation de Löve2D, sinon demande de l’aide à un animateur.

Nous te conseillons de télécharger :

- Notepad++ qui est très léger et dispose de toutes les fonctionnalités pour programmer : sur [https://notepad-plus-plus.org/downloads/](https://notepad-plus-plus.org/downloads/) sélectionne la dernière version plus sélectionne le lien vers la version « portable (.zip) » (par exemple [https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.9/npp.8.4.9.portable.x64.zip](https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.9/npp.8.4.9.portable.x64.zip) )
- VS code qui est utilisé par la majorité des professionnels mais un peu plus compliqué à installer (il faut créer un dossier data/ à côté de code.exe - fais toi aider si tu ne comprends pas, ou installe Notepad++ qui est très bien !)

## La création d’un projet et son exécution

Pour chaque atelier, tu devras créer un programme et l’exécuter avec Löve2D. Pour rester efficace nous te conseillons :

1. De créer un dossier pour chaque nouveau programme. À la base (racine) de la clé USB fait un clic droit dans la fenêtre [1], sélectionne « nouveau »[2], puis « dossier » [3].

![Love6_NouveauProjet.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love6_NouveauProjet.png)

1. Tu seras ensuite invité-e à entrer un nom pour ce dossier. Choisis un nom en relation avec le programme que tu veux écrire et t’y retrouver ensuite (par exemple : « Atelier 1 Exercice 1 » :

![Love7_Name_NouveauProjet.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love7_Name_NouveauProjet.png)

1. Dans ce dossier tu sauvegarderas le programme que tu auras créé avec l’éditeur que tu as choisis sous le nom « main.lua »
2. Ensuite, pour l’exécuter ou le lancer avec Löve2D, il te suffiras de faire un « glissé-déposé » en cliquant (gauche) sur le dossier du programme que tu as écris, de maintenir appuyer le bouton de gauche et pousser le fichier sur le raccourci « love.exe - Raccourci » et relâcher le bouton :

![Love8_lancer.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love8_lancer.png)

1. Et voilà, ton programme sera lancé !

![Love_gamelaunched.png](Ateliers%20Lo%CC%88ve%202D%202fe62e074caf49c7a1ea4179c144b8b4/Love_gamelaunched.png)

Voilà, tu es prêt-e pour commencer les ateliers ! 

## Fiches d’ateliers

[Atelier 1 : Affichage avec Löve](https://www.notion.so/Atelier-1-Affichage-avec-L-ve-9357c3caa9c64d898d5188381bb9e356)

[TP 1 : Affichage avec Löve (à raccourcir)](https://www.notion.so/TP-1-Affichage-avec-L-ve-raccourcir-3deb6d9e5f914cf0b8b91838d5f9a5ae)

[Atelier 2 : Déplacer une image](https://www.notion.so/Atelier-2-D-placer-une-image-599a6b35bf7942a1af96e65675a4f5f0)

[Atelier 3 : Contrôles](https://www.notion.so/Atelier-3-Contr-les-01ae1244e4a747ee9d35e64356caa745)

[Atelier 4 : Gérer les collisions](https://www.notion.so/Atelier-4-G-rer-les-collisions-02f3d05276bb484ebc01c37ff6502402)

[Atelier 5 : Sons](https://www.notion.so/Atelier-5-Sons-71198915d3eb494ba7302ee13bc6800f)

[Atelier 6 : Animation des sprites](https://www.notion.so/Atelier-6-Animation-des-sprites-a8e9ff54d006490580000042bb2223db)

[Atelier 7 : TileMap](https://www.notion.so/Atelier-7-TileMap-76f46d173ecc46b9b6c02bb8c1d676b9)

[Bouts de code](https://www.notion.so/Bouts-de-code-0cadecf62ae441ed8e2e27232700e407)

## Ressources

Cheatsheet Lua : 

[Lua cheatsheet](https://devhints.io/lua)

Cheatsheet Löve : À FAIRE
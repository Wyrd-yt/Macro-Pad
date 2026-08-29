# Macro-Pad
Voici tous les fichiers nécessaires à la réalisation du Macro Pad. Vous y retrouverez le .stl du boîtier du Pad, les programmes utilisés pour le logiciel (MacroPadConfig) et le Pad lui-même, et enfin le schéma électrique.

Fonctionnalités:  
  ● 8 touches programmables  
  ● 1 potentiomètre programmable  
  ● Écran TFT 1.8" 128x160  
  ● Joystick pour contrôler l'interface du Macro Pad  
  ● Jusqu'à 5 presets personnalisables  
  ● Logiciel de configuration sur PC  
  ● Communication entre le Macro Pad et le logiciel de configuration  
  
Matériel:  
    ● 1 Raspberry Pi Pico  
    ● 8 switches  
    ● 1 Écran TFT ST7735 1.8" 128x160  
    ● 1 Joystick  
    ● 1 Potentiomètre  
    ● 1 Boîtier imprimé en 3D  
  
    Structure du projet:
      Macro Pad/
      |___programmes/
      |    |___firmware_macro_pad/
      |    |___logiciel_macro_pad/
      |
      |___schéma electrique/
      |___fichiers 3D/


programmes/ :  
  ● Contient les programmes nécessaires au fonctionnement du Macro Pad.  
  
programmes/firmware_macro_pad/ :  
  ● Contient le programme à téléverser sur la Raspberry Pi Pico. Il permet l'affichage de l'interface sur l'écran du Pad et la gestion de la communication avec le logiciel. Veillez à installer toutes les bibliothèques nécessaires au bon fonctionnement du programme.  
  
programmes/logiciel_macro_pad/ :  
  ● Contient les différents programmes et les .exe nécessaires au bon fonctionnement du logiciel de configuration. Veillez à installer toutes les bibliothèques nécessaires au bon fonctionnement du logiciel.  

schéma electrique/ :  
  ● Contient le schéma électrique pour connecter correctement les différents composants entre eux. 

fichiers 3D/ :  
  ● Contient le fichier 3D (au format .stl) du boîtier du Macro Pad (boîte inférieure, face avant et roue du potentiomètre).

  Installation :
  ● Logiciel :  
    1.Télécharger et exécuter le Setup du logiciel  

  ● Firmware :  
    1. Installer Arduino IDE  
    2. Installer les bibliothèques nécessaires (veillez à installer la bibliothèque "Raspberry Pi Pico/RP2040/RP2350 by Earle F. Philhower, III" afin de ne pas rencontrer de problème avec les cartes. Si vous ne la trouvez        pas, entrez le lien suivant dans l'Arduino IDE ➝ Fichier ➝ Préférences ➝ URL de gestionnaire de cartes supplémentaires :  
       "https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json")  
    3. Ouvrir le fichier .ino situé dans programmes/firmware_macro_pad/  
    4. Sélectionner la Raspberry Pi Pico sur le port série où elle est branchée  
    5. Téléverser le firmware  


Si vous voulez utiliser le Pad, vous pouvez soit installer directement le logiciel via le Setup dans le RELEASE. Sinon vous pouvez installer les programmes du logiciel pour y apporter vos modifications.

  
Explication logiciel :  

● Tous les raccourcis sont stockés dans un fichier .json qui est un dictionnaire indépendant de Python qui permet d'éviter la réinitialisation des valeurs qu'on modifie lors du lancement d'un programme.
  
● Le logiciel fonctionne grâce à trois fichiers en .exe : MacroPadConfig.exe, arrierePlanCommunication.exe et watcher.exe.
  
● Le MacroPadConfig.exe est le logiciel principal. Attention si vous installez les programmes pour les modifier à créer un raccourci vers ce dernier si vous voulez avoir le logiciel sur votre bureau (le raccourci sera à mettre sur le bureau). Grâce à lui, vous pourrez configurer vos presets et les raccourcis correspondants pour chacune de vos touches. Si vous êtes perdu, cliquez sur le bouton "?", qui vous guidera vers la page "Guide d'utilisation". Avant de configurer votre Macro Pad, veuillez le synchroniser avec le logiciel afin qu'il le reconnaisse pour les prochaines modifications. Lorsque le bouton "Synchroniser" est cliqué, faites attention à bien suivre les étapes afin d'éviter tout bug du logiciel.  

● L'arrierePlanCommunication.exe est une extension du logiciel MacroPadConfig (qui tourne en arriere-plan) qui permet à votre Macro Pad de recevoir la configuration complète de vos presets sans avoir à lancer le logiciel principal de configuration. Cependant, arrierePlanCommunication.exe et MacroPadConfig.exe ne peuvent pas être en cours d'exécution en même temps, car ils utilisent tous les deux le même port série sur lequel est branché votre Macro Pad. Si les deux venaient à être exécutés en même temps, l'un des deux programmes n'aura pas accès au Macro Pad ce qui l'empêcherait de communiquer avec ce dernier. C'est pourquoi le logiciel principal (MacroPadConfig) ferme arrierePlanCommunication.exe à chaque lancement et le relance à chaque fois qu'il se ferme.

● Enfin, le watcher.exe est également une extension du logiciel MacroPadConfig qui permet de lancer arrierePlanCommunication.exe à chaque démarrage de votre PC afin que ce dernier puisse transmettre vos presets à votre Macro Pad sans action de votre part. Lorsque vous faites l'installation avec le Setup, ce programme sera automatiquement mis dans le dossier Startup afin qu'il s'exécute à chaque démarrage du PC.  

  
● Pour faciliter la communication entre le logiciel et le Macro Pad, un système de codes est utilisé :
1 = CTRL  
2 = SHIFT  
3 = ALT  
4 = WINDOWS  
5 = TAB  
6 = VERR MAJ  
7 = SPACE  
8 = DELETE  
9 = ENTER  
Les lettres sont écrites normalement. Cela donne des codes comme 1s (= CTRL + s).  Il faut noter que la librairie utilisée pour presser des touches utilise un clavier QWERTY. Il faut donc connaître l'équivalent des touches QWERTY en AZERTY (par exemple "=" en AZERTY est équivalent à "+" en QWERTY). La plus grande partie de la transformation des raccourcis en codes est effectuée dans le programme "logique.py", qui les transforme et les écrit sous la forme transformée dans le JSON. À noter : la rangée supérieure du clavier en AZERTY est équivalente aux nombres sur le QWERTY (par exemple "é" en AZERTY est équivalent à "2" en QWERTY). Puisque "logique.py" met dans le JSON la version transformée on ne peut pas convertir la rangée supérieure dans la partie logicielle car les nombres sont déjà occupés par les touches comme "CTRL" ou "ALT". Donc la conversion de cette rangée se fait dans le firmware du Macro Pad.  

● Le logiciel contient trois pages :  
1. La page principale qui apparaît dès le lancement (créée dans le fichier "interfaceMain.py") qui permet d'accéder aux autres pages, de synchroniser son Macro Pad, d'envoyer les modifications au Pad, et de modifier le nom des presets et les supprimer.
2. La page de modification qui apparaît lorsque le bouton "modifier" d'un preset est cliqué sur la page principale (créée dans le fichier "interfaceModifPage.py"). Elle permet de configurer et de modifier ses presets (nom et raccourcis).
3. La page d'aide (guide d'utilisation) qui apparaît lorsque le bouton "?" est cliqué sur la page principale (créée dans le fichier "interfaceHelp.py"). Elle permet d'accéder au guide d'utilisation pour comprendre comment fonctionne le logiciel.  
Le fichier "main.py" permet de regrouper ces pages et de les coordonner.  

● Afin de détecter un Macro Pad, le logiciel vérifie les appareils connectés au PC et attend de voir si l'un de ces appareils lui envoie "PICO OK". Si c'est le cas, il enregistre son numéro de série dans un autre fichier .json appelé "codeIdentification.json". Si le numéro de série du Macro Pad n'est pas présent dans ce dernier fichier, alors le logiciel l'enregistre dans "codeIdentification.json". 
  
Explication firmware :  
● Le firmware "firmware_macro_pad.ino" doit être téléversé sur la Raspberry Pi Pico. Il permet d'afficher l'interface sur l'écran du Pad, de gérer la communication avec le PC. Tant qu'aucune donnée n'est reçue de la part du PC, l'interface du Pad affiche une page de chargement. Il décode les raccourcis envoyés par le logiciel afin de pouvoir exécuter les raccourcis.
  

    
Licence : Licence personnelle et éducative — usage non commercial.
Vous pouvez télécharger, utiliser, modifier et reproduire ce projet gratuitement à des fins personnelles ou éducatives. Toute utilisation commerciale ou toute vente du projet ou de ses fichiers est interdite sans l’autorisation préalable de l’auteur. Toute version modifiée ou dérivée de ce projet reste soumise à cette même restriction et ne peut pas être vendue ou utilisée à des fins commerciales sans l'autorisation préalable de l'auteur.





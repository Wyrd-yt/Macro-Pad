# Macro-Pad
Voici tous les fichiers de la réalisation du Macro Pad. Vous y retrouverez le .stl du boitier du pad, les programmes utilisés pour le logiciel (MacroPadConfig) et le pad lui même, et enfin le schéma électrique.

Fonctionnalités:  
  ● 8 touches programmables  
  ● 1 Potentiomètre programmable  
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
    ● 1 Boitier imprimé en 3D  
  
    Structure du projet:
      Macro Pad/
      |___programmes/
      |    |___firmware_macro_pad/
      |    |___logiciel_macro_pad/
      |
      |___schéma electrique/


programmes/ :  
  ● Contient les programme nécessaires au fonctionnement du Macro Pad.  
  
programmes/firware_macro_pad/ :  
  ● Contient le programme à téléverser dans la Raspberry Pi Pico. Il permet l'affichage de l'interface affiché sur l'écran   du pad et la gestion de la communication avec le logiciel. Veillez à installer toutes les bibliothèques nécessaires au     bon fonctionnement du programme.  
  
programmes/logiciel_macro_pad :  
  ● Contient les différents programmes et les .exe nécessaire au bon fonctionnement du logiciel de configuration. Veillez    à installer toutes les bibliothèques nécessaires au bon fonctionnement du logiciel.  

schéma electrique/ :  
  ● Contient le schéma électrique pour connecter correctement les différents composants entre eux. 

  Installation :  
    ● Logiciel :  
      1.Télécharger et exécuter le Setup du logiciel  

  ● Firmware :  
    1. Installer Arduino IDE  
    2. Installer les bibliothèques nécessaires (veillez à installer la bibliothèque "Raspberry Pi Pico/RP2040/RP2350 by           Earle F. Philhower, III" afin de ne pas avoir de problème de cartes. Si vous ne la trouvez pas, entrez le lien             suivant dans l'Arduino IDE ➝ Fichier ➝ Préférences ➝ URL de gestionnaire de cartes supplémentaires :  
       "https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json")  
    3. Ouvrir le fichier .ino situé dans programmes/firmware_macro_pad/  
    4. Sélectionner la Raspberry Pi Pico sur le port série ou elle est branchée  
    5. Téléverser le firmware  

Explication logiciel :  
  
● Le logiciel fonctionne grâce à 3 fichiers en .exe : MacroPadConfig.exe, arrierePlanCommunication.exe et watcher.exe.
  
● Le MacroPadConfig.exe est le logiciel exécutable. Attention à créer un raccourci de ce dernier si vous voulez avoir le logiciel sur votre bureau (le raccourci sera à mettre sur le bureau). Grâce à lui, vous pourrez configurer vos presets et les raccourcis correspondants pour chacun de vos touches. Si vous êtes perdu, cliquez sur le bouton "?", qui vous guidera sur la page "Guide d'utilisation". Avant de configurer votre Macro Pad, veuillez le synchroniser avec le logiciel afin qu'il le reconnaisse pour les prochaines modifications. Lorsque le bouton "Synchroniser" est cliqué, faites attention à bien suivre les étapes afin d'éviter tout bug du logiciel.  

● Le arrierePlanCommunication.exe est une extension du logiciel MacroPadConfig qui permet à votre Macro Pad de recevoir la configuration complète de vos presets sans avoir à lancer le logiciel principale de configuration. Cependant, arrierePlanCommunication.exe et MacroPadConfig.exe ne peuvent pas être en cours d'exécution en même temps, car ils utilisent et lisent le même port série sur lequel est branché votre Macro Pad. Si les 2 venaient à être exécutés en même temps, l'un des 2 programmes n'aura pas accès au Macro Pad ce qui ne lui permettra pas de communiquer avec ce dernier. C'est pourquoi le logiciel principal (MacroPadConfig) ferme arrierePlanCommunication à chaque lancement et l'ouvre à chaque fois qu'il ferme.

● Enfin, le watcher.exe est également une extension de logiciel MacroPadConfig qui permet de lancer arrierePlanCommunication.exe à chaque démarrage de votre PC afin que ce dernier puisse communiquer vos presets à votre Macro Pad sans action de votre part. Lorsque vous faites l'installation avec le Setup, ce programme sera automatiquement mit dans le dossier Startup afin qu'il s'exécute à chaque démarrage du PC.
  
Explication firmware :  
● Le firmware "firmware_macro_pad.exe" doit être téléversé sur la Raspberry Pi Pico. Il permet d'afficher l'interface affiché sur l'écran du pad, de gérer la communication avec le PC. Tant que aucunes données n'est reçues de la part du PC, l'interface du pad affiche une page de chargement.  
  

    
Licence : Licence personnelle et éducative — usage non commercial.
Vous pouvez télécharger, utiliser, modifier et reproduire ce projet gratuitement à des fins personnelles ou éducatives. Toute utilisation commerciale ou vente du projet ou de ses fichiers est interdite sans l’autorisation préalable de l’auteur.




  
  


        
        
  


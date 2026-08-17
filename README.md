# Macro-Pad
Voici tous les fichiers de la réalisation du Macro Pad. Vous y retrouverez le .stl du boitier du pad, les programmes utilisés pour le logiciel (MacroPadConfig) et le pad lui même, et enfin le schéma électrique.

Fonctionnalités:  
  ● 8 touches programmables  
  ● Potentiomètre programmable  
  ● Écran TFT 1.8" 128x160  
  ● Joystick pour contrôler l'interface du Macro Pad  
  ● Jusqu'à 5 presets personnalisables  
  ● Logiciel de configuration sur PC  
  ● Communication entre le Macro Pad et le logiciel de configuration  
  
Matériel:  
    ● Raspberry Pi Pico  
    ● 8 switches  
    ● Écran TFT ST7735 1.8" 128x160  
    ● Joystick  
    ● Potentiomètre  
    ● Boitier imprimé en 3D  
  
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
      2. Installer les bibliothèques nécessaires (veillez à installer la bibliothèque "Raspberry Pi Pico/rp2040/rp2350 by           Earle F.Philhower" afin de ne pas avoir de problème de cartes. Si vous ne la trouvez pas, entrez le lien suivant           dans l'Arduino IDE ➝ Fichier ➝ Préférences ➝ URL de gestionnaire de cartes supplémentaires :  
         "https://github.com/earlephilhower/arduino-pico/releases/download/global/package_rp2040_index.json")  
      3. Ouvrir le fichier .ino situé dans programmes/firmware_macro_pad/  
      4. Sélectionner le Raspberry Pi Pico  
      5. Téléverser le firmware  

  
  


        
        
  


import json
import keyboard
import time
import os
import sys


presets = None

if getattr(sys, "frozen", False):
    dossier = os.path.dirname(sys.executable)
else:
    dossier = os.path.dirname(os.path.abspath(__file__))


cheminPresets = os.path.join(
    dossier,
    "presets.json"
)

cheminID = os.path.join(
    dossier,
    "codeIdentification.json"
)


with open(cheminPresets, "r", encoding="utf-8") as f:
    presets = json.load(f)

with open(cheminID, "r", encoding="utf-8") as c:
    ID = json.load(c)




def writeJsonPreset(presets):
    with open(cheminPresets, "w", encoding="utf-8") as f:
        json.dump(presets, f, indent=4, ensure_ascii=False) 


def writeJsonID(ID):
    with open(cheminID, "w", encoding="utf-8") as c:
        json.dump(ID, c, indent=4, ensure_ascii=False) 


def translateCode(presets, nb):

    codes = presets[f"preset{nb}"][1:]

    for i in range(len(codes)):
        codes[i] = codes[i].replace("1", "CTRL ")
        codes[i] = codes[i].replace("2", "SHIFT ")
        codes[i] = codes[i].replace("3", "ALT ")
        codes[i] = codes[i].replace("4", "WINDOWS ")
        codes[i] = codes[i].replace("5", "TAB ")
        codes[i] = codes[i].replace("6", "VERR MAJ ")
        codes[i] = codes[i].replace("7", "SPACE ")
        codes[i] = codes[i].replace("8", "DELETE ")
        codes[i] = codes[i].replace("9", "ENTER ")
            

    codes = ["+".join(code.split()) if len(code.split()) > 1 else code for code in codes]   
    return codes
            
def conversion():

    # NOTES : La conversion de la rangée du haut se fait sur le programme c++ car ces derniers caractères sont remplaçables par des chiffres.
    # Par conséquent on ne peut pas remplacer ces caractères par des chiffres dans le json car ils sont occupés par les touches comme CTRL.
    # Les convertir sur le programme c++ ne cause aucun probleme avec les codes

    for i in range(5):

        for j in range(1, 11):

            for k in range(len(presets[f"preset{i+1}"][j])):

                # LETTRES
                if presets[f"preset{i+1}"][j][k] == "a":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("a", "q")

                elif presets[f"preset{i+1}"][j][k] == "q":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("q", "a")
                
                elif presets[f"preset{i+1}"][j][k] == "z":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("z", "w")

                elif presets[f"preset{i+1}"][j][k] == "w":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("w", "z")
                    
                elif presets[f"preset{i+1}"][j][k] == "m":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("m", ";")

                # SYMBOLES / PONCTUATIONS

                elif presets[f"preset{i+1}"][j][k] == ",":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace(",", "m")

                elif presets[f"preset{i+1}"][j][k] == ";":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace(";", ",")

                elif presets[f"preset{i+1}"][j][k] == ":":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace(":", ".")

                elif presets[f"preset{i+1}"][j][k] == "!":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("!", "/")

                elif presets[f"preset{i+1}"][j][k] == "^":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("^", "[")

                elif presets[f"preset{i+1}"][j][k] == "$":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("$", "]")

                elif presets[f"preset{i+1}"][j][k] == "*":
                    presets[f"preset{i+1}"][j] = presets[f"preset{i+1}"][j].replace("*", "\\")

                


    writeJsonPreset(presets)

keys = [
    "ctrl", "shift", "alt", "windows gauche",
    "tab", "caps lock", "space", "backspace",
    "enter", "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", 
    "t", "u", "v", "w", "x", "y", "z",
    "&", "é", "\"", "'", "(", "-", "è",
    "_", "ç", "à", ")", "=", ",", ";",
    ":", "!","^", "$", "ù", "*", "<",
    "²"
]


def detectKey(switchNb, nb, newShortCut):

    maj = False

    keyboard.block_key("windows gauche")
    keyboard.block_key("caps lock")
    keyboard.block_key("tab")
    keyboard.block_key("shift")
    keyboard.block_key("backspace")
    keyboard.block_key("enter")
    keyboard.block_key("space")


    maxShortCut = [False, False, False, False, False, False]

    for i in range(len(maxShortCut)):

        while maxShortCut[i] == False:

            for touche in keys:

                if keyboard.is_pressed("f1") and maj == False:
                    maj = True
                    time.sleep(0.3)

                if keyboard.is_pressed("f1") and maj == True:
                    maj = False
                    time.sleep(0.3)

                if keyboard.is_pressed(touche) and maj == True:
                    if keyboard.is_pressed(")"):
                        newShortCut.append("°")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed("="):
                        newShortCut.append("+")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed("^"):
                        newShortCut.append("¨")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed("$"):
                        newShortCut.append("£")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed("ù"):
                        newShortCut.append("%")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed("*"):
                        newShortCut.append("µ")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed(","):
                        newShortCut.append("?")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed(";"):
                        newShortCut.append(".")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed(":"):
                        newShortCut.append("/")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed("!"):
                        newShortCut.append("§")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    elif keyboard.is_pressed("<"):
                        newShortCut.append(">")   
                        maxShortCut[i] = True
                        time.sleep(0.3)
                    else:              
                        newShortCut.append(touche.upper())   
                        maxShortCut[i] = True
                        time.sleep(0.3)

                if keyboard.is_pressed(touche) and maj == False:
                    newShortCut.append(touche)   
                    maxShortCut[i] = True
                    time.sleep(0.3)

                if keyboard.is_pressed("esc"):
                    maxShortCut = [True, True, True, True, True, True]
                    presets[f"preset{nb}"][switchNb] = "Aucun"
                    writeJsonPreset(presets)

    
    for i in range(len(newShortCut)):
        newShortCut[i] = newShortCut[i].replace("ctrl", "1")
        newShortCut[i] = newShortCut[i].replace("shift", "2")
        newShortCut[i] = newShortCut[i].replace("alt", "3")
        newShortCut[i] = newShortCut[i].replace("windows gauche", "4")
        newShortCut[i] = newShortCut[i].replace("tab", "5")
        newShortCut[i] = newShortCut[i].replace("caps lock", "6")
        newShortCut[i] = newShortCut[i].replace("space", "7")
        newShortCut[i] = newShortCut[i].replace("backspace", "8")
        newShortCut[i] = newShortCut[i].replace("enter", "9")


    keyboard.unblock_key("windows gauche")
    keyboard.unblock_key("caps lock")
    keyboard.unblock_key("tab")
    keyboard.unblock_key("shift")
    keyboard.unblock_key("backspace")
    keyboard.unblock_key("enter")
    keyboard.unblock_key("space")

    newShortCut = "".join(newShortCut)

    presets[f"preset{nb}"][switchNb] = newShortCut
    writeJsonPreset(presets)

    


    

    

    


        









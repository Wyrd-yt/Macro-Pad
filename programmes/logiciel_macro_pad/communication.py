import serial
from logique import presets, ID, writeJsonID
import serial.tools.list_ports

#code d'envoie:
# 1 = CTRL
# 2 = SHIFT
# 3 = ALT
# 4 = WINDOWS
# 5 = TAB
# 6 = VERR MAJ
# 7 = SPACE
# 8 = DELETE
# 9 = ENTER
#les lettres sont écrites normalement
#ça donne des codes comme 1s = CTRL + s
# le macro pad peut recevoir maximum 10 codes (sans compter le nom du preset)
# (le potentiometre a 2 codes pour les 2 sens différents)

pico = None

def connectVerif():
    global pico
    for i in range(len(ID)):
        for port in serial.tools.list_ports.comports():
            if port.serial_number == ID[f"{i+1}"]:

                try:
                    pico = serial.Serial(port.device, 115200)
                except:
                    pass

                if pico:
                    try:
                        validation = pico.readline().decode().strip()
                        if validation == "PICO OK":
                            return True
                    except:
                        return False

    return False





# vérifié si le macro pad est enregistré et sinon le faire
def verifMacroPad():
    global pico
    pico = None

    for port in serial.tools.list_ports.comports():
        try:
            pico = serial.Serial(port.device, 115200, timeout=2)
            
        except:
            print(pico)

            return "Erreur lors de la connexion avec le Macro Pad"

            
        try:
            validation = pico.readline().decode().strip()
            print(pico)
            if validation == "PICO OK":
                if port.serial_number in ID.values():

                    return "Le Macro Pad est déja enregistré !"
                
                else:
                    newID = port.serial_number
                    ID[f"{len(ID)+1}"] = newID
                    writeJsonID(ID)

                    return "Le Macro Pad a été enregistré avec succès !"
            else:

                return "Erreur lors de la communication avec le Macro Pad"
                
        except:

            return "Erreur lors de la synchronisation du Macro Pad."



def send(presets):
    if connectVerif():
        pico.write(f"{presets}\n".encode())
        return True

    else:
        return False


# send(presets)
# message = pico.readline().decode().strip()
# print(message)



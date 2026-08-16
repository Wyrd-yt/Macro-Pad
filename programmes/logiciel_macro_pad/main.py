from interfaceMain import showMain
from interfaceModifPage import showModifPage
from interfaceHelp import showHelpPage
import tkinter as tk
import subprocess
import os
import sys


if getattr(sys, "frozen", False):
    dossier = os.path.dirname(sys.executable)
else:
    dossier = os.path.dirname(os.path.abspath(__file__))


cheminBackground = os.path.join(
    dossier,
    "arrierePlanCommunication",
    "arrierePlanCommunication.exe"
)



subprocess.run(
    ["taskkill", "/IM", "arrierePlanCommunication.exe", "/F"],
    creationflags=subprocess.CREATE_NO_WINDOW
)

def fermer():

    subprocess.Popen([
        cheminBackground
    ])

    root.destroy()



root = tk.Tk()

root.protocol("WM_DELETE_WINDOW", fermer)

showMain(root, showModifPage, showHelpPage)

root.mainloop()

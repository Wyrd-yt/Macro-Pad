import os
import sys
import subprocess


if getattr(sys, "frozen", False):
    dossier = os.path.dirname(os.path.dirname(sys.executable))
else:
    dossier = os.path.dirname(os.path.abspath(__file__))


cheminBackground = os.path.join(
    dossier,
    "arrierePlanCommunication",
    "arrierePlanCommunication.exe"
)


processBackground = subprocess.Popen([cheminBackground])
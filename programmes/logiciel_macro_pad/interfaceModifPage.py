import tkinter as tk
from communication import connectVerif
from logique import presets, writeJsonPreset, translateCode, detectKey
from interfaceMain import sendPresetSelected, clearMain, presetSelected
import threading


newShortCut = []

switchPotenSelected = [
    False, False, False, False, False, False, False, False, False, False
]


def popModif(ombreModif, modif, boutonCancelModif, saisie, switchNb, root):
    global newShortCut
    newShortCut = []
    ombreModif.place(x=960, y=540, width=430, height=230, anchor="center")
    modif.place(x=960, y=540, width=400, height=200, anchor="center")
    modif.config(anchor="n", pady=50)
    boutonCancelModif.place(x=780, y=460, width=25, height=25, anchor="center")
    saisie.place(x=960, y=600, width=400, height=50, anchor="center")


    global thread
    thread = threading.Thread(
    target=detectKey,
    args=(switchNb, nb, newShortCut),
    daemon=True
    )

    thread.start()

    verifThread(root)



def verifThread(root):
    if thread.is_alive():
        saisieText = newShortCut
        saisieText = " + ".join(saisieText)
        saisie.config(text=saisieText)
        root.after(100, verifThread, root)
    else:
        clearPopModif(ombreModif, modif, boutonCancelModif, saisie)
        actualise(presets, nb)

        saisie.config(text="")


def actualise(presets, nb):
    codesPresetSelected = translateCode(presets, nb)

    if codesPresetSelected[0] == "":
        switch1.config(text="Aucun", fg = "white")
    else:
        switch1.config(text=codesPresetSelected[0], fg="black")

    if codesPresetSelected[1] == "":
        switch2.config(text="Aucun", fg="white")
    else:
        switch2.config(text=codesPresetSelected[1], fg="black")

    if codesPresetSelected[2] == "":
        switch3.config(text="Aucun", fg="white")
    else:
        switch3.config(text=codesPresetSelected[2], fg="black")

    if codesPresetSelected[3] == "":
        switch4.config(text="Aucun", fg="white")
    else:
        switch4.config(text=codesPresetSelected[3], fg="black")

    if codesPresetSelected[4] == "":
        switch5.config(text="Aucun", fg="white")
    else:
        switch5.config(text=codesPresetSelected[4], fg="black")

    if codesPresetSelected[5] == "":
        switch6.config(text="Aucun", fg="white")
    else:
        switch6.config(text=codesPresetSelected[5], fg="black")

    if codesPresetSelected[6] == "":
        switch7.config(text="Aucun", fg="white")
    else:
        switch7.config(text=codesPresetSelected[6], fg="black")

    if codesPresetSelected[7] == "":
        switch8.config(text="Aucun", fg="white")
    else:
        switch8.config(text=codesPresetSelected[7], fg="black")

    if codesPresetSelected[8] == "":
        textPotenHaut.config(text="Aucun 🠖", fg="white")
    else:
        textPotenHaut.config(text=f"{codesPresetSelected[8]} 🠖", fg="black")

    if codesPresetSelected[9] == "":
        textPotenBas.config(text="🠔 Aucun", fg="white")
    else:
        textPotenBas.config(text=f"🠔 {codesPresetSelected[9]}", fg="black")


def popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, nb):
    ombreConfirmSup.place(x=960, y=540, width=430, height=230, anchor="center")
    confirmSup.place(x=960, y=540, width=400, height=200, anchor="center")
    boutonConfirmSup.place(x=960, y=600, width=100, height=30, anchor="center")
    boutonCancelSup.place(x=780, y=460, width=25, height=25, anchor="center")

    switchPotenSelected[nb-1] = True


def clearConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup):
    ombreConfirmSup.place_forget()
    confirmSup.place_forget()
    boutonConfirmSup.place_forget()
    boutonCancelSup.place_forget()

    for i in range(len(switchPotenSelected)):
        switchPotenSelected[i] = False


def suppression():
    for cle, valeur in presetSelected.items():
        if valeur:
            nbPreset = int(cle.replace("preset", ""))

    for i in range(len(switchPotenSelected)):
        if switchPotenSelected[i] == True:
            presets[f"preset{nbPreset}"][i+1] = ""
            writeJsonPreset(presets)

    actualise(presets, nb)

        


def clearPopModif(ombreModif, modif, boutonCancelModif, saisie):

    ombreModif.place_forget()
    modif.place_forget()
    boutonCancelModif.place_forget()
    saisie.place_forget()
    


def modifPresetSelected(nb):
    presetSelected[f"preset{nb}"] = False


def showEntree():
    actualName = presetName.cget("text")
    presetName.config(text="")
    entree.place(x=950, y=200, width=300, height=100, anchor="center")

    if actualName != "Aucun":
            entree.insert(0, actualName)


def clearEntree():
    new_name = entree.get()
    entree.delete(0, tk.END)
    entree.place_forget()
    if new_name == "":
        presets[f"preset{nb}"][0] = "Aucun"
    else:
        presets[f"preset{nb}"][0] = new_name
    writeJsonPreset(presets)

    presetName.config(text=presets[f"preset{nb}"][0])


def showModifPage(root, showMain, showHelpPage):


    #config de la fenêtre
    root.title("Macro Pad Config")
    root.geometry("1920x1080")
    #met la page en grand format par défaut
    root.state("zoomed")
    root.configure(bg="#F2F2F2")

    global nb
    #avoir le numéro du preset selectionné
    nb = sendPresetSelected()

    #stocker les raccourcis du preset selectionné
    codesPresetSelected = translateCode(presets, nb)


    #label texte bienvenue
    lab_bienvenue = tk.Label(root, text="Bienvenue sur Macro Pad Config", font=("Segoe UI", 30, "bold"))
    lab_bienvenue.pack()

    #label si le macro pad est connecté
    lab_connection_true = tk.Label(root, text="✅ Macro Pad connecté ✅", font=("Segoe UI Emoji", 20), fg="green")

    #label si le macro pad est pas connecté
    lab_connection_false = tk.Label(root, text="❌ Macro Pad non connecté ❌", font=("Segoe UI Emoji", 20), fg="red")

    #vérifie si le macro pad est connecté et affiche le bon label en fonction
    if connectVerif() == True:
        #anchor="center" donc le point de référence devient le centre du label
        lab_connection_true.place(relx=0.5, y=100, anchor="center")
    else:
        lab_connection_false.place(relx=0.5, y=100, anchor="center")


    #ombres des labels switches
    ombreSwitch1 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch1.place(x=210, y=410, width=200, height=200, anchor="center")

    ombreSwitch2 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch2.place(x=510, y=410, width=200, height=200, anchor="center")

    ombreSwitch3 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch3.place(x=1430, y=410, width=200, height=200, anchor="center")

    ombreSwitch4 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch4.place(x=1730, y=410, width=200, height=200, anchor="center")

    ombreSwitch5 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch5.place(x=210, y=760, width=200, height=200, anchor="center")

    ombreSwitch6 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch6.place(x=510, y=760, width=200, height=200, anchor="center")

    ombreSwitch7 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch7.place(x=1430, y=760, width=200, height=200, anchor="center")

    ombreSwitch8 = tk.Label(root, anchor="center", bg="#969696")
    ombreSwitch8.place(x=1730, y=760, width=200, height=200, anchor="center")


    global switch1, switch2, switch3, switch4, switch5, switch6, switch7, switch8
    #configuration des labels switches

    # sw1
    if codesPresetSelected[0] == "":
        switch1 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch1 = tk.Label(root, text=codesPresetSelected[0], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch1.place(x=200, y=400, width=200, height=200, anchor="center")

    # sw2
    if codesPresetSelected[1] == "":
        switch2 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch2 = tk.Label(root, text=codesPresetSelected[1], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch2.place(x=500, y=400, width=200, height=200, anchor="center")

    # sw3
    if codesPresetSelected[2] == "":
        switch3 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch3 = tk.Label(root, text=codesPresetSelected[2], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch3.place(x=1420, y=400, width=200, height=200, anchor="center")

    # sw4
    if codesPresetSelected[3] == "":
        switch4 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch4 = tk.Label(root, text=codesPresetSelected[3], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch4.place(x=1720, y=400, width=200, height=200, anchor="center")

    # sw5
    if codesPresetSelected[4] == "":
        switch5 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch5 = tk.Label(root, text=codesPresetSelected[4], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch5.place(x=200, y=750, width=200, height=200, anchor="center")

    # sw6
    if codesPresetSelected[5] == "":
        switch6 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch6 = tk.Label(root, text=codesPresetSelected[5], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch6.place(x=500, y=750, width=200, height=200, anchor="center")

    # sw7
    if codesPresetSelected[6] == "":
        switch7 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch7 = tk.Label(root, text=codesPresetSelected[6], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch7.place(x=1420, y=750, width=200, height=200, anchor="center")

    # sw8
    if codesPresetSelected[7] == "":
        switch8 = tk.Label(root, text="Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        switch8 = tk.Label(root, text=codesPresetSelected[7], anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black", wraplength=150, justify="center")
    switch8.place(x=1720, y=750, width=200, height=200, anchor="center")


    switch1.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 1, root))
    switch2.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 2, root))
    switch3.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 3, root))
    switch4.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 4, root))
    switch5.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 5, root))
    switch6.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 6, root))
    switch7.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 7, root))
    switch8.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 8, root))



    # config des label de nomination des switchs
    switchName1 = tk.Label(root, text="swtich 1", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName1.place(x=200, y=275, width=200, height=20, anchor="center")

    switchName2 = tk.Label(root, text="swtich 2", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName2.place(x=500, y=275, width=200, height=20, anchor="center")

    switchName3 = tk.Label(root, text="swtich 3", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName3.place(x=1420, y=275, width=200, height=20, anchor="center")

    switchName4 = tk.Label(root, text="swtich 4", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName4.place(x=1720, y=275, width=200, height=20, anchor="center") 


    switchName5 = tk.Label(root, text="swtich 5", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName5.place(x=200, y=625, width=200, height=20, anchor="center")

    switchName6 = tk.Label(root, text="swtich 6", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName6.place(x=500, y=625, width=200, height=20, anchor="center")

    switchName7 = tk.Label(root, text="swtich 7", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName7.place(x=1420, y=625, width=200, height=20, anchor="center")

    switchName8 = tk.Label(root, text="swtich 8", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    switchName8.place(x=1720, y=625, width=200, height=20, anchor="center")



    global potentiometre, textPotenHaut, textPotenBas
    potentiometre = tk.Canvas(root, width=360, height=360, highlightthickness=0)
    potentiometre.pack(expand=True)
    #config de l'ombre du potentiometre
    potentiometre.create_oval(10,10,330,330, fill="#969696", outline="")
    #config du potentiometre
    potentiometre.create_oval(10,10,320,320, fill="#CCCCCC", outline="")

    # config du label de nomination du potentiometre
    potenName = tk.Label(root, text="potentiometre", anchor="center", font=("Segoe UI Emoji", 15, "bold"), bg="#F2F2F2", wraplength=150, justify="center")
    potenName.place(x=950, y=340, width=200, height=30, anchor="center")


    # config des textes dans le cercle du potentiometre
    if codesPresetSelected[8] == "":
        textPotenHaut = tk.Label(root, text="Aucun 🠖", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:
        textPotenHaut = tk.Label(root, text=f"{codesPresetSelected[8]} 🠖", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black",  wraplength=150, justify="center")
    textPotenHaut.place(x=950, y=480, width=150, height=80, anchor="center")

    if codesPresetSelected[9] == "":
        textPotenBas = tk.Label(root, text="🠔 Aucun", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="white", wraplength=150, justify="center")
    else:     
        textPotenBas = tk.Label(root, text=f"🠔 {codesPresetSelected[9]}", anchor="center", font=("Segoe UI Emoji", 20, "bold"), bg="#CCCCCC", fg="black",  wraplength=150, justify="center")
    textPotenBas.place(x=950, y=580, width=150, height=80, anchor="center")


    # bind des texte dans le cercle du potentiometre pour modifer les raccourcis attribués
    textPotenHaut.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 9, root))
    textPotenBas.bind("<Button-1>", lambda event: popModif(ombreModif, modif, boutonCancelModif, saisie, 10, root))




    global ombreModif, modif, boutonCancelModif, saisie
    # config des label de modification/ajout de raccourcis
    ombreModif = tk.Label(root, bg="#969696")
    modif = tk.Label(root, text="Entrer les raccourcis un par un. Appuyez sur echap lorsque vous avez finit de rentrer votre raccourci. Appuyez sur F1 pour activer et désactiver le Verr Maj.", font=("Segoe UI", 12, "bold"), bg="#CCCCCC", wraplength=350, justify="center")
    boutonCancelModif = tk.Label(root, text="X", font=("Segoe UI", 15, "bold"), fg="red", bg="#CCCCCC")
    saisie = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#CCCCCC", wraplength=350, justify="center")



    # config du bind pour enlever le popup d'ajout/modification de raccourcis
    boutonCancelModif.bind("<Button-1>", lambda event : clearPopModif(ombreModif, modif, boutonCancelModif, saisie))



    # config du bouton retour
    back = tk.Label(root, text="X", font=("Segoe UI", 20, "bold"), bg="#CCCCCC", fg="red")
    back.place(x=100, y=50, width= 50, height=50, anchor="center")

    back.bind("<Button-1>", lambda event: (clearMain(root), showMain(root,showModifPage, showHelpPage), modifPresetSelected(nb)))


    # config des ombres des bouton de suppression des raccourcis
    ombreSup1 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup1.place(x=204, y=544 ,anchor="center")

    ombreSup2 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup2.place(x=504, y=544 ,anchor="center")

    ombreSup3 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup3.place(x=1424, y=544 ,anchor="center")

    ombreSup4 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup4.place(x=1724, y=544 ,anchor="center")


    ombreSup5 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup5.place(x=204, y=894 ,anchor="center")

    ombreSup6 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup6.place(x=504, y=894 ,anchor="center")

    ombreSup7 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup7.place(x=1424, y=894 ,anchor="center")

    ombreSup8 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSup8.place(x=1724, y=894 ,anchor="center")


    # config des bouton de suppression des raccourcis
    sup1 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup1.place(x=200, y=540 ,anchor="center")

    sup2 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup2.place(x=500, y=540 ,anchor="center")

    sup3 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup3.place(x=1420, y=540 ,anchor="center")

    sup4 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup4.place(x=1720, y=540 ,anchor="center")


    sup5 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup5.place(x=200, y=890 ,anchor="center")

    sup6 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup6.place(x=500, y=890 ,anchor="center")

    sup7 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup7.place(x=1420, y=890 ,anchor="center")

    sup8 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    sup8.place(x=1720, y=890 ,anchor="center")


    sup1.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 1))
    sup2.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 2))
    sup3.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 3))
    sup4.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 4))

    sup5.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 5))
    sup6.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 6))
    sup7.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 7))
    sup8.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 8))



    ombreSupPotenHaut = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSupPotenHaut.place(x=955, y=745 , width=90, height=40, anchor="center") 

    ombreSupPotenBas = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSupPotenBas.place(x=955, y=805 , width=90, height=40, anchor="center")
    

    supPotenHaut = tk.Label(root, text="Supprimer 🠖", bg="#CCCCCC", width=10, height=2, fg="red")
    supPotenHaut.place(x=950, y=740 , width=90, height=40, anchor="center")

    supPotenBas = tk.Label(root, text="🠔 Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    supPotenBas.place(x=950, y=800 , width=90, height=40, anchor="center")



    supPotenHaut.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 9))
    supPotenBas.bind("<Button-1>", lambda event: popConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 10))



    ombreConfirmSup = tk.Label(root, bg="#969696")
    confirmSup = tk.Label(root, text="Êtes-vous sûr de vouloir supprimer ce preset ?", font=("Segoe UI", 12, "bold"), bg="#CCCCCC") 
    boutonConfirmSup = tk.Label(root, text="Supprimer", font=("Segoe UI", 10, "bold"), fg="red")
    boutonCancelSup = tk.Label(root, text="X", font=("Segoe UI", 15, "bold"), fg="red", bg="#CCCCCC")

    boutonConfirmSup.bind("<Button-1>", lambda event: (suppression(), clearConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup)))
    boutonCancelSup.bind("<Button-1>", lambda event: clearConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup))


    global presetName
    # config du label contenant le nom du preset selectionné
    presetName = tk.Label(root, text=presets[f"preset{nb}"][0], anchor="center", font=("Segoe UI", 40, "bold"), bg="#F2F2F2", justify="center")
    presetName.place(x=950, y=200, anchor="center")

    presetName.bind("<Button-1>", lambda event: showEntree())


    global entree
    entree = tk.Entry(root, font=("Segoe UI", 25, "bold"))


    entree.bind("<Return>", lambda event: clearEntree())









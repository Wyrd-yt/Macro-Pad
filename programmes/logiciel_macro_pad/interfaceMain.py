import tkinter as tk
from communication import connectVerif, send, verifMacroPad
from logique import presets, writeJsonPreset


#si faux l'entree n'est pas affichée et inversement, le entreState[0] correspondant à l'entree du preset 1
entreeState = [False, False, False, False, False]

#savoir quel preset est selectionné
presetSelected = {
    "preset1": False,
    "preset2": False,
    "preset3": False,
    "preset4": False,
    "preset5": False
}


# faire apparaitre le popup qui signal que l'envoie des preset a été un succès ou que aucun macro pad n'est connecté/detecté
def popDisconnected_Success(error, ombreError, boutonCrossError):
    if connectVerif() == False:
        error.config(text="Aucun macro pad n'est connecté ou détecté")
        ombreError.place(x=960, y=540, width=430, height=230, anchor="center")
        error.place(x=960, y=540, width=400, height=200, anchor="center")
        boutonCrossError.place(x=780, y=460, width=25, height=25, anchor="center")
    else:

        lab_connection_true.place(relx=0.5, y=100, anchor="center")
        lab_connection_false.place_forget()

        error.config(text="Envoie des presets réalisé avec succès !")
        ombreError.place(x=960, y=540, width=430, height=230, anchor="center")
        error.place(x=960, y=540, width=400, height=200, anchor="center")
        boutonCrossError.place(x=780, y=460, width=25, height=25, anchor="center")


# faire disparaitre le popup qui signal que aucun macro pad n'a été detecté connecté ou que l'envoie des preset a été un succès
def clearPopDisconnected(error, ombreError, boutonCrossError):
    error.place_forget()
    ombreError.place_forget()
    boutonCrossError.place_forget()


# faire apparaitre le popup de confirmation de suppression de preset
def popConfirmation(confirmSup,ombreConfirmSup, boutonConfirmSup, boutonCancelSup, nb):
    ombreConfirmSup.place(x=960, y=540, width=430, height=230, anchor="center")
    confirmSup.place(x=960, y=540, width=400, height=200, anchor="center")
    boutonConfirmSup.place(x=960, y=600, width=100, height=30, anchor="center")
    boutonCancelSup.place(x=780, y=460, width=25, height=25, anchor="center")

    presetSelected[f"preset{nb}"] = True


# faire disparaitre toute la page Main
def clearMain(root):
    for widget in root.winfo_children():
        widget.destroy()


# envoyer à interfaceModifPage le preset selectionné à travers un nombre
def sendPresetSelected():
    for cle, valeur in presetSelected.items():
        if valeur:
            nb = int(cle.replace("preset", ""))

            return nb


def modifPresetSelected(nb):
    presetSelected[f"preset{nb}"] = True




#fait apparaitre l'entree et disparaitre le texte du label preset quand ce dernier est préssé
def showEntree(entree, preset, x, nb):
    if entreeState[0] == False and entreeState[1] == False and entreeState[2] == False and entreeState[3] == False and entreeState[4] == False:
        entree.place(x=x, y=550,anchor="center", width=200, height=50)
        #si le preset a un nom on l'affiche directement dans l'entree pour éviter de le réécrire entierement
        if preset.cget("text") != "Ajouter":
            entree.insert(0, preset.cget("text"))
        preset.config(text="")
        entree.bind("<Return>", lambda event: hideEntree(entree, preset, nb))
        entreeState[nb] = True


# faire disparaitre les champ de texte permettant de changer le nom des presets
def hideEntree(entree, preset, nb):
    #récupere le texte de l'entree et la fait disparaitre
    new_name = entree.get()
    entree.delete(0, tk.END)
    entree.place_forget()
    #modifie le dictionnaire json et le réécrit dans le fichier json
    if new_name == "":
        presets[f"preset{nb}"][0] = "Aucun"
    else:
        presets[f"preset{nb}"][0] = new_name
    writeJsonPreset(presets)
    #remet la possibilité de faire apparaitre une entree et unbind la touche entrée
    entreeState[nb] = False
    entree.unbind("<Return>")
    #gere si un nom a été ajouter ou non
    if presets[f"preset{nb}"][0] == "Aucun":
        preset.config(text="Ajouter", fg="white")
    else:
        preset.config(text=presets[f"preset{nb}"][0], fg="black")



#si le bouton cancel sup (boutonCancelSup) est cliqué, le pop up confirmSup disparait
def clearConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup):
    confirmSup.place_forget()
    ombreConfirmSup.place_forget()
    boutonConfirmSup.place_forget()
    boutonCancelSup.place_forget()


#si le bouton confirm sup (boutonConfirmSup) est cliqué il supprime le nom du preset selectionné
def supression(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup):
    for cle, valeur in presetSelected.items():
        if valeur:
            nb = int(cle.replace("preset", ""))
            presets[cle][0] = "Aucun"
            for i in range(1, len(presets[cle])):
                presets[cle][i] = ""
            writeJsonPreset(presets)
            globals()[f"preset{nb}"].config(text="Ajouter", fg="white")

            clearConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup)
            globals()[f"entree{nb}"].delete(0, tk.END)

            presetSelected[f"preset{nb}"] = False


def popSynchronise(ombrePopupSynchro, popupSynchro, boutonCancelSynchro):
    ombrePopupSynchro.place(x=960, y=540, width=430, height=230, anchor="center")
    popupSynchro.place(x=960, y=540, width=400, height=200, anchor="center")
    boutonCancelSynchro.place(x=780, y=460, width=25, height=25, anchor="center")


    popupSynchro.config(text=verifMacroPad())

    send(presets)

    if connectVerif() == True:
        lab_connection_true.place(relx=0.5, y=100, anchor="center")
        lab_connection_false.place_forget()



def clearPopSynchronise(ombrePopupSynchro, popupSynchro, boutonCancelSynchro):
    ombrePopupSynchro.place_forget()
    popupSynchro.place_forget()
    boutonCancelSynchro.place_forget()



def popPlsConnect(ombrePlsConnect, plsConnect, boutonValid, boutonCancelPlsConnect):
    ombrePlsConnect.place(x=960, y=540, width=430, height=230, anchor="center")
    plsConnect.place(x=960, y=540, width=400, height=200, anchor="center")
    boutonValid.place(x=960, y=600, width=100, height=30, anchor="center")
    boutonCancelPlsConnect.place(x=780, y=460, width=25, height=25, anchor="center")



def clearPopPlsConnect(ombrePlsConnect, plsConnect, boutonValid, boutonCancelPlsConnect):
    ombrePlsConnect.place_forget()
    plsConnect.place_forget()
    boutonValid.place_forget()
    boutonCancelPlsConnect.place_forget()



# faire apparaitre la page principale
def showMain(root, showModifPage, showHelpPage):


    root.title("Macro Pad Config")
    root.geometry("1920x1080")
    #met la page en grand format par défaut
    root.state("zoomed")
    root.configure(bg="#F2F2F2")    
    

    #label texte bienvenue
    lab_bienvenue = tk.Label(root, text="Bienvenue sur Macro Pad Config", font=("Segoe UI", 30, "bold"))
    lab_bienvenue.pack()

    global lab_connection_true, lab_connection_false
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



    #configuration des ombres des presets
    ombrePreset1 = tk.Label(root, font=("Segoe UI", 30, "bold"), bg="#969696", width=10, height=14)
    ombrePreset1.place(x=330, y=560,anchor="center")  

    ombrePreset2 = tk.Label(root, font=("Segoe UI", 30, "bold"), bg="#969696", width=10, height=14)
    ombrePreset2.place(x=650, y=560,anchor="center")

    ombrePreset3 = tk.Label(root, font=("Segoe UI", 30, "bold"), bg="#969696", width=10, height=14)
    ombrePreset3.place(x=970, y=560,anchor="center")

    ombrePreset3 = tk.Label(root, font=("Segoe UI", 30, "bold"), bg="#969696", width=10, height=14)
    ombrePreset3.place(x=1290, y=560,anchor="center")

    ombrePreset3 = tk.Label(root, font=("Segoe UI", 30, "bold"), bg="#969696", width=10, height=14)
    ombrePreset3.place(x=1610, y=560,anchor="center")


    
    #config des presets
    #si ya rien dans le json par rapport au nom il affiche ajouter
    global preset1, preset2, preset3, preset4, preset5

    if presets["preset1"][0] == "Aucun":
        preset1 = tk.Label(root, text="Ajouter", font=("Segoe UI", 30, "bold"), bg="#CCCCCC",width=10, height=14, fg="white")
    else:
        preset1 = tk.Label(root, text=presets["preset1"][0], font=("Segoe UI", 30, "bold"), bg="#CCCCCC",width=10, height=14)
    preset1.place(x=320, y=550,anchor="center")

    if presets["preset2"][0] == "Aucun":
        preset2 = tk.Label(root, text="Ajouter", font=("Segoe UI", 30, "bold"), bg="#CCCCCC",width=10, height=14, fg="white")
    else:
        preset2 = tk.Label(root, text=presets["preset2"][0], font=("Segoe UI", 30, "bold"), bg="#CCCCCC", width=10, height=14)
    preset2.place(x=640, y=550,anchor="center")

    if presets["preset3"][0] == "Aucun":
        preset3 = tk.Label(root, text="Ajouter", font=("Segoe UI", 30, "bold"), bg="#CCCCCC",width=10, height=14, fg="white")
    else:
        preset3 = tk.Label(root, text=presets["preset3"][0], font=("Segoe UI", 30, "bold"), bg="#CCCCCC", width=10, height=14)
    preset3.place(x=960, y=550,anchor="center")

    if presets["preset4"][0] == "Aucun":
        preset4 = tk.Label(root, text="Ajouter", font=("Segoe UI", 30, "bold"), bg="#CCCCCC",width=10, height=14, fg="white")
    else:
        preset4 = tk.Label(root, text=presets["preset4"][0], font=("Segoe UI", 30, "bold"), bg="#CCCCCC", width=10, height=14)
    preset4.place(x=1280, y=550,anchor="center")

    if presets["preset5"][0] == "Aucun":
        preset5 = tk.Label(root, text="Ajouter", font=("Segoe UI", 30, "bold"), bg="#CCCCCC",width=10, height=14, fg="white")
    else:
        preset5 = tk.Label(root, text=presets["preset5"][0], font=("Segoe UI", 30, "bold"), bg="#CCCCCC", width=10, height=14)
    preset5.place(x=1600, y=550,anchor="center")


    #config des entree
    global entree1, entree2, entree3, entree4, entree5

    entree1 = tk.Entry(root,  font=("Segoe UI", 25, "bold"))
    entree2 = tk.Entry(root,  font=("Segoe UI", 25, "bold"))
    entree3 = tk.Entry(root,  font=("Segoe UI", 25, "bold"))
    entree4 = tk.Entry(root,  font=("Segoe UI", 25, "bold"))
    entree5 = tk.Entry(root,  font=("Segoe UI", 25, "bold"))


    #si le label preset est cliquer
    preset1.bind("<Button-1>", lambda event: showEntree(entree1, preset1, 320, 1))
    preset2.bind("<Button-1>", lambda event: showEntree(entree2, preset2, 640, 2))
    preset3.bind("<Button-1>", lambda event: showEntree(entree3, preset3, 960, 3))
    preset4.bind("<Button-1>", lambda event: showEntree(entree4, preset4, 1280, 4))
    preset5.bind("<Button-1>", lambda event: showEntree(entree5, preset5, 1600, 5))



    #configuration des ombres des bouton de suppression
    ombreSupPreset1 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSupPreset1.place(x=390, y=975 ,anchor="center")

    ombreSupPreset2 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSupPreset2.place(x=710, y=975 ,anchor="center")

    ombreSupPreset3 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSupPreset3.place(x=1030, y=975 ,anchor="center")

    ombreSupPreset4 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSupPreset4.place(x=1350, y=975 ,anchor="center")

    ombreSupPreset5 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSupPreset5.place(x=1670, y=975 ,anchor="center")


    #config des label suppression de presset
    supPreset1 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    supPreset1.place(x=385, y=970 ,anchor="center")

    supPreset2 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    supPreset2.place(x=705, y=970 ,anchor="center")

    supPreset3 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    supPreset3.place(x=1025, y=970 ,anchor="center")

    supPreset4 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    supPreset4.place(x=1345, y=970 ,anchor="center")

    supPreset5 = tk.Label(root, text="Supprimer", bg="#CCCCCC", width=10, height=2, fg="red")
    supPreset5.place(x=1665, y=970 ,anchor="center")


    ombreConfirmSup = tk.Label(root, bg="#969696")
    confirmSup = tk.Label(root, text="Êtes-vous sûr de vouloir supprimer ce preset ?", font=("Segoe UI", 12, "bold"), bg="#CCCCCC") 
    boutonConfirmSup = tk.Label(root, text="Supprimer", font=("Segoe UI", 10, "bold"), fg="red")
    boutonCancelSup = tk.Label(root, text="X", font=("Segoe UI", 15, "bold"), fg="red", bg="#CCCCCC")

    boutonConfirmSup.bind("<Button-1>", lambda event: supression(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup))
    boutonCancelSup.bind("<Button-1>", lambda event: clearConfirmSup(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup))

    


    #configuration du bind pour cliquer sur les boutons de suppression 
    supPreset1.bind("<Button-1>", lambda event: popConfirmation(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 1))
    supPreset2.bind("<Button-1>", lambda event: popConfirmation(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 2))
    supPreset3.bind("<Button-1>", lambda event: popConfirmation(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 3))
    supPreset4.bind("<Button-1>", lambda event: popConfirmation(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 4))
    supPreset5.bind("<Button-1>", lambda event: popConfirmation(confirmSup, ombreConfirmSup, boutonConfirmSup, boutonCancelSup, 5))




    #configuration des ombres des boutons de modifications
    ombreModifPreset1 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreModifPreset1.place(x=260, y=975 ,anchor="center")

    ombreModiPreset2 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreModiPreset2.place(x=580, y=975 ,anchor="center")

    ombreModiPreset3 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreModiPreset3.place(x=900, y=975 ,anchor="center")

    ombreModiPreset4 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreModiPreset4.place(x=1220, y=975 ,anchor="center")

    ombreModiPreset5 = tk.Label(root, bg="#969696", width=10, height=2)
    ombreModiPreset5.place(x=1540, y=975 ,anchor="center")


    #configuration des boutons de modification
    modifPreset1 = tk.Label(root, text="Modifier", bg="#CCCCCC", width=10, height=2)
    modifPreset1.place(x=255, y=970 ,anchor="center")

    modifPreset2 = tk.Label(root, text="Modifier", bg="#CCCCCC", width=10, height=2)
    modifPreset2.place(x=575, y=970 ,anchor="center")

    modifPreset3 = tk.Label(root, text="Modifier", bg="#CCCCCC", width=10, height=2)
    modifPreset3.place(x=895, y=970 ,anchor="center")

    modifPreset4 = tk.Label(root, text="Modifier", bg="#CCCCCC", width=10, height=2)
    modifPreset4.place(x=1215, y=970 ,anchor="center")

    modifPreset5 = tk.Label(root, text="Modifier", bg="#CCCCCC", width=10, height=2)
    modifPreset5.place(x=1535, y=970 ,anchor="center")


    modifPreset1.bind("<Button-1>", lambda event: (clearMain(root), modifPresetSelected(1), sendPresetSelected(), showModifPage(root, showMain, showHelpPage)))
    modifPreset2.bind("<Button-1>", lambda event: (clearMain(root), modifPresetSelected(2), sendPresetSelected(), showModifPage(root, showMain, showHelpPage)))
    modifPreset3.bind("<Button-1>", lambda event: (clearMain(root), modifPresetSelected(3), sendPresetSelected(), showModifPage(root, showMain, showHelpPage)))
    modifPreset4.bind("<Button-1>", lambda event: (clearMain(root), modifPresetSelected(4), sendPresetSelected(), showModifPage(root, showMain, showHelpPage)))
    modifPreset5.bind("<Button-1>", lambda event: (clearMain(root), modifPresetSelected(5), sendPresetSelected(), showModifPage(root, showMain, showHelpPage)))




    # configuration des label pop disconnected (si le bouton envoie et cliqué et que le macro pad n'est pas connecté)
    ombreError = tk.Label(root, bg="#969696")
    error = tk.Label(root, font=("Segoe UI", 12, "bold"), bg="#CCCCCC")
    boutonCrossError = tk.Label(root, text="X", font=("Segoe UI", 15, "bold"), fg="red", bg="#CCCCCC")

    boutonCrossError.bind("<Button-1>", lambda event: clearPopDisconnected(error, ombreError, boutonCrossError))




    # configuration de l'ombre du bouton save
    ombreEnvoie = tk.Label(root, bg="#969696", width=10, height=2)
    ombreEnvoie.place(x=1655, y=85, width=200, height=50, anchor="center")

    # configuration du bouton de sauvegarde
    envoie = tk.Label(root, text="Envoyer", font=("Segoe UI", 20, "bold"), bg="#CCCCCC")
    envoie.place(x=1650, y=80, width=200, height=50, anchor="center")

    # config du bind si on clique dessus
    envoie.bind("<Button-1>", lambda event: (send(presets), popDisconnected_Success(error, ombreError, boutonCrossError)))


    # configuration de l'ombre du bouton save
    ombreSynchronise = tk.Label(root, bg="#969696", width=10, height=2)
    ombreSynchronise.place(x=275, y=85, width=200, height=50, anchor="center")

    # config du bouton de synchronisation
    synchronise = tk.Label(root, text="Synchroniser", font=("Segoe UI", 20, "bold"), bg="#CCCCCC")
    synchronise.place(x=270, y=80, width=200, height=50, anchor="center")


    # config du bind si on clique dessus fait disparaitre le popup plsConnect
    synchronise.bind("<Button-1>", lambda event: popPlsConnect(ombrePlsConnect, plsConnect, boutonValid, boutonCancelPlsConnect))



    # config du popup qui demande de connecter le macro pad
    ombrePlsConnect = tk.Label(root, bg="#969696")
    plsConnect = tk.Label(root, text="Veuillez brancher votre Macro Pad. Ne validez pas sans avoir branché ce dernier.", font=("Segoe UI", 12, "bold"), bg="#CCCCCC", wraplength=350, justify="center")
    boutonValid = tk.Label(root, text="Valider", font=("Segoe UI", 10, "bold"), fg="red")
    boutonCancelPlsConnect = tk.Label(root, text="X", font=("Segoe UI", 15, "bold"), fg="red", bg="#CCCCCC")

    # config du bind si on clique dessus il fait disparaitre le popup plsConnect et fait apparaitre le popup synchronise
    boutonValid.bind("<Button-1>", lambda event: (clearPopPlsConnect(ombrePlsConnect, plsConnect, boutonValid, boutonCancelPlsConnect), popSynchronise(ombrePopupSynchro, popupSynchro, boutonCancelSynchro)))

    # config du bind si on clique dessus il fait disparaitre le popup plsConnect
    boutonCancelPlsConnect.bind("<Button-1>", lambda event: clearPopPlsConnect(ombrePlsConnect, plsConnect, boutonValid, boutonCancelPlsConnect))



    # config du popup synchro quand le bouton synchroniser est cliqué
    ombrePopupSynchro = tk.Label(root, bg="#969696")
    popupSynchro = tk.Label(root, text="", font=("Segoe UI", 12, "bold"), bg="#CCCCCC")
    boutonCancelSynchro = tk.Label(root, text="X", font=("Segoe UI", 15, "bold"), fg="red", bg="#CCCCCC")

    # config du bind si on clique dessus fait disparaitre le popup Synchronise
    boutonCancelSynchro.bind("<Button-1>", lambda event: clearPopSynchronise(ombrePopupSynchro, popupSynchro, boutonCancelSynchro))


    # config de l'ombre du bouton help
    boutonHelp = tk.Label(root, text="?", font=("Segoe UI", 20, "bold"), bg="#969696", fg="black")
    boutonHelp.place(x=85, y=85, width= 50, height=50, anchor="center")

    # config du bouton help qui dirigera vers la page Help (interfaceHelp)
    boutonHelp = tk.Label(root, text="?", font=("Segoe UI", 20, "bold"), bg="#CCCCCC", fg="black")
    boutonHelp.place(x=80, y=80, width= 50, height=50, anchor="center")

    # config du bind du bouton help pour qu'il dirige vers la page Help lorsqu'il est cliqué
    boutonHelp.bind("<Button-1>", lambda event: (clearMain(root), showHelpPage(root, showMain, showModifPage)))

















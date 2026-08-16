import tkinter as tk
from interfaceMain import clearMain


def showEntree(entree, root):
    entree.config(state="normal")
    entree.place(x=960, y=890, anchor="center")
    entree.insert(0, "wyrdproo@gmail.com")
    entree.config(state="readonly")

    def clic(event):
        if event.widget != entree:
            clearEntree(entree, root)

    root.bind("<Button-1>", clic)


def clearEntree(entree, root):
    entree.config(state="normal")
    entree.delete(0, tk.END)
    entree.config(state="readonly")
    entree.place_forget()

    root.unbind("<Button-1>")


def showHelpPage(root, showMain, showModifPage): # !!!!!  mettre les parametre root et showMain !!!!!


    #config de la fenêtre
    root.title("Macro Pad Config")
    root.geometry("1920x1080")
    #met la page en grand format par défaut
    root.state("zoomed")
    root.configure(bg="#F2F2F2")


    #label texte nomination de la page
    lab_title = tk.Label(root, text="Guide d'utilisation", font=("Segoe UI", 30, "bold"))
    lab_title.pack()

    Main = tk.Label(
        root, 
        text="1: PAGE PRINCIPALE", 
        font=("Segoe UI", 20, "bold"),
        wraplength=1820
        )
    
    Main.place(x=100, y=100)

    MainExplication = tk.Label(
        root, 
        text=(
        "● Veillez à synchroniser votre macro pad en cliquant sur le bouton synchroniser en haut a gauche. Il permet au logiciel de détecter un Macro Pad et de l'identifié.\n"
        "● Si vous cliquez sur le bouton synchroniser et que vous valider alors que le Macro Pad n'est pas branché, le logiciel plantera.\n"
        "● Le texte du dessus indique si un macro pad synchronisé est connecté ou non.\n"
        "● Vous avez la possibilité de cliquer sur le nom des labels pour les changer.\n"
        "● Une fois toutes vos modifications faites, veillez à appuyer sur le bouton envoyer afin que le Macro Pad reçoive les changements.\n"
        "● Les boutons supprimer supprimeront les presets correspondants à ces boutons en entier (le nom et les raccourcis).\n"
        "● Les boutons modifier vous redirigeront vers une autre page permettant de modifier le nom et les raccourcis des presets correspondants aux boutons cliqués.\n"
        ),
        font=("Segoe UI", 15),
        wraplength=1820,
        justify="left"
    )
    MainExplication.place(x=200, y=150)



    Modif = tk.Label(
        root, 
        text="2: PAGE DE MODIFICATION", 
        font=("Segoe UI", 20, "bold"),
        wraplength=1650
        )
    Modif.place(x=100,y=380)

    ModifExplication = tk.Label(
        root, 
        text=(
        "● Chaque carré corespond à un switch (comme écrit). L'ordre va de gauche à droite.\n"
        "● Le rond au milieu corespond au potentiometre (comme écrit). Le raccourci le plus en haut correspond au raccourci exécuté lorsque le potentiomtre tourne à droite (comme l'indique la flèche). Et le raccourci le plus en bas correspond au raccourci exécuté lorsque le potentiometre tourne à gauche (comme l'indique la flèche également).\n"
        "● Vous avez la possibilité de cliquer sur le nom du preset selectionné pour le modifier.\n"
        "● Pour changer les raccourcis des switchs, cliquez sur le switch auquel vous voulez apporter des modifications et entrez les touches du nouveau raccourci un par un. Tapez sur votre touche F1 pour activer le Verr Maj. Tapez sur votre touche échap (esc) pour finir votre saisie de raccourci.\n"
        "● Pour changer les raccourcis du potentiometre, cliquez sur le potentiometre et entrez les touches du nouveau raccourci un par un. Tapez sur votre touche F1 pour activer le Verr Maj. Tapez sur votre touche échap (esc) pour finir votre saisie de raccourci.\n"
        "● Les boutons supprimer en dessous des switchs (les carrés) supprimeront les raccourcis des switchs correspondants.\n"
        "● Les boutons supprimer en dessous du potentiometre (le rond) supprimeront les raccourcis attribués à ces boutons. Le bouton supprimer le plus en haut supprime le raccourci exécuté lorsque le potentiometre tourne à droite (comme l'indique les flèches) et inversement pour le bouton du bas.\n"
        ),
        font=("Segoe UI", 15),
        wraplength=1650,
        justify="left"
    )
    ModifExplication.place(x=200, y=430)


    # config du texte qui donne mon email si il y a un problème a signaler
    signal = tk.Label(root, text="Si vous avez un problème à reporter, vous pouvez le signaler en contactant l'adresse email suivante (cliquez pour copier-coller ;) ) :", font=("Segoe UI", 20, "bold"), bg="#F2F2F2", fg="black", wraplength=1700, justify="center")
    signal.place(x=960, y=830, anchor="center")

    email = tk.Label(root, text="email : wyrdproo@gmail.com", font=("Segoe UI", 20, "bold"), bg="#F2F2F2", fg="black", wraplength=1650, justify="center")
    email.place(x=960, y=890, anchor="center")

    merci = tk.Label(root, text="Merci !", font=("Segoe UI", 20, "bold"), bg="#F2F2F2", fg="black", wraplength=1650, justify="center")
    merci.place(x=960, y=950, anchor="center")


    email.bind("<Button-1>", lambda event: showEntree(entree, root))


    # config de l'entree read-only qui permet de copier-coller l'email
    entree = tk.Entry(root, state="readonly", font=("Segoe UI", 25, "bold"))
    

    # config du bouton retour
    back = tk.Label(root, text="X", font=("Segoe UI", 15, "bold"), bg="#CCCCCC", fg="red")
    back.place(x=100, y=50, width= 50, height=50, anchor="center")

    back.bind("<Button-1>", lambda event:(clearMain(root), showMain(root, showModifPage, showHelpPage)))








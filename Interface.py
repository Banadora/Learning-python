################### Labyrinthe - Interface ###################

# -*- coding: utf8 -*-

from tkinter import *
from tkinter.filedialog import *
from PIL import Image, ImageTk
from MapFuncs import *
from MoveFuncs import *
from CharFuncs import *


class MakeUI(Frame):

    """ Creates the user interface """

    def __init__(self, Fenetre, **kwargs):

        # Inherit datas
        Frame.__init__(self, Fenetre, width=1500, height=700, **kwargs)

        self.pack(fill=BOTH)
        self.KeysInfos = "\nVous êtes un héros qui cherche à s'échapper \ndu labyrinthe pour gagner du $$$\n\n" + \
         " Appuyez Z pour aller vers le haut\n" + \
         "   Appuyez Q pour aller vers la gauche\n" \
         "   Appuyez D pour aller vers la droite\n" \
         "Appuyez S pour aller vers le bas\n\n" + \
        "---------------------------------------------------------\n\n"
        self.FileName = ""
        self.ActualMap = {}
        self.LinesList = []
        self.EndOfMap = 0
        self.PlayFinalSound = 1
        self.TempPath = ""

        # Images imports
        self.ImgBlank = Image.open('Images/Blank.ico')
        self.TkImgBlank = ImageTk.PhotoImage(self.ImgBlank)
        self.ImgBlank.close()

        self.ImgMur = Image.open('Images/Wall.ico')
        self.TkImgMur = ImageTk.PhotoImage(self.ImgMur)
        self.ImgMur.close()

        self.ImgDollar = Image.open('Images/Dollar.ico')
        self.TkImgDollar = ImageTk.PhotoImage(self.ImgDollar)
        self.ImgDollar.close()

        self.ImgStairsUp = Image.open('Images/StairsUp.ico')
        self.TkImgStairsUp = ImageTk.PhotoImage(self.ImgStairsUp)
        self.ImgStairsUp.close()

        self.ImgStairsDown = Image.open('Images/StairsDown.ico')
        self.TkImgStairsDown = ImageTk.PhotoImage(self.ImgStairsDown)
        self.ImgStairsDown.close()

        # Move keys
        self.bind_all("z", lambda e: Move(self, "Z"))
        self.bind_all("q", lambda e: Move(self, "Q"))
        self.bind_all("s", lambda e: Move(self, "S"))
        self.bind_all("d", lambda e: Move(self, "D"))

        # Information frame
        self.FrameInfos = LabelFrame(self, text="Choix des paramètres", padx=2, pady=2)
        self.FrameInfos.pack(fill="both", expand="yes", padx=5, pady=5)

        # Cadre d'affichage de l'aancienne carte et des infos de jeu
        self.FrameCarte = LabelFrame(self, text="Infos", padx=2, pady=2)
        self.FrameCarte.pack(side=LEFT, fill="both", expand="yes", padx=2, pady=2)

        # Cadre d'affichage de la carte graphique
        self.FrameCarteGraph = LabelFrame(self, text="Carte", padx=2, pady=2)
        self.FrameCarteGraph.pack(side=RIGHT, fill="both", expand="yes", padx=2, pady=2)

        # Cadre des boutons de commandes
        self.FrameCtrl = Frame(self, padx=2, pady=2)
        self.FrameCtrl.pack(fill="both", expand="yes", padx=5, pady=5)

        # Affichage des informations
        self.MsgInfos = Label(self.FrameInfos, text=" ^ Menus de sélection du personnage et de la carte \t\t\t\t     Personnage : ")
        self.MsgInfos.pack(side=LEFT, padx=5, pady=5)

        # Affichage du personnage selectionné
        self.CanvasPersoSelect = Canvas(self.FrameInfos, width=500, height=40)
        self.CanvasPersoSelect.pack(side=RIGHT, padx=5, pady=5)

        self.MsgInfosCarte = Label(self.FrameCarte, text="", width=45)
        self.MsgInfosCarte.pack(padx=2, pady=2)

        self.MsgInfosCarteSup = Label(self.FrameCarte, text="", font=('Lucida Console', 10, 'bold'), width=45)
        self.MsgInfosCarteSup.pack(padx=2, pady=2)

        self.CanvasCarte = Canvas(self.FrameCarteGraph, width=670, height=660)
        self.CanvasCarte.pack(padx=0, pady=0)

        self.FctMenus(Fenetre)

###################################################################################################################
###################################################################################################################
    def FctMenus(self, Fenetre):
        # Menus
        ListePersos = ["Alien", "Angel", "Baby", "Boxer", "Chef", "Clown", "Dad", "Devil", "Doctor", "Dragon", "Firefighter", "Ghost",
            "Girl", "Kid", "King", "Knight", "Lawyer", "Leprechaun", "Man", "Mermaid", "Monster", "Ninja", "Nurse", "Pirate",
            "Policeman", "Prince", "Princess", "Queen", "Robot", "Santa", "Snowman", "Superhero", "Teacher", "Troll", "Vampire",
            "Werewolf", "Witch", "Zombie"]

        self.Menubar = Menu(Fenetre)

        self.MenuPersos = Menu(self.Menubar, tearoff=0)

        for elmt in ListePersos:
            self.MenuPersos.add_command(label=elmt, command=lambda elmt=elmt: PickChar(self, elmt))

        self.Menubar.add_cascade(label="Personnages", menu=self.MenuPersos)

######################################################
        ListeCartes = ["1.0 - Jardinet (Facile)",
                       "2.0 - Petite caverne (Moyen)",
                       "3.0 - Serpentin (Moyen)",
                       "4.1 - Plus haut (Facile)",
                       "5.1 - Maison (Moyen)"]

        self.MenuCartes = Menu(self.Menubar, tearoff=0)

        for elmt in ListeCartes:
            self.MenuCartes.add_command(label=elmt, command=lambda elmt=elmt: OpenMap(self, elmt))

        self.Menubar.add_cascade(label="Cartes", menu=self.MenuCartes)

######################################################
        Fenetre.config(menu=self.Menubar)

###################################################################################################################
###################################################################################################################

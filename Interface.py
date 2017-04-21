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
        self.KeysInfos = "\nVous êtes un héros qui cherche à s'échapper \n \
        du labyrinthe pour gagner du $$$\n\n" + \
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
        self.Difficulty = 99
        self.NbLignes = 1
        self.NbColonnes = 1
        self.PosX = 1
        self.PosY = 1
        self.MapLoaded = 0

        self.ImagesImport()

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
        self.MsgInfos = Label(self.FrameInfos, text="Personnage : ")
        self.MsgInfos.pack(side=LEFT, padx=5, pady=5)

        # Affichage du personnage selectionné
        self.CanvasPersoSelect = Canvas(self.FrameInfos, width=100, height=40)
        self.CanvasPersoSelect.pack(side=LEFT, padx=5, pady=5)

        # Difficulté
        self.MsgDifficultyBefore = Label(self.FrameInfos, text="Difficulté :")
        self.MsgDifficultyBefore.pack(side=LEFT, padx=2, pady=2)
        self.DifficultyScale = Scale(self.FrameInfos, from_=1, to=3, showvalue=0, orient=HORIZONTAL, length=75, sliderlength=25,
             variable=self.Difficulty, command=self.ShowDifficultyScale)
        self.DifficultyScale.set(2)
        self.DifficultyScale.pack(side=LEFT, padx=2, pady=2)
        self.MsgDifficulty = Label(self.FrameInfos, text=" ")
        self.MsgDifficulty.pack(side=LEFT, padx=2, pady=2)

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
            self.MenuCartes.add_command(label=elmt, command=lambda elmt=elmt: OpenMap(self, elmt, 1))

        self.Menubar.add_cascade(label="Cartes", menu=self.MenuCartes)

######################################################
        Fenetre.config(menu=self.Menubar)

###################################################################################################################
###################################################################################################################

    def ShowDifficultyScale(self, val):
        value = int(float(val))
        if value == 1:                 # Easy
            self.BlurLevel = 6
            self.LivesAtStart = 6
            self.Lives = self.LivesAtStart
            self.MsgDifficulty["text"] = "Facile"
        elif value == 2:               # Medium
            self.BlurLevel = 4
            self.LivesAtStart = 4
            self.Lives = self.LivesAtStart
            self.MsgDifficulty["text"] = "Medium"
        elif value == 3:               # Hard
            self.BlurLevel = 2
            self.LivesAtStart = 2
            self.Lives = self.LivesAtStart
            self.MsgDifficulty["text"] = "Bonhomme"

        if self.MapLoaded == 1:
            ShowMap(self)

###################################################################################################################
###################################################################################################################
    def ImagesImport(self):
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

        self.ImgBlur = Image.open('Images/Blur.ico')
        self.TkImgBlur = ImageTk.PhotoImage(self.ImgBlur)
        self.ImgBlur.close()

        self.ImgSnake = Image.open('Images/Snake.ico')
        self.TkImgSnake = ImageTk.PhotoImage(self.ImgSnake)
        self.ImgSnake.close()

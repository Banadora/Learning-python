################### Tests Tkinter - Classes ###################

# -*- coding: utf8 -*-

import os
import winsound
from tkinter import *
from tkinter.filedialog import *
from PIL import Image, ImageTk


class MakeUI(Frame):

    """ Classe de création d'interface utilisateur """

    def __init__(self, Fenetre, **kwargs):

        # Héritage et données
        Frame.__init__(self, Fenetre, width=1500, height=700, **kwargs)

        self.pack(fill=BOTH)
        self.InfosTouches = "\nVous êtes un héros qui cherche à s'échapper \ndu labyrinthe pour gagner du $$$\n\n" + \
         " Appuyez Z pour aller vers le haut\n" + \
         "   Appuyez Q pour aller vers la gauche\n" \
         "   Appuyez D pour aller vers la droite\n" \
         "Appuyez S pour aller vers le bas\n\n" + \
        "---------------------------------------------------------\n\n"
        self.FileName = ""
        self.CarteActuelle = {}
        self.ListeLignes = []
        self.FinDeCarte = 0
        self.PlayFinalSound = 1
        self.TempPath = ""

        # Importation des images
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

        # Definition des touches de direction
        self.bind_all("z", lambda e: self.Play("Z"))
        self.bind_all("q", lambda e: self.Play("Q"))
        self.bind_all("s", lambda e: self.Play("S"))
        self.bind_all("d", lambda e: self.Play("D"))

        # Cadre des informations
        self.FrameInfos = LabelFrame(self, text="Choix des paramètres", padx=2, pady=2)
        self.FrameInfos.pack(fill="both", expand="yes", padx=5, pady=5)

        # Cadre général du jeu
        #self.FrameGeneral = LabelFrame(self, text="Labyrinthe", padx=2, pady=2)
        #self.FrameGeneral.pack(fill="both", expand="yes", padx=5, pady=5)

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

        # Bouton d'ouverture de carte
        #self.BtnOuvrirCarte = Button(self.FrameInfos, text="Carte", bg="orange", state=DISABLED, width=10, command=self.OuvrirCarte)
        #self.BtnOuvrirCarte.pack(side="right", padx=5, pady=5)

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
    def ChoisirPerso(self, Perso):
        # Fonction d'ouverture du fichier personnage
        self.TempPathPerso = 'Images/Characters/' + Perso + '.ico'
        self.ImgPerso = Image.open(self.TempPathPerso)
        self.TkImgPerso = ImageTk.PhotoImage(self.ImgPerso)
        self.ImgPerso.close()

        self.CanvasPersoSelect.create_image(20, 20, image=self.TkImgPerso)

        return self.TkImgPerso

###################################################################################################################
###################################################################################################################
    def OuvrirCarte(self, Carte):
        # Ouverture de la carte au démarrage
        self.ListeLignes = []
        self.CarteActuelle = {}
        self.FileName = ""
        self.MsgInfosCarte["text"] = ""
        self.FinDeCarte = 0
        self.PlayFinalSound = 1

        self.TempPathCarte = 'Cartes/' + Carte + '.txt'
        #self.FileName = askopenfilename(title="Ouvrir une carte", filetypes=[('txt files', '.txt'), ('all files', '.*')])

        self.Fichier = open(self.TempPathCarte, "r")
        self.CarteActuelle = self.Fichier.read()
        self.Fichier.close()

        # Y = Ligne   X = Colonne
        if '1.0' in self.TempPathCarte:
            self.PosX = 2
            self.PosY = 1
            self.NbLignes = 6
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 1 : Jardinet  (Facile)"
        elif '2.0' in self.TempPathCarte:
            self.PosX = 4
            self.PosY = 1
            self.NbLignes = 20
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 2 : Petite caverne (Moyen)"
        elif '3.0' in self.TempPathCarte:
            self.PosX = 10
            self.PosY = 9
            self.NbLignes = 20
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 3 : Serpentin (Moyen)"
        elif '4.1' in self.TempPathCarte:
            self.PosX = 3
            self.PosY = 4
            self.NbLignes = 8
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 4.1 - Plus haut (Facile)"
        elif '5.1' in self.TempPathCarte:
            self.PosX = 4
            self.PosY = 9
            self.NbLignes = 12
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"

######################################################
        self.MsgInfosCarte["font"] = ('Lucida Console', 8)

        i = 0
        j = 0
        k = self.NbColonnes
        while i <= self.NbLignes - 1:
            self.ListeLignes.append(self.CarteActuelle[j:k])
            i += 1
            j = k + 1
            k = j + self.NbColonnes

        self.MsgInfosCarte["text"] = ""
        self.MsgInfosCarte["text"] = self.InfosTouches + "\n Position >>   Ligne : "\
             + str(self.PosY + 1) + "   Colonne : " + str(self.PosX) + \
        "\n\n\n---------------------------------------------------------\n\n"

        self.AfficherCarte()

###################################################################################################################
###################################################################################################################
    def Play(self, Touche):
        if self.FinDeCarte == 1:
            TouchePressee = "NULL"
        else:
            TouchePressee = Touche

        InfoSup = ""

######################################################
        if TouchePressee == "Z":
            LigneDuHero = self.ListeLignes[self.PosY]
            NouvelleLigneDuHero = self.ListeLignes[self.PosY - 1]
            if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '#':
                InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé."
            else:
                HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
                DebutNouvelleLigne = LigneDuHero[:self.PosX - 1]
                FinNouvelleLigne = LigneDuHero[self.PosX:]

                LigneDuHero = DebutNouvelleLigne + HeroRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY], LigneDuHero = LigneDuHero, self.ListeLignes[self.PosY]

                BlancRemplace = NouvelleLigneDuHero[self.PosX - 1:self.PosX].replace(' ', '~')
                DebutNouvelleLigne = NouvelleLigneDuHero[:self.PosX - 1]
                FinNouvelleLigne = NouvelleLigneDuHero[self.PosX:]

                NouvelleLigneDuHero = DebutNouvelleLigne + BlancRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY - 1], NouvelleLigneDuHero = NouvelleLigneDuHero, self.ListeLignes[self.PosY - 1]
                self.PosY -= 1

            if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '$':
                self.FinDeCarte = 1
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
                self.ChangerNiveau(self.TempPathCarte)

######################################################
        elif TouchePressee == "Q":
            LigneDuHero = self.ListeLignes[self.PosY]
            if LigneDuHero[self.PosX - 2:self.PosX - 1] == '#':
                InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé."
            else:
                DebutNouvelleLigne = LigneDuHero[0:self.PosX - 2]
                BlancRemplace = LigneDuHero[self.PosX - 2:self.PosX - 1].replace(' ', '~')
                HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
                FinNouvelleLigne = LigneDuHero[self.PosX:]

                LigneDuHero = DebutNouvelleLigne + BlancRemplace + HeroRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY], LigneDuHero = LigneDuHero, self.ListeLignes[self.PosY]
                self.PosX -= 1

            if LigneDuHero[self.PosX - 1:self.PosX] == '$':
                self.FinDeCarte = 1
            elif LigneDuHero[self.PosX - 1:self.PosX] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif LigneDuHero[self.PosX - 1:self.PosX] == 'v':
                self.ChangerNiveau(self.TempPathCarte)

######################################################
        elif TouchePressee == "S":
            LigneDuHero = self.ListeLignes[self.PosY]
            NouvelleLigneDuHero = self.ListeLignes[self.PosY + 1]
            if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '#':
                InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé."
            else:
                HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
                DebutNouvelleLigne = LigneDuHero[:self.PosX - 1]
                FinNouvelleLigne = LigneDuHero[self.PosX:]

                LigneDuHero = DebutNouvelleLigne + HeroRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY], LigneDuHero = LigneDuHero, self.ListeLignes[self.PosY]

                BlancRemplace = NouvelleLigneDuHero[self.PosX - 1:self.PosX].replace(' ', '~')
                DebutNouvelleLigne = NouvelleLigneDuHero[:self.PosX - 1]
                FinNouvelleLigne = NouvelleLigneDuHero[self.PosX:]

                NouvelleLigneDuHero = DebutNouvelleLigne + BlancRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY + 1], NouvelleLigneDuHero = NouvelleLigneDuHero, self.ListeLignes[self.PosY + 1]
                self.PosY += 1

            if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '$':
                self.FinDeCarte = 1
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
                self.ChangerNiveau(self.TempPathCarte)

######################################################
        elif TouchePressee == "D":
            LigneDuHero = self.ListeLignes[self.PosY]
            if LigneDuHero[self.PosX:self.PosX + 1] == "#":
                InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé."
            else:
                HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
                BlancRemplace = LigneDuHero[self.PosX:self.PosX + 1].replace(' ', '~')
                DebutNouvelleLigne = LigneDuHero[0:self.PosX - 1]
                FinNouvelleLigne = LigneDuHero[self.PosX + 1:]

                LigneDuHero = DebutNouvelleLigne + HeroRemplace + BlancRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY], LigneDuHero = LigneDuHero, self.ListeLignes[self.PosY]
                self.PosX += 1

            if LigneDuHero[self.PosX - 1:self.PosX] == '$':
                self.FinDeCarte = 1
            elif LigneDuHero[self.PosX - 1:self.PosX] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif LigneDuHero[self.PosX - 1:self.PosX] == 'v':
                self.ChangerNiveau(self.TempPathCarte)

######################################################
        self.AfficherCarte()

        i = 0
        while i <= self.NbLignes - 1:
            self.CarteActuelle += self.ListeLignes[i]
            self.CarteActuelle += "\n"
            i += 1

        self.MsgInfosCarte["text"] = ""
        self.MsgInfosCarteSup["text"] = ""

        self.MsgInfosCarte["text"] = self.InfosTouches + "\n Position >>   Ligne : " + str(self.PosY + 1) + \
            "   Colonne : " + str(self.PosX) + \
        "\n\n\n---------------------------------------------------------\n\n"

        if self.FinDeCarte == 0:
            self.MsgInfosCarteSup["text"] = InfoSup
        else:
            InfoSup = "\nBRAVO : pensez à dépenser vos $$$ !"
            self.MsgInfosCarteSup["text"] = InfoSup
            if self.PlayFinalSound == 1:
                winsound.PlaySound('Sons/Caisse enregistreuse.wav', winsound.SND_FILENAME)
                winsound.PlaySound('Sons/Pieces.wav', winsound.SND_FILENAME)
                self.PlayFinalSound = 0

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
            self.MenuPersos.add_command(label=elmt, command=lambda elmt=elmt: self.ChoisirPerso(elmt))

        self.Menubar.add_cascade(label="Personnages", menu=self.MenuPersos)

######################################################
        ListeCartes = ["1.0 - Jardinet (Facile)",
                       "2.0 - Petite caverne (Moyen)",
                       "3.0 - Serpentin (Moyen)",
                       "4.1 - Plus haut (Facile)",
                       "5.1 - Maison (Moyen)"]

        self.MenuCartes = Menu(self.Menubar, tearoff=0)

        for elmt in ListeCartes:
            self.MenuCartes.add_command(label=elmt, command=lambda elmt=elmt: self.OuvrirCarte(elmt))

        self.Menubar.add_cascade(label="Cartes", menu=self.MenuCartes)

######################################################
        Fenetre.config(menu=self.Menubar)

###################################################################################################################
###################################################################################################################
    def ChangerNiveau(self, Carte):
        if '4.1' in Carte:
            if ((self.PosX == 19) and (self.PosY == 6)):                        # 4.1 -> 4.2 (1)
                self.FrameCarteGraph["text"] = " 4.2 - Plus haut (Facile)"
                NouvelleCarte = "4.2 - Plus haut (Facile)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 19
                self.PosY = 5
                self.ListeLignes[5] = "# # #   #       ##~#"
        if '4.2' in Carte:
            if ((self.PosX == 19) and (self.PosY == 6)):                        # 4.2 -> 4.1 (1)
                self.FrameCarteGraph["text"] = " 4.1 - Plus haut (Facile)"
                NouvelleCarte = "4.1 - Plus haut (Facile)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 19
                self.PosY = 5
                self.ListeLignes[4] = "#  #       ## # #  #"
                self.ListeLignes[5] = "#### ######    # #~#"

######################################################
        if '5.1' in Carte:
            if ((self.PosX == 2) and (self.PosY == 5)):                        # 5.1 -> 5.2 (1)
                self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
                NouvelleCarte = "5.2 - Maison (Moyen)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 3
                self.PosY = 6
                self.ListeLignes[6] = "#v~    #     #      "
            if ((self.PosX == 14) and (self.PosY == 10)):                      # 5.1 -> 5.2 (2)
                self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
                NouvelleCarte = "5.2 - Maison (Moyen)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 2
                self.PosY = 1
                self.ListeLignes[1] = "#~v#    #v#  #      "
            if ((self.PosX == 3) and (self.PosY == 7)):                      # 5.1 -> 5.2 (3)
                self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
                NouvelleCarte = "5.2 - Maison (Moyen)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 10
                self.PosY = 2
                self.ListeLignes[2] = "# #  #  #~ # #      "
        if '5.2' in Carte:
            if ((self.PosX == 2) and (self.PosY == 6)):                        # 5.2 -> 5.1 (1)
                self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
                NouvelleCarte = "5.1 - Maison (Moyen)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 3
                self.PosY = 5
                self.ListeLignes[9] = "#$# ##   #   #    ##"
                self.ListeLignes[5] = "#^~### #### #  #   #"
            if ((self.PosX == 3) and (self.PosY == 1)):                        # 5.2 -> 5.1 (2)
                self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
                NouvelleCarte = "5.1 - Maison (Moyen)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 15
                self.PosY = 10
                self.ListeLignes[9] = "#$# ##   #   #    ##"
                self.ListeLignes[10] = "##     ##  ##^~## ##"
            if ((self.PosX == 10) and (self.PosY == 1)):                        # 5.2 -> 5.1 (3)
                self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
                NouvelleCarte = "5.1 - Maison (Moyen)"
                self.NbLignes = 8
                self.NbColonnes = 20
                self.OuvrirCarte(NouvelleCarte)
                self.PosX = 2
                self.PosY = 7
                self.ListeLignes[9] = "#$# ##   #   #    ##"
                self.ListeLignes[7] = "#~^#########  ##  ##"

###################################################################################################################
###################################################################################################################
    def AfficherCarte(self):
        # Suppression de l'ancienne carte si necessaire
        self.CanvasCarte.delete("all")

        # Positionnement des blocs
        for x in range(self.NbLignes):
            for y in range(self.NbColonnes):
                if self.ListeLignes[x][y] == '#':
                    self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgMur)
                elif self.ListeLignes[x][y] == '$':
                    self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgDollar)
                elif self.ListeLignes[x][y] == '~':
                    self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgPerso)
                elif self.ListeLignes[x][y] == ' ':
                    self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgBlank)
                elif self.ListeLignes[x][y] == '^':
                    self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgStairsUp)
                elif self.ListeLignes[x][y] == 'v':
                    self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgStairsDown)

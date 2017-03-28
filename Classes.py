################### Tests Tkinter - Classes ###################

# -*- coding: utf8 -*-

import os
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

        # Importation des murs et de la sortie $$
        self.ImgBlank = Image.open('Images/Blank.ico')
        self.TkImgBlank = ImageTk.PhotoImage(self.ImgBlank)
        self.ImgBlank.close()

        self.ImgMur = Image.open('Images/Wall.ico')
        self.TkImgMur = ImageTk.PhotoImage(self.ImgMur)
        self.ImgMur.close()

        self.ImgDollar = Image.open('Images/Dollar.ico')
        self.TkImgDollar = ImageTk.PhotoImage(self.ImgDollar)
        self.ImgDollar.close()

        # Definition des touches de direction
        self.bind_all("z", lambda e: self.Play("Z"))
        self.bind_all("q", lambda e: self.Play("Q"))
        self.bind_all("s", lambda e: self.Play("S"))
        self.bind_all("d", lambda e: self.Play("D"))

        # Cadre des informations
        self.FrameInfos = LabelFrame(self, text="Intro", padx=2, pady=2)
        self.FrameInfos.pack(fill="both", expand="yes", padx=5, pady=5)

        # Cadre général du jeu
        self.FrameGeneral = LabelFrame(self, text="Labyrinthe", padx=2, pady=2)
        self.FrameGeneral.pack(fill="both", expand="yes", padx=5, pady=5)

        # Cadre d'affichage de l'aancienne carte et des infos de jeu
        self.FrameCarte = LabelFrame(self.FrameGeneral, text="Infos", padx=2, pady=2)
        self.FrameCarte.pack(side=LEFT, fill="both", expand="yes", padx=2, pady=2)

        # Cadre d'affichage de la carte graphique
        self.FrameCarteGraph = LabelFrame(self.FrameGeneral, text="Carte", padx=2, pady=2)
        self.FrameCarteGraph.pack(side=RIGHT, fill="both", expand="yes", padx=2, pady=2)

        # Cadre des boutons de commandes
        self.FrameCtrl = Frame(self, padx=2, pady=2)
        self.FrameCtrl.pack(fill="both", expand="yes", padx=5, pady=5)

        # Affichage des informations
        self.MsgInfos = Label(self.FrameInfos, text="Sélection du personnage et de la carte")
        self.MsgInfos.pack(side="left", padx=5, pady=5)

        # Bouton pour quitter le programme
        self.BtnQuitter = Button(self.FrameInfos, text="Quitter", bg="red", width=10, command=self.quit)
        self.BtnQuitter.pack(side="right", padx=5, pady=5)

        # Bouton d'ouverture de carte
        self.BtnOuvrirCarte = Button(self.FrameInfos, text="Carte", bg="orange", state=DISABLED, width=10, command=self.OuvrirCarte)
        self.BtnOuvrirCarte.pack(side="right", padx=5, pady=5)

        # Bouton de choix du personnage
        self.BtnChoixPerso = Button(self.FrameInfos, text="Personnage", bg="orange", state=NORMAL, width=10, command=self.ChoisirPerso)
        self.BtnChoixPerso.pack(side="right", padx=5, pady=5)

        self.MsgInfosCarte = Label(self.FrameCarte, text="", width=45)
        self.MsgInfosCarte.pack(padx=2, pady=2)

        self.MsgInfosCarteSup = Label(self.FrameCarte, text="", font=('Lucida Console', 10, 'bold'), width=45)
        self.MsgInfosCarteSup.pack(padx=2, pady=2)

        self.CanvasCarte = Canvas(self.FrameCarteGraph, width=670, height=660)
        self.CanvasCarte.pack(padx=0, pady=0)

###################################################################################################################
###################################################################################################################
    def ChoisirPerso(self):
        # Fonction d'ouverture du fichier personnage
        self.FilePersoName = askopenfilename(title="Choisir un personnage", filetypes=[('ico files', '.ico'), ('all files', '.*')])
        self.ImgPerso = Image.open(self.FilePersoName)
        self.TkImgPerso = ImageTk.PhotoImage(self.ImgPerso)
        self.ImgPerso.close()
        self.BtnOuvrirCarte["state"] = NORMAL

###################################################################################################################
###################################################################################################################
    def OuvrirCarte(self):
        # Ouverture de la carte au démarrage

        self.ListeLignes = []
        self.CarteActuelle = {}
        self.FileName = ""
        self.MsgInfosCarte["text"] = ""

        self.FileName = askopenfilename(title="Ouvrir une carte", filetypes=[('txt files', '.txt'), ('all files', '.*')])
        self.Fichier = open(self.FileName, "r")
        self.CarteActuelle = self.Fichier.read()
        self.Fichier.close()

        # Y = Ligne   X = Colonne
        if self.FileName[-5] == '1':
            self.PosX = 2
            self.PosY = 1
            self.NbLignes = 6
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 1 : Jardinet  (Facile)"
        elif self.FileName[-5] == '2':
            self.PosX = 4
            self.PosY = 1
            self.NbLignes = 20
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 2 : Petite caverne  (Moyen)"

        self.FinDeCarte = 0
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

######################################################
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
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '$':
                self.FinDeCarte = 1
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

######################################################
        elif TouchePressee == "Q":
            LigneDuHero = self.ListeLignes[self.PosY]
            if LigneDuHero[self.PosX - 2:self.PosX - 1] == '#':
                InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé."
            elif LigneDuHero[self.PosX - 2:self.PosX - 1] == '$':
                self.FinDeCarte = 1
            else:
                DebutNouvelleLigne = LigneDuHero[0:self.PosX - 2]
                BlancRemplace = LigneDuHero[self.PosX - 2:self.PosX - 1].replace(' ', '~')
                HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
                FinNouvelleLigne = LigneDuHero[self.PosX:]

                LigneDuHero = DebutNouvelleLigne + BlancRemplace + HeroRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY], LigneDuHero = LigneDuHero, self.ListeLignes[self.PosY]

                self.PosX -= 1

######################################################
        elif TouchePressee == "S":
            LigneDuHero = self.ListeLignes[self.PosY]
            NouvelleLigneDuHero = self.ListeLignes[self.PosY + 1]
            if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '#':
                InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé."
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '$':
                self.FinDeCarte = 1
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

######################################################
        elif TouchePressee == "D":
            LigneDuHero = self.ListeLignes[self.PosY]
            if LigneDuHero[self.PosX:self.PosX + 1] == "#":
                InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé."
            elif LigneDuHero[self.PosX:self.PosX + 1] == '$':
                self.FinDeCarte = 1
            else:
                HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
                BlancRemplace = LigneDuHero[self.PosX:self.PosX + 1].replace(' ', '~')
                DebutNouvelleLigne = LigneDuHero[0:self.PosX - 1]
                FinNouvelleLigne = LigneDuHero[self.PosX + 1:]

                LigneDuHero = DebutNouvelleLigne + HeroRemplace + BlancRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY], LigneDuHero = LigneDuHero, self.ListeLignes[self.PosY]

                self.PosX += 1

######################################################
        i = 0
        self.CarteActuelle = ""

        # Re-positionnement des blocs
        self.CanvasCarte.delete("all")
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

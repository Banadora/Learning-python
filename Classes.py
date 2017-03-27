################### Tests Tkinter - Classes ###################

# -*- coding: utf8 -*-

import os
from tkinter import *
from tkinter.filedialog import *


class MakeUI(Frame):

    """ Classe de création d'interface utilisateur """

    def __init__(self, Fenetre, **kwargs):

        # Héritage et données
        Frame.__init__(self, Fenetre, width=768, height=576, **kwargs)

        self.pack(fill=BOTH)
        self.InfosTouches = "Vous êtes un ~ qui cherche à s'échapper du labyrinthe pour gagner du $$$\n\n \
                            Tapez Z pour aller vers le haut\n \
                            Tapez Q pour aller vers la gauche\n \
                            Tapez D pour aller vers la droite\n \
                            Tapez S pour aller vers le bas\n"
        self.FileName = ""
        self.CarteActuelle = {}
        self.ListeLignes = []

        # Definition des touches de direction
        self.bind_all("z", lambda e: self.Play("Z"))
        self.bind_all("q", lambda e: self.Play("Q"))
        self.bind_all("s", lambda e: self.Play("S"))
        self.bind_all("d", lambda e: self.Play("D"))

        # Cadre des informations
        self.FrameInfos = LabelFrame(self, text="Infos", padx=2, pady=2)
        self.FrameInfos.pack(fill="both", expand="yes", padx=5, pady=5)

        # Cadre d'affichage de la carte
        self.FrameCarte = LabelFrame(self, text="Carte", padx=2, pady=2)
        self.FrameCarte.pack(fill="both", expand="yes", padx=5, pady=5)

        # Cadre des boutons de commandes
        self.FrameCtrl = Frame(self, padx=2, pady=2)
        self.FrameCtrl.pack(fill="both", expand="yes", padx=5, pady=5)

        # Affichage des informations
        self.MsgInfos = Label(self.FrameInfos, text="Sélection de la carte")
        self.MsgInfos.pack(side="left", padx=5, pady=5)

        # Bouton d'ouverture de carte
        self.BtnOuvrir = Button(self.FrameInfos, text="Ouvrir", bg="orange", cursor="pirate", width=10, command=self.OuvrirCarte)
        self.BtnOuvrir.pack(side="right", padx=5, pady=5)

        # Bouton pour quitter le programme
        self.BtnQuitter = Button(self.FrameCtrl, text="Quitter", bg="red", width=20, command=self.quit)
        self.BtnQuitter.pack(side="left", padx=5, pady=5)

        self.AfficherTouche = Label(self.FrameCtrl, text="None",)
        self.AfficherTouche.pack(side="right", padx=5, pady=5)

        self.MsgInfosCarte = Label(self.FrameCarte, text="Pas de carte pour l'instant")
        self.MsgInfosCarte.pack(padx=2, pady=2)

        self.Carte = Label(self.FrameCarte, text=" ")
        self.Carte.pack(padx=2, pady=2)

###################################################################################################################
###################################################################################################################
    def OuvrirCarte(self):
        # Ouverture de la carte au démarrage

        self.FileName = askopenfilename(title="Ouvrir une carte", filetypes=[('txt files', '.txt'), ('all files', '.*')])
        self.Fichier = open(self.FileName, "r")
        self.CarteActuelle = self.Fichier.read()
        self.Fichier.close()

        self.Carte["text"] = self.CarteActuelle
        self.Carte["font"] = ('Lucida Console', 12, 'bold')

        # Y = Ligne   X = Colonne
        if self.FileName[-5] == '1':
            self.PosX = 2
            self.PosY = 1
            self.NbLignes = 6
            self.FrameCarte["text"] = " 1 : Jardinet  (Facile)"
        elif self.FileName[-5] == '2':
            self.PosX = 4
            self.PosY = 1
            self.NbLignes = 20
            self.FrameCarte["text"] = " 2 : Petite caverne  (Moyen)"

        i = 0
        j = 0
        k = 20
        while i <= self.NbLignes - 1:
            self.ListeLignes.append(self.CarteActuelle[j:k])
            #print(ListeLignes[i])
            i += 1
            j = k + 1
            k = j + 20

        self.MsgInfosCarte["text"] = ""
        self.MsgInfos["text"] = self.InfosTouches + "\n Position >>   Ligne : "\
             + str(self.PosY + 1) + "   Colonne : " + str(self.PosX)

###################################################################################################################
###################################################################################################################
    def Play(self, Touche):
        self.AfficherTouche["text"] = Touche
        TouchePressee = Touche
        InfoSup = ""

######################################################
        if TouchePressee == "Z":
            LigneDuHero = self.ListeLignes[self.PosY]
            NouvelleLigneDuHero = self.ListeLignes[self.PosY - 1]
            if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '#':
                InfoSup = "Il est impossible de traverser un mur !! Bien essayé."
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
                InfoSup = "Il est impossible de traverser un mur !! Bien essayé."
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
                InfoSup = "Il est impossible de traverser un mur !! Bien essayé."
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
                InfoSup = "Il est impossible de traverser un mur !! Bien essayé."
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
        while i <= self.NbLignes - 1:
            self.CarteActuelle += self.ListeLignes[i]
            self.CarteActuelle += "\n"
            i += 1

        self.MsgInfosCarte["text"] = InfoSup
        self.Carte["text"] = self.CarteActuelle
        self.MsgInfos["text"] = self.InfosTouches + "\n Position >>   Ligne : " + str(self.PosY + 1) + "   Colonne : " + str(self.PosX)


# -*- coding: utf-8 -*-

import winsound
from MapFuncs import *


###################################################################################################################
###################################################################################################################
def Move(self, Touche):
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
            ChangerNiveau(self, self.TempPathCarte)
        elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangerNiveau(self, self.TempPathCarte)

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
            ChangerNiveau(self, self.TempPathCarte)
        elif LigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangerNiveau(self, self.TempPathCarte)

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
            ChangerNiveau(self, self.TempPathCarte)
        elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangerNiveau(self, self.TempPathCarte)

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
            ChangerNiveau(self, self.TempPathCarte)
        elif LigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangerNiveau(self, self.TempPathCarte)

######################################################
    AfficherCarte(self)

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

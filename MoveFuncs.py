################### Labyrinthe - Movements functions ###################

# -*- coding: utf-8 -*-

import winsound
from MapFuncs import *


###################################################################################################################
###################################################################################################################
def Move(self, Touche):
    if self.EndOfMap == 1:
        TouchePressee = "NULL"
    else:
        TouchePressee = Touche

    InfoSup = ""
    self.DifficultyScale.config(state='disabled')

######################################################
    if TouchePressee == "Z":
        LigneDuHero = self.LinesList[self.PosY]
        NouvelleLigneDuHero = self.LinesList[self.PosY - 1]
        if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '#':
            InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé. \n\n-1 Vie'."
            self.Lives -= 1
        elif ((NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 's') or (NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '§')):
            self.LinesList[self.PosY - 1] = NouvelleLigneDuHero[:self.PosX - 1] + '§' + NouvelleLigneDuHero[self.PosX:]
            InfoSup = "\n\nOwWwWW un piège à serpent !! \nPas de chance. \n\n-1 Vie'."
            self.Lives -= 1
        else:
            HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
            DebutNouvelleLigne = LigneDuHero[:self.PosX - 1]
            FinNouvelleLigne = LigneDuHero[self.PosX:]

            LigneDuHero = DebutNouvelleLigne + HeroRemplace + FinNouvelleLigne
            self.LinesList[self.PosY], LigneDuHero = LigneDuHero, self.LinesList[self.PosY]

            BlancRemplace = NouvelleLigneDuHero[self.PosX - 1:self.PosX].replace(' ', '~')
            DebutNouvelleLigne = NouvelleLigneDuHero[:self.PosX - 1]
            FinNouvelleLigne = NouvelleLigneDuHero[self.PosX:]

            NouvelleLigneDuHero = DebutNouvelleLigne + BlancRemplace + FinNouvelleLigne
            self.LinesList[self.PosY - 1], NouvelleLigneDuHero = NouvelleLigneDuHero, self.LinesList[self.PosY - 1]
            self.PosY -= 1

        if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '$':
            self.EndOfMap = 1
        elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '^':
            ChangeLevel(self, self.TempPathCarte)
        elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangeLevel(self, self.TempPathCarte)

######################################################
    elif TouchePressee == "Q":
        LigneDuHero = self.LinesList[self.PosY]
        if LigneDuHero[self.PosX - 2:self.PosX - 1] == '#':
            InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé. \n\n-1 Vie'."
            self.Lives -= 1
        elif ((LigneDuHero[self.PosX - 2:self.PosX - 1] == 's') or (LigneDuHero[self.PosX - 2:self.PosX - 1] == '§')):
            self.LinesList[self.PosY] = LigneDuHero[:self.PosX - 2] + '§' + LigneDuHero[self.PosX - 1:]
            InfoSup = "\n\nOwWwWW un piège à serpent !! \nPas de chance. \n\n-1 Vie'."
            self.Lives -= 1
        else:
            DebutNouvelleLigne = LigneDuHero[0:self.PosX - 2]
            BlancRemplace = LigneDuHero[self.PosX - 2:self.PosX - 1].replace(' ', '~')
            HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
            FinNouvelleLigne = LigneDuHero[self.PosX:]

            LigneDuHero = DebutNouvelleLigne + BlancRemplace + HeroRemplace + FinNouvelleLigne
            self.LinesList[self.PosY], LigneDuHero = LigneDuHero, self.LinesList[self.PosY]
            self.PosX -= 1

        if LigneDuHero[self.PosX - 1:self.PosX] == '$':
            self.EndOfMap = 1
        elif LigneDuHero[self.PosX - 1:self.PosX] == '^':
            ChangeLevel(self, self.TempPathCarte)
        elif LigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangeLevel(self, self.TempPathCarte)

######################################################
    elif TouchePressee == "S":
        LigneDuHero = self.LinesList[self.PosY]
        NouvelleLigneDuHero = self.LinesList[self.PosY + 1]
        if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '#':
            InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé. \n\n-1 Vie'."
            self.Lives -= 1
        elif ((NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 's') or (NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '§')):
            self.LinesList[self.PosY + 1] = NouvelleLigneDuHero[:self.PosX - 1] + '§' + NouvelleLigneDuHero[self.PosX:]
            InfoSup = "\n\nOwWwWW un piège à serpent !! \nPas de chance. \n\n-1 Vie'."
            self.Lives -= 1
        else:
            HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
            DebutNouvelleLigne = LigneDuHero[:self.PosX - 1]
            FinNouvelleLigne = LigneDuHero[self.PosX:]

            LigneDuHero = DebutNouvelleLigne + HeroRemplace + FinNouvelleLigne
            self.LinesList[self.PosY], LigneDuHero = LigneDuHero, self.LinesList[self.PosY]

            BlancRemplace = NouvelleLigneDuHero[self.PosX - 1:self.PosX].replace(' ', '~')
            DebutNouvelleLigne = NouvelleLigneDuHero[:self.PosX - 1]
            FinNouvelleLigne = NouvelleLigneDuHero[self.PosX:]

            NouvelleLigneDuHero = DebutNouvelleLigne + BlancRemplace + FinNouvelleLigne
            self.LinesList[self.PosY + 1], NouvelleLigneDuHero = NouvelleLigneDuHero, self.LinesList[self.PosY + 1]
            self.PosY += 1

        if NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '$':
            self.EndOfMap = 1
        elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '^':
            ChangeLevel(self, self.TempPathCarte)
        elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangeLevel(self, self.TempPathCarte)

######################################################
    elif TouchePressee == "D":
        LigneDuHero = self.LinesList[self.PosY]
        if LigneDuHero[self.PosX:self.PosX + 1] == "#":
            InfoSup = "\n\nIl est impossible de traverser un mur !! \nBien essayé. \n\n-1 Vie'."
            self.Lives -= 1
        elif ((LigneDuHero[self.PosX:self.PosX + 1] == 's') or (LigneDuHero[self.PosX:self.PosX + 1] == '§')):
            self.LinesList[self.PosY] = LigneDuHero[:self.PosX] + '§' + LigneDuHero[self.PosX + 1:]
            InfoSup = "\n\nOwWwWW un piège à serpent !! \nPas de chance. \n\n-1 Vie'."
            self.Lives -= 1
        else:
            HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
            BlancRemplace = LigneDuHero[self.PosX:self.PosX + 1].replace(' ', '~')
            DebutNouvelleLigne = LigneDuHero[0:self.PosX - 1]
            FinNouvelleLigne = LigneDuHero[self.PosX + 1:]

            LigneDuHero = DebutNouvelleLigne + HeroRemplace + BlancRemplace + FinNouvelleLigne
            self.LinesList[self.PosY], LigneDuHero = LigneDuHero, self.LinesList[self.PosY]
            self.PosX += 1

        if LigneDuHero[self.PosX - 1:self.PosX] == '$':
            self.EndOfMap = 1
        elif LigneDuHero[self.PosX - 1:self.PosX] == '^':
            ChangeLevel(self, self.TempPathCarte)
        elif LigneDuHero[self.PosX - 1:self.PosX] == 'v':
            ChangeLevel(self, self.TempPathCarte)

######################################################
    ShowMap(self)

    i = 0
    while i <= self.NbLignes - 1:
        self.ActualMap += self.LinesList[i]
        self.ActualMap += "\n"
        i += 1

    self.MsgInfosCarte["text"] = ""
    self.MsgInfosCarteSup["text"] = ""

    self.MsgInfosCarte["text"] = self.KeysInfos + "\n Position >>   Ligne : " + str(self.PosY + 1) + \
        "   Colonne : " + str(self.PosX) + \
    "\n\n\nVies restantes : {0}".format(self.Lives) + \
    "\n\n\n---------------------------------------------------------\n\n"

    if self.Lives == 0:
        self.Lives = self.LivesAtStart
        OpenMap(self, self.LoadedMap, 1)
        InfoSup = ""

    if self.EndOfMap == 0:
        self.MsgInfosCarteSup["text"] = InfoSup
    else:
        InfoSup = "\nBRAVO : pensez à dépenser vos $$$ !"
        self.MsgInfosCarteSup["text"] = InfoSup
        if self.PlayFinalSound == 1:
            winsound.PlaySound('Sons/Caisse enregistreuse.wav', winsound.SND_FILENAME)
            winsound.PlaySound('Sons/Pieces.wav', winsound.SND_FILENAME)
            self.PlayFinalSound = 0

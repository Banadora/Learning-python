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

        self.BtnOuvrirCarte["state"] = NORMAL

        return self.TkImgPerso

###################################################################################################################
###################################################################################################################
    def OuvrirCarte(self, Carte):
        # Ouverture de la carte au démarrage
        self.ListeLignes = []
        self.CarteActuelle = {}
        self.FileName = ""
        self.MsgInfosCarte["text"] = ""

        self.TempPathCarte = 'Cartes/' + Carte + '.txt'
        #self.FileName = askopenfilename(title="Ouvrir une carte", filetypes=[('txt files', '.txt'), ('all files', '.*')])

        self.Fichier = open(self.TempPathCarte, "r")
        self.CarteActuelle = self.Fichier.read()
        self.Fichier.close()

        # Y = Ligne   X = Colonne
        #if self.FileName[-5] == '1':
        if '1.0' in self.TempPathCarte:
            self.PosX = 2
            self.PosY = 1
            self.NbLignes = 6
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 1 : Jardinet  (Facile)"
        #elif self.FileName[-5] == '2':
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
        elif '4.1.1' in self.TempPathCarte:
            self.PosX = 3
            self.PosY = 4
            self.NbLignes = 8
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 4.1 - Plus haut (Facile)"

######################################################
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
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '$':
                self.FinDeCarte = 1
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
                self.ChangerNiveau(self.TempPathCarte)
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
            elif LigneDuHero[self.PosX - 2:self.PosX - 1] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif LigneDuHero[self.PosX - 2:self.PosX - 1] == 'v':
                self.ChangerNiveau(self.TempPathCarte)
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
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif NouvelleLigneDuHero[self.PosX - 1:self.PosX] == 'v':
                self.ChangerNiveau(self.TempPathCarte)
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
            elif LigneDuHero[self.PosX:self.PosX + 1] == '^':
                self.ChangerNiveau(self.TempPathCarte)
            elif LigneDuHero[self.PosX:self.PosX + 1] == 'v':
                self.ChangerNiveau(self.TempPathCarte)
            else:
                HeroRemplace = LigneDuHero[self.PosX - 1:self.PosX].replace('~', ' ')
                BlancRemplace = LigneDuHero[self.PosX:self.PosX + 1].replace(' ', '~')
                DebutNouvelleLigne = LigneDuHero[0:self.PosX - 1]
                FinNouvelleLigne = LigneDuHero[self.PosX + 1:]

                LigneDuHero = DebutNouvelleLigne + HeroRemplace + BlancRemplace + FinNouvelleLigne
                self.ListeLignes[self.PosY], LigneDuHero = LigneDuHero, self.ListeLignes[self.PosY]

                self.PosX += 1

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
            winsound.PlaySound('Sons/Caisse enregistreuse.wav', winsound.SND_FILENAME)
            winsound.PlaySound('Sons/Pieces.wav', winsound.SND_FILENAME)
            InfoSup = "\nBRAVO : pensez à dépenser vos $$$ !"
            self.MsgInfosCarteSup["text"] = InfoSup

###################################################################################################################
###################################################################################################################
    def FctMenus(self, Fenetre):
        # Menus
        self.Menubar = Menu(Fenetre)

        self.MenuPerso = Menu(self.Menubar, tearoff=0)

        self.MenuPerso.add_command(label="Alien", command=lambda: self.ChoisirPerso("Alien"))
        self.MenuPerso.add_command(label="Angel", command=lambda: self.ChoisirPerso("Angel"))
        self.MenuPerso.add_command(label="Baby", command=lambda: self.ChoisirPerso("Baby"))

        self.MenuPerso.add_command(label="Boxer", command=lambda: self.ChoisirPerso("Boxer"))
        self.MenuPerso.add_command(label="Chef", command=lambda: self.ChoisirPerso("Chef"))
        self.MenuPerso.add_command(label="Clown", command=lambda: self.ChoisirPerso("Clown"))

        self.MenuPerso.add_command(label="Dad", command=lambda: self.ChoisirPerso("Dad"))
        self.MenuPerso.add_command(label="Devil", command=lambda: self.ChoisirPerso("Devil"))
        self.MenuPerso.add_command(label="Doctor", command=lambda: self.ChoisirPerso("Doctor"))

        self.MenuPerso.add_command(label="Dragon", command=lambda: self.ChoisirPerso("Dragon"))
        self.MenuPerso.add_command(label="Firefighter", command=lambda: self.ChoisirPerso("Firefighter"))
        self.MenuPerso.add_command(label="Ghost", command=lambda: self.ChoisirPerso("Ghost"))

        self.MenuPerso.add_command(label="Girl", command=lambda: self.ChoisirPerso("Girl"))
        self.MenuPerso.add_command(label="Kid", command=lambda: self.ChoisirPerso("Kid"))
        self.MenuPerso.add_command(label="King", command=lambda: self.ChoisirPerso("King"))

        self.MenuPerso.add_command(label="Knight", command=lambda: self.ChoisirPerso("Knight"))
        self.MenuPerso.add_command(label="Lawyer", command=lambda: self.ChoisirPerso("Lawyer"))
        self.MenuPerso.add_command(label="Leprechaun", command=lambda: self.ChoisirPerso("Leprechaun"))

        self.MenuPerso.add_command(label="Man", command=lambda: self.ChoisirPerso("Man"))
        self.MenuPerso.add_command(label="Mermaid", command=lambda: self.ChoisirPerso("Mermaid"))
        self.MenuPerso.add_command(label="Monster", command=lambda: self.ChoisirPerso("Monster"))

        self.MenuPerso.add_command(label="Ninja", command=lambda: self.ChoisirPerso("Ninja"))
        self.MenuPerso.add_command(label="Nurse", command=lambda: self.ChoisirPerso("Nurse"))
        self.MenuPerso.add_command(label="Pirate", command=lambda: self.ChoisirPerso("Pirate"))

        self.MenuPerso.add_command(label="Policeman", command=lambda: self.ChoisirPerso("Policeman"))
        self.MenuPerso.add_command(label="Prince", command=lambda: self.ChoisirPerso("Prince"))
        self.MenuPerso.add_command(label="Princess", command=lambda: self.ChoisirPerso("Princess"))

        self.MenuPerso.add_command(label="Queen", command=lambda: self.ChoisirPerso("Queen"))
        self.MenuPerso.add_command(label="Robot", command=lambda: self.ChoisirPerso("Robot"))
        self.MenuPerso.add_command(label="Santa", command=lambda: self.ChoisirPerso("Santa"))

        self.MenuPerso.add_command(label="Snowman", command=lambda: self.ChoisirPerso("Snowman"))
        self.MenuPerso.add_command(label="Superhero", command=lambda: self.ChoisirPerso("Superhero"))
        self.MenuPerso.add_command(label="Teacher", command=lambda: self.ChoisirPerso("Teacher"))

        self.MenuPerso.add_command(label="Troll", command=lambda: self.ChoisirPerso("Troll"))
        self.MenuPerso.add_command(label="Vampire", command=lambda: self.ChoisirPerso("Vampire"))
        self.MenuPerso.add_command(label="Werewolf", command=lambda: self.ChoisirPerso("Werewolf"))

        self.MenuPerso.add_command(label="Witch", command=lambda: self.ChoisirPerso("Witch"))
        self.MenuPerso.add_command(label="Zombie", command=lambda: self.ChoisirPerso("Zombie"))

        self.Menubar.add_cascade(label="Personnages", menu=self.MenuPerso)

######################################################
        self.MenuCarte = Menu(self.Menubar, tearoff=0)

        self.MenuCarte.add_command(label="1 : Jardinet (Facile)", command=lambda: self.OuvrirCarte("1.0 - Jardinet (Facile)"))
        self.MenuCarte.add_command(label="2 : Petite caverne (Moyen)", command=lambda: self.OuvrirCarte("2.0 - Petite caverne (Moyen)"))
        self.MenuCarte.add_command(label="3 : Serpentin (Moyen)", command=lambda: self.OuvrirCarte("3.0 - Serpentin (Moyen)"))
        self.MenuCarte.add_command(label="4 : Plus haut (Facile)", command=lambda: self.OuvrirCarte("4.1.1 - Plus haut (Facile)"))

        self.Menubar.add_cascade(label="Cartes", menu=self.MenuCarte)

######################################################
        Fenetre.config(menu=self.Menubar)

###################################################################################################################
###################################################################################################################
    def ChangerNiveau(self, Carte):
        if '4.1' in Carte:
            self.PosX = 19
            self.PosY = 5
            self.NbLignes = 8
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 4.2 - Plus haut (Facile)"
            NouvelleCarte = "4.2 - Plus haut (Facile)"
        if '4.2' in Carte:
            self.PosX = 19
            self.PosY = 5
            self.NbLignes = 8
            self.NbColonnes = 20
            self.FrameCarteGraph["text"] = " 4.1 - Plus haut (Facile)"
            NouvelleCarte = "4.1.2 - Plus haut (Facile)"

        self.OuvrirCarte(NouvelleCarte)

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

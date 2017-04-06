################### Labyrinthe - Maps functions ###################

# -*- coding: utf-8 -*-


###################################################################################################################
###################################################################################################################
def ShowMap(self):
        # Suppression de l'ancienne carte si necessaire
        self.CanvasCarte.delete("all")

        # Positionnement des blocs
        for x in range(self.NbLignes):
            for y in range(self.NbColonnes):
                if (x > (self.PosY + self.BlurLevel)) or (x < (self.PosY - self.BlurLevel)) \
                or (y > (self.PosX + (self.BlurLevel - 1))) or (y < (self.PosX - (self.BlurLevel + 1))):
                        self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgBlank)
                else:
                    if self.LinesList[x][y] == '#':
                        self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgMur)
                    elif self.LinesList[x][y] == '$':
                        self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgDollar)
                    elif self.LinesList[x][y] == '~':
                        self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgPerso)
                    elif self.LinesList[x][y] == ' ':
                        self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgBlank)
                    elif self.LinesList[x][y] == '^':
                        self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgStairsUp)
                    elif self.LinesList[x][y] == 'v':
                        self.CanvasCarte.create_image((32 + (y * 32)), (32 + (x * 32)), image=self.TkImgStairsDown)


###################################################################################################################
###################################################################################################################
def OpenMap(self, Carte, StartingMap):
    # Ouverture de la carte au démarrage
    self.LinesList = []
    self.ActualMap = {}
    self.FileName = ""
    self.MsgInfosCarte["text"] = ""
    self.EndOfMap = 0
    self.PlayFinalSound = 1

    if StartingMap == 1:
        self.DifficultyScale.config(state='normal')

    self.TempPathCarte = 'Cartes/' + Carte + '.txt'
    #self.FileName = askopenfilename(title="Ouvrir une carte", filetypes=[('txt files', '.txt'), ('all files', '.*')])

    self.Fichier = open(self.TempPathCarte, "r")
    self.ActualMap = self.Fichier.read()
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
        self.LinesList.append(self.ActualMap[j:k])
        i += 1
        j = k + 1
        k = j + self.NbColonnes

    self.MsgInfosCarte["text"] = ""
    self.MsgInfosCarte["text"] = self.KeysInfos + "\n Position >>   Ligne : "\
         + str(self.PosY + 1) + "   Colonne : " + str(self.PosX) + \
         "\n\n\nVies restantes : {0}".format(self.Lives) + \
        "\n\n\n---------------------------------------------------------\n\n"

    ShowMap(self)


###################################################################################################################
###################################################################################################################
def ChangeLevel(self, Carte):
    if '4.1' in Carte:
        if ((self.PosX == 19) and (self.PosY == 6)):                        # 4.1 -> 4.2 (1)
            self.FrameCarteGraph["text"] = " 4.2 - Plus haut (Facile)"
            NouvelleCarte = "4.2 - Plus haut (Facile)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 19
            self.PosY = 5
            self.LinesList[5] = "# # #   #       ##~#"
    if '4.2' in Carte:
        if ((self.PosX == 19) and (self.PosY == 6)):                        # 4.2 -> 4.1 (1)
            self.FrameCarteGraph["text"] = " 4.1 - Plus haut (Facile)"
            NouvelleCarte = "4.1 - Plus haut (Facile)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 19
            self.PosY = 5
            self.LinesList[4] = "#  #       ## # #  #"
            self.LinesList[5] = "#### ######    # #~#"

######################################################
    if '5.1' in Carte:
        if ((self.PosX == 2) and (self.PosY == 5)):                        # 5.1 -> 5.2 (1)
            self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
            NouvelleCarte = "5.2 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 3
            self.PosY = 6
            self.LinesList[6] = "#v~    #     #      "
        if ((self.PosX == 14) and (self.PosY == 10)):                      # 5.1 -> 5.2 (2)
            self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
            NouvelleCarte = "5.2 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 2
            self.PosY = 1
            self.LinesList[1] = "#~v#    #v#  #      "
        if ((self.PosX == 3) and (self.PosY == 7)):                      # 5.1 -> 5.2 (3)
            self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
            NouvelleCarte = "5.2 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 10
            self.PosY = 2
            self.LinesList[2] = "# #  #  #~ # #      "
    if '5.2' in Carte:
        if ((self.PosX == 2) and (self.PosY == 6)):                        # 5.2 -> 5.1 (1)
            self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
            NouvelleCarte = "5.1 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 3
            self.PosY = 5
            self.LinesList[9] = "#$# ##   #   #    ##"
            self.LinesList[5] = "#^~### #### #  #   #"
        if ((self.PosX == 3) and (self.PosY == 1)):                        # 5.2 -> 5.1 (2)
            self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
            NouvelleCarte = "5.1 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 15
            self.PosY = 10
            self.LinesList[9] = "#$# ##   #   #    ##"
            self.LinesList[10] = "##     ##  ##^~## ##"
        if ((self.PosX == 10) and (self.PosY == 1)):                        # 5.2 -> 5.1 (3)
            self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
            NouvelleCarte = "5.1 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OpenMap(self, NouvelleCarte, 0)
            self.PosX = 2
            self.PosY = 7
            self.LinesList[9] = "#$# ##   #   #    ##"
            self.LinesList[7] = "#~^#########  ##  ##"

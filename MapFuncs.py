
# -*- coding: utf-8 -*-


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

    AfficherCarte(self)


###################################################################################################################
###################################################################################################################
def ChangerNiveau(self, Carte):
    if '4.1' in Carte:
        if ((self.PosX == 19) and (self.PosY == 6)):                        # 4.1 -> 4.2 (1)
            self.FrameCarteGraph["text"] = " 4.2 - Plus haut (Facile)"
            NouvelleCarte = "4.2 - Plus haut (Facile)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OuvrirCarte(self, NouvelleCarte)
            self.PosX = 19
            self.PosY = 5
            self.ListeLignes[5] = "# # #   #       ##~#"
    if '4.2' in Carte:
        if ((self.PosX == 19) and (self.PosY == 6)):                        # 4.2 -> 4.1 (1)
            self.FrameCarteGraph["text"] = " 4.1 - Plus haut (Facile)"
            NouvelleCarte = "4.1 - Plus haut (Facile)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OuvrirCarte(self, NouvelleCarte)
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
            OuvrirCarte(self, NouvelleCarte)
            self.PosX = 3
            self.PosY = 6
            self.ListeLignes[6] = "#v~    #     #      "
        if ((self.PosX == 14) and (self.PosY == 10)):                      # 5.1 -> 5.2 (2)
            self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
            NouvelleCarte = "5.2 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OuvrirCarte(self, NouvelleCarte)
            self.PosX = 2
            self.PosY = 1
            self.ListeLignes[1] = "#~v#    #v#  #      "
        if ((self.PosX == 3) and (self.PosY == 7)):                      # 5.1 -> 5.2 (3)
            self.FrameCarteGraph["text"] = " 5.2 - Maison (Moyen)"
            NouvelleCarte = "5.2 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OuvrirCarte(self, NouvelleCarte)
            self.PosX = 10
            self.PosY = 2
            self.ListeLignes[2] = "# #  #  #~ # #      "
    if '5.2' in Carte:
        if ((self.PosX == 2) and (self.PosY == 6)):                        # 5.2 -> 5.1 (1)
            self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
            NouvelleCarte = "5.1 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OuvrirCarte(self, NouvelleCarte)
            self.PosX = 3
            self.PosY = 5
            self.ListeLignes[9] = "#$# ##   #   #    ##"
            self.ListeLignes[5] = "#^~### #### #  #   #"
        if ((self.PosX == 3) and (self.PosY == 1)):                        # 5.2 -> 5.1 (2)
            self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
            NouvelleCarte = "5.1 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OuvrirCarte(self, NouvelleCarte)
            self.PosX = 15
            self.PosY = 10
            self.ListeLignes[9] = "#$# ##   #   #    ##"
            self.ListeLignes[10] = "##     ##  ##^~## ##"
        if ((self.PosX == 10) and (self.PosY == 1)):                        # 5.2 -> 5.1 (3)
            self.FrameCarteGraph["text"] = " 5.1 - Maison (Moyen)"
            NouvelleCarte = "5.1 - Maison (Moyen)"
            self.NbLignes = 8
            self.NbColonnes = 20
            OuvrirCarte(self, NouvelleCarte)
            self.PosX = 2
            self.PosY = 7
            self.ListeLignes[9] = "#$# ##   #   #    ##"
            self.ListeLignes[7] = "#~^#########  ##  ##"

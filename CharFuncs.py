################### Labyrinthe - Character functions ###################

# -*- coding: utf-8 -*-

from PIL import Image, ImageTk


###################################################################################################################
###################################################################################################################
def PickChar(self, Char):
    # Fonction d'ouverture du fichier personnage
    self.TempPathPerso = 'Images/Characters/' + Char + '.ico'
    self.ImgPerso = Image.open(self.TempPathPerso)
    self.TkImgPerso = ImageTk.PhotoImage(self.ImgPerso)
    self.ImgPerso.close()

    self.CanvasPersoSelect.create_image(20, 20, image=self.TkImgPerso)

    return self.TkImgPerso
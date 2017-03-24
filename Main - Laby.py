################### Labyrinthe - Main ###################

# -*- coding: utf8 -*-

import os
from Data import *
from Fonctions import *

# ##################################### #

Carte, CarteNb = ChoixCarte()
Ligne, Colonne, NbLignes = Config(CarteNb)
CarteActuelle = ChargerCarte(Carte)
AfficherTouches()

AfficherCarte(ListeLignes, CarteActuelle, NbLignes)  
Touche = EntrerTouche()

while Touche != 'N' and End == False:
    
    Ligne, Colonne, ListeLignes = Deplacement(Touche, Ligne, Colonne, ListeLignes)
    End = TesterFin(CarteNb, Ligne, Colonne)
    
    if End == False:
        print("\nPosition actuelle >> Ligne : {}   Colonne : {}".format(Ligne+1, Colonne))
        AfficherCarte(ListeLignes, CarteActuelle, NbLignes)
        Touche = EntrerTouche()  
    
    
print("\n")
os.system("pause")
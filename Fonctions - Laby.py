################### Labyrinthe - Fonctions ###################

# -*- coding: utf8 -*-

import os
import pickle
from Data import *


def Config(CarteNb):
    
    if CarteNb == 1:
        Ligne = 1
        Colonne = 2
        NbLignes = 6
    elif CarteNb == 2:
        Ligne = 1
        Colonne = 4
        NbLignes = 20    
    return Ligne, Colonne, NbLignes

def ChoixCarte():
    
    print("~~~~~~~ Sélection de la carte ~~~~~~~")
    print("1 : Jardinet         (Facile)")
    print("2 : Petite caverne   (Moyen)")
    Carte = input("\nQuelle carte souhaitez-vous jouer ?  ")
    print("")
    
    if not Carte.isnumeric() or len(Carte) !=1:
        print("Sélection invalide : entrez le numéro de la carte")
        return ChoixCarte()
    else:
        CarteNb = int(Carte)
        if CarteNb < 1 or CarteNb > 2:
            print("Sélection invalide : entrez le numéro de la carte")
            return ChoixCarte()
        else:
            return Carte, CarteNb


def ChargerCarte(Carte):
    
    Carte += ".txt"
    CarteActuelle = {}
    
    
    if os.path.exists(Carte):
        Fichier = open(Carte, "r")
        CarteActuelle = Fichier.read()
        Fichier.close()
        return CarteActuelle
    else:
        print("La carte n'a pu être trouvée, retour à la sélection")
        return ChoixCarte()
    
    
    
def AfficherCarte(ListeLignes, CarteActuelle, NbLignes):
    
    i = 0
    j = 0
    k = 20    
    while i <= NbLignes-1:
        ListeLignes.append(CarteActuelle[j:k])
        print(ListeLignes[i])
        i += 1
        j = k + 1
        k = j + 20      


def AfficherTouches():
    
    print("Vous êtes un ~ qui cherche à s'échapper du labyrinthe pour gagner du $$$")
    print("Tapez Z pour aller vers le haut")
    print("Tapez S pour aller vers le bas")
    print("Tapez Q pour aller vers la gauche")
    print("Tapez D pour aller vers la droite\n")
    print("Tapez N pour quitter\n")
    
    
def EntrerTouche():
    
    Touche = input("\nEntrez un déplacement :  ")
    Touche = Touche.upper()
    if Touche != 'Z' and Touche != 'Q' and Touche != 'S' and Touche != 'D' and Touche != 'N':
        print("Entrée invalide")
        return EntrerTouche()
    else:
        return Touche
    
    

def Deplacement(Touche, Ligne, Colonne, ListeLignes):
    
    if Touche == 'Q':
        LigneDuHero = ListeLignes[Ligne]
        if LigneDuHero[Colonne-2:Colonne-1] == '#':
            print("Il est impossible de traverser un mur !! Bien essayé.")
            return Ligne, Colonne, ListeLignes
        else:
            DebutNouvelleLigne = LigneDuHero[0:Colonne-2]
            BlancRemplace = LigneDuHero[Colonne-2:Colonne-1].replace(' ', '~')
            HeroRemplace = LigneDuHero[Colonne-1:Colonne].replace('~', ' ')
            FinNouvelleLigne = LigneDuHero[Colonne:]
            
            LigneDuHero = DebutNouvelleLigne + BlancRemplace + HeroRemplace + FinNouvelleLigne
            ListeLignes[Ligne],LigneDuHero = LigneDuHero,ListeLignes[Ligne]
            
            Colonne -= 1
            return Ligne, Colonne, ListeLignes
     
    elif Touche == 'D':
        LigneDuHero = ListeLignes[Ligne]
        if LigneDuHero[Colonne:Colonne+1] == "#":
            print("Il est impossible de traverser un mur !! Bien essayé.")
            return Ligne, Colonne, ListeLignes
        else:
            HeroRemplace = LigneDuHero[Colonne-1:Colonne].replace('~', ' ')
            BlancRemplace = LigneDuHero[Colonne:Colonne+1].replace(' ', '~')
            DebutNouvelleLigne = LigneDuHero[0:Colonne-1]
            FinNouvelleLigne = LigneDuHero[Colonne+1:]
            
            LigneDuHero = DebutNouvelleLigne + HeroRemplace + BlancRemplace + FinNouvelleLigne     
            ListeLignes[Ligne],LigneDuHero = LigneDuHero,ListeLignes[Ligne]
           
            Colonne += 1        
            return Ligne, Colonne, ListeLignes
        
    elif Touche == 'S':
        LigneDuHero = ListeLignes[Ligne]
        NouvelleLigneDuHero = ListeLignes[Ligne+1]
        if NouvelleLigneDuHero[Colonne-1:Colonne] == '#':
            print("Il est impossible de traverser un mur !! Bien essayé.")
            return Ligne, Colonne, ListeLignes
        else:
            HeroRemplace = LigneDuHero[Colonne-1:Colonne].replace('~', ' ')
            DebutNouvelleLigne = LigneDuHero[:Colonne-1]
            FinNouvelleLigne = LigneDuHero[Colonne:]
            
            LigneDuHero = DebutNouvelleLigne + HeroRemplace + FinNouvelleLigne
            ListeLignes[Ligne],LigneDuHero = LigneDuHero,ListeLignes[Ligne]
            
            
            BlancRemplace = NouvelleLigneDuHero[Colonne-1:Colonne].replace(' ', '~')
            DebutNouvelleLigne = NouvelleLigneDuHero[:Colonne-1]
            FinNouvelleLigne = NouvelleLigneDuHero[Colonne:]
            
            NouvelleLigneDuHero = DebutNouvelleLigne + BlancRemplace + FinNouvelleLigne
            ListeLignes[Ligne+1],NouvelleLigneDuHero = NouvelleLigneDuHero,ListeLignes[Ligne+1]
            
            Ligne += 1
            return Ligne, Colonne, ListeLignes
        
    elif Touche == 'Z':
        LigneDuHero = ListeLignes[Ligne]
        NouvelleLigneDuHero = ListeLignes[Ligne-1]
        if NouvelleLigneDuHero[Colonne-1:Colonne] == '#':
            print("Il est impossible de traverser un mur !! Bien essayé.")
            return Ligne, Colonne, ListeLignes
        else:
            HeroRemplace = LigneDuHero[Colonne-1:Colonne].replace('~', ' ')
            DebutNouvelleLigne = LigneDuHero[:Colonne-1]
            FinNouvelleLigne = LigneDuHero[Colonne:]
            
            LigneDuHero = DebutNouvelleLigne + HeroRemplace + FinNouvelleLigne
            ListeLignes[Ligne],LigneDuHero = LigneDuHero,ListeLignes[Ligne]

        
            BlancRemplace = NouvelleLigneDuHero[Colonne-1:Colonne].replace(' ', '~')
            DebutNouvelleLigne = NouvelleLigneDuHero[:Colonne-1]
            FinNouvelleLigne = NouvelleLigneDuHero[Colonne:]
            
            NouvelleLigneDuHero = DebutNouvelleLigne + BlancRemplace + FinNouvelleLigne
            ListeLignes[Ligne-1],NouvelleLigneDuHero = NouvelleLigneDuHero,ListeLignes[Ligne-1]
            
            Ligne -= 1
            return Ligne, Colonne, ListeLignes    
    

def TesterFin(CarteNb, Ligne, Colonne):
    
    if CarteNb == 1:
        LigneFin = 1
        ColonneFin = 20
    elif CarteNb == 2:
        LigneFin = 18
        ColonneFin = 20
    
    
    if Ligne == LigneFin and Colonne == ColonneFin:
        print("\n$$$$$ $$$$ $$$$$$ $$$$$ $$$ $$$$$$$ $ $$$$$ $$ $$$$ ")
        print("Vous avez trouvé la sortie et remporté pleins de $$$$ !!")
        print("$$$$$ $$$$ $$$$$$ $$$$$ $$$ $$$$$$$ $ $$$$$ $$ $$$$ ")
        End = True
    else:
        End = False
    
    return End
    
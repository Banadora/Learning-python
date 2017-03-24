

# -*- coding: utf8 -*-


from tkinter import *

# création d'une instance de la classe TK, que l'on affecte à l'objet "root"
root = Tk()

# Quelques exemples de touches
root.bind("<Up>", maFonction) # Flèche haut

def maFonction(event):
    print("Z")
    
root.mainloop()
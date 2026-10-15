# -*- coding: utf-8 -*-
"""
Objectif : faire les fonctions necesssaires au fonctionnement de notre jeu

Auteur : Elie et Mattias

Date : 08/10/2026

ToDo : 

fenetre
couleur de fond

fonction pour la plateforme
foncion pou demarrer le jeu



"""


from tkinter import *

#Creation fenetre principale
Mafenetre = Tk()
Mafenetre.title('CasseBrique')

#Creation canvas
Largeur = 700
Hauteur = 500
Canevas = Canvas(Mafenetre, width = Largeur, height = Hauteur, bg = 'black')
Canevas.pack(padx = 5, pady = 5)

#Creation d'un widget Button(bouton go)(a finir avec la commande)
ButtonGo = Button(Mafenetre, text='Go')
ButtonGo.pack(side = LEFT, padx = 10, pady = 10)

#Creation d'un widget Button(bouton recommencer)(a finir avec la commande)
ButtonRecommencer = Button(Mafenetre, text='Recommencer')
ButtonRecommencer.pack(side = LEFT, padx = 5, pady = 5)

#Creation d'un widget Button(bouton fermer)
ButtonQuitter = Button(Mafenetre, text='Quitter', command = Mafenetre.destroy)
ButtonQuitter.pack(side = LEFT, padx = 5, pady = 5)

Mafenetre.mainloop()

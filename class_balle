"""
Objectif : creer la classe de la balle pour l'utiliser dans notre casse briques
Auteur : Elie et Mattias
Date : 15/10/26
ToDO : class balle avec les fonctions permettant de :
se deplacer
se deplacer selon l'axe des x
se deplacer selon l'axe des y

"""


import math as mt
import random as rd


#création de la classe balle
class Balle:
    def __init__(self, x, y, canvas, rayon=9, couleur="red", vitesse=5):
        self.x = x
        self.y = y
        self.rayon = rayon
        self.canvas = canvas
        self.couleur = couleur
        self.vitesse = vitesse
        self.dx = rd.random.choice([-1, 1]) * vitesse
        self.dy = -vitesse
        self.id = canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, fill=couleur)


#Déplace la balle et renvoie son ancienne position.
    def deplacer(self):
        ancienne_position = (self.x, self.y)
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.id, self.dx, self.dy)
        return ancienne_position


#faire rebondir la balle horizontalement
    def rebondir_horizontalement(self):
        self.dx = -self.dx


#faire rebondir la balle verticalement
    def rebondir_verticalement(self):
        self.dy = -self.dy


#sert a replacer la balle a un endroit voulu
    def placer(self, x, y):
        self.x, self.y = x, y
        self.canvas.coords(self.id, x - self.rayon, y - self.rayon, x + self.rayon, y + self.rayon)

#supprime la balle
    def supprimer(self):
        self.canvas.delete(self.id)
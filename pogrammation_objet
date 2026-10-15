#Objectifs: définir les différentes classes pour réaliser le jeu de casse brique pour le TP4 de développement python, CPE Lyon
#Crée le 08/10/2026
#Réalisé par SAVATIER Noah / TORTEROLO Alexis
#TO DO: classe brique, classe raquette, classse balle
#Infos : taille de la fenêtre ( 700*700+400+200)

import tkinter as tk
import math 

#Classe 1: Brique classique. Concept: rectangle immobile, disparaissant lorsqu'elle entre en contact avec la balle une fois.  

class briqueclassique:
    def __init__(self, x, y, caneva, largeur=20, longueur = 30, points = 10, couleur = "green"):
        self.__x = x
        self.__y = y
        self.__largeur = largeur
        self.__longueur = longueur
        self.__points = points
        self.__couleur = couleur
        self.__caneva = caneva

    def rectangle(self): #crée le visuel de la brique
        self.rectangle = self.__caneva.create_rectangle(self.__x, self.__y, self.__x + self.__longueur, self.__y + self.__largeur, fill = self.__couleur, width = 0)
    
    def touche(self, balle): # vérifie si la balle touche la brique
        if balle.__x + balle.__rayon > self.__x and balle.__y + balle.__rayon > self.__y and balle.__y - balle.__rayon < self.__y + self.__largeur and balle.__x - balle.__rayon < self.__x + self.__longueur:
            return True
        else:
            return False

    def supp(self, balle, points): #supprime la brique si elle est touchée par la balle et augmente le score du joueur
        if self.touche(self,balle) == True:
            self.caneva.delete(self.rectangle)
            points = points + 10

        

#Classe 2: Balle. Concept: cercle qui rebondit sur les bords de la fenêtre, sauf celui du bas. Elle rebondit également sur les briques
#          et a un effet sur elles qui diffère selon le type de la brique.

class balle:
    def __init__(self, x, y, caneva, vitesse, rayon=10, couleur = "red"):
            self.__x = x
            self.__y = y
            self.__rayon = rayon
            self.__couleur = couleur
            self.__canva = caneva
            self.__vitesse = 

    def disque(self, caneva): #crée le visuel de la balle
        Balle = caneva.create_oval(self.__x - self.__rayon, self.__y - self.__rayon, self.__x + self.__rayon, self.__y + self.__rayon, width = 1, fill = self.__couleur)

    def deplacement(self): # permet à la balle de se déplacer selon les règles de déplacement définies
        angle = math.random.uniform(0.2 * math.pi)
        DX = self.vitesse*math.cos(angle)
        DY = self.vitesse*math.sin(angle)

        if self.__x + self.__rayon + DX > self.__caneva.largeur:
            self.__x = 2*(self.__caneva.largeur - self.__rayon) - self.__x
            DX = - DX

        if self.__x - self.__rayon + DX < 0 :
            self.__x = 2 * self.__rayon - self.__x
            DX = -DX
        
        
        if self.__y + self.__rayon + DY > self.caneva.
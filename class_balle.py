"""
Objectif : creer la classe de la balle pour l'utiliser dans notre casse briques
Auteur : Elie et Mattias
Date : 15/10/26
ToDO : class balle avec les fonctions permettant de :
se deplacer
se deplacer selon l'axe des x
se deplacer selon l'axe des y

"""

import random
import math


facteur_vitesse_x = 0.65 * (3/4)
facteur_vitesse_y = 0.76 *(3/4)


class Balle:
    """Balle qui se déplace toute seule et rebondit sur les éléments du jeu."""

    def __init__(self, x, y, canvas, rayon=9, couleur="red", vitesse=5):
        """
        Crée la balle 
        Entrées : x, y (float) : centre de départ de la balle
                  canvas (Canvas) : canevas 
                  rayon (int) : rayon en pixels
                  couleur (str) : couleur de remplissage
                  vitesse (float) : vitesse de base utilisée pour calculer la vitesse initiale en x et en y
        """
        self.x = x
        self.y = y
        self.rayon = rayon
        self.canvas = canvas
        self.couleur = couleur
        self.vitesse = vitesse
        self.dx = random.choice([-1, 1]) * vitesse * facteur_vitesse_x
        self.dy = -vitesse * facteur_vitesse_y
        self.id = canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon,fill=couleur, outline="")

    def deplacer(self):
        """Déplace la balle d'un pas selon sa vitesse actuelle (dx, dy)"""
        
        self.x += self.dx
        self.y += self.dy
        self.canvas.move(self.id, self.dx, self.dy)

    def accelerer(self, facteur=1.02, vitesse_max=11):
        """Augmente la vitesse de la balle sans changer sa direction."""
        
        vitesse_actuelle = math.sqrt(self.dx **2 + self.dy **2)
        nouvelle_vitesse = min(vitesse_actuelle * facteur, vitesse_max)

        rapport = nouvelle_vitesse / vitesse_actuelle

        self.dx *= rapport
        self.dy *= rapport
        self.vitesse = nouvelle_vitesse

    

    def rebondir_horizontalement(self):
        """Inverse le sens horizontal de la balle (rebond sur un mur)"""
        
        self.dx = -self.dx

    def rebondir_verticalement(self):
        """Inverse le sens vertical de la balle (rebond sur un obstacle)"""
        
        self.dy = -self.dy

    def placer(self, x, y):
        """
        Replace la balle à une position précise (après une vie perdue)
        Entrées : x, y (float) : nouveau centre de la balle
        """
        self.x, self.y = x, y
        self.canvas.coords(
            self.id,
            x - self.rayon, y - self.rayon,
            x + self.rayon, y + self.rayon
        )

    def supprimer(self):
        """Efface la balle du canevas"""
        
        self.canvas.delete(self.id)
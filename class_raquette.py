"""
Objectif du fichier : classe raquette du casse brique

Auteurs : Mattias et Elie

Date: 15/10/2026

ToDo : Amelioration de la raquette et ajouter des options de jeux (ex: au bout de 5 rauqette brisees agrandire la raquette)

"""

class Raquette:
    """Raquette contrôlée par le joueur en bas de l'écran"""

    def __init__(self, x, y, canvas, largeur=110, hauteur=14,
                 couleur="blue", vitesse=9):
        """
        Crée la raquette et la dessine sur le canevas
        Entrées : x, y (float) : position du centre de la raquette
                  canvas (Canvas) : canevas Tkinter où dessiner
                  largeur, hauteur (int) : dimensions en pixels
                  couleur (str) : couleur de remplissage
                  vitesse (int) : pixels parcourus à chaque déplacement
        """
        self.x = x
        self.y = y
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.vitesse = vitesse
        self.id = canvas.create_rectangle(x - largeur / 2, y - hauteur / 2, x + largeur / 2, y + hauteur / 2,
        fill=couleur, outline="")

    def deplacer(self, direction, largeur_canvas):
        """
        Déplace la raquette horizontalement sans sortir du canevas.
        Entrées : direction (int) : -1 (gauche), 0 (immobile) ou 1 (droite)
                  largeur_canvas (int) : largeur du canevas en pixels
        """
        self.x += direction * self.vitesse
        demi = self.largeur / 2
        self.x = max(demi, min(largeur_canvas - demi, self.x))
        self.canvas.coords(self.id, self.x - demi, self.y - self.hauteur / 2, self.x + demi, self.y + self.hauteur / 2)

    def contient_x(self, x):
        """
        Indique si une abscisse se trouve au-dessus de la raquette.
        Entrée : x (float) : abscisse à tester (ex. celle de la balle)
        Sortie : bool : True si x est entre les deux bords de la raquette
        """
        return self.x - self.largeur / 2 <= x <= self.x + self.largeur / 2

    def haut(self):
        """Sortie : float : position en y du bord haut de la raquette."""
        return self.y - self.hauteur / 2

    def bas(self):
        """Sortie : float : position en y du bord bas de la raquette."""
        return self.y + self.hauteur / 2

    def supprimer(self):
        """Efface la raquette du canevas."""
        self.canvas.delete(self.id)
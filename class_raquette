"""
Objectif du fichier : classe raquette du casse brique

Auteurs : Mattias et Elie

Date: 15/10/2026

ToDo : Amelioration de la raquette et ajouter des options de jeux (ex: au bout de 5 rauqette brisees agrandire la raquette)

"""

vitesse_raquette = 9  # pixels parcourus à chaque déplacement


class Raquette:
    """
    Raquette contrôlée par le joueur
    (x, y) est la position du centre de la raquette
    """

    def __init__(self, x, y, canvas, largeur=110, hauteur=14, couleur='deepskyblue'):
        """
        Crée la raquette et la dessine sur le canevas
        Entrées : x, y : position du centre de la raquette
                  canvas : canevas Tkinter
                  largeur, hauteur : dimensions en pixels
                  couleur : couleur de remplissage
        """
        self.x = x
        self.y = y
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.vitesse = vitesse_raquette
        self.id = canvas.create_rectangle(self.coordonnees(), fill = couleur, outline = '')

    def coordonnees(self):
        """
        Calcule les coins du rectangle à partir du centre.
        Sortie : tuple (x1, y1, x2, y2) : coins haut gauche et bas droit
        """
        demi_largeur = self.largeur / 2
        demi_hauteur = self.hauteur / 2
        return (self.x - demi_largeur, self.y - demi_hauteur, self.x + demi_largeur, self.y + demi_hauteur)

    def deplacer(self, direction, largeur_canvas):
        """
        Déplace la raquette horizontalement sans sortir du canevas.
        Entrées : direction : -1 (gauche), 0 (immobile) ou 1 (droite)
                  largeur_canvas : largeur du canevas en pixels
        Sortie : aucune (la position et le dessin sont mis à jour)
        """
        self.x += direction * self.vitesse
        demi_largeur = self.largeur / 2
        # on bloque le centre pour que la raquette reste entière à l'écran
        self.x = max(demi_largeur, min(largeur_canvas - demi_largeur, self.x))
        self.canvas.coords(self.id, self.coordonnees())

    def contient_x(self, x):
        """
        Indique si une abscisse se trouve au-dessus de la raquette.
        Entrée : x : abscisse à tester (ex. celle de la balle)
        Sortie : True si x est entre les deux bords de la raquette
        """
        demi_largeur = self.largeur / 2
        return self.x - demi_largeur <= x <= self.x + demi_largeur

    def supprimer(self):
        "Efface la raquette du canevas"
        self.canvas.delete(self.id)
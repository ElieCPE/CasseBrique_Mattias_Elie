"""

Objectif : creer la classe des briques

Auteur : Elie et Mattias

Date : 15/10/26

ToDO : Ameliorer le jeu en le rendant plus avancer (plus de briques resistantes, 
des briques qui rendent la balle plus rapide etc...)
"""



class Brique:
    """Une brique qui peut nécessiter plusieurs impacts avant de
    disparaître."""

    def __init__(self, x1, y1, x2, y2, canvas, points=10, resistance=1, couleur="green"):
        """
        Crée la brique et la dessine sur le canevas.
        Entrées : x1, y1, x2, y2 (float) : coins haut gauche et bas droit
                  canvas (Canvas) : canevas Tkinter où dessiner
                  points (int) : points gagnés quand la brique est détruite
                  resistance (int) : nombre de coups avant destruction
                  couleur (str) : couleur de remplissage
        """
        self.canvas = canvas
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.points = points
        self.resistance = resistance
        self.couleur = couleur
        self.detruite = False
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black", width=2)

    def touche(self):
        """
        Enregistre un impact sur la brique
        Sortie : int : les points gagnés (0 si la brique résiste encore)
        """
        if self.detruite:
            return 0

        self.resistance -= 1
        if self.resistance <= 0:
            self.detruite = True
            self.canvas.delete(self.id)
            return self.points

        # Une brique résistante change de couleur après un impact.
        self.canvas.itemconfigure(self.id, fill="yellow")
        return 0

    def contient(self, x, y, rayon):
        """
        Test simple de recouvrement entre la balle et la brique
        Entrées : x, y : centre de la balle
                  rayon : rayon de la balle
        Sortie : bool : True s'il y a recouvrement
        """
        return (x + rayon >= self.x1 and x - rayon <= self.x2
            and y + rayon >= self.y1 and y - rayon <= self.y2)
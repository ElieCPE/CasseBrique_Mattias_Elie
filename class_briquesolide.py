"""
Objectif : Creer la brique solide

Auteur: Mattias et Elie

Date: 15/10/2026

ToDo:

"""

from class_brique import Brique


class BriqueSolide(Brique):
    def __init__(self, x1, y1, x2, y2, canvas):
        super().__init__(x1, y1, x2, y2, canvas, points=30, resistance=2, couleur="blue")

"""
Objectif : Creer la brique classique

Auteur: Mattias et Elie

Date: 15/10/2026

ToDo:
Creer des techniques plus avancees
"""

from class_brique import Brique

class BriqueClassique(Brique):
    def __init__(self, x1, y1, x2, y2, canvas):
        super().__init__(x1, y1, x2, y2, canvas, points=10, resistance=1, couleur="green")

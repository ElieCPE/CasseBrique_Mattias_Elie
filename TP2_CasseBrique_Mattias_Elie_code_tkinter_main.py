"""
Objectif : interface graphique Tkinter du casse-briques

Auteurs : Mattias et Elie

Date : 15/10/2026

ToDo : Amliorer le jeu en ajoutant des fonctionalites (accelertion de la balles au cours du jeu etc...)

"""

import tkinter as tk

from class_raquette import Raquette
from class_balle import Balle
from class_brique import Brique


largeur = 800
hauteur = 550
fps_ms = 20

# Touches qui font bouger la raquette (regroupées ici pour ne pas
# répéter la même liste dans appuyer_touche et relacher_touche).
touches_gauche = ("Left", "q", "Q", "a", "A")
touches_droite = ("Right", "d", "D")

# Vitesses de la balle (pixels par image), pour éviter les nombres
# "magiques" dans la boucle de jeu.
vitesse_horizontale_max = 5.5
vitesse_horizontale_min = 1.2
vitesse_initiale_x = 3.2
vitesse_initiale_y = -4.0


class JeuCasseBriques:
    """Fenêtre principale : affichage, commandes du joueur et boucle
    de jeu"""

    def __init__(self, fenetre):
        """
        Crée la fenêtre, ses widgets et l'état initial du jeu
        Entrée : fenetre : fenêtre Tkinter principale
        """
        self.fenetre = fenetre
        self.fenetre.title("Casse-briques")
        self.fenetre.resizable(False, False)
        self.fenetre.configure(bg="black")

        bandeau = tk.Frame(fenetre, bg="black")
        bandeau.pack(fill="x", padx=12, pady=(10, 6))

        self.label_score = tk.Label(
            bandeau, text="Score : 0", fg="white", bg="black", font=("Arial", 13, "bold"))
        self.label_score.pack(side="left")

        self.label_vies = tk.Label(bandeau, text="Vies : 3", fg="white", bg="black", font=("Arial", 13, "bold"))
        self.label_vies.pack(side="right")

        self.canvas = tk.Canvas(fenetre, width=largeur, height=hauteur, bg="black", highlightthickness=0)
        self.canvas.pack(padx=12)

        commandes = tk.Frame(fenetre, bg="black")
        commandes.pack(fill="x", padx=12, pady=8)

        tk.Button(commandes, text="Démarrer/reprendre", command=self.demarrer).pack(side="left")

        tk.Button(commandes, text="Pause", command=self.mettre_en_pause).pack(side="left", padx=6)

        tk.Button(commandes, text="Recommencer", command=self.recommencer).pack(side="left")

        tk.Label(commandes, text="Déplacement: flèches gauche/droite ou Q / D",
        fg="white", bg="black", font=("Arial", 10)).pack(side="right")

        # Un booléen par touche : plus simple à suivre qu'un ensemble.
        self.touche_gauche = False
        self.touche_droite = False

        self.score = 0
        self.vies = 3
        self.en_cours = False
        self.termine = False
        self.after_id = None

        self.fenetre.bind("<KeyPress>", self.appuyer_touche)
        self.fenetre.bind("<KeyRelease>", self.relacher_touche)
        self.fenetre.protocol("WM_DELETE_WINDOW", self.fermer)

        self.initialiser_partie()

    def initialiser_partie(self):
        """Remet le score, les vies et les briques à zéro, puis affiche le message de départ"""
        
        if self.after_id is not None:
            self.fenetre.after_cancel(self.after_id)
            self.after_id = None

        self.en_cours = False
        self.termine = False
        self.touche_gauche = False
        self.touche_droite = False
        self.canvas.delete("all")

        self.score = 0
        self.vies = 3
        self.raquette = Raquette(largeur / 2, hauteur - 35, self.canvas)
        self.balle = Balle(largeur / 2, hauteur - 60, self.canvas)
        self.briques = []
        self.creer_briques()
        self.actualiser_informations()
        self.message_id = self.canvas.create_text(largeur / 2, hauteur / 2 + 70, text="Clique sur « Démarrer / reprendre »",
            fill="white", font=("Arial", 16, "bold"))

    def creer_briques(self):
        """Crée et dessine toutes les briques du niveau"""
        
        colonnes = 10
        lignes = 5
        marge_gauche = 35
        marge_haut = 45
        largeur_brique = 66
        hauteur_brique = 22
        espace_x = 10
        espace_y = 9

        for ligne in range(lignes):
            for colonne in range(colonnes):
                x1 = marge_gauche + colonne*(largeur_brique + espace_x)
                y1 = marge_haut + ligne*(hauteur_brique + espace_y)
                x2 = x1 + largeur_brique
                y2 = y1 + hauteur_brique

                # Quelques briques bleues sont plus résistantes.
                if ligne == 0 and colonne % 3 == 0:
                    brique = Brique(x1, y1, x2, y2, self.canvas, points=30, resistance=2, couleur="orange")
                else:
                    brique = Brique(x1, y1, x2, y2, self.canvas, points=10, resistance=1, couleur="green")
                self.briques.append(brique)

    def actualiser_informations(self):
        "Met à jour l'affichage du score et des vies"
        
        self.label_score.config(text="Score: " + str(self.score))
        self.label_vies.config(text="Vies: " + str(self.vies))

    def appuyer_touche(self, evenement):
        """
        Réagit à l'appui d'une touche du clavier
        Entrée: evenement : événement clavier envoyé par Tkinter
        """
        touche = evenement.keysym
        if touche in touches_gauche:
            self.touche_gauche = True
        elif touche in touches_droite:
            self.touche_droite = True
        elif touche == "space":
            if self.en_cours:
                self.mettre_en_pause()
            else:
                self.demarrer()

    def relacher_touche(self, evenement):
        """
        Réagit au relâchement d'une touche du clavier
        Entrée : evenement : événement clavier envoyé par Tkinter
        """
        touche = evenement.keysym
        if touche in touches_gauche:
            self.touche_gauche = False
        elif touche in touches_droite:
            self.touche_droite = False

    def demarrer(self):
        """Lance ou reprend la partie"""
        
        if self.termine or self.en_cours:
            return
        self.en_cours = True
        self.canvas.delete(self.message_id)
        self.boucle_jeu()

    def mettre_en_pause(self):
        """Met la partie en pause et affiche un message au centre"""
        
        if not self.en_cours:
            return
        
        self.en_cours = False
        self.touche_gauche = False
        self.touche_droite = False
        self.message_id = self.canvas.create_text(largeur / 2, hauteur / 2, text="PAUSE — appuie sur Démarrer / espace",
            fill="white", font=("Arial", 17, "bold"))

    def boucle_jeu(self):
        """Fait avancer le jeu d'une image (déplacements, collisions),
        puis se reprogramme si la partie continue"""
        
        if not self.en_cours:
            return

        direction = 0
        if self.touche_gauche:
            direction -= 1
        if self.touche_droite:
            direction += 1
        self.raquette.deplacer(direction, largeur)

        self.balle.deplacer()
        balle = self.balle
        rayon = balle.rayon

        # Murs gauche et droit
        if balle.x - rayon <= 0:
            balle.x = rayon
            balle.rebondir_horizontalement()
        elif balle.x + rayon >= largeur:
            balle.x = largeur - rayon
            balle.rebondir_horizontalement()

        # Plafond : pas de rebond sur le bas, car une vie est perdue
        if balle.y - rayon <= 0:
            balle.y = rayon
            balle.rebondir_verticalement()

        # Collision avec la raquette : seulement si la balle descend
        if (balle.dy > 0
                and balle.y + rayon >= self.raquette.haut()
                and balle.y - rayon <= self.raquette.bas()
                and self.raquette.contient_x(balle.x)):
            balle.y = self.raquette.haut() - rayon
            balle.rebondir_verticalement()

            # Plus on tape loin du centre, plus la balle repart sur le côté
            ecart = (balle.x - self.raquette.x) / (self.raquette.largeur / 2)
            nouvelle_vitesse = ecart * vitesse_horizontale_max
            if nouvelle_vitesse > vitesse_horizontale_max:
                nouvelle_vitesse = vitesse_horizontale_max
            elif nouvelle_vitesse < -vitesse_horizontale_max:
                nouvelle_vitesse = -vitesse_horizontale_max
            balle.dx = nouvelle_vitesse

            # Évite une trajectoire presque verticale et trop lente
            if -vitesse_horizontale_min < balle.dx < vitesse_horizontale_min:
                if ecart >= 0:
                    balle.dx = vitesse_horizontale_min
                else:
                    balle.dx = -vitesse_horizontale_min

        # Collision avec la première brique touchée pendant cette image
        for brique in self.briques:
            if brique.detruite:
                continue
            if brique.contient(balle.x, balle.y, rayon):
                self.score += brique.touche()
                balle.rebondir_verticalement()
                self.actualiser_informations()
                break

        # La balle est passée sous la raquette : une vie en moins
        if balle.y - rayon > hauteur:
            self.vies -= 1
            self.actualiser_informations()
            if self.vies <= 0:
                self.fin_partie(False)
                return
            balle.placer(largeur / 2, hauteur - 60)
            balle.dx = vitesse_initiale_x
            balle.dy = vitesse_initiale_y
            self.mettre_en_pause()
            self.canvas.delete(self.message_id)
            self.message_id = self.canvas.create_text(largeur / 2, hauteur / 2, text="Vie perdue! Appuie sur Démarrer/espace",
                fill="white", font=("Arial", 16, "bold"))
            return

        # Victoire : on vérifie si toutes les briques sont détruites.
        toutes_detruites = True
        for brique in self.briques:
            if not brique.detruite:
                toutes_detruites = False
        if toutes_detruites:
            self.fin_partie(True)
            return

        self.after_id = self.fenetre.after(fps_ms, self.boucle_jeu)

    def fin_partie(self, victoire):
        """
        Arrête la partie et affiche le résultat final
        Entrée : victoire: True si le joueur a gagné
        """
        self.en_cours = False
        self.termine = True
        if victoire:
            message = "BRAVO, TU AS GAGNÉ!"
        else:
            message = "PARTIE TERMINÉE"
        texte = (message + "\nScore final: " + str(self.score)
                 + "\nClique sur Recommencer")
        self.message_id = self.canvas.create_text(largeur / 2, hauteur / 2, text=texte,
            fill="white", justify="center")

    def recommencer(self):
        """Relance une partie depuis le début"""
        
        self.initialiser_partie()

    def fermer(self):
        """Arrête la boucle de jeu puis ferme la fenêtre proprement"""
        
        if self.after_id is not None:
            self.fenetre.after_cancel(self.after_id)
        self.fenetre.destroy()


# Programme principal
if __name__ == "__main__":
    fenetre = tk.Tk()
    jeu = JeuCasseBriques(fenetre)
    fenetre.mainloop()
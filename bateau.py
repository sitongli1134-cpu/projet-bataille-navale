class Bateau:
    def __init__(self, ligne, colonne, longueur=1, vertical=False, marque='?'):
        self.ligne = ligne
        self.colonne = colonne
        self.longueur = longueur
        self.vertical = vertical
        self.marque = marque  # symbole propre au type de bateau

    @property
    def positions(self):
        """
        Retourne la liste des cases occupées par le bateau.
        """
        pos = []
        for i in range(self.longueur):
            if self.vertical:
                pos.append((self.ligne + i, self.colonne))
            else:
                pos.append((self.ligne, self.colonne + i))
        return pos

    def coule(self, grille):
        """
        Vérifie si le bateau est coulé.
        Un bateau est coulé si toutes ses cases sont marquées 'x'.
        """
        for (l, c) in self.positions:
            if grille.grille[grille.index(l, c)] != grille.touche:
                return False
        return True


# =====================
#     SOUS-CLASSES
# =====================

class PorteAvion(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=4, vertical=vertical, marque='🚢')


class Croiseur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=3, vertical=vertical, marque='⛴')


class Torpilleur(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque='🚣')


class SousMarin(Bateau):
    def __init__(self, ligne, colonne, vertical=False):
        super().__init__(ligne, colonne, longueur=2, vertical=vertical, marque='🐟')

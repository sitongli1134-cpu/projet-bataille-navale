class Grille:
    # caractères utilisés pour représenter les cases
    vide = '~'          # case vide
    touche = 'x'        # case touchée par défaut
    bateau_char = '⛵'   # caractère utilisé pour afficher un bateau

    def __init__(self, lignes, colonnes):
        self.lignes = lignes
        self.colonnes = colonnes

        # création de la grille vide
        self.grille = [self.vide] * (lignes * colonnes)

        # liste des bateaux déjà placés
        self.bateaux = []

    def index(self, ligne, colonne):
        return ligne * self.colonnes + colonne

    def tirer(self, ligne, colonne, touche=None):
        """
        Effectue un tir sur la case indiquée.
        Le paramètre 'touche' permet de choisir le caractère affiché (par défaut 'x').
        """
        if touche is None:
            touche = self.touche

        i = self.index(ligne, colonne)
        self.grille[i] = touche

    def peut_placer(self, bateau):
        """
        Vérifie si un bateau peut être placé sur la grille :
        - entièrement dans les limites
        - sans chevauchement
        """
        for (l, c) in bateau.positions:
            if l < 0 or l >= self.lignes or c < 0 or c >= self.colonnes:
                return False
            if self.grille[self.index(l, c)] != self.vide:
                return False
        return True

    def ajoute(self, bateau):
        """
        Place un bateau sur la grille, si possible.
        """
        if not self.peut_placer(bateau):
            print("Placement impossible : chevauchement ou hors de la grille.")
            return False

        for (l, c) in bateau.positions:
            self.grille[self.index(l, c)] = bateau.marque

        self.bateaux.append(bateau)
        return True

    def __str__(self):
        """
        Représentation textuelle de la grille.
        """
        texte = ""
        for i in range(self.lignes):
            ligne = self.grille[i * self.colonnes : (i + 1) * self.colonnes]
            texte += "".join(ligne) + "\n"
        return texte

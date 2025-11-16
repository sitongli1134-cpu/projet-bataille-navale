import random
from grille import Grille
from bateau import PorteAvion, Croiseur, Torpilleur, SousMarin

# ===============================
#   Génération des bateaux
# ===============================

def creer_bateaux():
    """
    Crée une liste contenant un bateau de chaque type.
    """
    return [
        PorteAvion(0, 0),
        Croiseur(0, 0),
        Torpilleur(0, 0),
        SousMarin(0, 0),
    ]


# ===============================
#   Placement aléatoire
# ===============================

def place_aleatoire(grille, bateau):
    """
    Tente de placer un bateau sur la grille à une position aléatoire.
    Continue jusqu'à ce qu'un placement valide soit trouvé.
    """
    while True:
        # orientation aléatoire
        vertical = random.choice([True, False])

        # limite correcte selon orientation
        if vertical:
            ligne = random.randint(0, grille.lignes - bateau.longueur)
            colonne = random.randint(0, grille.colonnes - 1)
        else:
            ligne = random.randint(0, grille.lignes - 1)
            colonne = random.randint(0, grille.colonnes - bateau.longueur)

        # mettre à jour position
        bateau.ligne = ligne
        bateau.colonne = colonne
        bateau.vertical = vertical

        if grille.peut_placer(bateau):
            grille.ajoute(bateau)
            break


# ===============================
#   Jeu principal
# ===============================

def jouer():
    print("=== BATAILLE NAVALE ===")

    # création de la grille
    g = Grille(8, 10)

    # création des bateaux
    bateaux = creer_bateaux()

    # placement aléatoire
    for b in bateaux:
        place_aleatoire(g, b)

    print("Bateaux placés !\n")

    # boucle de jeu
    while True:
        print(g)

        # demander un tir
        entree = input("Entrez un tir (ligne colonne) ou 'q' pour quitter : ")

        if entree.lower() == 'q':
            print("Fin du jeu.")
            break

        try:
            l, c = map(int, entree.split())
        except:
            print("Entrée invalide, utilisez : nombre nombre\n")
            continue

        # contrôle des limites
        if not (0 <= l < g.lignes and 0 <= c < g.colonnes):
            print("Coordonnées hors grille !\n")
            continue

        # effectuer un tir normal
        g.tirer(l, c, '⚫')  # un tir touche utilise ⚫

        # vérifier si un bateau est touché / coulé
        for b in bateaux:
            if (l, c) in b.positions:
                print("Touché !")

                if b.coule(g):
                    print(f"Bateau coulé : {b.marque}")
                    # afficher le bateau coulé en clair
                    for (x, y) in b.positions:
                        g.tirer(x, y, b.marque)
                break

        print()


if __name__ == "__main__":
    jouer()

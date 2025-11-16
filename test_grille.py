import os, sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from grille import Grille

def test_init():
    # teste si la grille est correctement initialisée
    g = Grille(5, 8)
    assert len(g.grille) == 5 * 8
    assert all(cell == g.vide for cell in g.grille)

def test_tirer():
    # teste si un tir est correctement enregistré
    g = Grille(5, 8)
    g.tirer(2, 3)
    assert g.grille[2 * 8 + 3] == g.touche

def test_print():
    # affiche la grille pour vérification visuelle
    g = Grille(3, 4)
    g.tirer(1, 2)
    print("=== GRILLE ===")
    print(g)

if __name__ == "__main__":
    test_init()
    print("Initialisation OK")
    test_tirer()
    print("Tir OK")
    test_print()
    print("Affichage OK")

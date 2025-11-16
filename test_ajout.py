from grille import Grille
from bateau import Bateau

g = Grille(5, 6)

b1 = Bateau(1, 1, longueur=3)    # horizontal : (1,1),(1,2),(1,3)
b2 = Bateau(0, 4, longueur=2)    # horizontal : (0,4),(0,5)
b3 = Bateau(1, 2, longueur=3)    # chevauche b1

print("Ajout b1 :", g.ajoute(b1))
print("Ajout b2 :", g.ajoute(b2))
print("Ajout b3 :", g.ajoute(b3))   # doit échouer

print("\nGrille :")
print(g)

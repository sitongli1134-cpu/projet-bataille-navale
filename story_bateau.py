from bateau import Bateau

def chevauchent(b1, b2):
    """
    Vérifie si deux bateaux se chevauchent.
    Deux bateaux se chevauchent s'ils partagent au moins une position.
    """
    positions_b1 = set(b1.positions)
    positions_b2 = set(b2.positions)

    # intersection non vide → chevauchement
    return len(positions_b1.intersection(positions_b2)) > 0


# ------------------------------
# User Story : "chevauchement"
# ------------------------------
print("=== User Story : chevauchement ===")

# Cas 1 : bateaux qui se chevauchent
b1 = Bateau(2, 3, longueur=3)   # occupe (2,3), (2,4), (2,5)
b2 = Bateau(2, 4, longueur=2)   # occupe (2,4), (2,5)

print("Bateaux b1 et b2 chevauchent ? ->", chevauchent(b1, b2))

# Cas 2 : bateaux séparés
b3 = Bateau(5, 1, longueur=3)   # occupe (5,1), (5,2), (5,3)
b4 = Bateau(3, 6, longueur=2)   # occupe (3,6), (3,7)

print("Bateaux b3 et b4 chevauchent ? ->", chevauchent(b3, b4))

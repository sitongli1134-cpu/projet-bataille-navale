from bateau import Bateau

def test_positions():
    b1 = Bateau(2, 3, longueur=3)
    assert b1.positions == [(2,3), (2,4), (2,5)]

    b2 = Bateau(2, 3, longueur=3, vertical=True)
    assert b2.positions == [(2,3), (3,3), (4,3)]

test_positions()
print("Test Bateau OK")

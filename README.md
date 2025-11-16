🛳️ Projet : Bataille Navale (Python)

Un mini-jeu de bataille navale réalisé en Python.
Le joueur doit tirer sur une grille afin de toucher et couler les bateaux placés aléatoirement.

📌 Fonctionnalités

Génération d'une grille 8 × 10

Placement aléatoire des 4 bateaux (sans chevauchement)

Types de bateaux :

🚢 Porte-avion (longueur 4)

⛴ Croiseur (longueur 3)

🚣 Torpilleur (longueur 2)

🐟 Sous-marin (longueur 2)

Système de tir : le joueur entre une ligne et une colonne

Affichage mis à jour après chaque tir

Détection :

✴ = touché

x = tir dans l'eau

~ = eau

Détection de bateau coulé

Fin de partie : tous les bateaux coulés

📂 Structure du projet
```
projet-bataille-navale/
│
├── bataille.py         # Logique du jeu complet
├── grille.py           # Gestion de la grille
├── bateau.py           # Classe Bateau + types de bateaux
├── story_bateau.py     # Scénarios de test
├── test_ajout.py       # Tests pour l'ajout de bateaux
├── test_bateau.py      # Tests pour la classe Bateau
├── test_grille.py      # Tests pour la grille
├── main.py             # Point d'entrée du jeu
├── requirements.txt    # Dépendances (standard library uniquement)
└── README.md           # Documentation du projet
```


▶️ Lancer le jeu
1️⃣ Créer un environnement virtuel

Windows :

python -m venv .venv
.venv\Scripts\activate


Mac / Linux :

python3 -m venv .venv
source .venv/bin/activate

2️⃣ Installer les dépendances
pip install -r requirements.txt


(Le projet utilise uniquement la bibliothèque standard de Python.)

3️⃣ Lancer le jeu
python main.py

🧪 Exécuter les tests
python test_grille.py
python test_bateau.py
python test_ajout.py

🖥️ Exemple d'affichage
```
~~~~🚣🚣~~~~
~~~~~~~~~~
~~~~🚢🚢🚢🚢~~
~~~~~~~⛴⛴⛴
~~~~~~~~~~
~~~~~~~~🐟🐟
~~~~~~~~~~
~~~~~~~~~~
```

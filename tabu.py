from __future__ import annotations
import math
import random
import matplotlib.pyplot as plt
nb_villes = 26
positions = {}

# assigner des positions aléatoires aux villes
# sur une grille allant de 0 à 100 sur les deux axes
for i in range(nb_villes):
    positions[chr(ord('A') + i)] = (
    random.randrange(0, 100),
    random.randrange(0, 100),
    )


# calcule la distance entre deux villes
def distance(a: str, b: str) -> float:
    xa, ya = positions[a][0], positions[a][1]
    xb, yb = positions[b][0], positions[b][1]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# calcule le score (que l'on cherche à MINIMISER)
# ceci correspond à la distance totale en
# passant par toutes les villes et en revenant à la ville initiale
def score(villes: list[str]) -> float:
    t = 0
    for i in range(len(villes) - 1):
        t+= distance(villes[i], villes[i+1])
    t+= distance(villes[-1], villes[0])
    return t

# liste les solutions voisines de la solution candidate en
# permutant l'ordre de passage entre deux villes et
# retourne la solution voisine et le mouvement menant à cette solution
def listerVoisins(candidat: list[str]) -> list[tuple[list, tuple]]:
    l = []
    for i in range(len(candidat) - 1):
        for j in range(i+1, len(candidat)):
            voisin = candidat[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            mouvement = tuple(sorted((voisin[i], voisin[j])))
            l.append((voisin, mouvement))
    return l

#recherche la meilleure solution
def rechercher(
    s0: list,
    max_iterations=1000,
    max_size_taboue_list=10
    ) -> list:
    s = s0
    candidat = s0
    listeTaboue = []
    iterations = 0
    while iterations < max_iterations:
        voisins_et_mouv = listerVoisins(candidat)
        candidat, candidat_mouvement = voisins_et_mouv[0]
        for v, m in voisins_et_mouv:
            if score(v) < score(candidat) and m not in listeTaboue:
                candidat, candidat_mouvement = v, m
        if score(candidat) < score(s):
            s = candidat
        listeTaboue.append(candidat_mouvement)
        if len(listeTaboue) > max_size_taboue_list:
            listeTaboue.pop(0)
        iterations += 1
    return s

def visualiser(s: list[str]):
    
    _, ax = plt.subplots()
    x = [positions[v][0] for v in s]
    y = [positions[v][1] for v in s]
    ax.plot(x, y, marker='x', markeredgecolor='r', color='b')
    for i, v in enumerate(s):
        ax.annotate(v, (x[i], y[i]))
    plt.show()

def main():
    # initialiser la solution initiale aléatoirement
    s0 = list(positions.keys())
    random.shuffle(s0)
    print('Solution initiale: ', s0)
    print('Coût de la solution initiale:', score(s0))
    print()
    # ici on teste l'algorithme avec différents paramètres
    params = [(2, 0), (2, 2), (10, 1), (10, 5), (100, 2), (100, 10)]
    for max_iterations, max_taboue_size in params:
        s = rechercher(s0, max_iterations, max_taboue_size)
        print(
        'Recherche avec ', max_iterations,
        ' iterations, et une liste taboue de taille ', max_taboue_size
        )
        print('Solution trouvée : ', s)
        print('Score de la solution trouvée: ', score(s))
        print()
    visualiser(s) # visualise la dernière solution trouvée
main()

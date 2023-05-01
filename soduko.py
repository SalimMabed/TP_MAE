from __future__ import annotations
import math
import random
def genererSolutionInitiale():
    # générer une liste de 9x9 élements
    g = [i for i in range(9) for _ in range(9)]
    random.shuffle(g)
    # reconvertir en matrix de dimension 2
    g = [g[i:i+9] for i in range(0, len(g), 9)]
    return g

def score(s):
    t = 0
    # lignes
    t += sum(1 for l in s if len(set(l)) != 9)
    # colonnes
    for i in range(9):
        col = set(l[i] for l in s)
        if len(set(col)) != 9:
            t+=1
    # sous grilles
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid_set = set(
                s[x][y] for x in range(i, i + 3)
                for y in range(j, j + 3)
            )
            if len(subgrid_set) != 9:
                t += 1
    return t

def generer_voisin(s):
    i = random.randrange(0, 9)
    j = random.randrange(0, 9)
    k = random.randrange(0, 9)
    l = random.randrange(0, 9)
    voisin = [l[:] for l in s]
    voisin[i][j], voisin[k][l] = voisin[k][l], voisin[i][j]
    return voisin

def rechercher(
        solution_initiale,
        temp = 1.0 ,
        taux_refroisissement = 0.99999,
        temp_minimale = 1e-7,
        max_iterations = 1e6 ,
):
    solution_actuelle =solution_initiale
    score_actuel = score(solution_actuelle)
    best_solution , best_score = solution_actuelle , score_actuel
    iteration = 0
    while temp> temp_minimale and iteration<max_iterations:
        voisin=generer_voisin(solution_actuelle)
        score_voisin = score(voisin)

        #decider si on doit accepter la solution
        delta_score = score_actuel - score_voisin
        if delta_score >=0 or math.exp(delta_score/temp) > random.random():
            solution_actuelle , score_actuel = voisin , score_voisin
        if best_score>score_actuel:
            best_solution,best_score=solution_actuelle,score_actuel
            if best_score==0:
                break
        
        #reduire la temperature
        temp*=taux_refroisissement
        iteration+=1
    return best_solution , best_score

s=genererSolutionInitiale()
s,score_s=rechercher(s)
print("\n".join(" ".join(str(i)for i in l)for l in s))
if score_s==0:
    print("la grille est valide!!")
else:
    print("la grille contient ", score_s,"erreurs")
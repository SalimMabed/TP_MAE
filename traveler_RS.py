from __future__ import annotations
import math
import random
import matplotlib.pyplot as plt

nb_villes = 26
positions = {}

def genererSolutionInitiale():
    for i in range(nb_villes):
        positions[i] = (
        random.randrange(0, 100),
        random.randrange(0, 100),
        )
    return  list(positions.keys())

def distance(a, b) -> float:
    xa, ya = positions[a][0], positions[a][1]
    xb, yb = positions[b][0], positions[b][1]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

def score(villes) -> float:
    t = 0
    for i in range(len(villes) - 1):
        t+= distance(villes[i], villes[i+1])
    t+= distance(villes[-1], villes[0])
    return t

def generer_voisin(s):
    i , j = random.sample(range(nb_villes), k=2)
    
    s[i], s[j] = s[j], s[i]

    return s

def rechercher(
        solution_initiale,
        temp = 1.0 ,
        taux_refroidissement = 0.99999,
        temp_minimale = 1e-7,
        max_iterations = 1e6 ,
):
    solution_actuelle =solution_initiale
    score_actuel = score(solution_actuelle)
    best_solution , best_score = solution_actuelle , score_actuel
    iteration = 0
    while temp> temp_minimale and iteration<max_iterations:
        voisin=generer_voisin(solution_actuelle[:])
        score_voisin = score(voisin)

        #decider si on doit accepter la solution
        delta_score = score_actuel - score_voisin
        if delta_score >=0 or math.exp(delta_score/temp) > random.random():
            solution_actuelle , score_actuel = voisin , score_voisin
        if best_score>score_actuel:
            best_solution,best_score=solution_actuelle[:],score_actuel
            if best_score==0:
                break
        
        #reduire la temperature
        temp*=taux_refroidissement
        iteration+=1
    return best_solution , best_score

def visualiser(s: list[str]):
    
    _, ax = plt.subplots()
    x = [positions[v][0] for v in s]
    y = [positions[v][1] for v in s]
    ax.plot(x, y, marker='x', markeredgecolor='r', color='b')
    for i, v in enumerate(s):
        ax.annotate(str(v), (x[i], y[i]))
    plt.show()


def main():

    s=genererSolutionInitiale()
    s,score_s=rechercher(s)

    print('Solution initiale: ', s)
    print('Coût de la solution initiale:', score(s))
    print() 
    print('Solution trouvée : ', s)
    print('Score de la solution trouvée: ', score(s))
    print()
    visualiser(s) # visualise la dernière solution trouvée
main()

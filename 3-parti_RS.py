import random
import math


def generateint():
    g=[]
    #g = [random.randint(0, 99) for _ in range(99)]
    g = [9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1]


    f = [g[i:i+3] for i in range(0, len(g), 3)]
    return g ,f


def score(s):
    
    score=0
    for i in s:
        score+=abs(sum(i)-maxscore)
    return  score

def generate_neighbors(g):
    i = random.randrange(0,len(g))
    j = random.randrange(0, len(g))
    k = random.randrange(0, 3)
    l = random.randrange(0, 3)
    voisin = [l[:] for l in g]
    voisin[i][k], voisin[j][l] = voisin[j][l], voisin[i][k]
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
        voisin=generate_neighbors(solution_actuelle)
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

s,f=generateint()
maxscore =sum(s)/len(f)
s,score_s=rechercher(f)

if score_s==0:
    print("solutions trovee")
    print(s)
else:
    print("la meilleur solution trouver est :")
    print(s)



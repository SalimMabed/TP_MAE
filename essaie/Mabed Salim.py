import random
import math
grid_size = 64



#Mabed Salim



def generate_grid():
    g=[]
    for i in range(grid_size):
        if i<grid_size//2:
            g.append(0)
        else:
            g.append(1)
    
    random.shuffle(g)
    g = [g[i:i+8] for i in range(0, len(g), 8)]
    return g 


def score(s:list):
    
    erreurs = 0
    #erreurs sur les lignes
    for i in range(len(s)-2):
        for j in range(len(s)-2):
            
            #lignes
            if (s[i][j] == s[i][j+1] and s[i][j] == s[i][j+2]):
                erreurs+=1 

            #diagonales
            if (s[i][j] == s[i+1][j+1] and s[i][j]==s[i+2][j+2]):
                erreurs+=1
            #diagonales 2
            """if(i>)
                if (s[i:j] == s[i-1:j-1]) and s[i:j]==s[i-2:j-2]:
                    erreurs+=1"""
            #colonnes
            if (s[i][j] == s[i+1][j] and s[i][j] == s[i+2][j]):
                erreurs+=1 


    return erreurs


def generate_neighour(s):
    i = random.randrange(0, 8)
    j = random.randrange(0, 8)
    k = random.randrange(0, 8)
    l = random.randrange(0, 8)
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
        voisin=generate_neighour(solution_actuelle)
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

s= generate_grid()
print("\n".join(" ".join(str(i)for i in l)for l in s))

print("La grille contient ",score(s)," erreurs \n\n\n")

s,s_score=rechercher(s)


print("\n".join(" ".join(str(i)for i in l)for l in s))
print("La grille contient ",score(s)," erreurs ")

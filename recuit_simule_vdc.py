import random
import math

nb_villes = 5
position = {}
max_iter=1e5
t_min=1e-11
taux_refr = 0.999999




for i in range(nb_villes):
    position[i]=[random.randrange(0,1000),random.randrange(0,1000)]

s0=list(position.keys())

random.shuffle(s0)

def distance_euclidienne(a:int,b:int):

    x1, y1 = position[a][0], position[a][1]
    x2, y2 = position[b][0], position[b][1]
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

def score(s:list[int]):
    somme=0
    for i in range(len(s)-1):
        somme+=distance_euclidienne(s[i],s[i+1])
    somme+=distance_euclidienne(s[0],s[-1])
    return somme
def generervoisin(candidat):
    i, j = random.sample(
        range(nb_villes),
        k=2)
    candidat [i], candidat[j] = candidat[j], candidat[i]
    return candidat


def aleatoire(delta_score, temp):
    p=math.exp(delta_score/temp)

    if(p > random.random()):
        return True
    return False


def rechercher(s0,t0=1.0):
    candidat = s0
    s = s0
    s_score=score(s)
    nb_iter=0
    while(nb_iter < max_iter and t0 > t_min):
        if(nb_iter%1000):
            print(nb_iter)
        voisin = generervoisin(candidat)
        candidat_score=score(candidat)
        voisin_score = score(voisin)
        delta_score = candidat_score - voisin_score  # minimiser
        if(delta_score>0 or aleatoire(delta_score,t0)):
            candidat = voisin
            candidat_score = voisin_score
        if(s_score > candidat_score):
            s = candidat
            s_score=candidat_score
        nb_iter+=1
        t0 = t0*taux_refr
    return s, s_score

def visualiser(s):
    import matplotlib.pyplot as plt
    _, ax = plt.subplots()
    x = [position[v][0] for v in s]
    y = [position[v][1] for v in s]
    ax.plot(x, y, marker='x', markeredgecolor='r', color='b')
    for i, v in enumerate(s):
        ax.annotate(v, (x[i], y[i]))
    plt.show()



s ,s_score= rechercher(s0)
print("s",s,"score",s_score)
visualiser(s)
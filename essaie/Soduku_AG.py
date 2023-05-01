import random
Soduku_Size = 9
POPULATION_SIZE = 100
MUTATION_RATE = 0.05
MAX_GENERATIONS = 10000
MAX_SCORE = sum(range(Soduku_Size))


def genererIndividu():
    # générer une liste de 9x9 élements
    g = [i for i in range(Soduku_Size) for _ in range(Soduku_Size)]
    random.shuffle(g)
    # reconvertir en matrix de dimension 2
    g = [g[i:i+Soduku_Size] for i in range(0, len(g), Soduku_Size)]
    return g

"""def genererIndividu():
    for i in range(Soduku_Size):
        l=[]
        l.append(random.sample(range(1, 10), Soduku_Size))

    return l
"""
def score(s):
    t = 0
    # lignes
    t += sum(1 for l in s if len(set(l)) != Soduku_Size)
    # colonnes
    for i in range(Soduku_Size):
        col = set(l[i] for l in s)
        if len(set(col)) != Soduku_Size:
            t+=1
    # sous grilles
    for i in range(0, Soduku_Size, 3):
        for j in range(0, Soduku_Size, 3):
            subgrid_set = set(
                s[x][y] for x in range(i, i + 3)
                for y in range(j, j + 3)
            )
            if len(subgrid_set) != Soduku_Size:
                t += 1
    return t

def selection(population,tournament_size):
    tournoi=random.sample(population,tournament_size)
    return min(tournoi,key=score)

    


def croisement(parent1, parent2):

    crossover_point = random.randrange(1, Soduku_Size)
    enfant1 = parent1[:crossover_point] + parent2[crossover_point:]
    enfant2 = parent2[:crossover_point] + parent1[crossover_point:]

    return enfant1, enfant2

def muter(individu):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(Soduku_Size), 2)
        individu[idx1], individu[idx2] = individu[idx2], individu[idx1]

def evoluer(population):
    scores = [score(pi) for pi in population]
    nouvelle_population = []
    for _ in range(POPULATION_SIZE):
        # sélection à la roue de la fortune biaisée
        parent1, parent2 = random.choices(population, weights=scores, k=2)
        # croisement et mutation
        enfant1, enfant2 = croisement(parent1, parent2)
        muter(enfant1)
        muter(enfant2)
        nouvelle_population.append(enfant1)
        nouvelle_population.append(enfant2)
    return nouvelle_population


def rechercher():
    
    population = [genererIndividu() for _ in range(POPULATION_SIZE)]
    for generation in range(MAX_GENERATIONS):
        best_solution = max(population, key=score)
        if score(best_solution) == MAX_SCORE:
            return best_solution, generation
        population = evoluer(population)

    return None, MAX_GENERATIONS

solution, generation = rechercher()
if solution:
    print(solution, 'après', generation, 'générations.')
else:
    print('Pas de solution trouvée après', generation, 'générations.')

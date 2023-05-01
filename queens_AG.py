import random
BOARD_SIZE = 8
POPULATION_SIZE = 100
MUTATION_RATE = 0.05
MAX_GENERATIONS = 1000
MAX_SCORE = sum(range(BOARD_SIZE))


def genererIndividu():
    return random.sample(range(1, 1 + BOARD_SIZE), BOARD_SIZE)

def score(individu: list) -> int:
    # erreurs sur les lignes
    erreurs = abs(len(individu) - len(set(individu)))
    # erreurs sur les diagonales
    for i in range(len(individu)):
        for j in range(i + 1, len(individu)):

            if abs(i - j) == abs(individu[i] - individu[j]):
                erreurs += 1
    return MAX_SCORE - erreurs

def croisement(parent1, parent2):
    crossover_point = random.randrange(1, BOARD_SIZE)
    enfant1 = parent1[:crossover_point] + parent2[crossover_point:]
    enfant2 = parent2[:crossover_point] + parent1[crossover_point:]
    return enfant1, enfant2

def muter(individu):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(BOARD_SIZE), 2)
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
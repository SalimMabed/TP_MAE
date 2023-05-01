import random
import math
import matplotlib.pyplot as plt

nb_villes = 26
positions = {}

POPULATION_SIZE = 100
MUTATION_RATE = 0.05
MAX_GENERATIONS = 1000


def generate_individual():
    for i in range(nb_villes):
        positions[i] = (
        random.randrange(0, 100),
        random.randrange(0, 100),
        )
    return  list(positions.keys())

def calculate_distance(city1, city2):
    x1, y1 = positions[city1]
    x2, y2 = positions[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def calculate_fitness(individual):
    distance = 0
    for i in range(len(individual)):
        if i == len(individual) - 1:
            distance += calculate_distance(individual[i], individual[0])
        else:
            distance += calculate_distance(individual[i], individual[i+1])
    return 1 / distance

def select_parents(population):
    fitnesses = [calculate_fitness(individual) for individual in population]
    return random.choices(population, weights=fitnesses, k=2)

def crossover(parent1, parent2):
    crossover_point = random.randrange(1, len(parent1))
    child1 = parent1[:crossover_point] + [city for city in parent2 if city not in parent1[:crossover_point]]
    child2 = parent2[:crossover_point] + [city for city in parent1 if city not in parent2[:crossover_point]]
    return child1, child2

def mutate(individual):
    if random.random() < MUTATION_RATE:
        idx1, idx2 = random.sample(range(len(individual)), 2)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]

def evolve_population(population):
    new_population = []
    while len(new_population) < len(population):
        parent1, parent2 = select_parents(population)
        child1, child2 = crossover(parent1, parent2)
        mutate(child1)
        mutate(child2)
        new_population.append(child1)
        new_population.append(child2)
    return new_population

def visualiser(s: list[str]):
    _, ax = plt.subplots()
    x = [positions[v][0] for v in s]
    y = [positions[v][1] for v in s]
    ax.plot(x, y, marker='x', markeredgecolor='r', color='b')
    for i, v in enumerate(s):
        ax.annotate(str(v), (x[i], y[i]))
    plt.show()

def search():
    population = [generate_individual() for _ in range(POPULATION_SIZE)]
    for generation in range(MAX_GENERATIONS):
        best_individual = max(population, key=calculate_fitness)
        print("Generation:", generation, "Best distance:", 1/calculate_fitness(best_individual))
        
        population = evolve_population(population)
    return best_individual, 1/calculate_fitness(best_individual)

best_individual, best_distance = search()
print("Best individual:", best_individual)
print("Best distance:", best_distance)

visualiser(best_individual)

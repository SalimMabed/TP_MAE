import math
import random

# Define the number of cities and their positions
nb_villes = 26
positions = {}
for i in range(nb_villes):
    positions[chr(ord('A') + i)] = (
        random.randrange(0, 100),
        random.randrange(0, 100),
    )

# Define the function to calculate the distance between two cities
def distance(a, b):
    xa, ya = positions[a][0], positions[a][1]
    xb, yb = positions[b][0], positions[b][1]
    return math.sqrt((xa - xb) ** 2 + (ya - yb) ** 2)

# Define the function to calculate the score (total distance) of a route
def score(villes):
    t = 0
    for i in range(len(villes) - 1):
        t+= distance(villes[i], villes[i+1])
    t+= distance(villes[-1], villes[0])
    return t

# Define the function to generate the neighboring solutions of a given solution
def listerVoisins(candidat):
    l = []
    for i in range(len(candidat) - 1):
        for j in range(i+1, len(candidat)):
            voisin = candidat[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            l.append(voisin)
    return l

# Define the function to perform the Tabu Search algorithm
def rechercher(s0, max_iterations=1000):
    s = s0
    candidat = s0
    iterations = 0
    while iterations < max_iterations:
        voisins = listerVoisins(candidat)
        candidat = min(voisins, key=score)
        if score(candidat) < score(s):
            s = candidat
        iterations += 1
    return s

# Define the function to visualize the solution
import matplotlib.pyplot as plt
def visualiser(s):
    x = [positions[v][0] for v in s]
    y = [positions[v][1] for v in s]
    plt.plot(x, y, marker='x', markeredgecolor='r', color='b')
    for i, v in enumerate(s):
        plt.annotate(v, (x[i], y[i]))
    plt.show()

# Define the main function to run the algorithm
def main():
    # Generate a random initial solution
    s0 = list(positions.keys())
    random.shuffle(s0)
    print('Initial solution: ', s0)
    print('Initial score:', score(s0))
    # Perform the Tabu Search algorithm with a fixed number of iterations
    s = rechercher(s0, max_iterations=1000)
    print('Final solution: ', s)
    print('Final score: ', score(s))
    # Visualize the final solution
    visualiser(s)

# Run the main function
main()

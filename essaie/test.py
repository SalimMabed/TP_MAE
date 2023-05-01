import random
Soduku_Size = 9
POPULATION_SIZE = 100
MUTATION_RATE = 0.05
MAX_GENERATIONS = 1000
MAX_SCORE = sum(range(Soduku_Size))

grid_size =64

def generateint():
    
    g=[]
    for i in range(grid_size):
        if i<grid_size//2:
            g.append(0)
        else:
            g.append(1)
    
    random.shuffle(g)
    g = [g[i:i+8] for i in range(0, len(g), 8)]
    return g 


print(generateint())
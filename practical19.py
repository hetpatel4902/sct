import numpy as np
from geneticalgorithm import geneticalgorithm as ga

def fitness(x):
    return (x**2+3*x+2)

varbound = np.array([[-6,0]])
model = ga(function=fitness, dimension=1, variable_type='real', variable_boundaries=varbound)
model.run()
fittest_individual = model.best_variable[0]
print('Fittest individual:', fittest_individual, 'Fitness:', -model.best_function)

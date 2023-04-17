from geneticalgorithm import geneticalgorithm as ga
import numpy as np

def f(X):
    x1, x2 = X
    return -1 * (4*x1 + 5*x2)

varbound = np.array([(1, 2), (1, 2)])

model = ga(function=f, dimension=2, variable_type='real', variable_boundaries=varbound)

model.run()
print('Fitness:', -model.best_function)
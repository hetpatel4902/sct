import matplotlib.pyplot as plt
import numpy as np

def triangular(x, a, b, c):
    return np.maximum(np.minimum((x - a) / (b - a), (c - x) / (c - b)), 0)

def trapezoidal(x, a, b, c, d):
    return np.maximum(np.minimum((x - a) / (b - a), 1, (d - x) / (d - c)), 0)

x = np.linspace(0, 10, 1000)

tri = triangular(x, 3, 5, 7)
plt.plot(x, tri, label='Triangular')

trap = trapezoidal(x, 2, 4, 6, 8)
plt.plot(x, trap, label='Trapezoidal')

plt.xlabel('x')
plt.ylabel('Membership degree')
plt.title('Fuzzy Membership Functions')
plt.legend()

plt.show()

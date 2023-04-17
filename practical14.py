import numpy as np

R1 = np.array([[0.4, 0.8], [0.1, 0.6]])
R2 = np.array([[0.7, 0.2], [0.5, 0.9]])

U = np.array(['low', 'high'])
C = np.array([[np.fmax(np.fmin(R1[i], R2[j]), 0) for j in range(len(U))] for i in range(len(U))])
print(C)

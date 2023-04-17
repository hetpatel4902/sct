import numpy as np

I = np.array([[1, 1, 1], [-1, 1, -1], [1, 1, 1]])
H = np.array([[1, -1, 1], [1, 1, 1], [1, -1, 1]])

target_I = 1
target_H = -1

I_flat = I.flatten()
H_flat = H.flatten()

weights = np.zeros(I_flat.shape)
bias = 0

def activation(x):
    return 1 if x >= 0 else -1

for i in range(100):

    I_output = activation(np.dot(I_flat, weights) + bias)
    error_I = target_I - I_output
    weights += error_I * I_flat
    bias += error_I

    H_output = activation(np.dot(H_flat, weights) + bias)
    error_H = target_H - H_output
    weights += error_H * H_flat
    bias += error_H

I_output = activation(np.dot(I_flat, weights) + bias)
H_output = activation(np.dot(H_flat, weights) + bias)

print("Weights:", weights)
print("Bias:", bias)
print("I Output:", I_output)
print("H Output:", H_output)
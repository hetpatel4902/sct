import numpy as np

X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])

Y = np.array([[1, 0], [0, 1], [0, 1], [1, 0]])

learning_rate = 0.1
num_iterations = 1000

weights = np.random.rand(2, 2)

bias = np.zeros((1, 2))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

for i in range(num_iterations):
    output = sigmoid(np.dot(X, weights) + bias)
    
    error = Y - output
    
    weights += learning_rate * np.dot(X.T, error * output * (1 - output))
    bias += learning_rate * np.sum(error * output * (1 - output), axis=0, keepdims=True)

test_data = np.array([[0.5, 0.5], [0.2, 0.8], [0.8, 0.2]])
test_output = sigmoid(np.dot(test_data, weights) + bias)

print(test_output)

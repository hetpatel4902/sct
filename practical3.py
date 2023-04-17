import numpy as np

train_A = np.array([[1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1]])

train_B = np.array([[1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 1],
                    [1, 0, 0, 0, 1]])

train_A = train_A.flatten()
train_B = train_B.flatten()

def hebb_learning_rule(train_data):
    n = len(train_data)
    weights = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i == j:
                weights[i][j] = 0
            else:
                weights[i][j] += train_data[i] * train_data[j]
    return weights

weights = hebb_learning_rule(train_A)
weights += hebb_learning_rule(train_B)

test_A = np.array([1, 1, 1, 0, 1,
                   1, 0, 0, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1])

test_B = np.array([1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1,
                   1, 1, 1, 1, 1,
                   1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1])

test_A = test_A.flatten()
test_B = test_B.flatten()

output_A = np.dot(weights, test_A)
output_H = np.dot(weights, test_B)

if np.greater(np.any(output_A) ,np.any(output_H)):
    print("Predicted letter is A")
else:
    print("Predicted letter is B")
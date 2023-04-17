import numpy as np

input = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
output = np.array([[0], [1], [1], [1]])

def activation(x):
    return np.where(x >= 0, 1, -1)

def MR_I(train_input, train_output, weight):

    n = weight.shape[1]

    m = train_input.shape[0]

    eta = 0.1

    for i in range(m):
        y1 = activation(np.dot(train_input[i], weight))
        y2 = activation(np.dot(y1, np.ones((n, 1))))
        error = train_output[i] - y2
        weight += eta * error * y1.reshape(1, -1)

    return weight

def Madaline(train_input, train_output, n):
    weight = np.random.rand(train_input.shape[1], n)

    for i in range(10):

        weight = MR_I(train_input, train_output, weight)

    return weight

weight = Madaline(input, output, 1)

for i in range(4):
    y1 = activation(np.dot(input[i], weight))
    y2 = activation(np.dot(y1, np.ones((1, 1))))
    print("Input:", input[i], "Output:", y2[0])


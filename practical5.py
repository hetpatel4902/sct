import numpy as np

class Adaline:
    def __init__(self, learning_rate=0.1, epochs=50):
        self.learning_rate = learning_rate
        self.epochs = epochs
    
    def fit(self, X, y):
        self.weights = np.zeros(X.shape[1])
        self.bias = 0
        
        for epoch in range(self.epochs):
            output = self.predict(X)
            
            error = y - output
            
            self.weights += self.learning_rate * np.dot(X.T, error)
            self.bias += self.learning_rate * error.sum()
    
    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y = np.array([-1, -1, -1, 1])

model = Adaline()
model.fit(X, y)

predictions = model.predict(X)
print(predictions)

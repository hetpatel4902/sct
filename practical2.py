import numpy as np

def mp_neuron(x, w, b):
    z = np.dot(w, x) + b
    y = 1 if z >= 0 else 0
    return y

def logic_and(x):
    w = np.array([1, 1])
    b = -1
    return mp_neuron(x, w, b)

def logic_or(x):
    w = np.array([1, 1])
    b = 0
    return mp_neuron(x, w, b)

def logic_not(x):
    w = np.array([-1])
    b = 0
    return mp_neuron(x, w, b)

x_and = np.array([0, 0])
y_and = logic_and(x_and)
print(f"AND({x_and}) = {y_and}")

x_and = np.array([0, 1])
y_and = logic_and(x_and)
print(f"AND({x_and}) = {y_and}")

x_and = np.array([1, 0])
y_and = logic_and(x_and)
print(f"AND({x_and}) = {y_and}")

x_and = np.array([1, 1])
y_and = logic_and(x_and)
print(f"AND({x_and}) = {y_and}")

x_or = np.array([0, 0])
y_or = logic_or(x_or)
print(f"OR({x_or}) = {y_or}")

x_or = np.array([0, 1])
y_or = logic_or(x_or)
print(f"OR({x_or}) = {y_or}")

x_or = np.array([1, 0])
y_or = logic_or(x_or)
print(f"OR({x_or}) = {y_or}")

x_or = np.array([1, 1])
y_or = logic_or(x_or)
print(f"OR({x_or}) = {y_or}")

x_not = np.array([0])
y_not = logic_not(x_not)
print(f"NOT({x_not}) = {y_not}")

x_not = np.array([1])
y_not = logic_not(x_not)
print(f"NOT({x_not}) = {y_not}")
import numpy as np
import matplotlib.pyplot as plt

def identity(x):
    """Identity activation function"""
    return x

def linear(x):
    """Linear activation function"""
    return x

def binary_step(x):
    """Binary step activation function"""
    return np.where(x >= 0, 1, 0)

def bipolar_step(x):
    """Bipolar step activation function"""
    return np.where(x >= 0, 1, -1)

def bell_shaped(x, a=1, b=1, c=0):
    """Bell-shaped activation function"""
    return a * np.exp(-b * (x - c)**2)

# plot activation functions
x = np.linspace(-5, 5, 1000)

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.plot(x, identity(x))
plt.title("Identity Function")

plt.subplot(2, 3, 2)
plt.plot(x, linear(x))
plt.title("Linear Function")

plt.subplot(2, 3, 3)
plt.plot(x, binary_step(x))
plt.title("Binary Step Function")

plt.subplot(2, 3, 4)
plt.plot(x, bipolar_step(x))
plt.title("Bipolar Step Function")

plt.subplot(2, 3, 5)
plt.plot(x, bell_shaped(x))
plt.title("Bell-Shaped Function")

plt.show()

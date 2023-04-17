import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
# System parameters
dt = 0.1
tank_height = 10
tank_radius = 5
inflow_valve_area = 0.1
outflow_valve_area = 0.2
# Initial water level
h_init = 2

# Desired water level
h_ref = 5
# Define the neural network model
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, input_shape=(1,), activation='relu'),
    tf.keras.layers.Dense(1, activation='linear')
])
# Compile the model
model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=0.01))
# Simulation loop
t = 0
h = h_init
inflow_rate = 0
outflow_rate = 0
h_data = []
t_data = []
while t < 50:
    # Compute the control action
    error = h_ref - h
    control_input = model.predict(np.array([error]))
    inflow_rate = max(control_input, 0)
    outflow_rate = max(-control_input, 0)
    
    # Update the water level
    inflow_volume = inflow_rate * inflow_valve_area * dt
    outflow_volume = outflow_rate * outflow_valve_area * dt
    delta_h = (inflow_volume - outflow_volume) / (np.pi * tank_radius**2)
    h = max(h + delta_h, 0)
    
    # Record the data
    t_data.append(t)
    h_data.append(h)
    
    # Update the time
    t += dt
# Plot the results
plt.plot(t_data, h_data)
plt.xlabel('Time (s)')
plt.ylabel('Water Level (m)')
plt.show()

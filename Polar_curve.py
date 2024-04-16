import numpy as np
import matplotlib.pyplot as plt

# Define the range of theta values
theta = np.linspace(0, 2*np.pi, 1000)

# Calculate r values using the polar equation
r = 1 - np.cos(3 * theta)

# Convert polar coordinates to Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# Plot the polar curve
plt.figure(figsize=(8, 8))
plt.plot(x, y)
plt.title('Polar Curve: $r = 1 - \cos(3\Theta)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.axis('equal')  # Ensure aspect ratio is equal
plt.show()

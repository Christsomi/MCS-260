import numpy as np
import matplotlib.pyplot as plt

# Polar coordinates
r = 2
theta = (np.pi *3) /4

# Plot
plt.figure(figsize=(6, 6))
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r, 'ro')  # 'ro' indicates red color and circle marker
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 6.67430e-11  
AU = 1.496e11    
day = 86400      

planets = {
    'Mercury': {'mass': 3.301e23, 'a': 0.39, 'period': 88},
    'Venus': {'mass': 4.867e24, 'a': 0.72, 'period': 225},
    'Earth': {'mass': 5.972e24, 'a': 1.0, 'period': 365},
    'Mars': {'mass': 6.39e23, 'a': 1.52, 'period': 687}
}

initial_conditions = {}
for planet, properties in planets.items():
    a = properties['a'] * AU
    T = properties['period'] * day
    initial_conditions[planet] = {
        'a': a,
        'T': T,
        'theta': 0,
        'x': a * np.cos(0),
        'y': a * np.sin(0),
        'vx': -2 * np.pi * a / T * np.sin(0),
        'vy': 2 * np.pi * a / T * np.cos(0)
    }


fig, ax = plt.subplots()
ax.set_xlim(-AU * 2, AU * 2)
ax.set_ylim(-AU * 2, AU * 2)
ax.set_aspect('equal', adjustable='box')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')
ax.set_title('Inner Planets Orbiting the Sun')

planet_plots = {}

sun, = ax.plot(0, 0, 'yo', ms=10, label='Sun')

for planet, properties in planets.items():
    a = properties['a'] * AU
    orbit = plt.Circle((0, 0), a, color='grey', fill=False, linestyle='dashed', linewidth=0.5)
    ax.add_artist(orbit)

def update(frame):
    for planet, properties in planets.items():
        ic = initial_conditions[planet]
        ic['theta'] += 2 * np.pi / ic['T'] * day
        ic['x'] = ic['a'] * np.cos(ic['theta'])
        ic['y'] = ic['a'] * np.sin(ic['theta'])
        ic['vx'] = -2 * np.pi * ic['a'] / ic['T'] * np.sin(ic['theta'])
        ic['vy'] = 2 * np.pi * ic['a'] / ic['T'] * np.cos(ic['theta'])
        if planet in planet_plots:
            planet_plots[planet].set_data(ic['x'], ic['y'])
        else:
            planet_plots[planet], = ax.plot(ic['x'], ic['y'], 'o', label=planet)
    return planet_plots.values()

ani = FuncAnimation(fig, update, frames=np.arange(0, 365, 1), interval=50, blit=True)

plt.legend(loc='upper right')
plt.show()

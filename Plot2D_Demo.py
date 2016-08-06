'''
Created on 6 Aug 2016

@author: dave.barnett
'''

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import Engine2D

particles = [Engine2D.Particle(0, 600, 10, 1, 0, 1)]
world = Engine2D.World(True, 20, particles, 9.8, 1)

fig = plt.figure()
ax = fig.add_subplot(111)

framesPerSecond = 50

x = []
y = []

def update(num, P, L):
    contents = world.update(framesPerSecond)
    
    x.append(contents[0].x)
    y.append(contents[0].y)
    
    P.set_data(contents[0].x, contents[0].y)
    
    L.set_data(x, y)

P, = ax.plot([0.0], [0.0], 'bo')
L, = ax.plot([0.0], [0.0], 'r-')
ax.axis('scaled')
ax.set_xlim(0, 600)
ax.set_ylim(0, 600)
ax.grid(True)

ani = animation.FuncAnimation(fig, update, 180, fargs=(P,L), interval=framesPerSecond, blit=False)
plt.show()
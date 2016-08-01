import sys
import pygame
from Engine2D import *

pygame.init()
clock = pygame.time.Clock()
tick = 75

x = 750
y = 600
floorHeight = 20
size = (x,y)
P1 = Particle(100,560,10,10,0,1)
P2 = Particle(200,570,20,10,0,1)
P3 = Particle(300,560,10,-10,0,3)
world = World(True,20,[P1,P2,P3],9.8,1)

running = True
while running:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyPhys - MJB")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        contents = world.update(tick)
        for item in contents:
            pygame.draw.circle(screen,item.colour,(int(item.x),int(y-item.y)),item.size)
        pygame.draw.line(screen,(255,255,255),(0,y-floorHeight),(x,y-floorHeight))
        pygame.display.flip()
        clock.tick(tick)
        screen.fill((0,0,0))

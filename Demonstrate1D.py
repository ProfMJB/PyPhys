import sys
import pygame
from Engine1D import *

pygame.init()
clock = pygame.time.Clock()
tick = 75

x = 750
y = 600
floorHeight = 20
size = (x,y)
P1 = Particle(560,100,10,0,1)
P2 = Particle(570,200,20,0,1)
P3 = Particle(560,300,10,0,3)
world = World(True,20,[P1,P2,P3])

running = True
while running:
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyPhys - Max Barnett")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running = False
        contents = world.update(tick)
        for item in contents:
            pygame.draw.circle(screen,item.colour,(item.pos2,int(y-item.pos)),item.size)
            pygame.draw.line(screen,(255,255,255),(0,y-floorHeight),(x,y-floorHeight))
        pygame.display.flip()
        clock.tick(tick)
        screen.fill((0,0,0))

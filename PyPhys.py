import sys
import pygame

pygame.init()
clock = pygame.time.Clock()
gravity = 9.8 #Earth = 9.8
tick = 75
air = 1



class thing():
    def __init__(self,pos,pos2,size,velocity,density=1,colour=(255,255,255)):
        self.pos = pos
        self.pos2 = pos2
        self.size = size
        self.velocity = velocity
        self.colour = colour
        self.density = density
        self.mass = density * size * size
        
    def updatePos(self,isFloor,floorHeight):
        F = -(self.mass * gravity) + (self.size * self.velocity * air * -1)
        self.velocity += (F / self.mass) / tick
        self.pos += self.velocity
        if isFloor:
            heightFromFloor = self.pos - self.size - floorHeight
            if heightFromFloor < 0:
                if self.velocity < 0:
                    self.velocity *= -1
                self.pos = floorHeight - heightFromFloor + self.size
        
class world():
    def __init__(self,x,y,isFloor,floorHeight=20,contents = None):
        self.x = x
        self.y = y
        self.size = x,y
        self.isFloor = isFloor
        self.floorHeight = y - floorHeight
        if contents == None:
            self.contents = []
        else:
            self.contents = contents
        
    def Begin(self):
        running = True
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption("PyPhys - Max Barnett")
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    running = False
            for item in self.contents:
                pygame.draw.circle(self.screen,item.colour,(item.pos2,int(self.y-item.pos)),item.size)
                item.updatePos(self.isFloor,self.y-self.floorHeight)
            if self.isFloor:
                pygame.draw.line(self.screen,(255,255,255),(0,self.floorHeight),(self.x,self.floorHeight))
            pygame.display.flip()
            clock.tick(tick)
            self.screen.fill((0,0,0))

if __name__ == "__main__":
    thing1 = thing(560,100,10,0,1)
    thing2 = thing(570,200,20,0,1)
    thing3 = thing(560,300,10,0,3)
    world = world(750,600,True,50,[thing1,thing2,thing3])
    world.Begin()

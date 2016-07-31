class Particle():
    def __init__(self,pos,pos2,size,velocity,density=1,colour=(255,255,255)):
        self.pos = pos
        self.pos2 = pos2
        self.size = size
        self.velocity = velocity
        self.colour = colour
        self.density = density
        self.mass = density * size * size
        
    def updatePos(self,isFloor,floorHeight,gravity,air,tick):
        F = -(self.mass * gravity) + (self.size * self.velocity * air * -1)
        self.velocity += (F / self.mass) / tick
        self.pos += self.velocity
        if isFloor:
            heightFromFloor = self.pos - self.size - floorHeight
            if heightFromFloor < 0:
                if self.velocity < 0:
                    self.velocity *= -1
                self.pos = floorHeight - heightFromFloor + self.size

class World():
    def __init__(self,isFloor,floorHeight=20,contents=None,gravity=9.8,air=1):
        self.isFloor = isFloor
        self.floorHeight = floorHeight
        self.gravity = gravity
        self.air = air
        if contents == None:
            self.contents = []
        else:
            self.contents = contents
        
    def update(self,tick):
        for particle in self.contents:
                particle.updatePos(self.isFloor,self.floorHeight,self.gravity,self.air,tick)
        return self.contents

class Particle():
    def __init__(self,x,y,size,velocityx,velocityy,density=1,colour=(255,255,255)):
        self.x = float(x)
        self.y = float(y)
        self.size = size
        self.vx = float(velocityx)
        self.vy = float(velocityy)
        self.colour = colour
        self.density = float(density)
        self.mass = density * size * size
        
    def updatePos(self,isFloor,floorHeight,gravity,air,tick):
        Fy = -(self.mass * gravity) + (self.size * self.vy * air * -1)
        Fx = self.size * self.vx * air * -1
        self.vx += (Fx / self.mass) / tick
        self.vy += (Fy / self.mass) / tick
        self.x += self.vx
        self.y += self.vy
        if isFloor:
            heightFromFloor = self.y - self.size - floorHeight
            if heightFromFloor < 0:
                if self.vy < 0:
                    self.vy *= -1
                self.y = floorHeight - heightFromFloor + self.size

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

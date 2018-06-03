import pygame
from pygame.locals import *
import random
from NN import *
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)
size =  (   1500,  1000)
running = True

def touching(obj1,obj2):
    if (obj2.x+obj2.Length>=obj1.x>=obj2.x and obj2.y+obj2.weith>=obj1.y>=obj2.y): 
        return True
    elif (obj2.x+obj2.Length>=obj1.x+obj1.Length>=obj2.x and obj2.y+obj2.weith>=obj1.y>=obj2.y):
        return True
    elif (obj2.x+obj2.Length>=obj1.x>=obj2.x and obj2.y+obj2.weith>=obj1.y+obj1.weith>=obj2.y):
        return True
    elif (obj2.x+obj2.Length>=obj1.x+obj1.Length>=obj2.x and obj2.y+obj2.weith>=obj1.y+obj1.weith>=obj2.y):
        return True
    else:return False
def tile(x,y):
    x *= 100
    y *= 100
    if screen.get_at((x, y))[0:3] == WHITE:
        return 0
    elif screen.get_at((x, y))[0:3] == BLACK:
        return 1
    elif screen.get_at((x, y))[0:3] == RED:
        return 2
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Playground")
pygame.mouse.set_visible(1)
clock = pygame.time.Clock()
class world:
    def __init__(self):
        pass
    def update(self):
        pass
        
WORLD = world()        
class food:
    def __init__(self):
        self.x = random.randint(0,15)*100
        self.y = random.randint(0,10)*100
        self.Length = 50
        self.weith = 50
        self.exsit = True
    def generate(self):
        if self.exsit:
            pygame.draw.rect(screen, RED, [self.x, self.y, self.Length, self.weith])
            self.exsit = True
        else:pass
    def update(self):
        for i in os:
            if touching(i,food1):
                food1.exsit = False
def evlution(layer,neuron):
    o = organism()
    o.update()
    o.brain.buildlayer(layer)
    for i in range(2,layer+2):
        o.brain.layer[i].buildneuron(neuron)
    return o
class organism:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Length = 50
        self.weith = 50
        self.hunger = 0
        self.vision = [0 for x in range(0,150)]
        self.life = 0
        self.brain = neuralnetwork(self.vision)
        self.brain.layer[1].buildneuron(3)
    def update(self):
        self.hunger += 5
        if self.hunger < 100:
            pygame.draw.rect(screen, BLACK, [self.x, self.y, self.Length, self.weith])
            self.life += 1
        else:pass
        for x in range(0,15):
            for y in range(0,10):
                self.vision[10*x+y] = tile(x,y)
        self.brain.run()
        self.output = self.brain.layer[1].forward()
        if self.output[0]==0:
            self.x += 100
        elif self.output[1]==0:
            self.x += -100
        elif self.output[2]==0:
            self.y += 100
        elif self.output[3]==0:
            self.y += -100

     
food1 = food()
pygame.init()


os = [evlution(500,500) for i in range(5)]
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    for i in os:
        if touching(i,food1):
            i.life += 100
    screen.fill(WHITE)
    WORLD.update()
    food1.generate()
    food1.update()
    for i in os:
        i.update()
    pygame.display.update()
    clock.tick(1)
pygame.quit()
import pygame
from pygame.locals import *
import random
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
        self.x = random.randint(0,(size[0]-100))
        self.y = random.randint(0,(size[1]-100))
        self.Length = 50
        self.weith = 50
        self.exsit = True
    def generate(self):
        if self.exsit:
            pygame.draw.rect(screen, RED, [self.x, self.y, self.Length, self.weith])
            self.exsit = True
        else:pass
    def update(self):
        if touching(o1,food1):
            food1.exsit = False
class organism:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.Length = 50
        self.weith = 50
        self.hunger = 0
    def update(self):
        self.hunger += 0.01
        if self.hunger < 100:
            keys = pygame.key.get_pressed()
            if keys[K_UP]:
                self.y += -100
            elif keys[K_DOWN]:
                self.y += 100
            elif keys[K_LEFT]:
                self.x += -100
            elif keys[K_RIGHT]:
                self.x += 100
            pygame.draw.rect(screen, BLACK, [self.x, self.y, self.Length, self.weith])
        else:pass

food1 = food()
o1 = organism()
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    screen.fill(WHITE)
    WORLD.update()
    food1.generate()
    food1.update()
    o1.update()
    hungerness = myfont.render(('Hunger:'+ str(o1.hunger)), False, (0, 0, 0))
    screen.blit(hungerness,(0,0)) 
    pygame.display.update()
    clock.tick(144)   
pygame.quit()
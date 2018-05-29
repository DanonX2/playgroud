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
x = size[0]/2
y = size[1]/2
'''
def touching(obj1,obj2):
    if obj1.x >= obj2.x '''
class food:
    def __init__(self):
        self.x = random.randint(0,(size[0]-100))
        self.y = random.randint(0,(size[1]-100))
        self.Length = 100
        self.weith = 100
    def generate(self):
        pygame.draw.rect(screen, RED, [self.x, self.y, self.Length, self.weith])
class organism:
    pass
food1 = food()
def main():
    food1.generate()
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Playground")
clock = pygame.time.Clock()
while running:
    keys = pygame.key.get_pressed()
    pygame.mouse.set_visible(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    main()
    pygame.display.flip()
    clock.tick(144)
pygame.quit()
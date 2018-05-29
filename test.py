import pygame
BLACK = (   0,   0,   0)
WHITE = ( 255, 255, 255)
GREEN = (   0, 255,   0)
RED   = ( 255,   0,   0)
BLUE  = (   0,   0, 255)

size =  (   1500,  1000)
running = True
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Playground")
clock = pygame.time.Clock()
while running:
    pygame.mouse.set_visible(1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")
    screen.fill(WHITE)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
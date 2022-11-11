import pygame
from pygame.draw import *
from random import randint


pygame.init()


FPS = 1
screen = pygame.display.set_mode((1200, 850))
pygame.display.set_caption("Catch the ball")


SCREEN_ = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
m = 0


def new_ball():
    '''рисует новый шарик '''
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    event.x, event.y = event.pos
    global m
    if (event.x-x)**2 + (event.y-y)**2 <= r**2:
        print('Click!')
        m += 1
    else:
        print('Мимо :(')


pygame.display.update()
clock = pygame.time.Clock()
end = False


while not end:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
    for i in range(randint(1, 4)):
        new_ball()
    pygame.display.update()
    screen.fill(SCREEN_)


print(m)
pygame.quit()

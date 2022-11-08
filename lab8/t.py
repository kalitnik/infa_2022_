import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 250, 5), (100, 100, 200, 200))
polygon(screen, (150, 100, 10), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (200, 110, 10), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (2, 255, 225), (200, 200), 50)
circle(screen, (2, 255, 240), (200, 200), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
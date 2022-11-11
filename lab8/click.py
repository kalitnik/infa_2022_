import pygame
from pygame.draw import *
pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                circle(screen, (255,255,0), event.pos, 40)
                pygame.display.update()
            elif event.button == 3:
                circle(screen,  (0,255,255), event.pos, 30)
                pygame.display.update()

pygame.quit()
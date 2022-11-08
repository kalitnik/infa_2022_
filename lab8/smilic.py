import pygame
from pygame.draw import *

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 255, 255), (0, 0, 400, 400))
#face
circle(screen, (225, 225, 0), (200, 200), 100)
circle(screen, (0, 0, 0), (200, 200), 100,2)
#r_eye
circle(screen, (200, 0, 0), (240, 180), 30)
circle(screen, (0, 0, 0), (240, 180), 30,2)
circle(screen, (0, 0, 0), (240, 180), 10)
#l_eye
circle(screen, (200, 0, 0), (160, 180), 30)
circle(screen, (0, 0, 0), (160, 180), 30,2)
circle(screen, (0, 0, 0), (160, 180), 10)
#eyebrows
line(screen, (0, 0, 0), (220, 155), (270, 140),4)
line(screen, (0, 0, 0), (180, 155), (130, 140),4)
#mouse
line(screen, (0,0,0),(160,250),(240,250),20)


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
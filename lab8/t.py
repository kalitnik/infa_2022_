import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 300))

rect(screen, (255, 250, 5), (100, 100, 200, 200))
polygon(screen, (150, 100, 10), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (200, 110, 10), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (2, 255, 225), (200, 200), 50)
circle(screen, (2, 255, 240), (200, 200), 50, 5)

#травушка
x1 = 90; y1 = 270
x2 = 350; y2 = 300
N = 40
color = (0, 250, 0)
h = (x2 - x1) // (N + 1)
x = x1 + h
for i in range(N):
    line(screen, color, (x, y1), (x, y2))
    x += h

pygame.display.update() #чтобы фигуры отобразились на экране, экран нужно обновить
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
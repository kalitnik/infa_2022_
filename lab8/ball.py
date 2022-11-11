import pygame
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
m2 = 0


def new_ball():
    '''рисует новый шарик 
    x,y - координаты центра
    r - радиус
    '''
    global x, y, r, color
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    pygame.draw.circle(screen, color, (x, y), r)


def sqr():
    '''рисует рамочку'''
    global a, b, del1, del2
    a= randint(200, 400)
    b = randint(200, 400)
    del1 =  randint(100, 200)
    del2 =  randint(100, 200)
    pygame.draw.rect(screen, (0, 240, 255), (a, b, a + del1, b + del2),25)


def click(event):
    '''подсчитывает количество нажатий на шарик, на рамку
    выводит в консоль "мимо"/"клик" при промахе/попадании
    '''
    event.x, event.y = event.pos
    global m, m2
    if (event.x-x)**2 + (event.y-y)**2 <= r**2:
        print('Click!')
        m += 1
    elif (a <= event.x <= (a + del1)) and  (b <= event.y <= b+25):
        m2 += 2
        print('Clik!!!')
    elif (a <= event.x <= (a + del1)) and (b + del2 <= event.y <= b + del2):
        m2 += 2
        print('Clik!!!')
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
    sqr()
    for i in range(randint(1, 4)):
        new_ball()
    pygame.display.update()
    screen.fill(SCREEN_)


print(m, 'баллов за шарик', m2, 'баллов за рамку')
pygame.quit()

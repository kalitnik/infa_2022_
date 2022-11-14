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
COLORS = [RED, BLUE, YELLOW, GREEN, CYAN]
m = 0
m2 = 0


def ball():
    '''рисует шарик-цель (не пурпурного цвета),
    за который начисляется балл
    x,y - координаты центра
    r - радиус
    '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(30, 100)
    color = COLORS[randint(0, 4)]
    pygame.draw.circle(screen, color, (x, y), r)


def new_ball():
    '''рисует шарик-мусор(пурпурного цвета),
    за который не начисляются баллы
    x1, y1 - координаты центра
    r1 - радиус
    '''
    global x1, y1, r1
    x1 = randint(100, 1100)
    y1 = randint(100, 900)
    r1 = randint(10, 100)
    pygame.draw.circle(screen, MAGENTA, (x1, y1), r1)


def sqr():
    '''рисует рамочку'''
    global a, b, del1, del2
    a = randint(200, 400)
    b = randint(200, 400)
    del1 = randint(100, 200)
    del2 = randint(100, 200)
    color = COLORS[randint(0, 4)]
    pygame.draw.rect(screen, color, (a, b, a + del1, b + del2), 25)


def click(event):
    '''подсчитывает количество нажатий на не пурпурный шарик, на рамку
    выводит в консоль "мимо"/"клик" при промахе/попадании
    '''
    event.x, event.y = event.pos
    global m, m2
    if (event.x-x)**2 + (event.y-y)**2 <= r**2:
        print('Click!')
        m += 1
    elif a <= event.x and event.x <= a+del1:
        if (b <= event.y and event.y <= b+25) or (b+del2 <= event.y and event.y <= b+del2-25):
            m2 += 2
            print('Clik!!!')
    elif b <= event.y and event.y <= b+del2:
        if (a <= event.x and event.x <= a+25) or (a+del1 <= event.x and event.x <= a+del1-25):
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
    ball()
    for i in range(randint(1, 4)):
        new_ball()
    pygame.display.update()
    screen.fill(SCREEN_)


print(m, 'баллов за шарик', m2, 'баллов за рамку')
pygame.quit()

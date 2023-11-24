import pygame, datetime
import math

pygame.init()
done = True
clock = pygame.time.Clock()
size = width, height = 400, 405
h2, w2 = height//2, width//2
screen = pygame.display.set_mode(size)
imageclock = pygame.image.load('images\main-clock.png')
rad = 175

radiis = {'min': rad - 55, 'sec': rad - 15}
clock60 = dict(zip(range(60), range(0, 360, 6)))

def position(dictt, hand, key):
    x = h2 + radiis[key] * math.cos(math.radians(dictt[hand]) - math.pi/2)
    y = w2 + radiis[key] * math.sin(math.radians(dictt[hand]) - math.pi/2)
    return x, y

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False

    t = datetime.datetime.now()
    minute, second = t.minute, t.second
    screen.blit(imageclock, (0, 0))
    
    pygame.draw.line(screen, pygame.Color('black'), (h2, w2), position(clock60, minute, 'min'), 10)
    pygame.draw.line(screen, pygame.Color('black'), (h2, w2), position(clock60, second, 'sec'), 5)
    pygame.draw.circle(screen, (0, 0, 0), (h2, w2), 8)

    pygame.display.flip()
    clock.tick(60)
import pygame
from datetime import datetime
import math

pygame.init()
done = True
clock = pygame.time.Clock()
r = h, w = 600, 400
h2, w2 = h//2, w//2
rad = 175
screen = pygame.display.set_mode(r)


radiis = {'hour': rad - 100, 'min': rad - 55, 'sec': rad - 15}
clock12 = dict(zip(range(12), range(0, 360, 30)))
clock60 = dict(zip(range(60), range(0, 360, 6)))

def position(dictt, hand, key):
    x = h2 + radiis[key] * math.cos(math.radians(dictt[hand]) - math.pi/2)
    y = w2 + radiis[key] * math.sin(math.radians(dictt[hand]) - math.pi/2)
    return x, y

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    
    t = datetime.now()
    hours, minute, second = t.hour % 12, t.minute, t.second

    pygame.draw.circle(screen, (50, 50, 50), (h2, w2), rad)
    pygame.draw.line(screen, pygame.Color('red'), (h2, w2), position(clock12, hours, 'hour'), 15)
    pygame.draw.line(screen, pygame.Color('orange'), (h2, w2), position(clock60, minute, 'min'), 10)
    pygame.draw.line(screen, pygame.Color('yellow'), (h2, w2), position(clock60, second, 'sec'), 5)
    pygame.draw.circle(screen, (255, 255, 255), (h2, w2), 8)



    pygame.display.flip()
    clock.tick(60)
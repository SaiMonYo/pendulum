import pygame
from pygame import gfxdraw
import math
import random
import time

# pygame colours
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
YELLOW = (255,255, 0)
ORANGE = (255, 69 ,0)
GREY  = ( 30, 30, 30)

WIDTH = 1920
HEIGHT = 1080

pygame.init()

FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

G = 0.9

m = 400

r = 100

a = math.pi/2

v = 0

aa = 0

points = []

startPos = (int(WIDTH / 2), int(HEIGHT / 2))
xoff, yoff = startPos

running = True

while running:
    #v *= 0.9996
    win.fill(BLACK)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    aa = -G * math.sin(a) / r
    v += aa
    a += v


    x = float(r * math.sin(a)+xoff)
    y = float(r * math.cos(a)+yoff)

    points.append((x, y))

    pygame.draw.line(win, WHITE, startPos, (x, y), 6)
    pygame.draw.circle(win, WHITE, (int(x), int(y)), int(m / 10))

    if len(points) > 2:
        pygame.draw.lines(win, WHITE, False, points)

    pygame.display.update()
    
    r += 0.5

    
pygame.quit()


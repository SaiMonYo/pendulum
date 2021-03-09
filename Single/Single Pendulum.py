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

# gravity constant
G = 0.9

# mass of ball
m = 400

# length of arm
r = 200

# starting angle
a = math.pi/2

# velocity
v = 0

# acceleration
aa = 0

# points for tracing
points = []

# where pendulum will be attatched
startPos = (int(WIDTH / 2), int(HEIGHT / 2))
xoff, yoff = startPos

running = True

while running:
    # dampening - more realistic stops it going for ever
    #v *= 0.9996

    # clearing screen
    win.fill(BLACK)
    # ticking FPS
    clock.tick(FPS)
    # clicks x button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # calculating angular acceration
    aa = -G * math.sin(a) / r
    # updating velocity
    v += aa
    # updating angle
    a += v

    
    x = r * math.sin(a)+xoff
    y = r * math.cos(a)+yoff

    points.append((x, y))

    # drawing pendulum
    pygame.draw.line(win, WHITE, startPos, (x, y), 6)
    pygame.draw.circle(win, WHITE, (int(x), int(y)), int(m / 10))

    # drawing path
    if len(points) > 2:
        pygame.draw.lines(win, WHITE, False, points)

    pygame.display.update()
    

    
pygame.quit()

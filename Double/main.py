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

G = 2

'''

θ1'' = 	−g (2 m1 + m2) sin θ1 − m2 g sin(θ1 − 2 θ2) − 2 sin(θ1 − θ2) m2 (θ2'2 L2 + θ1'2 L1 cos(θ1 − θ2))
        ________________________________________________________________________________________________
                            L1 (2 m1 + m2 − m2 cos(2 θ1 − 2 θ2))

                
θ2'' = 	2 sin(θ1 − θ2) (θ1'2 L1 (m1 + m2) + g(m1 + m2) cos θ1 + θ2'2 L2 m2 cos(θ1 − θ2))
        ________________________________________________________________________________
                            L2 (2 m1 + m2 − m2 cos(2 θ1 − 2 θ2))
'''
def ang_acc_1(m1, m2, L1, L2, a1, a2, v1, v2):
    # broken down above equations to form easier to manage chunks
    num1 = -G * (2 * m1 + m2) * math.sin(a1)
    num2 = -m2 * G * math.sin(a1 - 2 * a2)
    num3 = -2 * math.sin(a1-a2)
    num4 =  m2 * ((v2 * v2) * L2 + (v1 * v1) * L1 * math.cos(a1-a2))
    numerator = num1 + num2 + (num3 * num4)
    
    denominator = L1 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))

    return numerator/denominator

def ang_acc_2(m1, m2, L1, L2, a1, a2, v1, v2):

    num1 = 2 * math.sin(a1 - a2)
    num2 = (v1 * v1) * L1 * (m1 + m2) + G * (m1+ m2) * math.cos(a1) + (v2 * v2) * L2 * m2 * math.cos(a1-a2)

    numerator = num1 * num2
    
    denominator = L2 * (2 * m1 + m2 - m2 * math.cos(2 * a1 - 2 * a2))

    return numerator/denominator


WIDTH = 1920
HEIGHT = 1080

pygame.init()

FPS = 60
win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# mass 
m1 = 200
m2 = 200

# length
L1 = 200
L2 = 200

# angle
a1 = math.pi/2
a2 = math.pi/2

# angular veloctiy
v1 = 0
v2 = 0

# angular acceleration
aa1 = 0
aa2 = 0

# used for tracing path
points2 = []

startPos = (int(WIDTH/2) , int(HEIGHT/4))
xoff, yoff = startPos
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # clearing the screen
    win.fill(BLACK)
    delta = clock.tick(FPS) / 1000

    # calculating angular acceleration
    aa1 = ang_acc_1(m1, m2, L1, L2, a1, a2, v1, v2)
    aa2 = ang_acc_2(m1, m2, L1, L2, a1, a2, v1, v2)

    # calculating angular velocity based on angular acceleration
    v1 += aa1
    v2 += aa2

    # updating angle based on velocity
    a1 += v1
    a2 += v2

    # polar coordinates to work out where the pendulum end will be
    x1 = float(L1 * math.sin(a1)+xoff)
    y1 = float(L1 * math.cos(a1)+yoff)

    # polar coordinates to work out where the pendulum will be
    x2 = float(x1 + L2 * math.sin(a2))
    y2 = float(y1 + L2 * math.cos(a2))

    points2.append((x2, y2))

    # draw first pendulum
    pygame.draw.line(win, WHITE, startPos, (x1, y1), 6)
    pygame.draw.circle(win, WHITE, (int(x1), int(y1)), int(m1 / 10))
    # draw second pendulum
    pygame.draw.line(win, WHITE, (x1, y1), (x2, y2), 6)
    pygame.draw.circle(win, WHITE, (int(x2), int(y2)), int(m2 / 10))

    if len(points2) > 2:
        pygame.draw.lines(win, WHITE, False, points2)
        #if len(points2) > 500:
            #points2 = points2[1:]

    pygame.display.update()

    

#pygame.quit()

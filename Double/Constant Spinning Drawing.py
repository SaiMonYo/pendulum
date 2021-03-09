import pygame
from pygame import gfxdraw
import math
import random

# pygame colours
WHITE = (255,255,255)
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)
YELLOW = (255,255, 0)
ORANGE = (255, 69 ,0)
GREY  = ( 30, 30, 30)



# gravity
G = 9.8




class Pendulum():
    def __init__(self, win, centre, mass, length, angle, angVel, angAcc, drawPath = False):
        self.win = win
        
        self.w, self.h = self.win.get_size()


        self.centre = centre
        
        self.mass = mass
        self.length = length
        self.angle = angle
        self.angVel = angVel
        self.angAcc = angAcc

        self.drawPath = drawPath

        # where the ball is - or the end od the stick
        self.x, self.y = self.get_ballpos()

        self.points = []

    def get_ballpos(self):
        # polar coordinates
        xcoord = math.sin(self.angle) * self.length
        ycoord = math.cos(self.angle) * self.length

        endx = xcoord + self.centre[0]
        endy = -ycoord  + self.centre[1]

        return endx, endy

    def update_vel(self):
        self.angVel += self.angAcc

    def update_angle(self, delta):
        # adding vel to angle
        self.angle += self.angVel * delta
        self.x, self.y = self.get_ballpos()
        # adding points to draw for its trail
        self.points.append((self.x, self.y))

    def show(self):
        if len(self.points) > 2 and self.drawPath:
            pygame.draw.lines(self.win, (180, 180, 180), False, self.points, 2)
        
        pygame.draw.aaline(self.win, WHITE, self.centre, (self.x, self.y))

        pygame.draw.circle(self.win, WHITE, (int(self.x), int(self.y)), int(self.mass / 10))

        
    

WIDTH = 1000
HEIGHT = 1000

win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
clock = pygame.time.Clock()
win.fill(BLACK)

FPS = 144





def make_random_pens(n):
    pens = []
    for i in range(n):
        if i == 0:  
            pen = Pendulum(win, centre, 100, random.random() * 100, math.pi * 4 * random.random(), random.random() * 2, 0)
            pens.append(pen)
        elif i == n - 1:
            prevpen = pens[-1]
            pen = Pendulum(win, (prevpen.x, prevpen.y), 100, random.random() * 100, math.pi * 4 * random.random(), random.random() * 2, 0, True)
            pens.append(pen)
        else:
            prevpen = pens[-1]
            pen = Pendulum(win, (prevpen.x, prevpen.y), 100, random.random() * 100, math.pi * 4 * random.random(), random.random() * 2, 0)
            pens.append(pen)
    return pens

def make_flower_pens(petals, speed):
    pen1 = Pendulum(win, centre, 200, 200, math.pi * 4 * random.random(), speed, 0)
    pen2 = Pendulum(win, (pen1.x, pen1.y), 200, 200, math.pi * 4 * random.random(), -speed * (petals -1), 0, True)

    pens = [pen1, pen2]
    return pens

centre = WIDTH / 2, HEIGHT / 2

pens = make_flower_pens(5, 2)

pygame.display.update()

while True:
    delta = clock.tick(FPS) / 1000
    # termination when cross in pressed on pygame window
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
    win.fill(BLACK)
    for pen in pens:
        pen.update_vel()
    for i,pen in enumerate(pens):
        if i == 0:
            pen.update_angle(delta)
        else:
            pen.centre = (pens[i-1].x, pens[i-1].y)
            pen.update_angle(delta)

    
    for pen in pens[::-1]:
        pen.show()

    pygame.display.update()



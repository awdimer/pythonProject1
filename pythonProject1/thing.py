import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '0,0'
import pgzrun
from pgzhelper import *
import random

WIDTH = 1000
zombie = Actor("zombie",center = (100,100), anchor=('center','center'))

HEIGHT = 1000
correction_angle = 90
player = Actor("player", center =(100,100), anchor=('center','center'))

gravity = 3
move_ticker = 0
mx,my = pygame.mouse.get_pos()
zombieAlive = False
zombieWait= 100
zombieDraw = False





def update():
    global velocity,gravity,velocity1,event,run,window,mouse,player_rect,angle,player_pos,mx,my
    keys = pygame.key.get_pressed()
    event = pygame.event.get()
    mx,my = pygame.mouse.get_pos()
    player.scale = 1

    zombierotate()
    zombieSpawn()

    if keys[pygame.K_LEFT]:
        if player.x > 0:
            player.x -= 5
    if keys[pygame.K_RIGHT]:
        if player.x < 1000:
            player.x += 5
    if keys[pygame.K_UP]:
        if player.y > 0:
            player.y -= 10
    if keys[pygame.K_DOWN]:
        if player.y < 1000:
            player.y += 5

def rotate(player,mx,my):
    player.rect = pygame.transform.rotate(player.rect,mx,my)

def on_mouse_move(pos):
    player.angle = player.angle_to(pos)

def on_mouse_down():
    print()

class enemy(object):
    def __init__(self, x, y,end,img):
        self.x = x
        self.y = y
        self.path = [x, end]
        self.walkCount = 0
        self.vel = 3
        self.img = Actor("zombie")

    def draw(self):
        self.move()






    def move(self):
        if self.vel > 0:  # If we are moving right
            if self.x < self.path[1] + self.vel:  # If we have not reached the furthest right point on our path.
                self.x += self.vel
            else:  # Change direction and move back the other way
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0
        else:  # If we are moving left
            if self.x > self.path[0] - self.vel:  # If we have not reached the furthest left point on our path
                self.x += self.vel
            else:  # Change direction
                self.vel = self.vel * -1
                self.x += self.vel
                self.walkCount = 0


def rotate1(zombie,mx,my):
    zombie.rect = pygame.transform.rotate(zombie.rect,mx,my)


def zombierotate():
    print()
    zombie.angle = zombie.angle_to(player)


def zombieSpawn():
    global zombieAlive,zombieDraw
    if zombieAlive == False:
        pygame.time.delay(1000000)
        zombieAlive = True
    if zombieAlive == True:
        zombie.x = random.randint(50,500)
        zombie.y = random.randint(50,500)
        zombieDraw = True






def draw():
    screen.clear()
    player.draw()
    if zombieDraw == True:
        zombie.draw()


pgzrun.go()

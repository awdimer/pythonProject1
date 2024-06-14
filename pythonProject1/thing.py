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
bullet = Actor("bullet",center =(100,100), anchor=('center','center'))
bulletPointx = 0
bulletPointy = 0
bulletDraw = False
gravity = 3
move_ticker = 0
mx,my = pygame.mouse.get_pos()
zombieAlive = False
zombieWait = 100
zombieDraw = False
zombieAlive1 = True
zombieSpeed = 1
playerHealth = 3
bulletVelocity = 5
dx,dy = pygame.mouse.get_pos()
def update():
    global velocity,gravity,velocity1,event,run,window,mouse,player_rect,angle,player_pos,mx,my
    keys = pygame.key.get_pressed()
    event = pygame.event.get()
    mx,my = pygame.mouse.get_pos()
    player.scale = 1
    bullet.scale = .1
    player.angle = round(player.angle)
    print(player.angle)
    zombieRotate()
    zombieSpawn()
    zombieMove()
    checkCollide()


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

def rotate3(bullet,mx,my):
    bullet.rect = pygame.transform.rotate(bullet.rect,mx,my)

def on_mouse_move(pos):
    player.angle = player.angle_to(pos)

def on_mouse_down(pos):
    global bulletPointx,bulletPointy
    global bulletDraw
    bulletPointx, bulletPointy = pygame.mouse.get_pos()
    bulletDraw = True
    bulletMove()

def bulletMove():
    global dx, dy
    bullet.x = player.x
    bullet.y = player.y
    bullet.angle = player.angle
    bullet.angle = round(0)
    dx,dy = pygame.mouse.get_pos()
    if dx != bullet.x:
        if dx > bullet.x:
            bullet.x = bullet.x + bulletVelocity
        if dx < bullet.x:
            bullet.x = bullet.x - bulletVelocity
    if dy != bullet.y:
        if dy > bullet.y:
            bullet.y = bullet.y + bulletVelocity
        if dy < bullet.y:
            bullet.y = bullet.y - bulletVelocity

def rotate1(zombie,mx,my):
    zombie.rect = pygame.transform.rotate(zombie.rect,mx,my)


def zombieRotate():
    zombie.angle = zombie.angle_to(player)


def zombieSpawn():
    global zombieAlive,zombieDraw,zombieAlive1
    if zombieAlive == False:
        zombieAlive = True

    if zombieAlive == True and zombieAlive1 == True:
        zombie.x = random.randint(50,500)
        zombie.y = random.randint(50, 500)
        if zombie.x == player.x and zombie.y == player.y:
            zombieSpawn()

        zombieDraw = True
        zombieAlive1 = False



def zombieMove():
    global zombieSpeed1
    if player.x != zombie.x:
        if player.x > zombie.x:
            zombie.x = zombie.x + zombieSpeed
        if player.x < zombie.x:
            zombie.x = zombie.x - zombieSpeed
    if player.y != zombie.y:
        if player.y > zombie.y:
            zombie.y = zombie.y + zombieSpeed
        if player.y < zombie.y:
            zombie.y = zombie.y - zombieSpeed
def checkCollide():
    if player.collidepoint(zombie.x,zombie.y):
        playerHit()

def playerHit():
    global playerHealth,zombieAlive,zombieDraw
    playerHealth -= 1
    zombieAlive = False
    zombieDraw = False


def draw():
    screen.clear()
    player.draw()
    if zombieDraw == True:
        zombie.draw()
    if bulletDraw == True:
        bullet.draw()

pgzrun.go()

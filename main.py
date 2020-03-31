import pygame
import random
import math
from pygame import mixer


pygame.init()
# screen
screen = pygame.display.set_mode((800, 600))
#background music
mixer.music.load("background.wav")
mixer.music.play(-1)
# TITLE AND ICON
pygame.display.set_caption("DRAGNOWAR")
icon = pygame.image.load('asteroid.png')
pygame.display.set_icon(icon)
# player
playerimage = pygame.image.load('ufo (2).png')
playerX = 370
playerY = 480
playerX_change = 0
# ENEMY

ENEimage =[]
ENEX = []
ENEY=[]
ENEX_change =[]
ENEY_change =[]
num=7
for i in range(num):
    ENEimage.append(pygame.image.load('dragon.png'))
    ENEX.append(random.randint(0, 735))
    ENEY.append(random.randint(50, 150))
    ENEX_change.append(4)
    ENEY_change.append(40)
# bullet
# ready=u cant see the bullet on the screen
# fire -the bullet is moving
bulletimage = pygame.image.load('bullet (1).png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

# background
bgd = pygame.image.load('79261.jpg')
#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
#gameovertezt
fontover = pygame.font.Font('freesansbold.ttf',64)

def show_score(x, y):
    score = font.render("Score :"+str(score_value),True, (255,255,255))
    screen.blit(score, (x, y))
def game_over_text():
    OVER = fontover.render("GAME OVER ", True, (255, 255, 255))
    screen.blit(OVER, (200, 250))
def player(x, y):
    screen.blit(playerimage, (x, y))


def enemy(x, y, i):
    screen.blit(ENEimage[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimage, (x + 16, y + 10))


def collision(ENEX, ENEY, bulletX, bulletY):
    distance = math.sqrt((math.pow(ENEX - bulletX, 2)) + (math.pow(ENEY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


# GAME LOOP
running = True
while running:
    screen.fill((255, 0, 0))
    screen.blit(bgd, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # key direction
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    b_sound =mixer.Sound('laser.wav')
                    b_sound.play()
                    bulletX = playerX
                    fire_bullet(playerX, bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    for i in range(num):
        #gameover
        if ENEY[i] >=440 :
            for j in range(num):
                ENEY[j] =2000
                game_over_text()
                break
        ENEX[i] += ENEX_change[i]
        if ENEX[i] <= 0:
            ENEX_change[i] = 4
            ENEY[i] += ENEY_change[i]
        elif ENEX[i] >= 736:
            ENEX_change[i] = -4
            ENEY[i] += ENEY_change[i]
            # collision
        collis = collision(ENEX[i], ENEY[i], bulletX, bulletY)
        if collis:
            e_sound=mixer.Sound('explosion.wav')
            e_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            ENEX[i] = random.randint(0, 735)
            ENEY[i] = random.randint(50, 150)
        enemy(ENEX[i],ENEY[i],i)
        # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change


    player(playerX, playerY)
    show_score(textX, textY)
    # enemy(ENEX, ENEY)
    pygame.display.update()

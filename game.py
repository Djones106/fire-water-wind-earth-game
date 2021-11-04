# Fire, Water, Wind, Earth Game
import pygame
import random
import math
#iniating the game
pygame.init()

#creating game window
screen = pygame.display.set_mode((800, 600))

#background image
background = pygame.image.load('background.png')
#Title and Icon 
pygame.display.set_caption('Fire, Air, Earth, Water')

#Elements
fireIcon = pygame.image.load('05_Fire_III.png')

fireX = 370
fireY = 480
fireX_change = 0
#Enemy
enemyImg = pygame.image.load('78_Darkness_Armor.png')

enemyX = random.randint(0, 735)
enemyY = random.randint(50, 150)
enemyX_change = 3
enemyY_change = 40

#Fireball
#Ready - You can't see the fireball on the screen
#Fire - The fireball is currently moving
fireballImg = pygame.image.load('02_Fire_Element.png')

fireballX = 0
fireballY = 480
fireballX_change = 0
fireballY_change = 10
fireball_state = "ready"

score = 0

#for movement
def fire (x,y):
    screen.blit(fireIcon, [x, y])

def enemy (x,y):
    screen.blit(enemyImg, [x, y])

def fire_fireball(x,y):
    global fireball_state
    fireball_state = "fire"
    screen.blit(fireballImg, (x,y))

def isCollision(enmeyX, enemyY, fireballX, fireballY):
    distance = math.sqrt((math.pow(enemyX-fireballX,2)) + (math.pow(enemyY-fireballY,2)))
    if distance < 27:
        return True
    else:
        return False

#Game Loop
run = True
while run:
    #RGB - Red, Green, Blue    
    screen.fill((211,211,211))
    #background image
    screen.blit(background, (0,0))
    
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT: #need to be in all caps
            run = False
        # if keystroke is pressed check wheter its right or left

        if event.type == pygame.KEYDOWN:            
            if event.key == pygame.K_LEFT:
                fireX_change = -3
            if event.key == pygame.K_RIGHT:
                fireX_change = 3
            if event.key == pygame.K_SPACE:
                if fireball_state is "ready":
                    fireballX = fireX
                    fire_fireball(fireballX, fireballY)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                fireX_change = 0
    
    #Checking for boundries of spaceship so it doesn't go out of bounds   
    fireX += fireX_change
    if fireX <= 0:
        fireX = 0
    elif fireX >= 780:
        fireX = 780

    #Enemy movement
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change
    elif enemyX >= 780:
        enemyX_change = -4
        enemyY += enemyY_change

    #Fireball Movement
    if fireballY <=0:
        fireballY =480
        fireball_state = "ready"

    if fireball_state is "fire":
        fire_fireball(fireballX, fireballY)
        fireballY -= fireballY_change

    #Collision
    collision = isCollision(enemyX, enemyY, fireballX, fireballY)
    if collision:
        fireballY = 480
        fireball_state = "ready"
        score += 10
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    fire(fireX, fireY)
    enemy(enemyX, enemyY)
    pygame.display.update()    


pygame.quit()

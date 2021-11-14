# Fire, Water, Wind, Earth Game
import pygame
import random
import math
from pygame import mixer


#iniating the game
pygame.init()

#creating game window
screen = pygame.display.set_mode((800, 600))

#background image
background = pygame.image.load('img/background.png')

#Background sound
mixer.music.load('background.mp3')
mixer.music.play(-1)

#Title and Icon 
pygame.display.set_caption('Fire Blaster')

#Elements

fireIcon = pygame.image.load('img/05_Fire_III.png')


fireX = 370
fireY = 480
fireX_change = 0
#Enemy
enemyImg = []
enemyX =[]
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('img/78_Darkness_Armor.png'))
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(50, 150))
    enemyX_change.append(3)
    enemyY_change.append(40)

#Fireball
#Ready - You can't see the fireball on the screen
#Fire - The fireball is currently moving
fireballImg = pygame.image.load('img/02_Fire_Element.png')

fireballX = 0
fireballY = 480
fireballX_change = 0
fireballY_change = 10
fireball_state = "ready"

# Score
score_value = 0
font = pygame.font.Font('Manokwary.ttf', 32)

textX = 10
textY = 10

#Game Over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (0,0,0))
    screen.blit(over_text, (200, 250))

#for movement
def fire (x,y):
    screen.blit(fireIcon, [x, y])

def enemy (x,y,i):
    screen.blit(enemyImg[i], [x, y])

def fire_fireball(x,y):
    global fireball_state
    fireball_state = "fire"
    screen.blit(fireballImg, (x,y))

def isCollision(enemyX, enemyY, fireballX, fireballY):
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
                    fireball_Sound = mixer.Sound('Swoosh.wav')
                    fireball_Sound.play()
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
    for i in range(num_of_enemies):

        #Game Over
        if enemyY[i] > 450:
            for i in range(num_of_enemies):
                enemyY[i] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 780:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        
        #Collision
        collision = isCollision(enemyX[i], enemyY[i], fireballX, fireballY)
        if collision:
            explosion_Sound = mixer.Sound('pop8.wav')
            explosion_Sound.play()
            fireballY = 480
            fireball_state = "ready"
            score_value += 10
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i], enemyY[i], i)

    #Fireball Movement
    if fireballY <=0:
        fireballY =480
        fireball_state = "ready"

    if fireball_state is "fire":
        fire_fireball(fireballX, fireballY)
        fireballY -= fireballY_change

    

    fire(fireX, fireY)
    show_score(textX, textY)
    pygame.display.update()    


pygame.quit()

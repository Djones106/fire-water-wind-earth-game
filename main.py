import pygame
from pygame.constants import MOUSEBUTTONDOWN
import button
import random
from pygame import mixer

#Iniating the game
pygame.init()
#Creating Game Window
screen = pygame.display.set_mode((800, 600))

#Background Image
#Window Title
pygame.display.set_caption('Fire, Water, Wind, Earth')

#Instructions 
start_background = pygame.image.load('start_img.png')
start_img = pygame.image.load('startbtn.png')
exit_img = pygame.image.load('exit.png')

#Game Background Image
background = pygame.image.load('background.png')

#Background Sound
mixer.music.load('background.mp3')
mixer.music.play(-1)

#Elements Button Image
fireIcon = pygame.image.load('02_Fire_Element.png')
waterIcon = pygame.image.load('50_Water_Element.png')
earthIcon = pygame.image.load('34_Earth_Element.png')
airIcon = pygame.image.load('18_Air_Element.png')

#Element Choice Image
fireElement = pygame.image.load('05_Fire_III.png')
waterElement = pygame.image.load('53_Water_III.png')
earthElement = pygame.image.load('37_Earth_III.png')
airElement = pygame.image.load('21_Air_III.png')

#Create button instances
start_button =button.Button(450,500, start_img, 1)
exit_button =button.Button(650,500, exit_img, 1)
fire_button =button.Button(250, 450, fireIcon, 2)
water_button =button.Button( 350, 450, waterIcon, 2)
earth_button =button.Button(450, 450, earthIcon,2)
air_button =button.Button(550, 450, airIcon, 2)

#Define Game Variables
pl_score = 0
cp_score = 0
i = 0 

start_game = False    

#Game Loop
run = True
while run:
    if start_game == False:
        #Draw Start Menu
        screen.blit(start_background, (0,0))
        #Add Buttons
        if start_button.draw(screen):
            start_game = True

                    #Game Window
            screen.blit(background, (0,0))    
            fire_button.draw(screen)
            water_button.draw(screen)
            earth_button.draw(screen)
            air_button.draw(screen)
        if exit_button.draw(screen):
            run = False



    for event in pygame.event.get():
        #Quit Game
        if event.type == pygame.QUIT:
            run = False

            #Click Event
        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked = event.pos
            action = False
            if fire_button.rect.collidepoint(clicked):
                if pygame.mouse.get_pressed()[0] == 1 and clicked == False:
                    clicked = True
                    action = True
                print('fire')
           
        
    pygame.display.update()

pygame.quit()

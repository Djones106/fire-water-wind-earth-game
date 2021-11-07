import pygame
from pygame.constants import MOUSEBUTTONDOWN
import button
import random
from pygame import mixer

#Iniating the game
pygame.init()

#Creating Game Window
screen = pygame.display.set_mode((800, 600))

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

class GameObject:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw_object(self):
        self.rect = pygame.Surface.blit(self.image)

#Declares Objects
fire = GameObject(100, 100, fireElement, 3)
water = GameObject(100, 100, waterElement, 3)
earth = GameObject(100, 100, earthElement, 3)
air = GameObject(100, 100, airElement, 3)

cp_fire = GameObject(100, 100, fireElement, 3)
cp_water = GameObject(100, 100, waterElement, 3)
cp_earth = GameObject(100, 100, earthElement, 3)
cp_air = GameObject(100, 100, airElement, 3)


#Define Game Variables

choices = [fire, water, earth, air, cp_fire, cp_water, cp_earth, cp_air]

pl_score = 0
cp_score = 0


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
        if exit_button.draw(screen):
            run = False
    else:
        #Game Window
        screen.blit(background, (0,0))    
        fire_button.draw(screen)
        water_button.draw(screen)
        earth_button.draw(screen)
        air_button.draw(screen)

        
                

    for event in pygame.event.get():
        #Quit Game
        if event.type == pygame.QUIT:
            run = False
        
        #Click Event
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            if mouse[0] in range(250,350):
                fire_button = True
                fire.draw(screen)
            elif mouse[0] in range(350,450):
                print("Water")
            elif mouse[0] in range (450,550):
                print("Earth")
            else: 
                mouse[0] in range(550,650)
                print("Wind")
        
              
                    

    
    
  
    pygame.display.update()        

pygame.quit()
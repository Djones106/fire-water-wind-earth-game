import pygame
import button
from pygame import mixer

#Iniating the game
pygame.init()

#Creating Game Window
screen = pygame.display.set_mode((800, 600))

#Background Image
background = pygame.image.load('background.png')

#Background Sound
mixer.music.load('background.mp3')
mixer.music.play(-1)

#Window Title
pygame.display.set_caption('Fire, Air, Earth, Water')

#Instructions 
start_img = pygame.image.load('start_img.png')
#Elements Imagae
fireIcon = pygame.image.load('02_Fire_Element.png')
waterIcon = pygame.image.load('50_Water_Element.png')
earthIcon = pygame.image.load('34_Earth_Element.png')
airIcon = pygame.image.load('18_Air_Element.png')

#Create button instances
fire_button = button.Element(250, 450, fireIcon, 2)
water_button = button.Element( 350, 450, waterIcon, 2)
earth_button = button.Element(450, 450, earthIcon,2)
air_button = button.Element(550, 450, airIcon, 2)

#Define Game Variables
start_game = False

#Game Loop
run = True
while run:
    #if start_game == False:
        #Draw Menu

   
    screen.blit(background, (0,0))    
    fire_button.draw(screen)
    water_button.draw(screen)
    earth_button.draw(screen)
    air_button.draw(screen)
                

    for event in pygame.event.get():
        #Quit Game
        if event.type == pygame.QUIT:
            run = False
    
    
  
    pygame.display.update()        

pygame.quit()
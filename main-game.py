import pygame
from pygame.constants import MOUSEBUTTONDOWN
import button
import random
from pygame import mixer
import time, os, sys

  
#Iniating the game

#Creating Game Window

#Window Title

#Game clock


#Instructions -- Start Menu --
start_background = pygame.image.load('start_img.png')
start_img = pygame.image.load('startbtn.png')
exit_img = pygame.image.load('exit.png')

#Game Background Image
background = pygame.image.load('background.png')

#Background Sound
mixer.music.load('background.mp3')
mixer.music.play(-1)

# ---Assets ---

#Font
pygame.font.init()
font = pygame.font.Font('Manokwary.ttf', 64)
text_pos = (500,500)

font_blk = [0,0,0]
font_red = [255,0,0]
font_wht = [255,255,255]



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
player_score = 0
computer_score = 0

def Fire_Water_Wind_Earth():
    os.environ['SDL_VIDEO_CENTERED'] = 'True'
    i = -1
    
    #Creating Game Window
    main()



def main(i, player_score, computer_score, screen):
    #Iniating the game
    pygame.init()
    start_game = False 
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Fire, Water, Wind, Earth')
    #Main Game Screen Actions
    text = font.render("Choose Element", 1, font_blk)
    textpos = text.get_rect()
    textpos.centerx = screen.get_rect().centerx
    textpos.centery = (screen.get_rect().centery)/4

    pl_score = font.render("Your Score: "+ str(player_score), 1, font_blk)
    pl_score_pos = pl_score.get_rect()

    cp_score = font.render("Elemental's Score : " +str(computer_score), 1, font_blk)
    cp_score_pos = cp_score.get_rect()

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
            screen.blit(text, textpos)
            screen.blit(pl_score,pl_score_pos)
            screen.blit(cp_score)

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
        clock = pygame.time.Clock() 
if __name__ == '__main__':
    
    pygame.quit()       
                

    

  


# Fire, Water, Wind, Earth Game
import pygame
from random import randint
#iniating the game
pygame.init()

#creating game window
screen_width = 800
screen_height = int(screen_width * 0.8)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Fire Water Wind Earth')

#running the game
run = True
while run:

    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT:
            run = False
pygame.quit()

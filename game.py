# Fire, Water, Wind, Earth Game
import pygame

#iniating the game
pygame.init()

#creating game window
screen = pygame.display.set_mode((800, 600))
#Title and Icon 
pygame.display.set_caption('Fire, Air, Earth, Water')

#Elements
fireIcon = pygame.image.load('02_Fire_Element.png')

fireX = 300
fireY = 480

def fire ():
    screen.blit(fireIcon, [fireX, fireY])

#Game Loop
run = True
while run:
    #RGB - Red, Green, Blue    
    screen.fill((211,211,211))
    for event in pygame.event.get():
        #quit game
        if event.type == pygame.QUIT: #need to be in all caps
            run = False
  
    fire()

    pygame.display.update()    


pygame.quit()

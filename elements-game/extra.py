class Game():
    def __init__(self):
        self.start_button =button.Button(450,500, start_img, 1)
        self.exit_button =button.Button(650,500, exit_img, 1)
        self.fire_button =button.Button(250, 450, fireIcon, 2)
        self.water_button =button.Button( 350, 450, waterIcon, 2)
        self.earth_button =button.Button(450, 450, earthIcon,2)
        self.air_button =button.Button(550, 450, airIcon, 2)
        self.fire = button.Button(100,100, fireElement, 3)
    
    def player(self):
        if self.fire_button.clicked(30):
            self.p_opition = "fire"
            self.screen.blit(fire) 
        elif self.water_button.clicked(30):
            self.p_option = "water"
            self.screen.blit(waterElement, (100,100))
        elif self.earth_button.clicked(30):
            self.p_option = "earth"
            self.screen.blit(earthElement, (100,100))
        else:
            self.air_button.clicked(30)
            self.p_option = "air"
            self.screen.blit(airElement, (100,100))
        
        return self.p_option



choices = [fire, water, earth, air, cp_fire, cp_water, cp_earth, cp_air]

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


#Game Loop
run = True
while run:
    
   
        
        #Click Event
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse = pygame.mouse.get_pos()
        if mouse[0] in range(250,350):
            fire_button = True
            
        elif mouse[0] in range(350,450):
            print("Water")
        elif mouse[0] in range (450,550):
            print("Earth")
        else: 
            mouse[0] in range(550,650)
            print("Wind")

       
              
   
               

     
    
  
       
Fire_Water_Wind_Earth()
pygame.quit()
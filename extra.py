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




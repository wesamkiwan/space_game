class Settings:


    def __init__(self) :
        
        #screen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(0,0,0)
        #ship settings
        self.ship_speed=5
        self.ship_limit=2
        #bullet settings
        self.bullet_color=(255,88,4)
        self.bullet_height=15
        self.bullet_width=3
        self.bullet_speed=4.0
        self.max_bullets=6
        #enemies settings
        self.enemy_speed=10.0
        self.enemies_drop_speed=10
        self.fleet_direction=1    #1 means right and -1 means left
        
    
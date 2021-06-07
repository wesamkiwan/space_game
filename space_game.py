import pygame
import sys
<<<<<<< HEAD
from settings import Settings
from ship import Ship
=======

>>>>>>> 9116cfc9efdc978c0c73a36e292b872ec9b7dde9


class SpaceGame:
    def __init__(self):
        pygame.init()
<<<<<<< HEAD
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("Space Game")
        self.ship=Ship(self)        
=======
        self.screen=pygame.display.set_mode((1200,800))
        self.bg_color=(230,230,230)
>>>>>>> 9116cfc9efdc978c0c73a36e292b872ec9b7dde9

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            
<<<<<<< HEAD
            self.screen.fill(self.settings.bg_color)
            self.ship.draw_ship()
=======
            self.screen.fill(self.bg_color)
>>>>>>> 9116cfc9efdc978c0c73a36e292b872ec9b7dde9
            pygame.display.flip()
        
if __name__=='__main__':
    sg=SpaceGame()
    sg.run_game()
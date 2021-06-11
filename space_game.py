import pygame
import sys

from pygame.constants import KEYDOWN
from settings import Settings
from ship import Ship


class SpaceGame:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("Space Game")
        self.ship=Ship(self)        

    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self.update_screen()
            


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        pygame.display.flip()
            
            
            
            
    def check_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type==pygame.KEYDOWN:
                self._check_keydown_events(event)

                
            elif event.type==pygame.KEYUP:
                self._check_keyup_events(event)

                

    def _check_keydown_events(self,event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=True
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=True

            

    def _check_keyup_events(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False


            
        
if __name__=='__main__':
    sg=SpaceGame()
    sg.run_game()
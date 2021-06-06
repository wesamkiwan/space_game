import pygame
import sys



class SpaceGame:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        self.bg_color=(230,230,230)

    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            
            self.screen.fill(self.bg_color)
            pygame.display.flip()
        
if __name__=='__main__':
    sg=SpaceGame()
    sg.run_game()
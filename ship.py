import pygame

class Ship:
    def __init__(self, my_game):
        self.screen=my_game.screen
        self.settings=my_game.settings 
        self.screen_rect=my_game.screen.get_rect()
        self.image=pygame.image.load('images/ship.png')
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom
        self.x=float(self.rect.x)

        self.moving_right=False
        self.moving_left=False

        




    def update(self):
        if self.moving_right:
            self.rect.x+=1
        if self.moving_left:
            self.rect.x-=1

    def draw_ship(self):
        self.screen.blit(self.image, self.rect)
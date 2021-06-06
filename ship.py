import pygame

class Ship:
    def __init__(self, my_game):
        self.screen=my_game.screen 
        self.screen_rect=my_game.get_rect()
        self.image=pygame.image.load("images/ship.bmp")
        self.rect=self.image.get_rect()
        self.rect.midbottom=self.screen_rect.midbottom

    def draw_ship(self):
        self.screen.blit(self.image, self.rect)
import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, SpaceGame):
        super().__init()
        self.screen=SpaceGame.screen
        self.image=pygame.image.load('images/enemy1.pmb')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)
        
import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, SpaceGame):
        super().__init__()
        self.screen=SpaceGame.screen
        self.settings=SpaceGame.settings
        self.image=pygame.image.load('images/enemy1.png')
        self.rect=self.image.get_rect()
        self.rect.x=self.rect.width
        self.rect.y=self.rect.height
        self.x=float(self.rect.x)

    def update(self):
        self.x+=self.settings.enemy_speed
        self.rect.x=self.x

import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,SpaceGame):
        super().__init__()
        self.screen=SpaceGame.screen
        self.settings=SpaceGame.settings
        self.color=self.settings.bullet_color

        self.rect=pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet.height)
        self.rect.midtop=SpaceGame.ship.rect.midtop

        self.y=float(self.rect.y)
        

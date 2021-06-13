import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self,SpaceGame):
        super().__init__()
        self.screen=SpaceGame.screen
        self.settings=SpaceGame.settings
        self.color=self.settings.bullet_color

        self.rect=pygame.Rect(0,0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop=SpaceGame.ship.rect.midtop

        self.y=float(self.rect.y)
    

    def update(self):
        self.y-=self.settings.bullet_speed                     #change the bullet's y-coordination according to the bullet_speed (the origin point in pygame is the top left corner)
        self.rect.y=self.y                                     #change the y position of bullet's rectangle


    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)


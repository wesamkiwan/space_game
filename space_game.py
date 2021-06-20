import pygame
import sys
from bullet import Bullet

from pygame.constants import KEYDOWN
from settings import Settings
from ship import Ship

from enemy import Enemy



class SpaceGame:
    def __init__(self):
        pygame.init()
        self.settings=Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        pygame.display.set_caption("Space Game")
        self.ship=Ship(self)
        self.bullets=pygame.sprite.Group()
        self.enemies=pygame.sprite.Group()
        self._create_fleet()


    def run_game(self):
        while True:
            self.check_events()
            self.ship.update()
            self._update_bullets()
            self.update_screen()


    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom<=0:
                self.bullets.remove(bullet)

    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.draw_ship()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.enemies.draw(self.screen)                  

        pygame.display.flip()

    def _create_fleet(self):
        enemy=Enemy(self)
        enemy_width, enemy_height=enemy.rect.size
        available_space_x=self.settings.screen_width - (2*enemy_width)
        ship_height=self.ship.rect.height
        available_space_y=(self.settings.screen_height-(3*enemy_height)-ship_height)
        number_rows=available_space_y//(2*enemy_height)
        number_enemies_x=available_space_x // (2*enemy_width)
        for row in range(number_rows-2):
            for enemy_number in range(number_enemies_x):
                self._create_enemy(enemy_number, row)

    def _create_enemy(self, enemy_number, row):
            enemy=Enemy(self)
            enemy_width, enemy_height=enemy.rect.size          
            enemy.x=enemy_width+2*enemy_width*enemy_number
            enemy.rect.x=enemy.x
            enemy.rect.y=enemy.rect.height+(2*enemy.rect.height*row)
            self.enemies.add(enemy)

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
        elif event.key==pygame.K_q:
            sys.exit()
        elif event.key==pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key==pygame.K_RIGHT:
            self.ship.moving_right=False
        elif event.key==pygame.K_LEFT:
            self.ship.moving_left=False

    def _fire_bullet(self):
        if len(self.bullets)<self.settings.max_bullets:
            new_bullet=Bullet(self)
            self.bullets.add(new_bullet)


            
        
if __name__=='__main__':
    sg=SpaceGame()
    sg.run_game()
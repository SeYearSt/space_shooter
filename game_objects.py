import pygame
from settings import *

class Plasmoid(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Plasmoid,self).__init__()

class Player(pygame.sprite.Sprite):
    max_speed = 10
    def __init__(self):
        super(Player,self).__init__()

        self.image = pygame.image.load("pictures/player.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.current_speed = - self.max_speed
        elif keys[pygame.K_RIGHT]:
            self.current_speed = self.max_speed
        else:
            self.current_speed = 0

        self.rect.move_ip((self.current_speed,0))
                 
class Background(pygame.sprite.Sprite):
    
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load("pictures/background2.png")
        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT

        
    def update(self):
        self.rect.bottom +=5

        if self.rect.bottom >= self.rect.height:
            self.rect.bottom = HEIGHT

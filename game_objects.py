import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()

        self.image = pygame.image.load("pictures/player.png")
        self.rect = self.image.get_rect()

        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10


    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            print("left")
        if keys[pygame.K_RIGHT]:   
            print("RIGHT")

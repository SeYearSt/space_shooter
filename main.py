import sys
import pygame
from game_objects import *
from settings import *

pygame.init()
pygame.display.set_caption("Hello, World!")

screen = pygame.display.set_mode(SIZE)


#Game objects
player = Player()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    
    screen.fill(BACKGROUND_COLOR)
    
    player.update()
    
    screen.blit(player.image,player.rect)
    
    pygame.display.flip()

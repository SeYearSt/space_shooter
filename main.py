import sys
import pygame
from game_objects import *
from settings import *

pygame.init()
pygame.display.set_caption("Hello, World!")

screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

#Game objects
background = Background()
player = Player()



#Groups
all_objects = pygame.sprite.Group()

all_objects.add(background)
all_objects.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    
    screen.fill(BACKGROUND_COLOR)
    
    all_objects.update()

    all_objects.draw(screen)
    
    
    pygame.display.flip()
    clock.tick(30)

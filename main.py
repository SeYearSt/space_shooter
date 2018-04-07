
from game_objects import *
from settings import *

pygame.init()
pygame.display.set_caption("Space shooter!")

screen = pygame.display.set_mode(SIZE)

clock = pygame.time.Clock()

#Groups
plasmoids = pygame.sprite.Group()
all_objects = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

#Game objects
background = Background()
player = Player(clock,plasmoids)

all_objects.add(background)
all_objects.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
    
    screen.fill(BACKGROUND_COLOR)

    all_objects.update()
    plasmoids.update()

    all_objects.draw(screen)
    plasmoids.draw(screen)

    pygame.display.flip()
    clock.tick(30)

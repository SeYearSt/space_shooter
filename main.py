import pygame
from game_objects import *
from settings import *

clock = pygame.time.Clock()




#Groups
bullets = pygame.sprite.Group()
all_objects = pygame.sprite.Group()
asteroids = pygame.sprite.Group()

#Game objects
background = Background()
player =  Player(clock,bullets)
game_over = GameOver()

#adding in groups
all_objects.add(background)
all_objects.add(player)


def main ():
    GAME_OVER = False

    pygame.init()
    pygame.display.set_caption("Space shooter!")

    screen = pygame.display.set_mode(SIZE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return 0

        screen.fill(BACKGROUND_COLOR)

        Asteroid.process_asteroids(clock,asteroids)

        pygame.sprite.groupcollide(bullets, asteroids, True,True)

        for el in list(asteroids):
            if pygame.sprite.collide_rect(player,el):
                all_objects.remove(player)
                GAME_OVER = True


        all_objects.update()
        bullets.update()
        asteroids.update()

        all_objects.draw(screen)
        asteroids.draw(screen)
        bullets.draw(screen)
        if GAME_OVER:
            screen.blit(game_over.image,game_over.rect)
        pygame.display.flip()

        clock.tick(30)

main()


import pygame
import random
from settings import *


class Player(pygame.sprite.Sprite):
    speed_x = 10
    speed_y = 12
    shooting_limit = 200
    current_shooting = 0

    def __init__(self, clock,Bullets_group):
        self.clock = clock

        self.Bullets_group = Bullets_group

        super(Player, self).__init__()

        self.image = pygame.image.load(PLAYER_PICTURE_NAME)

        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT - 10
        self.rect.centerx = WIDTH // 2


    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.centerx -= self.speed_x

        if keys[pygame.K_RIGHT] and self.rect.right < WIDTH:
            self.rect.centerx += self.speed_x

        if keys[pygame.K_UP] and self.rect.top >0:
            self.rect.bottom -= self.speed_y

        if keys[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
            self.rect.bottom += self.speed_y

        self.shooting()

    def shooting(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.current_shooting <=0:
            self.Bullets_group.add(Bullet(self.rect.centerx, self.rect.top))
            self.current_shooting = self.shooting_limit
        else:
            self.current_shooting -= self.clock.get_time()


class Bullet(pygame.sprite.Sprite):
    def __init__(self,position_x,position_y,speed = 20):

        self.speed = speed

        super(Bullet,self).__init__()

        self.image = pygame.image.load(BULLET_NAME)

        self.rect = self.image.get_rect()

        self.rect.centerx = position_x
        self.rect.bottom = position_y

    def update(self):

        self.rect.bottom -= self.speed

        if self.rect.bottom < 0:
            del self


class Background(pygame.sprite.Sprite):
    def __init__(self):
        super(Background, self).__init__()

        self.image = pygame.image.load(BACKGROUND_PICTURE_NAME)

        self.rect = self.image.get_rect()

        self.rect.bottom = HEIGHT

    def update(self):
        self.rect.bottom += 5

        if self.rect.bottom >= self.rect.height:
            self.rect.bottom = HEIGHT

class GameOver(pygame.sprite.Sprite):
    def __init__(self):
        super(GameOver,self).__init__()

        self.image = pygame.image.load(GAME_OVER_NAME)

        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH // 2
        self.rect.centery = HEIGHT // 2


class Asteroid(pygame.sprite.Sprite):
    min_speed = 5
    max_speed = 10
    current_count = 0
    cool_down = 250
    current_cooldown = 0

    def __init__(self):

        super(Asteroid,self).__init__()

        Asteroid.current_count += 1

        self.image = pygame.image.load("pictures/asteroid{}.png".format(random.randint(1,3)))

        self.rect = self.image.get_rect()

        self.rect.top = -10
        self.rect.right = random.randint(0,WIDTH)

        self.current_speed = random.randint(self.min_speed,self.max_speed)

    def update(self):

        self.rect.bottom += self.current_speed

    @staticmethod
    def process_asteroids(clock,asteroids):
        if Asteroid.current_cooldown <= 0:
            asteroids.add(Asteroid())
            Asteroid.current_cooldown = Asteroid.cool_down
        else:
            Asteroid.current_cooldown -= clock.get_time()

        for a in list(asteroids):
            if (a.rect.right < 0 or a.rect.left > WIDTH or a.rect.top >= HEIGHT):
                asteroids.remove(a)





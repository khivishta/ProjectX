import pygame
import random


class Mask(pygame.sprite.Sprite):
    def __init__(self, WINDOW_SIZE):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/m6.png').convert_alpha()
        side = 35
        self.image = pygame.transform.scale(image, (side, side))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WINDOW_SIZE[0]-side)
        self.rect.y = random.randrange(WINDOW_SIZE[1]-side)
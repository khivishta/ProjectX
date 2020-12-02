import pygame
import random


class Mask(pygame.sprite.Sprite):
    def __init__(self, window_size):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/m2.jpeg').convert_alpha()
        side = 35
        self.image = pygame.transform.scale(image, (side, side))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(window_size[0]-side)
        self.rect.y = random.randrange(window_size[1]-side)
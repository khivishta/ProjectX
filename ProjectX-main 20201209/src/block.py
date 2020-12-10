import pygame
import random

# define a group for blocks


class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/wall.png').convert()

        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Ends(pygame.sprite.Sprite):
    def __init__(self, WINDOW_SIZE):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/end.png').convert_alpha()
        side = 35
        self.image = pygame.transform.scale(image, (side, side))
        self.rect = self.image.get_rect()
        self.rect.x = WINDOW_SIZE[0]-side
        self.rect.y = WINDOW_SIZE[1]-side

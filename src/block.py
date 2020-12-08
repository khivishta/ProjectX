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
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((70,60))
        self.rect = self.image.get_rect()
        self.image.fill(pygame.Color("blue"))      
        self.rect.center  = (765,570)


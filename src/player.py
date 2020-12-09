import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,WINDOW_SIZE):
        self.WINDOW_SIZE = WINDOW_SIZE
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/player2.png').convert_alpha()
        self.width = 35
        self.height=30
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.width-WINDOW_SIZE[0]
        self.rect.y = self.height-WINDOW_SIZE[1]
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,WINDOW_SIZE):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('img/player2.png').convert_alpha()
        self.width = 35
        self.height=30
        self.image = pygame.transform.scale(image, (self.width, self.height))
        self.rect = self.image.get_rect()
        self.rect.x = self.width-WINDOW_SIZE[0]
        self.rect.y = self.height-WINDOW_SIZE[1]
        
    def update(self):
        self.speedx = 0
        self.speedy = 0 
        keypress = pygame.key.get_pressed()
        if self.rect.centerx > 800:
            self.rect.centerx = 800
        if self.rect.centerx < 0:
            self.rect.centerx = 0
        if self.rect.centery > 600:
            self.rect.centery = 600
        if self.rect.centery < 0:
            self.rect.centery = 0

        if keypress [pygame.K_a]:
            self.rect.centerx -= 5
        if keypress [pygame.K_s]:
            self.rect.centery += 5
        if keypress [pygame.K_w]:
            self.rect.centery -= 5
        if keypress [pygame.K_d]:
            self.rect.centerx += 5
    
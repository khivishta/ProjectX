import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((25,25))
        self.rect = self.image.get_rect()
        self.image.fill(pygame.Color("green"))      
        self.rect.center  = (25,25)
        self.speedx = 0
        self.speedy = 0
        
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
    

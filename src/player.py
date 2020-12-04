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
       
       if keypress [pygame.K_a]:
           self.speedx = -5
       if keypress [pygame.K_s]:
           self.speedy = 5
       if keypress [pygame.K_w]:
           self.speedy = -5
       if keypress [pygame.K_d]:
           self.speedx = 5
       self.rect.x += self.speedx
       self.rect.y += self.speedy
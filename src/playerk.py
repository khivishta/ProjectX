# Pygame template - skeleton for a new pygame project
import pygame
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'pic')

# player class

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.rect = self.image.get_rect()
        self.image.fill(pygame.Color("green"))      
        self.rect.center  = (50,250)
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


# initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#assets folder


# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Draw / render
    screen.fill(pygame.Color("blue"))
    all_sprites.draw(screen)
    
    
    pygame.display.flip()

pygame.quit()

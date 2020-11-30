# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:00:20 2020

@author: Khivishta
"""

import pygame
import os
import sys



#define dimensions of screen

WIDTH= 800
HEIGHT=600
FPS = 30
RED = (255, 0, 0)
GRAY = (150, 150, 150)

#initialise pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("mask example")
clock = pygame.time.Clock()
running = True



class Mask(pygame.sprite.Sprite):
    #sprite for the mask
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('pic,''m2.jpeg').convert()
        self.image = pygame.transform.scale(self.image, (100, 130))
        self.rect=self.image.get_rect()
        self.rect.center= (WIDTH/2 , HEIGHT/2)

    def update(self):
        # any code here will happen every time the game loop updates
        self.rect.x += 5
        if self.rect.left > WIDTH:
            self.rect.right = 0



all_sprites = pygame.sprite.Group()
mask=Mask()
all_sprites.add(mask)
#update

running = True
while running:
     # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

screen.fill(GRAY)
screen.blit(get_image('m2.jpeg'), (20, 20))

pygame.display.update()

 #update           
all_sprites.update()

#draw/render masks

all_sprites.draw(screen)

pygame.display.flip()

clock.tick(60)

pygame.run()

pygame.quit()
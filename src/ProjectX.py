# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 10:00:20 2020

@author: Khivishta
"""

import pygame
import os

pic = "pic/"

#define dimensions of mask

WIDTH= 360
HEIGHT=480


#define colors

GREEN=(0,255,0)

class Mask(pygame.sprite.Sprite):
    #sprite for the mask
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(pic, "m1.jpg")).convert()
        self.image.fill=(GREEN)
        self.rect=self.image.get_rect()
        self.rect.center= (WIDTH/2 , HEIGHT/2)

all_sprites = pygame.sprite.Group()
mask=Mask()
all.sprites.add(mask)
#update 

all_sprites.update()

#draw/render masks

all_sprites.draw(screen)
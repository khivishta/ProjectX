# -*- coding: utf-8 -*-
"""
Created on Mon Dec  7 00:41:46 2020

@author: Anil
"""


import pygame
#import arcade

import random

# defining variable

WINDOW_SIZE = (800, 600)
N_MASKS = 10
background = pygame.image.load("background1.jpg")
background_rect = background.get_rect()
screen = pygame.display.set_mode((WINDOW_SIZE))

# a maze, 0 is path and 1 is blocks
background_group = [
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],]

class Block(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('wall.png').convert()

        self.image = pygame.transform.scale(image, (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Mask(pygame.sprite.Sprite):
    def __init__(self, window_size):
        pygame.sprite.Sprite.__init__(self)
        image = pygame.image.load('m2.jpeg').convert_alpha()
        side = 35
        self.image = pygame.transform.scale(image, (side, side))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(window_size[0]-side)
        self.rect.y = random.randrange(window_size[1]-side)
        
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
       if keypress [pygame.K_ESCAPE]:
           pygame.quit()
       self.rect.x += self.speedx
       self.rect.y += self.speedy
        
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.all_masks = pygame.sprite.Group()
        self.all_blocks = pygame.sprite.Group()
        self.player = Player()
        self.score = 0
        maze_height = len(background_group)
        maze_width = len(background_group[0])
        width = int(WINDOW_SIZE[0] / maze_width)
        height = int(WINDOW_SIZE[1] / maze_height)
        for i in range(maze_height):
            for z in range(maze_width):
                if background_group[i][z] == 1:
                    x = width * z
                    y = height * i
                    block = Block(width, height, x, y)
                    self.all_sprites.add(block)
                    self.all_masks.add(block)
                    
        for i in range(N_MASKS):
                mask = Mask(WINDOW_SIZE)
                while pygame.sprite.spritecollide(mask, self.all_sprites, False):                     #code so that masks does not overlap with each other
                        mask = Mask(WINDOW_SIZE)
    
                self.all_sprites.add(mask)
                self.all_masks.add(mask)
    

    def run(self):
        while True:
                       
            self.clock.tick(60)
           

           # check if the player has intersected with any masks attempt.
        
            # if pygame.sprite.spritecollideany(self.player,self.all_masks,True):
            #      self.score  =+ 10
            #      print(self.score)
            
            pygame.display.set_caption("Mask Warriors")
            self.all_sprites.add(self.player)
            screen.fill(pygame.Color("grey"))
            screen.blit(background, background_rect)
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.update()
            
            
            #Cycle through all masks currently on screen attempt 2.
            # for self.mask in self.all_masks:
            #     mask_collided= arcade.check_for_collision_with_list(self.mask, self.player)
            #     for masks in mask_collided:
            #         self.mask.remove_from_sprite_lists()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()


game = Game()
game.run()

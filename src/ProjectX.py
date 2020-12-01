#import necessary packages
import pygame, sys
from pygame import *
import os
import random
import arcade
import os, sys, pygame
 
from pygame.locals import *
 
#defining variables
 
WIDTH=800
HEIGHT=600
N_MASKS=10
score=0

size = (700, 700)  # size of the window
 
white = (255, 255, 255)  # what is white
 
block_group = []  # the group of blocks 

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
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]]
 

# define a group for blocks
class Block:
    def __init__(self, img, rect):
        self.img = img
        self.rect = rect
 
    # draw blocks
    def draw(self, screen):
        screen.blit(self.img, self.rect)
 
# draw bakgrounds
def drawBackground(screen):
    block_group.clear()
 
    # defind a figure for block
    block1_img = pygame.image.load('image/wall.png').convert()
 
    # drap the map
    for i in range(10):
        for j in range(10):
            if background_group[i][j] == 1:
                block = Block(block1_img, Rect(70*j, 70*i, 70, 70))  
                block.draw(screen)  
                block_group.append(block)  
 
    # def the end 
    block_final = Block(pygame.image.load('image/end.png').convert(), Rect(630, 630, 70, 70))
    block_final.draw(screen)
    block_group.append(block_final)
 
 
def game():
    # pygame
    pygame.init()
    # define the screen
    screen = pygame.display.set_mode(size, 0, 32)
    # define the background figure
    background1 = pygame.image.load('image/background1.jpg').convert()
    # mane t=of the window
    pygame.display.set_caption("map")
    # start
    while True:
        # fresh the window with white
        screen.fill(white)
        # draw the background
        screen.blit(background1, (0, 0))
        # draw the map
        drawBackground(screen)
        for event in pygame.event.get():
            if event.type == QUIT:
                #an error will be there if you close the window as the "if" cannot be finished
                pygame.quit()
                sys.exit()
        # refresh
        pygame.display.update()


class collectingmasks():


  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()

    # Initialize an 800x600 screen to draw stuff on.
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Don't quit yet.
    self.done = False

    mask = pygame.image.load('m2.jpeg').convert()
    mask = pygame.transform.scale(mask,(75,75))
    color = (255, 0, 0)  # rgb. This is red.
    mask.set_colorkey(color)
    multi_masks_pos = []
    # Draw new stuff.
    for i in range(N_MASKS):
        pos = (random.randint(75,WIDTH-75), random.randint( 75,HEIGHT-75))
        multi_masks_pos.append(pos)
        mask_rect = mask.get_rect(center=pos)
    while not self.done: 
      for i in range(N_MASKS):
        mask_rect = mask.get_rect(center=multi_masks_pos[i])
        self.screen.blit(mask, mask_rect)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          self.done = True
    # Update the game screen.
      pygame.display.flip()

    # Throttle screen updates to sixty times per second.
      self.clock.tick(60)

      
# Check whether the player has intersected with any masks.
# for mask in multi_masks_pos[:]:
#     if player.colliderect(mask):
#        multi_masks_pos.remove(mask)
#        score=score+1
#        print("Score:", score)

# main
game = collectingmasks()

pygame.QUIT



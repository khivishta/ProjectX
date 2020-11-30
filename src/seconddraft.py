
# import necessary packages
import pygame, sys
from pygame import *
import os
import random
WIDTH=800
HEIGHT=600
N_MASKS=10

class MyExcitingGame():


  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()

    # Initialize an 800x600 screen to draw stuff on.
    self.screen = pygame.display.set_mode((WIDTH, HEIGHT))

    # Don't quit yet.
    self.done = False

    # Set the character's initial position.
    self.x = 0
    self.y = 0


  def run(self):
    
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
      # Look for keypresses and set member variables based on them.

 
      self.screen.fill((255, 255, 255))   # white

      
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

      # main
game = MyExcitingGame()
game.run()

pygame.QUIT

#https://noidea.dog/blog/pygame-adventures
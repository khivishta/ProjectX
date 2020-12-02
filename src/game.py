#import necessary packages
from pygame import *
import os
import arcade
import os, sys, pygame
from block import drawBackground
from mask import Mask
 
#defining variable
 

WINDOW_SIZE = (800,600)
N_MASKS = 10
score=0

class Game:
  def __init__(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    # Initialize screen to draw stuff on.
    self.screen = pygame.display.set_mode(WINDOW_SIZE)
    self.done = False
    self.masks = Mask(WINDOW_SIZE, N_MASKS)
    pygame.display.set_caption("Mask Warriors")
    grey = (128,128,128)
    self.screen.fill(grey)

    # draw the background
    
  def run(self):
    while not self.done:
      drawBackground(self.screen)
      # draw the blocks
      #self.blocks.draw(self)
      # draw the masks
      self.masks.draw(self.screen)
      # Throttle screen updates to sixty times per second.
      self.clock.tick(60)
      pygame.display.update()
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
            self.done = True


game = Game()
game.run()



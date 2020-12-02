import pygame
import random

class Mask:
  def __init__(self, window_size, n_masks):
    mask = pygame.image.load('img/m2.jpeg').convert()
    side = 70
    mask = pygame.transform.scale(mask,(side,side))
    color = (255, 0, 0)  # rgb. This is red.
    mask.set_colorkey(color)
    self.mask = mask
    self.multi_masks_pos = []
    # Draw new stuff.
    for i in range(n_masks):
        pos = (random.randint(side, window_size[0] - side), random.randint( side, window_size[1] - side))
        self.multi_masks_pos.append(pos)
    
  def draw(self, screen):
      for pos in self.multi_masks_pos:
        mask_rect = self.mask.get_rect(center=pos)
        screen.blit(self.mask, mask_rect)

      
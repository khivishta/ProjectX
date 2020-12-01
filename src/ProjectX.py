print("hello game!")

import os, sys, pygame
 
from pygame.locals import *
 
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
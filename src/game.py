import pygame
import time
import sys
import random 
from block import Block
from mask import Mask
from player import Player

# defining variable

WINDOW_SIZE = (800, 600) #tuple for screen size
N_MASKS = 10


# a maze, 0 is path and 1 is blocks
map1 = [
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

map2 = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],]

map3 = [
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],]

background_group = [map1,map2,map3]

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.all_masks = pygame.sprite.Group()
        self.all_blocks = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.player = Player()
        self.score = 0
        
       

        #generating random maze
        background = random.choice(background_group)
        #height of maze contain x lists
        maze_height = len(background)
        #length of first list inside list 
        maze_width = len(background[0])
        #find out height and width of each block, get the first element which is the width
        width = int(WINDOW_SIZE[0] / maze_width)
        #get the second element which is the height and divide by maze height in our schema and get block dimensions
        height = int(WINDOW_SIZE[1] / maze_height)
        #for each position , find the x and y coordinates of block on screen
        for i in range(maze_height):
            for z in range(maze_width):
                if background[i][z] == 1:
                    x = width * z
                    y = height * i
                    #create a block with the width , height and position on screen that we calculated
                    block = Block(width, height, x, y)
                    #add to sprites
                    self.all_sprites.add(block)
                    self.all_blocks.add(block)

        #placing 10 masks on screen randomly
        for i in range(N_MASKS):
            mask = Mask(WINDOW_SIZE)
            #code so that masks does not overlap with each other and also with blocks and player
            while pygame.sprite.spritecollide(mask, self.all_sprites, False):           
                mask = Mask(WINDOW_SIZE)
            #if false  stop looping , and place mask inside the sprite
            self.all_sprites.add(mask)
            self.all_masks.add(mask)
        self.done = False
        pygame.display.set_caption("Mask Warriors")
        self.all_players.add(self.player)


        # main loop

    def run(self):
        while not self.done:
            pygame.display.flip()
            grey = (128, 128, 128)
            self.screen.fill(grey)
            self.all_blocks.update()
            self.all_masks.update()
            self.all_players.update()
            self.all_blocks.draw(self.screen)
            self.all_masks.draw(self.screen)
            self.all_players.draw(self.screen)
            myfont = pygame.font.SysFont("monospace", 20)
            scoretext = myfont.render("Score = "+str(self.score), 1, (255,0,0))
            self.screen.blit(scoretext, (5, 10))
            self.clock.tick(60)

            # check if the player has intersected with any masks attempt , the True removes the mask                
            if pygame.sprite.spritecollide(self.player, self.all_masks, True):                    
                    self.score  += 10
                    
            while self.score == 10 * N_MASKS:
                # they show winning screen
                pygame.display.flip()
                self.screen.fill((0,0,0))
                myfont = pygame.font.SysFont("monospace", 50)
                text = myfont.render("You won!", 1, (255,0,0))
                text_rect = text.get_rect(center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))
                self.screen.blit(text, text_rect)
                pygame.display.update()
                time.sleep(5)
                pygame.quit()
                sys.exit()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    self.done = True        

game = Game()
game.run()

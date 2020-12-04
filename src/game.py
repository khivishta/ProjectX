import pygame
import arcade
from block import Block
from mask import Mask
from player import Player
import pygame
import time
import sys
# defining variable

WINDOW_SIZE = (800, 600)
N_MASKS = 10


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
                    self.all_blocks.add(block)

        for i in range(N_MASKS):
            mask = Mask(WINDOW_SIZE)
            while pygame.sprite.spritecollide(mask, self.all_sprites, False):           #code so that masks does not overlap with each other
                mask = Mask(WINDOW_SIZE)

            self.all_sprites.add(mask)
            self.all_masks.add(mask)
        self.done = False
        pygame.display.set_caption("Mask Warriors")
        self.all_players.add(self.player)


        # draw the background

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

            # check if the player has intersected with any masks attempt.                
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
            #Cycle through all masks currently on screen attempt 2.
            # for self.mask in self.all_masks:
            #     mask_collided= arcade.check_for_collision_with_list(self.mask, self.player)
            #     for masks in mask_collided:
            #         self.mask.remove_from_sprite_lists()

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
        


game = Game()
game.run()

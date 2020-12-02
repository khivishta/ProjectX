import pygame
from block import Block
from mask import Mask
from player import Player

# defining variable

WINDOW_SIZE = (800, 600)
N_MASKS = 10
score = 0

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
            while pygame.sprite.spritecollide(mask, self.all_sprites, False):
                mask = Mask(WINDOW_SIZE)

            self.all_sprites.add(mask)
            self.all_masks.add(mask)
        self.done = False
        pygame.display.set_caption("Mask Warriors")
        grey = (128, 128, 128)
        self.screen.fill(grey)
        self.all_sprites.add(Player())
        # draw the background

    def run(self):
        while not self.done:
            self.all_sprites.update()
            self.clock.tick(60)
            pygame.display.update()
            self.all_sprites.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True


game = Game()
game.run()

import pygame
import arcade
from block import Block
from mask import Mask
from player import Player

# defining variable

screen = pygame.display.set_mode((800,600))
WINDOW_SIZE = (800, 600)
N_MASKS = 10

isOver = False

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
        self.player = Player()
        self.block = pygame.sprite.Group()
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
                    self.block.add(block)
                    rect = pygame.Rect(0,0,x,y)
                    pygame.draw.rect(self.screen,(0,0,0),rect)
                    rect.x = width
                    rect.y = height

                    


        for i in range(N_MASKS):
            mask = Mask(WINDOW_SIZE)
            while pygame.sprite.spritecollide(mask, self.all_sprites, False):           #code so that masks does not overlap with each other
                mask = Mask(WINDOW_SIZE)

            self.all_sprites.add(mask)
            self.all_masks.add(mask)
        self.done = False
        pygame.display.set_caption("Mask Warriors")
        self.all_sprites.add(self.player)

        #draw the background
        #player = self.player
        #rect = self.block
        #if pygame.Rect.colliderect(rect, player): 
        #    self.speedy = 0
        #    self.speedx = 0
    
    
    def run(self):
        while not self.done:
                       
            self.clock.tick(60)
            pygame.display.update()

            # check if the player has intersected with any masks attempt.
        
            # if pygame.sprite.spritecollideany(self.player,self.all_masks,True):
            #      self.score  =+ 10
            #      print(self.score)
            

            white = (0,0,0)
            screen.fill(white)
            grey = (128, 128, 128)
            self.screen.fill(grey)
            background = pygame.image.load('image/background2.png').convert()
            self.screen.blit(background, (0, 0))
            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            
            """
            rect1 = pygame.Rect(0,0,25,25)
            rect1.centerx = 25
            rect1.centery = 25
            pygame.draw.rect(screen, (pygame.Color("green")), rect1)

            up = False
            down = False
            left = False
            right = False

            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        left = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        down = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        right = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_w:
                        up = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        left = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_s:
                        down = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_d:
                        right = False
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w:
                        up = False

            if left == True:
                rect1.centerx -= 4
            if right == True:
                rect1.centerx -= 4
            if up == True:
                rect1.centery -= 4
            if down == True:
                rect1.centery -= 4

    
            if rect1.centerx in range (720,800) and rect1.centery in range (540,600):
                global isOver
                isOver = True
            
            """
            #Cycle through all masks currently on screen attempt 2.
            # for self.mask in self.all_masks:
            #     mask_collided= arcade.check_for_collision_with_list(self.mask, self.player)
            #     for masks in mask_collided:
            #         self.mask.remove_from_sprite_lists()

            global isOver
            if isOver:
                white = (0,0,0)
                screen.fill(white)
                self.screen.blit(pygame.image.load('image\over.jpg').convert(), (0, 0))
                pygame.display.update()
            

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True


game = Game()
game.run()

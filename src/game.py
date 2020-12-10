import pygame
import time
import sys
import random

from block import Block, Ends
from mask import Mask
from player import Player

# defining variables

WINDOW_SIZE = (800, 600)  # tuple for screen size
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
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], ]

map2 = [
    [0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1, 1, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0], ]

map3 = [
    [0, 1, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 0], ]


class Game:
    def __init__(self):
        pygame.init()
     
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.clock = pygame.time.Clock()
        self.all_sprites = pygame.sprite.Group()
        self.all_masks = pygame.sprite.Group()
        self.all_blocks = pygame.sprite.Group()
        self.all_players = pygame.sprite.Group()
        self.all_ends = pygame.sprite.Group()
        self.player = Player(WINDOW_SIZE)
        self.ends = Ends(WINDOW_SIZE)
        self.score = 0
        self.endgame = 0
        self.again = 0
        self.background_group = [map1, map2, map3]
        self.intro = True
        pygame.display.set_caption("Mask Warriors")
        pygame.display.flip()
        pygame.display.update()
        # generating random maze
        background = random.choice(self.background_group)
        # height of maze contain x lists
        maze_height = len(background)
        # length of first list inside list
        maze_width = len(background[0])
        # find out height and width of each block, get the first element which is the width
        width = int(WINDOW_SIZE[0] / maze_width)
        # get the second element which is the height and divide by maze height in our schema and get block dimensions
        height = int(WINDOW_SIZE[1] / maze_height)
        # for each position , find the x and y coordinates of block on screen
        for i in range(maze_height):
            for z in range(maze_width):
                if background[i][z] == 1:
                    x = width * z
                    y = height * i
                    # create a block with the width , height and position on screen that we calculated
                    block = Block(width, height, x, y)
                    # add to sprites
                    self.all_sprites.add(block)
                    self.all_blocks.add(block)

        # placing 10 masks on screen randomly
        for i in range(N_MASKS):
            mask = Mask(WINDOW_SIZE)

            # code so that masks does not overlap with each other and also with blocks and player, false does not remove anything

            while pygame.sprite.spritecollide(mask, self.all_sprites, False):
                mask = Mask(WINDOW_SIZE)
            # if false  stop looping , and place mask inside the sprite
            self.all_sprites.add(mask)
            self.all_masks.add(mask)
        self.done = False

        
        self.all_players.add(self.player)

        self.all_ends.add(self.ends)
        self.all_sprites.add(self.ends)

        # add the bgm
        bgm = pygame.mixer.music.load("sound/bgm.ogg")
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()
        pygame.mixer.music.play(-1, 0)
        pygame.mixer.init()

    def update(self):
        self.player.speedx = 0
        self.player.speedy = 0
        keypress = pygame.key.get_pressed()

        if self.player.rect.centerx > WINDOW_SIZE[0]-(self.player.width/2):
            self.player.rect.centerx = WINDOW_SIZE[0]-(self.player.width/2)
        if self.player.rect.centerx < (self.player.width/2):
            self.player.rect.centerx = (self.player.width/2)
        if self.player.rect.centery > WINDOW_SIZE[1]-(self.player.height/2):
            self.player.rect.centery = WINDOW_SIZE[1]-(self.player.height/2)
        if self.player.rect.centery < (self.player.height/2):
            self.player.rect.centery = (self.player.height/2)

        if keypress[pygame.K_a]:
            self.player.speedx = -5
        if keypress[pygame.K_s]:
            self.player.speedy = 5
        if keypress[pygame.K_w]:
            self.player.speedy = -5
        if keypress[pygame.K_d]:
            self.player.speedx = 5
        self.player.rect.x += self.player.speedx
        self.player.rect.y += self.player.speedy

        # main loop

    def run(self):
        grey = (128, 128, 128)
        GameDone = False
        while self.intro:
            check_close_event()
            self.screen.fill(grey)
            myfont = pygame.font.SysFont(
                    "They definitely dont have this installed Gothic", 50)
            text = myfont.render("Press any key to start!", 1, (255, 0, 0))
            text_rect = text.get_rect(
                    center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))
            self.screen.blit(text, text_rect)
            pygame.display.update()
            self.clock.tick(15)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    self.intro = False               
        timer = 10
        dt = 0

        while not self.done:

            pygame.display.flip()
            
            self.screen.fill(grey)
            self.all_ends.update()
            self.all_ends.draw(self.screen)
            self.all_blocks.update()
            self.all_blocks.draw(self.screen)
            self.all_masks.update()
            self.update()

            self.all_masks.draw(self.screen)
            self.all_players.draw(self.screen)

            myfont = pygame.font.SysFont("monospace", 20)
            scoretext = myfont.render(
                "Score = "+str(self.score), 1, (255, 0, 0))
            self.screen.blit(scoretext, (5, 10))
            self.clock.tick(60)

            # check if the player has crashed on the wall
            if pygame.sprite.spritecollide(self.player, self.all_blocks, False):
                sound_crash = pygame.mixer.Sound("sound/crash.ogg")
                sound_crash.set_volume(0.2)
                # add the sound for collect
                self.score -= 3
                timer -= 2
                sound_crash.play()
                time.sleep(0.2)

            # Timer
            if timer <= 0:
                # Allocated time has fallen below 0, end screen shown, waits for user to close window
                self.endgame = 1

            
            # timer is decreased by increments of dt, time remaining is displayed
            timer -= dt
            timer_text = myfont.render(
                "Time remaining:" + str(round(timer)), True, pygame.Color("blue"))
            self.screen.blit(timer_text, (520, 10))
            dt = self.clock.tick(60)/500

            # check if the player has intersected with any masks attempt , the True removes the mask
            if pygame.sprite.spritecollide(self.player, self.all_masks, True):
                sound_collet = pygame.mixer.Sound("sound/collect.ogg")
                sound_collet.set_volume(0.2)
                # add the sound for collect
                self.score += 10
                timer += 4
                sound_collet.play()

            if pygame.sprite.spritecollide(self.player, self.all_ends, False):
                self.endgame = 1

            while self.endgame == 1:
                pygame.mixer.pause()
                pygame.display.flip()
                self.screen.fill((0, 0, 0))
                myfont = pygame.font.SysFont(
                    "They definitely dont have this installed Gothic", 50)
                text = ""
                if timer <= 0:
                    text = myfont.render("You ran out of time!", 1, (255, 0, 0))
                    GameDone = True
                    pygame.mixer.music.stop()
                    sound_collet = pygame.mixer.Sound("sound/collect.ogg")
                    sound_collet.set_volume(0.2)

                elif self.score >= 8 * N_MASKS:
                    # they show winning screen
                    text = myfont.render(
                        "You won with a score of " + str(self.score), 1, (255, 0, 0))
                    GameDone = True
                    pygame.mixer.music.stop()
                    sound_collet = pygame.mixer.Sound("sound/collect.ogg")
                    sound_collet.set_volume(0.2)

                else:
                    text = myfont.render("You lose! your score was only: "  + str(self.score), 1, (255, 0, 0))
                    GameDone = True
                    pygame.mixer.music.stop()
                    sound_collet = pygame.mixer.Sound("sound/collect.ogg")
                    sound_collet.set_volume(0.2)
                    
                text_rect = text.get_rect(
                    center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))
                self.screen.blit(text, text_rect)
                pygame.display.update()                            
                check_close_event()
                
                """
                while GameDone:  # pause game loop, show restart 
                    time.sleep(5)
                    self.screen.fill(grey)
                    myfont = pygame.font.SysFont(
                        "They definitely dont have this installed Gothic", 50)
                    text = myfont.render("Press any key to start again!", 1, (255, 0, 0))
                    text_rect = text.get_rect(
                        center=(WINDOW_SIZE[0]/2, WINDOW_SIZE[1]/2))
                    self.screen.blit(text, text_rect)
                    pygame.display.update() 
                    events = pygame.event.get()
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:  # press space to restart
                            GameDone = False
                            game.run()  # initialize variables
                """
            check_close_event()


def check_close_event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


game = Game()
game.run()

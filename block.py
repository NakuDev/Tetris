import pygame
import random

class Block:
    def __init__(self, game_limit, nb_tiles_x, nb_tiles_y, tile_x, tile_y):
        self.screen = pygame.display.get_surface()
        self.screen_width, self.screen_height = self.screen.get_size()

        self.spawned = False
        self.bloc = random.randint(0,4)

        if self.bloc == 0:
            self.image = pygame.image.load("assets/textures/yellow_bloc.png")
        elif self.bloc == 1:
            self.image = pygame.image.load("assets/textures/red_block.png")
        elif self.bloc == 2:
            self.image = pygame.image.load("assets/textures/purple_bloc.png")
        elif self.bloc == 3:
            self.image = pygame.image.load("assets/textures/green_bloc.png")
        elif self.bloc == 4:
            self.image = pygame.image.load("assets/textures/blue_bloc.png")

        self.rect = self.image.get_rect()

        self.game_limit = game_limit
        self.nb_tiles_x = nb_tiles_x
        self.nb_tiles_y = nb_tiles_y
        self.tile_x = tile_x
        self.tile_y = tile_y

    def spawn(self):
        self.spawned = True
        self.pos_x = self.nb_tiles_x//2* self.tile_x + self.game_limit[0]
        self.pos_y = self.game_limit[1]

    def update(self):
        if self.spawned:
            self.pos_y += self.tile_y

    def draw:
        pass
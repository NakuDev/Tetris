import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, game_limit, nb_tiles_x, nb_tiles_y, tile_x, tile_y):
        super(Block, self).__init__()
        self.screen = pygame.display.get_surface()
        self.screen_width, self.screen_height = self.screen.get_size()

        self.spawned = False
        self.bloc = random.randint(0,4)
        self.speed = 2

        self.game_limit = game_limit
        self.nb_tiles_x = nb_tiles_x
        self.nb_tiles_y = nb_tiles_y
        self.tile_x = tile_x
        self.tile_y = tile_y

        if self.bloc == 0:
            self.image = pygame.image.load("assets/textures/yellow_bloc.png")
            self.image = pygame.transform.scale(self.image, (self.tile_x*2, self.tile_y*2))
        elif self.bloc == 1:
            self.image = pygame.image.load("assets/textures/red_block.png")
            self.image = pygame.transform.scale(self.image, (self.tile_x*2, self.tile_y*3))
        elif self.bloc == 2:
            self.image = pygame.image.load("assets/textures/purple_bloc.png")
            self.image = pygame.transform.scale(self.image, (self.tile_x*2, self.tile_y*3))
        elif self.bloc == 3:
            self.image = pygame.image.load("assets/textures/green_bloc.png")
            self.image = pygame.transform.scale(self.image, (self.tile_x*2, self.tile_y*3))
        elif self.bloc == 4:
            self.image = pygame.image.load("assets/textures/blue_bloc.png")
            self.image = pygame.transform.scale(self.image, (self.tile_x, self.tile_y*4))

        self.rect = self.image.get_rect(topleft=(self.game_limit[0], self.game_limit[1]))
        self.mask = pygame.mask.from_surface(self.image)

        self.rotation = 0

    def rotate(self):
        a = self.rect.topleft
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect(topleft=a)
        self.mask = pygame.mask.from_surface(self.image)
        self.rotation += 1
        if self.rotation > 3:
            self.rotation = 0

    def spawn(self):
        self.spawned = True
        self.rect.x = self.nb_tiles_x//2 * self.tile_x + self.game_limit[0]
        self.rect.y = self.game_limit[1]

    def update(self):
        if self.spawned:
            self.rect.y += self.speed

    def draw(self):
        self.screen.blit(self.image, self.rect)
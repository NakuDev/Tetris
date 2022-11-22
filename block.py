import pygame
import random

class Block(pygame.sprite.Sprite):
    def __init__(self, game_limit, nb_tiles_x, nb_tiles_y, tile_x, tile_y, bloc_log):
        super(Block, self).__init__()
        self.screen = pygame.display.get_surface()
        self.screen_width, self.screen_height = self.screen.get_size()

        self.spawned = False
        n = random.randint(0,100)
        if n <= 7:
            self.bloc = 4
        elif n <= 17:
            self.bloc = 0
        elif n <= 34:
            self.bloc = 5
        elif n <= 45:
            self.bloc = 6
        elif n <= 67:
            self.bloc = 1
        elif n <= 80:
            self.bloc = 3
        elif n <= 100:
            self.bloc = 2

        if bloc_log is not None:
            if bloc_log[0] == bloc_log[1]:
                while self.bloc == bloc_log[0]:
                    self.bloc = random.randint(0,6)
        self.speed = 1.5

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
        elif self.bloc == 5:
            self.image = pygame.image.load("assets/textures/orange_bloc.png")
            self.image = pygame.transform.scale(self.image, (self.tile_x*2, self.tile_y*3))
        elif self.bloc == 6:
            self.image = pygame.image.load("assets/textures/darkblue_bloc.png")
            self.image = pygame.transform.scale(self.image, (self.tile_x*2, self.tile_y*3))

        self.rect = self.image.get_rect(topleft=(self.game_limit[0]//2-self.image.get_width()*0.5-5, self.game_limit[1]+self.screen.get_height()//20))
        self.mask = pygame.mask.from_surface(self.image)

        self.rotation = 0

        self.holded = False

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
        if self.spawned and not self.holded:
            self.rect.y += self.speed
        if self.holded:
            self.rect.topleft = (self.game_limit[0] + self.game_limit[2] + (self.screen.get_width() - self.game_limit[2] - self.game_limit[0])//2 - self.rect.width//2, self.screen.get_height()//3 - self.rect.height//2)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def ToggleHold(self):
        if self.holded:
            self.holded = False
        else:
            self.holded = True
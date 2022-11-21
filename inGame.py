import pygame
from math import floor
from block import Block
from field import Field

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class inGame:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_width, self.screen_height = self.screen.get_size()

        # créer le text du record de points
        self.font = pygame.font.Font("assets/fonts/8-bit-pusab.ttf", 20)
        self.record_text = self.font.render("Best:", False, WHITE)

        self.lost = False

        # self.game_limit = [x, y, width, height]
        self.game_limit = [self.screen_width // 6, 0, (self.screen_width // 6) * 3, self.screen_height]
        self.left_border = pygame.Rect(self.game_limit[0] - 10, self.game_limit[1], 10, self.game_limit[3])
        self.right_border = pygame.Rect(self.game_limit[0] + self.game_limit[2], self.game_limit[1], 10,
                                        self.game_limit[3])
        self.bottom_border = pygame.Rect(self.game_limit[0], self.game_limit[1] + self.game_limit[3]-10, self.game_limit[2], 10)

        # séparer la zone de jeux en tuiles, chaques tuiles représentent un bloc, la zone de jeu fait 10
        self.game_tiles_x = 10
        self.game_tile_x = self.game_limit[2] // self.game_tiles_x
        self.game_tiles_y = self.game_limit[3]//self.game_tile_x
        self.game_tile_y = self.game_limit[3] // self.game_tiles_y

        #générer les blocs
        self.currentblock = Block(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x,self.game_tile_y)
        self.nextblock = Block(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x, self.game_tile_y)
        self.currentblock.spawn()

        self.field = Field(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x, self.game_tile_y)

    def update(self):

        self.checklose()

        if not self.lost:
            self.currentblock.update()
            self.nextblock.update()

            self.field.checklines()

            #check for collision with the border of the map
            if pygame.Rect.colliderect(self.currentblock.rect, self.bottom_border):
                tile_x = floor((self.currentblock.rect.x-self.game_limit[0])//self.game_tile_x)
                tile_y = floor((self.currentblock.rect.y-self.game_limit[1])//self.game_tile_y)
                self.field.addblock(self.currentblock.bloc, self.currentblock.rotation, tile_x, tile_y)
                self.change_bloc()
            if pygame.Rect.colliderect(self.currentblock.rect, self.left_border):
                self.currentblock.rect.x += self.game_tile_x
            elif pygame.Rect.colliderect(self.currentblock.rect, self.right_border):
                self.currentblock.rect.x -= self.game_tile_x

            if pygame.sprite.spritecollide(self.currentblock, self.field.cube_group, False, pygame.sprite.collide_mask):
                tile_x = floor((self.currentblock.rect.x-self.game_limit[0])//self.game_tile_x)
                tile_y = floor((self.currentblock.rect.y-self.game_limit[1])//self.game_tile_y)
                self.field.addblock(self.currentblock.bloc, self.currentblock.rotation, tile_x, tile_y)
                self.change_bloc()
            return False
        else:
            return True

    def checklose(self):
        for cell in self.field.chart[0]:
            if cell != 0:
                self.lost = True

    def change_bloc(self):
        self.currentblock = self.nextblock
        self.currentblock.spawn()
        self.nextblock = Block(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x,
                               self.game_tile_y)

    def draw(self):

        # Afficher le text du record de point
        self.screen.blit(self.record_text, (self.screen_width // 10 * 7, self.screen_height // 40))

        # Afficher les limites de jeu
        pygame.draw.rect(self.screen, WHITE, self.left_border)
        pygame.draw.rect(self.screen, WHITE, self.right_border)
        pygame.draw.rect(self.screen, WHITE, self.bottom_border)

        self.currentblock.draw()
        self.nextblock.draw()

        self.field.draw()

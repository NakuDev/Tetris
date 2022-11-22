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
        self.score = 0
        self.font = pygame.font.Font("assets/fonts/8-bit-pusab.ttf", 15)
        self.record_text = self.font.render("Score: " + str(self.score), False, WHITE)

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

        self.bloc_log = None

        #générer les blocs
        self.currentblock = Block(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x,self.game_tile_y, self.bloc_log)
        self.nextblock = Block(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x, self.game_tile_y, self.bloc_log)
        self.currentblock.spawn()
        self.bloc_log = [self.currentblock.bloc, self.nextblock.bloc]

        self.field = Field(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x, self.game_tile_y)

        self.drop_sound = pygame.mixer.Sound("assets/sound_effects/drop.mp3")
        self.holded_bloc = None

    def update(self):

        self.checklose()

        if not self.lost:
            self.currentblock.update()
            self.nextblock.update()
            if self.holded_bloc is not None:
                self.holded_bloc.update()

            n_lines = self.field.checklines()

            #check for collision with the border of the map
            if pygame.Rect.colliderect(self.currentblock.rect, self.bottom_border):
                self.drop_sound.play()
                tile_x = floor((self.currentblock.rect.x-self.game_limit[0])//self.game_tile_x)
                tile_y = floor((self.currentblock.rect.y-self.game_limit[1])//self.game_tile_y)
                self.field.addblock(self.currentblock.bloc, self.currentblock.rotation, tile_x, tile_y)
                self.change_bloc()
            if pygame.Rect.colliderect(self.currentblock.rect, self.left_border):
                self.currentblock.rect.x += self.game_tile_x
            elif pygame.Rect.colliderect(self.currentblock.rect, self.right_border):
                self.currentblock.rect.x -= self.game_tile_x

            if pygame.sprite.spritecollide(self.currentblock, self.field.cube_group, False, pygame.sprite.collide_mask):
                self.drop_sound.play()
                tile_x = floor((self.currentblock.rect.x-self.game_limit[0])//self.game_tile_x)
                tile_y = floor((self.currentblock.rect.y-self.game_limit[1])//self.game_tile_y)
                self.field.addblock(self.currentblock.bloc, self.currentblock.rotation, tile_x, tile_y)
                self.change_bloc()

            self.update_score(n_lines)
            return False
        else:
            return True


    def update_score(self, complete_lines):
        n = 100
        self.score += n*complete_lines**2
        self.record_text = self.font.render("Score: " + str(self.score), False, WHITE)


    def checklose(self):
        for cell in self.field.chart[0]:
            if cell != 0:
                self.lost = True

    def change_bloc(self):
        self.currentblock = self.nextblock
        self.currentblock.spawn()
        self.nextblock = Block(self.game_limit, self.game_tiles_x, self.game_tiles_y, self.game_tile_x,
                               self.game_tile_y, self.bloc_log)
        self.bloc_log.pop(0)
        self.bloc_log.append(self.nextblock.bloc)

    def keep_bloc(self):
        inter = self.holded_bloc
        self.holded_bloc = self.currentblock
        if inter is None:
            self.change_bloc()
        else:
            inter.rect.topleft = self.currentblock.rect.topleft
            self.currentblock = inter
        self.holded_bloc.holded = True
        self.currentblock.holded = False

    def draw(self):

        # Afficher le text du record de point
        self.screen.blit(self.record_text, (self.screen_width // 10 * 7, self.screen_height // 40))

        # Afficher les limites de jeu
        pygame.draw.rect(self.screen, WHITE, self.left_border)
        pygame.draw.rect(self.screen, WHITE, self.right_border)
        pygame.draw.rect(self.screen, WHITE, self.bottom_border)

        self.currentblock.draw()
        self.nextblock.draw()
        if self.holded_bloc is not None:
            self.holded_bloc.draw()

        self.field.draw()

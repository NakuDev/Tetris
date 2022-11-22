import pygame
from cube import Cube

class Field:
    def __init__(self, game_limit, tiles_x, tiles_y, tile_x, tile_y):
        self.screen = pygame.display.get_surface()
        self.chart = [[0 for x in range(tiles_x)] for x in range(tiles_y)]

        self.game_limit = game_limit
        self.tiles_x = tiles_x
        self.tiles_y = tiles_y
        self.tile_x = tile_x
        self.tile_y = tile_y

        self.yellow_cube_img = pygame.image.load("assets/textures/yellow_cube.png")
        self.red_cube_img = pygame.image.load("assets/textures/red_cube.png")
        self.purple_cube_img = pygame.image.load("assets/textures/purple_cube.png")
        self.green_cube_img = pygame.image.load("assets/textures/green_cube.png")
        self.blue_cube_img = pygame.image.load("assets/textures/blue_cube.png")

        self.cube_group = pygame.sprite.Group()

        self.fourlines_effect = pygame.mixer.Sound("assets/sound_effects/4-lines effect.mp3")

    def addblock(self, type, rotation, x, y):
        if type == 0:
            self.addcube(type, x, y)
            self.addcube(type, x+1, y)
            self.addcube(type, x, y+1)
            self.addcube(type, x+1, y+1)
        elif type == 1:
            if rotation == 0 or rotation == 2:
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x, y + 1)
                self.addcube(type, x, y + 2)
            else:
                self.addcube(type, x, y)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 2, y + 1)
        elif type == 2:
            if rotation == 0:
                self.addcube(type, x, y)
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x, y + 2)
            elif rotation == 1:
                self.addcube(type, x, y)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 2, y)
            elif rotation == 2:
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y + 2)
            else:
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 2, y + 1)
        elif type == 3:
            if rotation == 0 or rotation == 2:
                self.addcube(type, x, y)
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 1, y + 2)
            else:
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 2, y)
        elif type == 4:
            if rotation == 0 or rotation == 2:
                self.addcube(type, x, y)
                self.addcube(type, x, y + 1)
                self.addcube(type, x, y + 2)
                self.addcube(type, x, y + 3)
            else:
                self.addcube(type, x, y)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 2, y)
                self.addcube(type, x + 3, y)
        elif type == 5:
            if rotation == 0:
                self.addcube(type, x, y)
                self.addcube(type, x + 1, y)
                self.addcube(type, x, y + 1)
                self.addcube(type, x, y + 2)
            elif rotation == 1:
                self.addcube(type, x, y)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 2, y)
                self.addcube(type, x + 2, y + 1)
            elif rotation == 2:
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 1, y + 2)
                self.addcube(type, x, y + 2)
            else:
                self.addcube(type, x, y)
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 2, y + 1)
        else:
            if rotation == 0:
                self.addcube(type, x, y)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 1, y + 2)
            elif rotation == 1:
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y + 1)
                self.addcube(type, x + 2, y + 1)
                self.addcube(type, x + 2, y)
            elif rotation == 2:
                self.addcube(type, x, y)
                self.addcube(type, x, y + 1)
                self.addcube(type, x, y + 2)
                self.addcube(type, x + 1, y + 2)
            else:
                self.addcube(type, x, y)
                self.addcube(type, x, y + 1)
                self.addcube(type, x + 1, y)
                self.addcube(type, x + 2, y)

    def addcube(self, type, x, y):
        self.chart[y][x] = Cube(type, (x*self.tile_x+self.game_limit[0], y*self.tile_y+self.game_limit[1]), self.tile_x, self.tile_y)
        self.cube_group.add(self.chart[y][x])

    def checklines(self):
        complete_lines = 0
        i = 0
        for row in self.chart:
            filled = True
            for cell in row:
                if cell == 0:
                    filled = False
            if filled:
                complete_lines += 1
                for cell in row:
                    self.cube_group.remove(cell)
                self.chart.pop(i)
                self.chart.insert(0, [0 for x in range(self.tiles_x)])

                a = 0
                for row in self.chart:
                    if a > i:
                        break
                    for cell in row:
                        if cell != 0:
                            cell.down()
                    a += 1

            i += 1

        if complete_lines == 4:
            self.fourlines_effect.play()
        return complete_lines


    def draw(self):
        self.cube_group.draw(self.screen)
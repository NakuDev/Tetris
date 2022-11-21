import pygame

class Cube(pygame.sprite.Sprite):
    def __init__(self, type, pos, tile_x, tile_y):
        super(Cube, self).__init__()
        self.screen = pygame.display.get_surface()

        self.tile_y = tile_y

        if type == 0:
            self.image = pygame.image.load("assets/textures/yellow_cube.png")
            self.image = pygame.transform.scale(self.image, (tile_x, tile_y))
        elif type == 1:
            self.image = pygame.image.load("assets/textures/red_cube.png")
            self.image = pygame.transform.scale(self.image, (tile_x, tile_y))
        elif type == 2:
            self.image = pygame.image.load("assets/textures/purple_cube.png")
            self.image = pygame.transform.scale(self.image, (tile_x, tile_y))
        elif type == 3:
            self.image = pygame.image.load("assets/textures/green_cube.png")
            self.image = pygame.transform.scale(self.image, (tile_x, tile_y))
        elif type == 4:
            self.image = pygame.image.load("assets/textures/blue_cube.png")
            self.image = pygame.transform.scale(self.image, (tile_x, tile_y))

        self.rect = self.image.get_rect(topleft=(pos))
        self.mask = pygame.mask.from_surface(self.image)

    def down(self):
        self.rect.y += self.tile_y
    def draw(self):
        self.screen.blit(self.image, self.rect)
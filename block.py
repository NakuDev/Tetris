import pygame
import random

class Block:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_width, self.screen_height = self.screen.get_size()

        self.spawned = False
        self.bloc = random.randint(0,5)

    def Update(self):
        pass
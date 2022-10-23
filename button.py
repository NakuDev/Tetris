import pygame

class Button:
    #Initialiser la classe
    def __init__(self, x, y, image):
        self.screen = pygame.display.get_surface()
        self.image = image
        self.rect = self.image.get_rect() #Hitbox de l'objet
        self.rect.topleft = (x-self.rect.width//2, y)
        self.isHere = True

    def isPressed(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0] == 1:
                self.isHere = False
                return True

    #Dessiner le bouton
    def draw(self):
        self.screen.blit(self.image, (self.rect.x, self.rect.y))
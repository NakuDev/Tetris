import pygame
from button import Button

class Menu:
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.screen_width, self.screen_height = self.screen.get_size()

        self.list_button = []

        self.run = True

        self.music_name = ""
        self.font = pygame.font.Font("assets/fonts/8-bit-pusab.ttf", 10)

        # Créer le bouton "start" et le bouton "exit"
        self.start_button = Button(self.screen_width // 2, self.screen_height // 4,
                                   pygame.transform.scale(pygame.image.load("assets/textures/start_button.png"), (300, 150)))
        self.list_button.append(self.start_button)
        self.exit_button = Button(self.screen_width // 2, self.screen_height // 2,
                                  pygame.transform.scale(pygame.image.load("assets/textures/exit_button.png"), (300, 150)))
        self.list_button.append(self.exit_button)

    def Display(self):

        for button in self.list_button:
            if button.isHere:
                button.draw()

        #Ecrire le nom de la musique en bas à droite
        self.music_name_rended = self.font.render(self.music_name, False, (255, 255, 255))
        self.screen.blit(self.music_name_rended, (self.screen_width-self.music_name_rended.get_width()-10, self.screen_width-self.music_name_rended.get_height()-10))
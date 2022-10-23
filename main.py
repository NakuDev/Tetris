import pygame
from button import Button
from menu import Menu
from block import Block

WHITE = (255,255,255)
BLACK = (0,0,0)

class Game:
    #Charger la classe (definir les variables, les arguments)
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()
        pygame.display.set_caption("Tetris")
        self.running = True
        self.clock = pygame.time.Clock()

        self.menu = Menu()
        self.menu.music_name = "Tetris Ragtime Piano"

        #créer le text du record de points
        self.font = pygame.font.Font("assets/fonts/8-bit-pusab.ttf", 20)
        self.record_text = self.font.render("Best:", False, WHITE)

        #self.game_limit = [x, y, width, height]
        self.game_limit = [self.screen_width//6, 0, (self.screen_width//6)*3, self.screen_height]
        self.left_border = pygame.Rect(self.game_limit[0]-10, self.game_limit[1], 10, self.game_limit[3])
        self.right_border = pygame.Rect(self.game_limit[0]+self.game_limit[2]-10, self.game_limit[1], 10, self.game_limit[3])

        #séparer la zone de jeux en tuiles, chaques tuiles représentent un bloc, la zone de jeu fait 10
        self.game_tiles = 10
        self.game_tile_x = self.game_limit[2]//self.game_tiles
        self.game_tile_y = self.game_limit[3]//self.game_tiles

        self.block = Block()

    #Gérer les évenement (input)
    def Handling_events(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            if keys[pygame.K_1]:
                self.menu.music_name = "Classic Tetris Music"
                pygame.mixer.music.load("assets/musics/tetris_music.mp3")
                pygame.mixer.music.play(-1)
            elif keys[pygame.K_2]:
                self.menu.music_name = "Tetris Ragtime Piano"
                pygame.mixer.music.load("assets/musics/Tetris RagTime.mp3")
                pygame.mixer.music.play(-1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False



        if self.menu.run:
            if self.menu.exit_button.isPressed():
                self.running = False
            if self.menu.start_button.isPressed():
                self.menu.run = False



    def Update(self):

        if not self.menu.run:
            self.block.Update()

    #Afficher/dessiner le jeu
    def Display(self):

        #Colorie l'écran en noir
        screen.fill(BLACK)

        #Si nous somme dans le menu, Dessiner chaque boutons du menu
        if self.menu.run:
            self.menu.Display()
        else:

            #Afficher le text du record de point
            self.screen.blit(self.record_text, (self.screen_width//10*7, self.screen_height//40))

            #Afficher les limites de jeu
            pygame.draw.rect(self.screen, WHITE, self.left_border)
            pygame.draw.rect(self.screen, WHITE, self.right_border)

        pygame.display.flip()

    #Boucle de Jeu
    def Run(self):
        while self.running:
            self.Handling_events()
            self.Update()
            self.Display()

pygame.init()

volume = 0.1

pygame.mixer.music.load("assets/musics/tetris_music.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((800, 800))

game = Game(screen)
game.Run()

pygame.quit()
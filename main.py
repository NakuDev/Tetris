import pygame
from button import Button
from menu import Menu
from block import Block
from inGame import inGame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Game:
    #Charger la classe (definir les variables, les arguments)
    def __init__(self, screen):
        self.screen = screen
        self.screen_width, self.screen_height = self.screen.get_size()
        pygame.display.set_caption("Tetris")
        self.running = True
        self.clock = pygame.time.Clock()

        self.menu = Menu()
        self.menu.music_name = "Classic Tetris Music"

        self.gamelaunched = False

        self.left_tick = 0
        self.right_tick = 0
        self.up_tick = 0

        self.last_score = 0

    #Gérer les évenement (input)
    def Handling_events(self):

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL]:
            if keys[pygame.K_1]:
                self.menu.music_name = "Classic Tetris Music"
                pygame.mixer.music.load("assets/musics/tetris_music.mp3")
                pygame.mixer.music.play(-1)
            if keys[pygame.K_2]:
                self.menu.music_name = "Tetris Ragtime Piano"
                pygame.mixer.music.load("assets/musics/Tetris RagTime.mp3")
                pygame.mixer.music.play(-1)

        if not self.menu.run:

            if keys[pygame.K_LEFT] or keys[pygame.K_q]:
                if self.left_tick == 0:
                    self.ingame.currentblock.rect.x -= self.ingame.game_tile_x
                    if pygame.sprite.spritecollide(self.ingame.currentblock, self.ingame.field.cube_group, False):
                        self.ingame.currentblock.rect.x += self.ingame.game_tile_x
                if self.left_tick > 6:
                    self.left_tick = 0
                else:
                    self.left_tick += 1
            else:
                self.left_tick = 0
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                if self.right_tick == 0:
                    self.ingame.currentblock.rect.x += self.ingame.game_tile_x
                    if pygame.sprite.spritecollide(self.ingame.currentblock, self.ingame.field.cube_group, False):
                        self.ingame.currentblock.rect.x -= self.ingame.game_tile_x
                if self.right_tick > 6:
                    self.right_tick = 0
                else:
                    self.right_tick += 1
            else:
                self.right_tick = 0
            if not self.menu.run:
                if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                    self.ingame.currentblock.speed = 10
                else:
                    self.ingame.currentblock.speed = 2

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif not self.menu.run:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP or event.key == pygame.K_z:
                        self.ingame.currentblock.rotate()
                        if pygame.sprite.spritecollide(self.ingame.currentblock, self.ingame.field.cube_group, False):
                            self.ingame.currentblock.rect.x -= self.ingame.game_tile_x
                    if event.key == pygame.K_SPACE:
                        self.ingame.keep_bloc()
                    '''if event.key == pygame.K_LEFT:
                        self.ingame.currentblock.rect.x -= self.ingame.game_tile_x
                    if event.key == pygame.K_RIGHT:
                        self.ingame.currentblock.rect.x += self.ingame.game_tile_x'''

        if self.menu.run:
            if self.menu.exit_button.isPressed():
                self.running = False
            if self.menu.start_button.isPressed():
                self.menu.run = False

    def Update(self):

        if not self.menu.run:
            if not self.gamelaunched:
                self.ingame = inGame()
                self.gamelaunched = True

            if self.ingame.update():
                self.gamelaunched = False
                self.menu.start_button.isHere = True
                self.menu.exit_button.isHere = True
                self.menu.run = True
                self.last_score = self.ingame.score
        else:
            self.menu.update(self.last_score)

    #Afficher/dessiner le jeu
    def Display(self):

        #Colorie l'écran en noir
        screen.fill(BLACK)

        #Si nous somme dans le menu, Dessiner chaque boutons du menu
        if self.menu.run:
            self.menu.Display()
        else:
           self.ingame.draw()

        pygame.display.flip()

    #Boucle de Jeu
    def Run(self):
        while self.running:
            self.Handling_events()
            self.Update()
            self.Display()
            self.clock.tick(60)

pygame.init()

volume = 0.1

pygame.mixer.music.load("assets/musics/tetris_music.mp3")
pygame.mixer.music.set_volume(volume)
pygame.mixer.music.play(-1)

screen = pygame.display.set_mode((600, 700))

game = Game(screen)
game.Run()

pygame.quit()
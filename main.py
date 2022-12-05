import pygame
from obj import Obj
from obj import Button

pygame.init()


class Main:

    def __init__(self, x, y, titulo, icone, musica):

        self.rect = None
        self.MousePos = None
        self.mouse = None
        self.tela = pygame.display.set_mode([x, y])
        pygame.display.set_caption(titulo)
        pygame.display.set_icon(pygame.image.load(icone))

        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self.loop = True

        self.tela_menu = Obj('game/menu.jpg', 0, 0)
        self.tittle = Obj('game/titulo.png', 40, 20)

    def buttons(self):
        ButtonGrups = pygame.sprite.Group()

        Botton_1 = Button(1, self.tela, 'game/start1.png', 'game/start2.png', ButtonGrups)
        Botton_1.rect.center = (120, 320)

        Botton_2 = Button(1, self.tela, 'game/options1.png', 'game/options2.png', ButtonGrups)
        Botton_2.rect.center = (120, 420)

        Botton_3 = Button(0, self.tela, 'game/quit.png', 'game/quit.png', ButtonGrups)
        Botton_3.rect.center = (120, 520)

        ButtonGrups.update()
        ButtonGrups.draw(self.tela)

    def draw(self):
        self.tela_menu.drawing(self.tela)
        self.tittle.drawing(self.tela)

    def events(self):
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                self.loop = False

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            self.buttons()
            pygame.display.update()


game = Main(800, 600, "Aconselhador do Reino", 'game/icone.jpeg', 'game/Medieval.mp3')
game.update()

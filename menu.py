import pygame
from obj import Obj, Button

class Menu:
    def __init__(self, tela):

        self.loop = True
        self.change_scene = False
        self.tela_menu = Obj('game/menu.jpg', 0, 0)
        self.tittle = Obj('game/titulo.png', 40, 20)
        self.tela = tela

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

    def draw(self, tela):
        self.tela_menu.drawing(tela)
        self.tittle.drawing(tela)

    def update(self):
        while self.loop:
            self.draw()
            self.buttons()
            pygame.display.update()

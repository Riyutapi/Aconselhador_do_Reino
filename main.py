import pygame
from pygame.locals import *
import sys

pygame.init()
tela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Aconselhador do Reino")
icon = pygame.image.load('game/icone.jpeg')
pygame.display.set_icon(icon)

pygame.mixer.music.load('game/Medieval.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


def placa():
    pygame.draw.rect(tela, (100, 48, 8), pygame.Rect(200, 150, 400, 300))
    pygame.draw.rect(tela, (75, 73, 71), pygame.Rect(200, 150, 400, 300), 5)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 155, 390, 290), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 175, 390, 250), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 200, 390, 200), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 225, 390, 150), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 250, 390, 100), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 275, 390, 50), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 300, 390, 4), 4)
    pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(580, 130, 40, 40))
    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(580, 130, 40, 40), 3)

class Start(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.MousePos = None
        self.mouse = None
        self.image = pygame.image.load("game/start1.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load('game/start1.png').convert()
        self.image1.set_colorkey((255, 255, 255))
        self.image1.convert_alpha()

        self.image2 = pygame.image.load("game/start2.png").convert()
        self.image2.set_colorkey((255, 0, 255))
        self.image2.convert_alpha()

        self.touche = False

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                self.image = self.image2
                placa()
            else:
                self.touche = False
                self.image = self.image1
        pass


class Options(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.MousePos = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()
        self.image = pygame.image.load("game/options1.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load('game/options1.png').convert()
        self.image1.set_colorkey((255, 255, 255))
        self.image1.convert_alpha()

        self.image2 = pygame.image.load("game/options2.png").convert()
        self.image2.set_colorkey((255, 0, 255))
        self.image2.convert_alpha()

        self.touche = False

    def update(self):
        self.mouse = pygame.mouse.get_pressed()
        self.MousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(self.MousePos):
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                self.image = self.image2
                placa()

            else:
                self.touche = False
                self.image = self.image1
        pass


class Quit(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.MousePos = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()
        self.image = pygame.image.load("game/quit1.png").convert()
        self.image.set_colorkey((255, 255, 255))
        self.image.convert_alpha()
        self.rect = self.image.get_rect()

        self.touche = False

    def update(self):
        if self.rect.collidepoint(self.MousePos):
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                pygame.quit()
                sys.exit()
        pass


def menu():
    background_menu = pygame.image.load('game/menu.jpg')
    titulo = pygame.image.load('game/titulo.png').convert()
    titulo.set_colorkey((255, 255, 255))
    tela.blit(background_menu, (0, 0))
    tela.blit(titulo, (85, 20))

    ButtonGrups = pygame.sprite.Group()

    Botton_1 = Start(ButtonGrups)
    Botton_1.rect.center = (120, 320)

    Botton_2 = Options(ButtonGrups)
    Botton_2.rect.center = (120, 420)

    Botton_3 = Quit(ButtonGrups)
    Botton_3.rect.center = (120, 520)

    ButtonGrups.update()
    ButtonGrups.draw(tela)


while True:

    for sair in pygame.event.get():
        if sair.type == QUIT:
            pygame.quit()
            sys.exit()

    menu()

    pygame.display.update()

import pygame
import sys


def placa(tela):
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

class Obj:

    def __init__(self, image, x, y):

        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)

        self.sprite.image = pygame.image.load(image).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect[0] = x
        self.sprite.rect[1] = y

    def drawing(self, tela):
        self.group.draw(tela)


class Button(pygame.sprite.Sprite):
    def __init__(self, number, tela, imagem1, imagem2, *groups):
        super().__init__(*groups)

        self.MousePos = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()
        self.image = pygame.image.load(imagem1).convert_alpha()
        self.rect = self.image.get_rect()

        self.image1 = pygame.image.load(imagem1).convert_alpha()
        self.image2 = pygame.image.load(imagem2).convert_alpha()

        self.tela = tela
        self.condicao = number
        self.touche = False

    def update(self):
        if self.rect.collidepoint(self.MousePos):
            if self.mouse[0]:
                self.touche = True
                pygame.mouse.get_rel()
                if self.condicao == 0:
                    pygame.mouse.get_rel()
                    pygame.quit()
                    sys.exit()

                self.image = self.image2
                placa(self.tela)


            else:
                self.touche = False
                self.image = self.image1


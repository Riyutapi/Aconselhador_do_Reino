import pygame
import sys


def placa(tela):
    pygame.draw.rect(tela, (100, 48, 8), pygame.Rect(200, 150, 400, 300))
    pygame.draw.rect(tela, (75, 73, 71), pygame.Rect(200, 150, 400, 300), 5)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 155, 390, 290), 4)
    for i in range(5):
        pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, (175 + (i * 25)), 390, 250 - (i * 50)), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 300, 390, 4), 4)
    pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(580, 130, 40, 40))
    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(580, 130, 40, 40), 3)


class Obj:
    def __init__(self, image, x, y):
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(image).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    def drawing(self, tela):
        self.group.draw(tela)


class Button(pygame.sprite.Sprite):
    def __init__(self, number, tela, imagem1, imagem2, *groups, toggle_placa, main):
        super().__init__(*groups)

        self.MousePos = pygame.mouse.get_pos()
        self.mouse = pygame.mouse.get_pressed()
        self.image_normal = pygame.image.load(imagem1).convert_alpha()
        self.image1 = self.image_normal.copy()  # Crie uma cópia da imagem normal
        self.image2 = pygame.image.load(imagem2).convert_alpha()
        self.image = self.image1  # Imagem inicial definida como image1

        self.rect = self.image.get_rect()

        self.tela = tela
        self.condicao = number
        self.touche = False
        self.toggle_placa = toggle_placa
        self.main = main


class Main:
    def __init__(self, x, y, titulo, icone, musica):
        pygame.init()
        self.tela = pygame.display.set_mode([x, y])
        pygame.display.set_caption(titulo)
        pygame.display.set_icon(pygame.image.load(icone))

        pygame.mixer.music.load(musica)
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

        self.loop = True

        self.tela_menu = Obj('game/menu.jpg', 0, 0)
        self.tittle = Obj('game/titulo.png', 40, 20)
        self.display_placa = False  # Variável para controlar a exibição da placa

        self.button_grups = pygame.sprite.Group()  # Definindo button_grups como um atributo da classe

        self.create_buttons()

    def create_buttons(self):
        # Cria os botões e os adiciona ao grupo de botões (button_grups)
        button_positions = [(120, 320), (120, 420), (120, 520)]
        button_images = [('game/start1.png', 'game/start2.png'),
                         ('game/options1.png', 'game/options2.png'),
                         ('game/quit.png', 'game/quit.png')]

        for i in range(len(button_positions)):
            button = Button(i + 1, self.tela, button_images[i][0], button_images[i][1], self.button_grups,
                            toggle_placa=self.toggle_placa, main=self)
            button.rect.center = button_positions[i]

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.loop = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.display_placa:
                    mouse_pos = pygame.mouse.get_pos()
                    if not (200 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 450):
                        continue  # Ignora o evento se o clique não estiver dentro da placa
                    if 580 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 170:
                        self.toggle_placa()

                for button in self.button_grups:
                    if button.rect.collidepoint(event.pos):
                        if button.condicao == 3:
                            sys.exit()
                        elif button.condicao == 1:
                            button.image = button.image2
                        elif button.condicao == 2:
                            button.image = button.image2
                        if not self.display_placa:
                            self.toggle_placa()

    def draw(self):
        self.tela_menu.drawing(self.tela)
        self.tittle.drawing(self.tela)

        if self.display_placa:
            placa(self.tela)

    def update(self):
        while self.loop:
            self.draw()
            self.events()
            self.button_grups.update()
            self.button_grups.draw(self.tela)
            pygame.display.update()

    def toggle_placa(self):
        self.display_placa = not self.display_placa
        for button in self.button_grups:
            if button.condicao == 1 and not self.display_placa:
                button.image = button.image1
            if button.condicao == 2 and not self.display_placa:
                button.image = button.image1


game = Main(800, 600, "Aconselhador do Reino", 'game/icone.jpeg', 'game/Medieval.mp3')
game.update()

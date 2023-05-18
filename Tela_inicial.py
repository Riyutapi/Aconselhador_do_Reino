import pygame
import sys


class Obj:  # Classe objeto para receber uma imagem, converter em sprite, posicionar e desenhar
    def __init__(self, image, x, y):  # Receber as imagens e posições
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(image).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    def drawing(self, tela):  # Desenhar na tela
        self.group.draw(tela)


def botao(tela):  # Desenhar os botões
    # Posição e as imagens
    botao_posicao = [(35, 280), (35, 380), (35, 480)]
    botao_start = ('game/start1.png', 'game/start2.png')
    botao_options = ('game/options1.png', 'game/options2.png')
    botao_quit = Obj('game/quit.png', botao_posicao[2][0], botao_posicao[2][1])

    # Variações das imagens dos botões e o índice delas
    botao_start_objs = [Obj(img, botao_posicao[0][0], botao_posicao[0][1]) for img in botao_start]
    botao_start_objs[game.botao_start_index].drawing(tela)
    botao_options_objs = [Obj(img, botao_posicao[1][0], botao_posicao[1][1]) for img in botao_options]
    botao_options_objs[game.botao_options_index].drawing(tela)
    botao_quit.drawing(tela)


def painel(tela):  # Desenhar um painel com comandos do pygame
    # Painel
    pygame.draw.rect(tela, (100, 48, 8), pygame.Rect(200, 150, 400, 300))
    pygame.draw.rect(tela, (75, 73, 71), pygame.Rect(200, 150, 400, 300), 5)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 155, 390, 290), 4)
    for i in range(5):
        y = (175 + (i * 25))
        altura = 250 - (i * 50)
        pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, y, 390, altura), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 300, 390, 4), 4)

    # Botão para fechar
    pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(580, 130, 40, 40))
    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(580, 130, 40, 40), 3)
    fechar_img = Obj('game/fechar.png', 580, 130)
    fechar_img.drawing(tela)


def opcao(tela):  # Desenhar as opções do painel do botão options
    # Imagens
    opcao_images = ['game/placa2.png', 'game/credits.png', 'game/sound.png']
    som_images = ['game/som(0).png', 'game/som(0.3).png', 'game/som(0.6).png', 'game/som(1).png']

    # Posição delas e desenhar
    placa1_img = Obj(opcao_images[0], 340, 210)
    placa2_img = Obj(opcao_images[0], 340, 325)
    credits_img = Obj(opcao_images[1], 345, 350)
    sound_img = Obj(opcao_images[2], 340, 175)
    placa1_img.drawing(tela)
    sound_img.drawing(tela)
    placa2_img.drawing(tela)
    credits_img.drawing(tela)

    # Variações das imagens do som e o índice delas
    som_images_objs = [Obj(img, 350, 212) for img in som_images]
    som_images_objs[game.som_image_index].drawing(tela)


def credit(tela):  # Desenhar os créditos no painel das opções
    credit_images = ['game/creditos.png', 'game/placa2.png', 'game/voltar.png']
    creditos_img = Obj(credit_images[0], 100, 155)
    placa3_img = Obj(credit_images[1], 340, 350)
    voltar_img = Obj(credit_images[2], 370, 358)
    creditos_img.drawing(tela)
    placa3_img.drawing(tela)
    voltar_img.drawing(tela)


class Main:  # Classe de iniciação
    def __init__(self, x, y, titulo, icone, musica):
        pygame.init()

        # Janela
        self.tela = pygame.display.set_mode([x, y])
        pygame.display.set_caption(titulo)
        pygame.display.set_icon(pygame.image.load(icone))

        # Índice dos botões no começo
        self.som_image_index = 3
        self.botao_start_index = 0
        self.botao_options_index = 0

        # Musica
        pygame.mixer.music.load(musica)
        pygame.mixer.music.play(-1)

        # Manter a execução do programa
        self.loop = True

        # Background
        self.tela_menu = Obj('game/fundo.jpg', 0, 0)
        self.tittle = Obj('game/titulo.png', 40, 20)

        # Janelas abertas pelos botões
        self.abrir_painel = False
        self.abrir_credit = False

    def toggle_som(self):  # Mudar a imagem do botão som e o volume da música
        if self.som_image_index == 3:
            self.som_image_index = 2
            pygame.mixer.music.set_volume(0.6)
        elif self.som_image_index == 2:
            self.som_image_index = 1
            pygame.mixer.music.set_volume(0.3)
        elif self.som_image_index == 1:
            self.som_image_index = 0
            pygame.mixer.music.set_volume(0)
        else:
            self.som_image_index = 3
            pygame.mixer.music.set_volume(1)

    def draw(self):  # O que será desenhado na tela
        global call_opcao  # Poder utilizar como parâmetro nos events
        # Os desenhos que se mantém durante a tela inicial
        self.tela_menu.drawing(self.tela)
        self.tittle.drawing(self.tela)
        botao(self.tela)

        if self.abrir_painel:  # Verificar se precisa abrir o painel
            painel(self.tela)
            call_opcao = False
            if self.botao_options_index == 1:  # Verificar se o painel foi aberto pelo botão das options
                call_opcao = True
                if self.abrir_credit:  # Verificar se apertarão o botão credits
                    credit(self.tela)
                    call_opcao = False
            if call_opcao:  # Abrir as opções do botão options
                opcao(self.tela)

    def fechar_painel(self):  # Fechar o painel e mudar a imagem do botão
        self.abrir_painel = not self.abrir_painel
        if self.botao_options_index == 1 and not self.abrir_painel:
            self.botao_options_index = 0
        if self.botao_start_index == 1 and not self.abrir_painel:
            self.botao_start_index = 0
        self.abrir_credit = False

    def update(self):  # Manter a janela atualizada
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()

    def events(self):  # Os eventos que ocorrerão conforme o click do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fechar a janela se apertarem o 'x' dela
                self.loop = False
            # Verificar o click do botão esquerdo do mouse
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()  # Verificar a posição do mouse
                if not self.abrir_painel:  # Se o painel estiver fechado
                    if 38 <= mouse_pos[0] <= 200 and 280 <= mouse_pos[1] <= 363:
                        # Mudar o sprite do botão start e abrir o painel
                        self.botao_start_index = 1
                        self.abrir_painel = True
                    elif 38 <= mouse_pos[0] <= 200 and 380 <= mouse_pos[1] <= 463:
                        # Mudar o sprite do botão options e abrir o painel
                        self.botao_options_index = 1
                        self.abrir_painel = True
                    elif 38 <= mouse_pos[0] <= 200 and 480 <= mouse_pos[1] <= 563:
                        sys.exit()  # Fechar o jogo pelo botão quit
                else:  # Se o painel estiver aberto
                    if not (200 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 450):
                        continue  # Ignorar os cliques do mouse se não estiver dentro do painel
                    if 580 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 170:
                        self.fechar_painel()  # Fechar o painel pelo botão dele
                    if self.abrir_credit and 340 <= mouse_pos[0] <= 453 and 350 <= mouse_pos[1] <= 433:
                        self.abrir_credit = False  # Voltar a tela dos credits para options
                    if call_opcao:  # Se apertarem no botão das options
                        if 340 <= mouse_pos[0] <= 453 and 210 <= mouse_pos[1] <= 293:
                            self.toggle_som()  # Mudar o sprite do som e seu volume
                        if 340 <= mouse_pos[0] <= 453 and 325 <= mouse_pos[1] <= 408:
                            self.abrir_credit = True  # Abrir os credits


# Começar a tela inicial
game = Main(800, 600, "Aconselhador do Reino", 'game/icone.jpeg', 'game/Medieval.mp3')
game.update()

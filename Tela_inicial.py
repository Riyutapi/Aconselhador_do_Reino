import pygame
import sys
import os
import re


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
    botao_start = ('game/1_tela_inicial/start1.png', 'game/1_tela_inicial/start2.png')
    botao_options = ('game/1_tela_inicial/options1.png', 'game/1_tela_inicial/options2.png')
    botao_quit = Obj('game/1_tela_inicial/quit.png', botao_posicao[2][0], botao_posicao[2][1])

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
    fechar_img = Obj('game/geral/fechar.png', 580, 130)
    fechar_img.drawing(tela)


def opcao(tela):  # Desenhar as opções no painel do botão options
    # Imagens
    opcao_images = ['game/geral/placa2.png', 'game/1_tela_inicial/credits.png', 'game/1_tela_inicial/sound.png']
    som_images = ['game/1_tela_inicial/som(0).png', 'game/1_tela_inicial/som(0.3).png',
                  'game/1_tela_inicial/som(0.6).png', 'game/1_tela_inicial/som(1).png']
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


def voltar(tela):  # Botão de voltar
    placa3_img = Obj('game/geral/placa2.png', 340, 350)
    voltar_img = Obj('game/geral/voltar.png', 370, 358)
    placa3_img.drawing(tela)
    voltar_img.drawing(tela)


def credit(tela):  # Desenhar os créditos no painel das opções
    creditos_img = Obj('game/1_tela_inicial/creditos.png', 100, 155)
    creditos_img.drawing(tela)
    voltar(tela)


def start(tela):  # Desenhar as opções no painel do botão start
    # Imagens
    start_images = ['game/1_tela_inicial/placa3.png', 'game/1_tela_inicial/novo_jogo.png',
                    'game/1_tela_inicial/continue.png']
    # Posição delas e desenhar
    placa4_img = Obj(start_images[0], 300, 195)
    placa5_img = Obj(start_images[0], 300, 305)
    new_game_img = Obj(start_images[1], 312, 220)
    continue_img = Obj(start_images[2], 330, 335)
    placa4_img.drawing(tela)
    new_game_img.drawing(tela)
    placa5_img.drawing(tela)
    continue_img.drawing(tela)


def novo_jogo(tela):  # Desenhar as opções do novo jogo
    # Imagens
    novo_jogo_images = ['game/1_tela_inicial/nick.png', 'game/geral/certo.png']
    # Posição delas e desenhar
    novo_jogo_img = Obj(novo_jogo_images[0], 320, 180)
    confirmar_img = Obj(novo_jogo_images[1], 525, 255)
    novo_jogo_img.drawing(tela)
    confirmar_img.drawing(tela)
    voltar(tela)
    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(280, 250, 240, 50))


def criar_arquivo(texto):  # Criar arquivo save com o nick
    pasta = "save"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    arquivo = open(os.path.join(pasta, "save.txt"), "w")
    arquivo.write("nick = " + texto + '\n')
    arquivo.close()


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
        self.tela_menu = Obj('game/1_tela_inicial/fundo.jpg', 0, 0)
        self.tittle = Obj('game/1_tela_inicial/titulo.png', 40, 20)

        # Janelas abertas pelos botões
        self.abrir_painel = False
        self.abrir_credit = False
        self.abrir_novo_jogo = False
        self.abrir_continue = False
        self.exibir_mensagem_tela = False

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
        global call_start
        # Os desenhos que se mantém durante a tela inicial
        self.tela_menu.drawing(self.tela)
        self.tittle.drawing(self.tela)
        botao(self.tela)

        if self.abrir_painel:  # Verificar se precisa abrir o painel
            painel(self.tela)
            call_opcao = False
            call_start = False
            if self.botao_options_index == 1:  # Verificar se o painel foi aberto pelo botão das options
                call_opcao = True
                if self.abrir_credit:  # Verificar se foi clickado o botão credits
                    credit(self.tela)
                    call_opcao = False
            elif self.botao_start_index == 1:  # Verificar se o painel foi aberto pelo botão das start
                call_start = True
                if self.abrir_novo_jogo:  # Verificar se foi clickado o botão New Game
                    self.exibir_mensagem_tela = False
                    novo_jogo(self.tela)
                    call_start = False

                    texto = ""
                    texto_digitado = True
                    contador = 0

                    while texto_digitado:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:  # Fechar a janela se apertarem o 'x' dela
                                self.loop = False
                                texto_digitado = False
                            # Verificar o click do botão esquerdo do mouse
                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                mouse_pos = pygame.mouse.get_pos()  # Verificar a posição do mouse
                                if 580 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 170:
                                    self.fechar_painel()  # Fechar o painel pelo botão dele
                                    texto_digitado = False
                                if 340 <= mouse_pos[0] <= 452 and 350 <= mouse_pos[1] <= 433:
                                    self.abrir_novo_jogo = False  # Voltar a tela de New Game para start
                                    texto_digitado = False
                                if texto != "" and 528 <= mouse_pos[0] <= 564 and 255 <= mouse_pos[1] <= 295:
                                    criar_arquivo(texto)  # Salvar o Nickname em um arquivo
                                    sys.exit()
                            else:
                                if event.type == pygame.KEYDOWN:  # Verificar a tecla do teclado
                                    if event.key == pygame.K_BACKSPACE:  # Apagar o que foi digitado
                                        texto = texto[:-1]
                                    elif event.key == pygame.K_RETURN or event.key == pygame.K_TAB \
                                            or event.key == pygame.K_ESCAPE:  # Ignorar teclas
                                        pass
                                    else:
                                        if len(texto) < 8:  # Verificar se o Nickname atingiu o limite de 8 caracteres
                                            texto += event.unicode
                                            ultima_letra = event.unicode

                                            # Arrumar o acento '~' para funcionar como de costume
                                            if event.unicode == '~' and contador == 0:
                                                contador += 1
                                                texto = texto[:-1]
                                            elif event.unicode == '~' and contador == 1:
                                                contador = 0
                                            elif ultima_letra != '~' and contador == 1:
                                                contador = 0

                                novo_jogo(self.tela)  # Redesenhar a tela de novo jogo
                                self.exibir_mensagem(texto, 255, 255, 255, 260)  # Desenhar texto na tela
                                pygame.display.flip()  # Atualizar o que está sendo digitado
                if self.abrir_continue:  # Verificar se foi clickado o botão Continue
                    arquivo = os.path.join("save", "save.txt")
                    if os.path.exists(arquivo):  # Verificar se o arquivo save existe
                        with open(arquivo, 'r') as file:
                            conteudo = file.read()
                            padrao = r"nick = (.+)"
                            resultado = re.search(padrao, conteudo)  # Contar quantos caracteres existem no nick
                            if resultado:
                                inicio = resultado.start(1)
                                fim = resultado.end(1)
                                caracteres = conteudo[inicio:fim]
                                if len(caracteres) <= 8:  # Se for do tamanho certo
                                    sys.exit()
                                elif self.exibir_mensagem_tela:   # Se for do tamanho errado
                                    self.exibir_mensagem("Error", 255, 0, 0, 115)
                            elif self.exibir_mensagem_tela:  # Se não existir nick
                                self.exibir_mensagem("Error", 255, 0, 0, 115)
                    elif self.exibir_mensagem_tela:   # Se não existir arquivo save
                        self.exibir_mensagem("Not Found", 255, 0, 0, 115)
            if call_opcao:  # Abrir as opções do botão options
                opcao(self.tela)
            elif call_start:  # Abrir as opções do botão options
                start(self.tela)

    def fechar_painel(self):  # Fechar o painel e mudar a imagem do botão
        self.abrir_painel = not self.abrir_painel
        if self.botao_options_index == 1 and not self.abrir_painel:
            self.botao_options_index = 0
        if self.botao_start_index == 1 and not self.abrir_painel:
            self.botao_start_index = 0
        self.abrir_credit = False
        self.abrir_novo_jogo = False

    def exibir_mensagem(self, mensagem, red, blue, green, y):  # Exibir mensagem
        cor = (red, blue, green)
        fonte = pygame.font.SysFont("Bookman Old Style", 30)
        texto_surface = fonte.render(mensagem, True, cor)
        largura_texto = texto_surface.get_width()
        posicao_texto = ((self.tela.get_width() - largura_texto) // 2, y)
        self.tela.blit(texto_surface, posicao_texto)

    def update(self):  # Manter a janela atualizada
        while self.loop:
            self.draw()
            self.events()
            pygame.display.update()  # Atualizar parte da tela

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
                        self.exibir_mensagem_tela = False
                    if (self.abrir_credit or self.abrir_novo_jogo) and 340 <= mouse_pos[0] <= 452 \
                            and 350 <= mouse_pos[1] <= 433:
                        self.abrir_credit = False  # Voltar a tela dos credits para options
                        self.abrir_novo_jogo = False  # Voltar a tela do novo jogo para start
                    if call_opcao:  # Se apertarem no botão das options
                        if 340 <= mouse_pos[0] <= 452 and 210 <= mouse_pos[1] <= 292:
                            self.toggle_som()  # Mudar o sprite do som e seu volume
                        if 340 <= mouse_pos[0] <= 452 and 325 <= mouse_pos[1] <= 407:
                            self.abrir_credit = True  # Abrir os credits
                    if call_start:  # Se apertarem no botão do start
                        if 304 <= mouse_pos[0] <= 494 and 203 <= mouse_pos[1] <= 284:
                            self.abrir_novo_jogo = True  # Criar arquivo save com nick
                        if 304 <= mouse_pos[0] <= 494 and 313 <= mouse_pos[1] <= 394:
                            self.abrir_continue = True  # Verificar o save
                            self.exibir_mensagem_tela = True  # Mensagem se tiver algo errado no save


# Começar a tela inicial
game = Main(800, 600, "Aconselhador do Reino", 'game/1_tela_inicial/icone.jpeg', 'game/1_tela_inicial/Medieval.mp3')
game.update()

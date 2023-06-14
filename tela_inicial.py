import pygame
import sys
import os
import re
from comum import Obj, exibir_mensagem


def botao(tela: pygame.Surface):
    """
    Desenha os botões na tela fornecida.

    Args:
        tela (pygame.Surface): Superfície da tela onde os botões serão desenhados.

    """
    # Posição e as imagens
    botao_posicao = [(35, 280), (35, 380), (35, 480)]
    botao_start = ('1_tela_inicial/start1.png', '1_tela_inicial/start2.png')
    botao_options = ('1_tela_inicial/options1.png', '1_tela_inicial/options2.png')
    botao_quit = Obj('1_tela_inicial/quit.png', botao_posicao[2][0], botao_posicao[2][1])
    # Variações das imagens dos botões e o índice delas
    botao_start_objs = [Obj(img, botao_posicao[0][0], botao_posicao[0][1]) for img in botao_start]
    botao_start_objs[botao_start_index].drawing(tela)
    botao_options_objs = [Obj(img, botao_posicao[1][0], botao_posicao[1][1]) for img in botao_options]
    botao_options_objs[botao_options_index].drawing(tela)
    botao_quit.drawing(tela)


def painel(tela: pygame.Surface):
    """
    Desenha um painel com comandos do pygame na tela fornecida.

    Args:
        tela (pygame.Surface): Superfície da tela onde o painel será desenhado.

    """
    # Desenho do painel
    pygame.draw.rect(tela, (100, 48, 8), pygame.Rect(200, 150, 400, 300))
    pygame.draw.rect(tela, (75, 73, 71), pygame.Rect(200, 150, 400, 300), 5)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 155, 390, 290), 4)
    for i in range(5):
        y = (175 + (i * 25))
        altura = 250 - (i * 50)
        pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, y, 390, altura), 4)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(205, 300, 390, 4), 4)
    # Desenho do botão para fechar
    pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(580, 130, 40, 40))
    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(580, 130, 40, 40), 3)
    fechar_img = Obj('geral/fechar.png', 580, 130)
    fechar_img.drawing(tela)


def opcao(tela: pygame.Surface):
    """
    Desenha as opções no painel de botões de opções.

    Args:
        tela (pygame.Surface): Superfície da tela onde as opções serão desenhadas.

    """
    # Imagens
    opcao_images = ['geral/placa2.png', '1_tela_inicial/credits.png', '1_tela_inicial/sound.png']
    som_images = ['geral/som(0).png', 'geral/som(0.3).png',
                  'geral/som(0.6).png', 'geral/som(1).png']
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
    som_images_objs[som_image_index].drawing(tela)


def voltar(tela: pygame.Surface):
    """
    Exibe um botão de voltar na tela fornecida.

    Args:
        tela (pygame.Surface): Superfície da tela onde o botão será exibido.

    """
    placa3_img = Obj('geral/placa2.png', 340, 350)
    voltar_img = Obj('geral/voltar.png', 370, 358)
    placa3_img.drawing(tela)
    voltar_img.drawing(tela)


def credit(tela: pygame.Surface):
    """
    Desenha os créditos na tela do painel de opções.

    Args:
        tela (pygame.Surface): Superfície da tela onde os créditos serão desenhados.

    """
    creditos_img = Obj('1_tela_inicial/creditos.png', 100, 155)
    creditos_img.drawing(tela)
    voltar(tela)


def start(tela: pygame.Surface):
    """
    Desenha as opções no painel do botão "Start".

    Args:
        tela (pygame.Surface): Superfície da tela onde as opções serão desenhadas.
        
    """
    # Imagens
    start_images = ['geral/placa3.png', '1_tela_inicial/novo_jogo.png', '1_tela_inicial/continue.png']
    # Posiciona as imagens
    placa4_img = Obj(start_images[0], 300, 195)
    placa5_img = Obj(start_images[0], 300, 305)
    new_game_img = Obj(start_images[1], 312, 220)
    continue_img = Obj(start_images[2], 330, 335)
    # Desenhar as imagens
    placa4_img.drawing(tela)
    new_game_img.drawing(tela)
    placa5_img.drawing(tela)
    continue_img.drawing(tela)


def novo_jogo(tela: pygame.Surface):
    """
    Desenha as opções do novo jogo na tela fornecida.

    Args:
        tela (pygame.Surface): Superfície da tela onde as opções serão desenhadas.

    """
    # Imagens
    novo_jogo_images = ['1_tela_inicial/nick.png', 'geral/certo.png']
    # Posição delas e desenhar
    novo_jogo_img = Obj(novo_jogo_images[0], 320, 180)
    confirmar_img = Obj(novo_jogo_images[1], 525, 255)
    novo_jogo_img.drawing(tela)
    confirmar_img.drawing(tela)
    voltar(tela)
    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(280, 250, 240, 50))


def criar_arquivo(texto: str):
    """
    Cria um arquivo de save com o nick fornecido e variavel para mudar o minigame.

    Args:
        texto (str): Nick a ser salvo no arquivo.

    """
    pasta = "save"
    if not os.path.exists(pasta):
        os.makedirs(pasta)
    arquivo = open(os.path.join(pasta, "save.txt"), "w")
    arquivo.write("nick = " + texto + '\navancar = 1')
    arquivo.close()


def escurecer(tela: pygame.Surface):
    """
    Escurece a tela e diminui o som da musica gradualmente.

    Args:
        tela (pygame.Surface): Superfície da tela a ser escurecida.

    """
    # Verificar o volume da música
    if som_image_index == 3:
        volume = 1
    elif som_image_index == 2:
        volume = 0.6
    elif som_image_index == 1:
        volume = 0.3
    else:
        volume = 0
    # Salvar o volume da música no arquivo save.txt
    pasta = "save"
    with open(os.path.join(pasta, "save.txt"), 'r') as arquivo:
        conteudo = arquivo.read()
        linhas = conteudo.split("\n")
        volume_existente = False
        # Verificar se existe volume no arquivo save
        for i, linha in enumerate(linhas):
            if "volume = " in linha:
                linhas[i] = "volume = " + str(volume)
                volume_existente = True
                break
        # Se não existir, adicionar a linha de volume
        if not volume_existente:
            linhas.append("volume = " + str(volume))
    # Sobregravar o arquivo save.txt com as linhas atualizadas
    with open(os.path.join(pasta, "save.txt"), 'w') as arquivo:
        arquivo.write("\n".join(linhas))
    # Crie uma superfície preta do mesmo tamanho da tela
    superficie_preta = pygame.Surface((800, 600))
    superficie_preta.fill((0, 0, 0))
    # Escurecer a imagem gradualmente
    for opacidade in range(255):
        for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
        # Redesenhar os elementos na tela
        tela_menu.drawing(tela)
        tittle.drawing(tela)
        botao(tela)
        # Definir a opacidade da superfície preta
        superficie_preta.set_alpha(opacidade)
        # Aplicar a superfície preta à tela
        tela.blit(superficie_preta, (0, 0))

        if opacidade % 25 == 0:  # Ajustar volume da música gradualmente
            pygame.mixer.music.set_volume(volume)
            volume -= 0.1
        # Atualizar a tela
        pygame.display.flip()
        # Aguardar um curto período de tempo entre cada quadro
        pygame.time.wait(5)


def tela_inicial(tela: pygame.Surface):
    """
    Função principal.

    Args:
        tela (pygame.Surface): Superfície da tela a ser escurecida.

    Return:
        None, pois as modificações para a progressão do game está no arquivo save

    """
    # Variaveis usadas em várias funções
    global som_image_index
    global botao_start_index
    global botao_options_index
    global tela_menu
    global tittle
    # Index da imagem inicial
    som_image_index = 3
    botao_start_index = 0
    botao_options_index = 0
    # Musica
    pygame.mixer.music.load('1_tela_inicial/Medieval.mp3')
    pygame.mixer.music.play(-1)
    # Som das placas
    placa_som = pygame.mixer.Sound('geral/placa.wav')
    # Arquivo save
    arquivo = os.path.join("save", "save.txt")
    if os.path.exists(arquivo):  # Verificar se o arquivo save existe
        with open(arquivo, 'r') as file:
            conteudo = file.read()
            linhas = conteudo.split("\n")  # Divide o conteúdo em linhas
            for linha in linhas:
                if "volume = " in linha:  # Verificar o volume segundo o save
                    valor_volume = linha.split("=")[-1].strip()
                    volume = float(valor_volume)
                    if volume == 1:
                        som_image_index = 3
                        pygame.mixer.music.set_volume(1)
                        placa_som.set_volume(1)
                    elif volume == 0.6:
                        som_image_index = 2
                        pygame.mixer.music.set_volume(0.6)
                        placa_som.set_volume(0.6)
                    elif volume == 0.3:
                        som_image_index = 1
                        pygame.mixer.music.set_volume(0.3)
                        placa_som.set_volume(0.3)
                    else:
                        som_image_index = 0
                        pygame.mixer.music.set_volume(0)
                        placa_som.set_volume(0)
    # Background
    tela_menu = Obj('1_tela_inicial/fundo.png', 0, 0)
    tittle = Obj('1_tela_inicial/titulo.png', 40, 20)
    # Janelas abertas pelos botões
    abrir_painel = False
    abrir_credit = False
    abrir_novo_jogo = False
    abrir_continue = False
    exibir_mensagem_tela = False

    while True:
        # O que será mostrado na tela
        tela_menu.drawing(tela)
        tittle.drawing(tela)
        botao(tela)
        if abrir_painel:  # Verificar se precisa abrir o painel
            painel(tela)
            call_opcao = False
            call_start = False
            if botao_options_index == 1:  # Verificar se o painel foi aberto pelo botão das options
                call_opcao = True
                if abrir_credit:  # Verificar se foi clickado o botão credits
                    credit(tela)
                    call_opcao = False
            elif botao_start_index == 1:  # Verificar se o painel foi aberto pelo botão das start
                call_start = True
                if abrir_novo_jogo:  # Verificar se foi clickado o botão New Game
                    # Variáveis de controle
                    exibir_mensagem_tela = False
                    call_start = False
                    texto = ""
                    texto_digitado = True
                    contador = 0
                    # Tela do novo jogo
                    novo_jogo(tela)
                    while texto_digitado:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:  # Fechar o jogo pela janela
                                texto_digitado = False
                            # Verificar o click do botão esquerdo do mouse
                            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                                mouse_pos = pygame.mouse.get_pos()  # Verificar a posição do mouse
                                if 580 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 170:
                                    abrir_painel = not abrir_painel
                                    if botao_options_index == 1 and not abrir_painel:
                                        botao_options_index = 0
                                    if botao_start_index == 1 and not abrir_painel:
                                        botao_start_index = 0
                                    abrir_credit = False
                                    abrir_novo_jogo = False
                                    texto_digitado = False
                                if 340 <= mouse_pos[0] <= 452 and 350 <= mouse_pos[1] <= 433:
                                    placa_som.play()
                                    abrir_novo_jogo = False  # Voltar a tela de New Game para start
                                    texto_digitado = False
                                if texto != "" and 528 <= mouse_pos[0] <= 564 and 255 <= mouse_pos[1] <= 295:
                                    criar_arquivo(texto)  # Salvar o Nickname em um arquivo
                                    escurecer(tela)
                                    pygame.mixer.music.stop()
                                    return
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
                                novo_jogo(tela)  # Redesenhar a tela de novo jogo
                                exibir_mensagem(texto, 255, 255, 255, 30, 0, 260, tela)  # Desenhar texto na tela
                                pygame.display.flip()  # Atualizar o que está sendo digitado
                if abrir_continue:  # Verificar se foi clickado o botão Continue
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
                                    escurecer(tela)
                                    pygame.mixer.music.stop()
                                    return
                                elif exibir_mensagem_tela:   # Se for do tamanho errado
                                    exibir_mensagem("Error", 255, 0, 0, 30, 0, 115, tela)
                            elif exibir_mensagem_tela:  # Se não existir nick
                                exibir_mensagem("Error", 255, 0, 0, 30, 0, 115, tela)
                    elif exibir_mensagem_tela:   # Se não existir arquivo save
                        exibir_mensagem("Not Found", 255, 0, 0, 30, 0, 115, tela)
            if call_opcao:  # Abrir as opções do botão options
                opcao(tela)
            elif call_start:  # Abrir as opções do botão options
                start(tela)
        # Os eventos que ocorrerão conforme o click do mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            # Verificar o click do botão esquerdo do mouse
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()  # Verificar a posição do mouse
                if not abrir_painel:  # Se o painel estiver fechado
                    if 38 <= mouse_pos[0] <= 200 and 280 <= mouse_pos[1] <= 363:
                        # Mudar o sprite do botão start e abrir o painel
                        placa_som.play()
                        botao_start_index = 1
                        abrir_painel = True
                    elif 38 <= mouse_pos[0] <= 200 and 380 <= mouse_pos[1] <= 463:
                        # Mudar o sprite do botão options e abrir o painel
                        placa_som.play()
                        botao_options_index = 1
                        abrir_painel = True
                    elif 38 <= mouse_pos[0] <= 200 and 480 <= mouse_pos[1] <= 563:
                        sys.exit()  # Fechar o jogo pelo botão quit
                else:  # Se o painel estiver aberto
                    if not (200 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 450):
                        continue  # Ignorar os cliques do mouse se não estiver dentro do painel
                    if 580 <= mouse_pos[0] <= 620 and 130 <= mouse_pos[1] <= 170:
                        # Fechar o painel pelo botão dele
                        abrir_painel = not abrir_painel
                        if botao_options_index == 1 and not abrir_painel:
                            botao_options_index = 0
                        if botao_start_index == 1 and not abrir_painel:
                            botao_start_index = 0
                        abrir_credit = False
                        abrir_novo_jogo = False
                        exibir_mensagem_tela = False
                    if (abrir_credit or abrir_novo_jogo) and 340 <= mouse_pos[0] <= 452 \
                            and 350 <= mouse_pos[1] <= 433:
                        placa_som.play()
                        abrir_credit = False  # Voltar a tela dos credits para options
                        abrir_novo_jogo = False  # Voltar a tela do novo jogo para start
                    if call_opcao:  # Se apertarem no botão das options
                        if 340 <= mouse_pos[0] <= 452 and 210 <= mouse_pos[1] <= 292: # Alterar o volume da música
                            if som_image_index == 3:
                                som_image_index = 2
                                pygame.mixer.music.set_volume(0.6)
                                placa_som.set_volume(0.6)
                            elif som_image_index == 2:
                                som_image_index = 1
                                pygame.mixer.music.set_volume(0.3)
                                placa_som.set_volume(0.3)
                            elif som_image_index == 1:
                                som_image_index = 0
                                pygame.mixer.music.set_volume(0)
                                placa_som.set_volume(0)
                            else:
                                som_image_index = 3
                                pygame.mixer.music.set_volume(1)
                                placa_som.set_volume(1)
                        if 340 <= mouse_pos[0] <= 452 and 325 <= mouse_pos[1] <= 407:
                            placa_som.play()
                            abrir_credit = True  # Abrir os credits
                    if call_start:  # Se apertarem no botão do start
                        if 304 <= mouse_pos[0] <= 494 and 203 <= mouse_pos[1] <= 284:
                            placa_som.play()
                            abrir_novo_jogo = True  # Criar arquivo save com nick
                        if 304 <= mouse_pos[0] <= 494 and 313 <= mouse_pos[1] <= 394:
                            placa_som.play()
                            abrir_continue = True  # Verificar o save
                            exibir_mensagem_tela = True  # Mensagem se tiver algo errado no save
        # Atualizar tela
        pygame.display.update()

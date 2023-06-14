import pygame
import os
import sys
from comum import Obj, exibir_mensagem, dialogo_por_letra, dialogo_ocioso

def mapa(tela: pygame.Surface):
    """
    Local: mapa.
    Efeito: transição.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Música e variavel de controle
    pygame.mixer.music.load('1_tela_inicial/Medieval.mp3')
    pygame.mixer.music.play(-1)
    som = 0
    # Imagens do mapa
    imagens = [
        pygame.image.load('mapa/mapa_completo.png').convert_alpha(),
        pygame.image.load('mapa/mapa_cachorro.png').convert_alpha(),
        pygame.image.load('mapa/mapa_leao.png').convert_alpha(),
        pygame.image.load('mapa/mapa_porco.png').convert_alpha(),
        pygame.image.load('mapa/mapa_tatu.png').convert_alpha(),
        pygame.image.load('mapa/mapa_tigre.png').convert_alpha(),
        pygame.image.load('mapa/mapa_tordo.png').convert_alpha(),
        pygame.image.load('mapa/mapa_caveira.png').convert_alpha()
    ]
    # Imagens da província em vermelha
    cachorro = [
        pygame.image.load('mapa/mapa_completo.png').convert_alpha(),
        pygame.image.load('mapa/mapa_leao.png').convert_alpha(),
        pygame.image.load('mapa/mapa_porco.png').convert_alpha(),
        pygame.image.load('mapa/mapa_tatu.png').convert_alpha(),
        pygame.image.load('mapa/mapa_tigre.png').convert_alpha(),
        pygame.image.load('mapa/mapa_tordo.png').convert_alpha(),
        pygame.image.load('mapa/mapa_caveira.png').convert_alpha()
    ]

    while True:
        for opacidade in range(255):  # Clarear a imagem gradualmente
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
            
            # Ajustar volume da música gradualmente
            if som < volume and opacidade % 25 == 0:
                som += 0.1
                pygame.mixer.music.set_volume(som)

            # Redesenhar imagens na tela
            tela.blit(superficie_preta, (0, 0))
            for imagem in imagens:
                imagem.set_alpha(opacidade)
                tela.blit(imagem, (0, 0))
            pygame.display.flip()

        while True:  # Efeito do território piscando
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
            for imagem in imagens:  # Mapa
                tela.blit(imagem, (0, 0))
            pygame.display.flip()
            pygame.time.wait(400)
            for imagem in cachorro:  # Província
                tela.blit(imagem, (0, 0))
            pygame.display.flip()
            pygame.time.wait(400)


def cutscene12(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.
    Efeito: transição.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto12 = "Confie em mim. A única vez que eu errei\nfoi quando achei que tinha errado."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    while True:
                        som = volume
                        for opacidade in range(255, -1, -1):  # Escurecer a imagem gradualmente
                            for evento in pygame.event.get():
                                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                                    pygame.quit()
                                    sys.exit()
                            if som != 0:  # Diminuir a música gradualmente
                                if opacidade % 25 == 0:
                                    som -= 0.1
                                    pygame.mixer.music.set_volume(som)
                            # Desenhar na tela com opacidade
                            tela.blit(superficie_preta, (0, 0))
                            sala_trono.set_alpha(opacidade)
                            aconselhador_invertido.set_alpha(opacidade)
                            rei_triste.set_alpha(opacidade)
                            tela.blit(sala_trono, (0, 0))
                            tela.blit(aconselhador_invertido, (-40, 260))
                            tela.blit(rei_triste, (258, 90))
                            pygame.display.flip()
                        # Próxima cutscene
                        mapa(tela)
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto12, aconselhador, tela)
        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto12, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto12, aconselhador, tela)


def cutscene11(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto11 = "Mas como eu irei jogar vava? E como você\nsabe que ele trocaria o território por uma\nplaca de vídeo?"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene12(tela)
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto11, rei_derrota, tela)
        # Exibir diálogo do rei
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_derrota, texto11, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto11, rei_derrota, tela)


def cutscene10(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto10 = "sua RTX 4060 Ti em troca do território dele,\ncertamente ele aceitará."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene11(tela)
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto10, aconselhador, tela)
        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto10, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto10, aconselhador, tela)


def cutscene9(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto9 = "Meu rei, o duque Jopô é aspirante a piloto de\nbalão e gaymer, se você desafiá-lo em uma\n" + \
             "corrida de balões, colocando como prêmio"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene10(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto9, aconselhador, tela)
        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto9, tela)
        # Avançar a animação de ociosidade do personagem
        contador = dialogo_ocioso(contador, nick, texto9, aconselhador, tela)


def cutscene8(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto8 = "Pelo nome já conseguiria deduzir de quem\nera. Qual seu plano para recuperarmos\nessa província?"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene9(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto8, rei_derrota, tela)
        # Exibir diálogo do rei
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_derrota, texto8, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto8, rei_derrota, tela)


def cutscene7(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto7 = "Iniciaremos com a província mais próxima,\na auto proclamada como Ducado de Jopô,\ninstaurada pelo duque Jopô."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene8(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto7, aconselhador, tela)
        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto7, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto7, aconselhador, tela)


def cutscene6(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto6 = "Odeio burocracia. Como vamos lidar com\nessa situação?"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene7(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto6, rei_derrota, tela)
        # Exibir diálogo do rei
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_derrota, texto6, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto6, rei_derrota, tela)


def cutscene5(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto5 = "Por motivos burocráticos."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene6(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto5, aconselhador, tela)
        # Exibir diálogo do conselheiro
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto5, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto5, aconselhador, tela)


def cutscene4(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Mudar imagem do rei
    tela.blit(sala_trono, (0, 0))
    tela.blit(aconselhador_invertido, (-40, 260))
    tela.blit(rei_triste, (258, 90))
    pygame.display.flip()
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto5 = "Mas o que? Por que só fui informado disso\nagora?"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene5(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto5, rei_derrota, tela)
        # Exibir diálogo do rei
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_derrota, texto5, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto5, rei_derrota, tela)


def cutscene3(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto4 = "Bem agora que encerramos as festividades,\nlamento informar, mas estamos enfrentando\nvárias revoltas."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene4(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto4, aconselhador, tela)
        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto4, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto4, aconselhador, tela)


def cutscene2(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.
    Efeito: transição e sonoros.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    texto3 = "Todos saúdam o novo rei!"
    passar = False
    # Imagens
    rei_feliz = pygame.image.load('personagens_cenario/rei-vitoria.png').convert_alpha()
    aconselhador = Obj('personagens_falas/aconselhador.png', 43, 476)
    # Variável de controle, Música e sons
    som = 0

    pygame.mixer.music.load('geral/Trono.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(som)

    aplauso_som = pygame.mixer.Sound('2_corrida_balao/aplausos.wav')
    porta_som = pygame.mixer.Sound('2_corrida_balao/porta.wav')
    aplauso_som.set_volume(volume)
    porta_som.set_volume(volume)

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
        exibir_mensagem("Duas Semanas Depois...", 255, 255, 255, 50, 0, 0, tela)
        pygame.display.flip()
        tempo_inicial1 = pygame.time.get_ticks()
        while pygame.time.get_ticks() - tempo_inicial1 < 1500:  # Esperar mensagem
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  #Ignorar clicke do mouse
                    pass
        for opacidade in range(255):  # Clarear a imagem gradualmente
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
            if som < volume:  # Ajustar volume da música gradualmente
                if opacidade % 25 == 0:
                    som += 0.1
                    pygame.mixer.music.set_volume(som)
            # Redesenhar a tela
            tela.blit(superficie_preta, (0, 0))
            sala_trono.set_alpha(opacidade)
            rei_feliz.set_alpha(opacidade)
            aconselhador_invertido.set_alpha(opacidade)
            tela.blit(sala_trono, (0, 0))
            tela.blit(rei_feliz, (258, 90))
            tela.blit(aconselhador_invertido, (-40, 260))
            pygame.display.flip()
            pygame.time.wait(5)
        # Com diálogo
        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                    if passar:  # Avançar cena
                        while True:
                            for evento in pygame.event.get():
                                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                                    pygame.quit()
                                    sys.exit()
                                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  #Ignorar clicke do mouse
                                    pass
                                else:  # Avançar cena
                                    tela.blit(sala_trono, (0, 0))
                                    tela.blit(rei_feliz, (258, 90))
                                    tela.blit(aconselhador_invertido, (-40, 260))
                                    pygame.display.flip()
                                    aplauso_som.play()
                                    tempo_inicial = pygame.time.get_ticks()
                                    while pygame.time.get_ticks() - tempo_inicial < 6000:  # Esperar aplausos
                                        for evento in pygame.event.get():
                                            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                                                pygame.quit()
                                                sys.exit()
                                            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  #Ignorar clicke do mouse
                                                pass
                                    tempo_inicial2 = pygame.time.get_ticks()
                                    porta_som.play()
                                    while pygame.time.get_ticks() - tempo_inicial2 < 3000:  # Esperar porta fechando
                                        for evento in pygame.event.get():
                                            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                                                pygame.quit()
                                                sys.exit()
                                            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  #Ignorar clicke do mouse
                                                pass
                                    cutscene3(tela)
                    if not passar:  # Manter cena
                        passar = True
                        # Animação do avançar_dialogo
                        contador = dialogo_ocioso(contador, nick, texto3, aconselhador, tela)
            # Exibir diálogo do aconselhador
            if not passar:  # Exibir letra por letra
                contador, passar = dialogo_por_letra(nick, aconselhador, texto3, tela)
            # Animação do avançar_dialogo
            contador = dialogo_ocioso(contador, nick, texto3, aconselhador, tela)


def cutscene1(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: quarto do castelo.
    Efeito: transição.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto2 = "Lamentamos o falecimento do rei, mas\nvocê deve assumir a responsabilidade.\nSua coroação será daqui duas semanas."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo com clique do mouse
                if passar:  # Avançar cena
                    som = volume
                    for opacidade in range(255, -1, -1):  # Escurecer a imagem gradualmente
                        for evento in pygame.event.get():
                            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                                pygame.quit()
                                sys.exit()
                        if som != 0:  # Ajustar volume da música gradualmente
                            if opacidade % 25 == 0:
                                som -= 0.1
                                pygame.mixer.music.set_volume(som)
                        tela.blit(superficie_preta, (0, 0))
                        quarto_castelo.set_alpha(opacidade)
                        tela.blit(quarto_castelo, (0, 0))
                        pygame.display.flip()
                        pygame.time.wait(5)
                    cutscene2(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto2, aconselhador, tela)
        # Diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto2, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto2, aconselhador, tela)


def cutscene(tela: pygame.Surface):
    """
    Emissor: príncipe.
    Local: quarto do castelo.
    Efeito: transição.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    """
    # Texto do diálogo
    texto = "Primeiro minha mãe, agora meu pai…"
    # Criar objeto para o personagem principal
    principe_luto = Obj('personagens_falas/principe-velorio.png', 43, 476)
    # Carregar e reproduzir música de fundo
    pygame.mixer.music.load('2_corrida_balao/Melancolia.mp3')
    pygame.mixer.music.play(-1)
    # Definir variáveis de controle
    passar = False
    som = 0
    # Tela sem diálogo
    for opacidade in range(255):  # Clarear a imagem gradualmente
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
        if som < volume:  # Ajustar volume da música gradualmente
            if opacidade % 25 == 0:
                som += 0.1
                pygame.mixer.music.set_volume(som)
        # Redesenhar a tela
        tela.blit(superficie_preta, (0, 0))
        quarto_castelo.set_alpha(opacidade)
        tela.blit(quarto_castelo, (0, 0))
        pygame.display.flip()
        pygame.time.wait(5)
    # Com diálogo
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene1(tela)
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Príncipe", texto, principe_luto, tela)
        # Exibir diálogo do príncipe
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Príncipe", principe_luto, texto, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Príncipe", texto, principe_luto, tela)


def corrida_balao(tela: pygame.Surface):
    """
    Função principal que controla a progressão do jogo de corrida de balão.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Returns:
        None, pois as modificações para a progressão do jogo estão no arquivo save.

    """
    # Variaveis usadas em várias funções
    global aconselhador
    global contador
    global nick
    global volume
    global superficie_preta
    global rei_derrota
    global quarto_castelo
    global sala_trono
    global aconselhador_invertido
    global rei_triste
    # Ler o arquivo save.txt para obter o nickname e o nivel do volume
    arquivo = os.path.join("save", "save.txt")
    with open(arquivo, 'r') as file:
        conteudo = file.read()
        linhas = conteudo.split("\n")
        for linha in linhas:  # Conteudo por linha
            if "nick =" in linha:  # Nickname
                nickname = linha.split("=")[-1].strip()
                nick = str(nickname)
            if "volume = " in linha:  # Volume
                valor_volume = linha.split("=")[-1].strip()
                volume = float(valor_volume)
    # Tela preta
    superficie_preta = pygame.Surface((800,600))
    superficie_preta.fill((0, 0, 0))
    # Imagens
    rei_triste = pygame.image.load('personagens_cenario/rei-derrota.png').convert_alpha()
    quarto_castelo = pygame.image.load('2_corrida_balao/quarto_castelo.png').convert()
    rei_derrota = Obj('personagens_falas/rei-derrota.png', 43, 476)
    aconselhador = Obj('personagens_falas/aconselhador.png', 43, 476)
    sala_trono = pygame.image.load('geral/trono.png').convert()
    aconselhador_sala = pygame.image.load('personagens_cenario/aconselhador.png').convert_alpha()
    aconselhador_invertido = pygame.transform.flip(aconselhador_sala, True, False)
    # Variável para animar o avançar_dialogo
    contador = 0
    # Iniciar as cutscenes
    cutscene(tela)
    #Loop Principal
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                quit()

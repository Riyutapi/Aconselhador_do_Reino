import pygame, sys, os, time, random
from typing import List, Tuple, Optional
from comum import Obj, exibir_mensagem, pause, dialogo_por_letra, \
    dialogo_ocioso, nick_volume, definir_volume, resultado


def final_corrida2(tela: pygame.Surface, vencedor: int):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela onde a sequência final será executada.
        vencedor (int): Indica o resultado da corrida (0 para derrota, 1 para vitória).
        
    Return:
        None, para voltar a cutscene anterior

    """
    passar2 = False
    texto_derrota2 = "Não temos tempo para lamentar a derrota."
    texto_vitoria2 = "Não temos tempo para comemorar a vitória."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar2:  # Avançar cena
                    return
                
                if not passar2:  # Manter a cena
                    passar2 = True
                    # Animação do avançar_dialogo
                    if vencedor == 0:
                        contador = dialogo_ocioso(contador, nick, texto_derrota2, aconselhador, tela)
                    elif vencedor == 1:
                        contador = dialogo_ocioso(contador, nick, texto_vitoria2, aconselhador, tela)

        # Exibir diálogo do aconselhador
        if not passar2:  # Exibir letra por letra
            if vencedor == 0:
                contador, passar2 = dialogo_por_letra(nick, aconselhador, texto_derrota2, tela)
            elif vencedor == 1:
                contador, passar2 = dialogo_por_letra(nick, aconselhador, texto_vitoria2, tela)

        # Animação do avançar_dialogo
        if vencedor == 0:
            contador = dialogo_ocioso(contador, nick, texto_derrota2, aconselhador, tela)
        elif vencedor == 1:
            contador = dialogo_ocioso(contador, nick, texto_vitoria2, aconselhador, tela)


def final_corrida(tela: pygame.Surface, vencedor: int, lista_imagem_final: List[Tuple[pygame.Surface, Tuple[int, int]]]):
    """
    Emissor: rei.
    Local: sala do trono.
    Efeito: transições.
    Mecânica: atualizar o arquivo save.

    Args:
        tela (pygame.Surface): Superfície da tela onde a sequência final será executada.
        vencedor (int): Indica o resultado da corrida (0 para derrota, 1 para vitória).
        lista_imagem_final (List[Tuple[pygame.Surface, Tuple[int, int]]]): Lista de imagens e sua localização no final do jogo.
   
    Return:
        None, para voltar a cutscene anterior

    """
    passar = False
    texto_derrota1 = "Droga! Perdi minha placa de vídeo, e ele\nnão quer mais nada em troca do território."
    texto_vitoria1 = "Viva! Consegui manter minha placa de vídeo\ne reconquistar o território."
    som = 0

    pasta = "save"
    vitorias = 0
    minigame1 = 0
    avancar = 2  # Valor a ser atualizado

    if vencedor == 1:
        vitorias = 1
        minigame1 = 1

    with open(os.path.join(pasta, "save.txt"), 'r') as arquivo:
        conteudo = arquivo.read()
        linhas = conteudo.split("\n")
        vitorias_existente = False
        minigame1_existente = False

    # Atualizar vitorias no arquivo save
    for i, linha in enumerate(linhas):
        if "vitorias = " in linha:
            linhas[i] = "vitorias = " + str(vitorias)
            vitorias_existente = True
            break

    # Atualizar minigame1 no arquivo save
    for i, linha in enumerate(linhas):
        if "minigame1 = " in linha:
            linhas[i] = "minigame1 = " + str(minigame1)
            minigame1_existente = True
            break

    # Atualizar avancar no arquivo save
    for i, linha in enumerate(linhas):
        if "avancar = " in linha:
            linhas[i] = "avancar = " + str(avancar)
            break

    # Se não existir, adicionar as linhas de vitorias, minigame1 e avancar
    if not vitorias_existente:
        linhas.append("vitorias = " + str(vitorias))

    if not minigame1_existente:
        linhas.append("minigame1 = " + str(minigame1))

    if not any("avancar = " in linha for linha in linhas):
        linhas.append("avancar = " + str(avancar))

    # Sobregravar o arquivo save.txt com as linhas atualizadas
    with open(os.path.join(pasta, "save.txt"), 'w') as arquivo:
        arquivo.write("\n".join(linhas))

    while True:
        for opacidade1 in range(255, -1, -1):  # Escurecer a imagem gradualmente
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
            
            # Ajustar volume da música gradualmente
            if opacidade1 % 25 == 0:
                som -= 0.1
                pygame.mixer.music.set_volume(som)

            # Redesenhar imagens na tela
            tela.blit(superficie_preta, (0, 0))
            for i in range(0, len(lista_imagem_final), 2):
                imagem = lista_imagem_final[i]
                coordenadas = lista_imagem_final[i+1]
                imagem.set_alpha(opacidade1)
                tela.blit(imagem, coordenadas)

            pygame.display.flip()
            pygame.time.wait(5)  # Aguardar um curto período de tempo entre cada quadro

        break
    
    pygame.mixer.music.load('geral/Trono.mp3')
    pygame.mixer.music.play(-1)

    while True:
        for opacidade2 in range(255):  # Clarear a imagem gradualmente
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()

            if som < volume:  # Ajustar volume da música gradualmente
                if opacidade2 % 25 == 0:
                    som += 0.1
                    pygame.mixer.music.set_volume(som)

            # Redesenhar a tela
            tela.blit(superficie_preta, (0, 0))
            sala_trono.set_alpha(opacidade2)
            aconselhador_invertido.set_alpha(opacidade2)
            tela.blit(sala_trono, (0, 0))
            tela.blit(aconselhador_invertido, (-40, 260))

            if vencedor == 0:
                rei_triste.set_alpha(opacidade2)
                tela.blit(rei_triste, (258, 90))
                
            elif vencedor == 1:
                rei_feliz.set_alpha(opacidade2)
                tela.blit(rei_feliz, (258, 90))

            pygame.display.flip()
            pygame.time.wait(5)  # Aguardar um curto período de tempo entre cada quadro

        break

    while True:
        pygame.mixer.music.set_volume(volume)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    final_corrida2(tela, vencedor)
                    return
                
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    if vencedor == 0:
                        contador = dialogo_ocioso(contador, "Rei", texto_derrota1, rei_derrota, tela)
                    elif vencedor == 1:
                        contador = dialogo_ocioso(contador, "Rei", texto_vitoria1, rei_vitoria, tela)

        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            if vencedor == 0:
                contador, passar = dialogo_por_letra("Rei", rei_derrota, texto_derrota1, tela)
            elif vencedor == 1:
                contador, passar = dialogo_por_letra("Rei", rei_vitoria, texto_vitoria1, tela)

        # Animação do avançar_dialogo
        if vencedor == 0:
            contador = dialogo_ocioso(contador, "Rei", texto_derrota1, rei_derrota, tela)
        elif vencedor == 1:
            contador = dialogo_ocioso(contador, "Rei", texto_vitoria1, rei_vitoria, tela)


def meio_corrida2(tela: pygame.Surface):
    """
    Emissor: jopo.
    Local: corrida.

    Args:
        tela (pygame.Surface): Superfície da tela onde a sequência final será executada.
        
    Return:
        None, para voltar a cutscene anterior

    """
    passar2 = False
    texto17 = "Como eu poderia ter feito isso?"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar2:  # Avançar cena
                    return
                
                if not passar2:  # Manter a cena
                    passar2 = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Jôpo", texto17, jopo, tela)

        # Exibir diálogo do aconselhador
        if not passar2:  # Exibir letra por letra
            contador, passar2 = dialogo_por_letra("Jôpo", jopo, texto17, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Jôpo", texto17, jopo, tela)


def meio_corrida(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: corrida.

    Args:
        tela (pygame.Surface): Superfície da tela onde a sequência final será executada.

    Return:
        1, para iniciar o contador de tempo para a metade da corrida

    """
    passar = False
    texto16 = "Você que chamou esse bicho?"
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    meio_corrida2(tela)
                    return 1
                
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto16, rei_derrota, tela)

        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_derrota, texto16, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto16, rei_derrota, tela)


def inicio_corrida2(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: corrida.

    Args:
        tela (pygame.Surface): Superfície da tela onde a sequência final será executada.
        
    Return:
        None, para voltar a cutscene anterior

    """
    passar = False
    texto15 = "Você acha que é o rei da cocada preta?\nNão sei como seu balão consegue carregar\ntanta arrogância."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    return
                
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto15, rei_vitoria, tela)

        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_vitoria, texto15, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto15, rei_vitoria, tela)


def inicio_corrida(tela: pygame.Surface):
    """
    Emissor: jopo.
    Local: corrida.
    Efeito: transição.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar ao laço principal

    """
    # Música e variavel de controle
    pygame.mixer.music.load('2_corrida_balao/jogo/Corrida.mp3')
    pygame.mixer.music.play(-1)
    som = 0

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
            ceu.set_alpha(opacidade)
            jopo_balao.set_alpha(opacidade)
            player_balao.set_alpha(opacidade)
            tela.blit(ceu, (0, 0))
            tela.blit(jopo_balao, (10, 160))
            tela.blit(player_balao, (10, 15))
            pygame.display.flip()

        passar = False
        texto14 = "Hoje, serei o vitorioso desta competição.\nTodos serão testemunhas do meu domínio\nabsoluto sobre o céu!"

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()

                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                    if passar:  # Avançar cena
                        inicio_corrida2(tela)
                        return
                    
                    if not passar:  # Manter a cena
                        passar = True
                        # Animação do avançar_dialogo
                        contador = dialogo_ocioso(contador, "Jôpo", texto14, jopo, tela)

            # Exibir diálogo do aconselhador
            if not passar:  # Exibir letra por letra
                contador, passar = dialogo_por_letra("Jôpo", jopo, texto14, tela)
            # Animação do avançar_dialogo
            contador = dialogo_ocioso(contador, "Jôpo", texto14, jopo, tela)


def mapa(tela: pygame.Surface):
    """
    Local: mapa.
    Efeito: transição.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

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

        for _ in range(0, 5):
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()

            for imagem in imagens:  # Mapa
                tela.blit(imagem, (0, 0))

            pygame.display.flip()
            pygame.time.wait(400)  # Aguardar um curto período de tempo entre cada quadro

            for imagem in cachorro:  # Província
                tela.blit(imagem, (0, 0))

            pygame.display.flip()
            pygame.time.wait(400)  # Aguardar um curto período de tempo entre cada quadro

        for opacidade in range(255, -1, -1):  # Escurecer a imagem gradualmente
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
            
            # Ajustar volume da música gradualmente
            if opacidade % 25 == 0:
                som -= 0.1
                pygame.mixer.music.set_volume(som)

            # Redesenhar imagens na tela
            tela.blit(superficie_preta, (0, 0))
            for imagem in imagens:
                imagem.set_alpha(opacidade)
                tela.blit(imagem, (0, 0))

            pygame.display.flip()

        inicio_corrida(tela)

        return


def cutscene13(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.
    Efeito: transição.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto13 = "Confie em mim. A única vez que eu errei\nfoi quando achei que tinha errado."

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
                        return
                    
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto13, aconselhador, tela)
                    
        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto13, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto13, aconselhador, tela)


def cutscene12(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto12 = "Mas como eu irei jogar vava? E como você\nsabe que ele trocaria o território por uma\nplaca de vídeo?"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene13(tela)
                    return
                
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto12, rei_derrota, tela)

        # Exibir diálogo do rei
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_derrota, texto12, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto12, rei_derrota, tela)


def cutscene11(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto11 = "sua RTX 4060 Ti em troca do território dele,\ncertamente ele aceitará."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene12(tela)
                    return
                
                if not passar:  # Manter a cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto11, aconselhador, tela)

        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto11, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto11, aconselhador, tela)


def cutscene10(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto10 = "Meu rei, o duque Jôpo é aspirante a piloto de\nbalão e gaymer, se você desafiá-lo em uma\n" + \
             "corrida de balões, colocando como prêmio"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene11(tela)
                    return
                
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto10, aconselhador, tela)

        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto10, tela)
        # Avançar a animação de ociosidade do personagem
        contador = dialogo_ocioso(contador, nick, texto10, aconselhador, tela)


def cutscene9(tela: pygame.Surface):
    """
    Emissor: rei.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto9 = "Pelo nome já conseguiria deduzir de quem\nera. Qual seu plano para recuperarmos\nessa província?"

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
                
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene10(tela)
                    return
                
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Rei", texto9, rei_derrota, tela)

        # Exibir diálogo do rei
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Rei", rei_derrota, texto9, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Rei", texto9, rei_derrota, tela)


def cutscene8(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto8 = "Iniciaremos com a província mais próxima,\na auto proclamada como Ducado de Jopô,\ninstaurada pelo duque Jopô."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene9(tela)
                    return
                
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, nick, texto8, aconselhador, tela)

        # Exibir diálogo do aconselhador
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra(nick, aconselhador, texto8, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, nick, texto8, aconselhador, tela)


def cutscene7(tela: pygame.Surface):
    """
    Emissor: aconselhador.
    Local: sala do trono.

    Args:
        tela (pygame.Surface): Superfície da tela do jogo.

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    passar = False
    texto7 = "Vamos desafiá-las, e para ficarem propensas\na aceitar, vamos colocar a condição que\neles vencerão em caso de empate."

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene8(tela)
                    return
                
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

    Return:
        None, para voltar a cutscene anterior

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
                    return
                
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

    Return:
        None, para voltar a cutscene anterior

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
                    return
                
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

    Return:
        None, para voltar a cutscene anterior

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
                    return
                
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

    Return:
        None, para voltar a cutscene anterior

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
                    return
                
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

    Return:
        None, para voltar a cutscene anterior

    """
    # Variável de controle para avançar o diálogo e texto do diálogo
    texto3 = "Todos saúdam o novo rei!"
    passar = False

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
        tempo_inicial = pygame.time.get_ticks()

        while pygame.time.get_ticks() - tempo_inicial < 1500:  # Esperar mensagem
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
            pygame.time.wait(5)  # Aguardar um curto período de tempo entre cada quadro

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

                                    porta_som.play()
                                    tempo_inicial = pygame.time.get_ticks()

                                    while pygame.time.get_ticks() - tempo_inicial < 3000:  # Esperar mensagem
                                        for evento in pygame.event.get():
                                            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                                                pygame.quit()
                                                sys.exit()

                                            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  #Ignorar clicke do mouse
                                                pass

                                    cutscene3(tela)
                                    return
                                
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

    Return:
        None, para voltar a cutscene anterior

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
                        pygame.time.wait(5)  # Aguardar um curto período de tempo entre cada quadro

                    cutscene2(tela)
                    return
                
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

    Return:
        None, para sair da cutscene

    """
    # Texto do diálogo
    texto = "Primeiro minha mãe, agora meu pai…"

    # Criar objeto para o personagem principal
    principe_luto = Obj('personagens_falas/principe-velorio.png', 43, 481)

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
        pygame.time.wait(5)  # Aguardar um curto período de tempo entre cada quadro

    # Com diálogo
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Avançar o diálogo
                if passar:  # Avançar cena
                    cutscene1(tela)
                    return
                
                if not passar:  # Manter cena
                    passar = True
                    # Animação do avançar_dialogo
                    contador = dialogo_ocioso(contador, "Príncipe", texto, principe_luto, tela)

        # Exibir diálogo do príncipe
        if not passar:  # Exibir letra por letra
            contador, passar = dialogo_por_letra("Príncipe", principe_luto, texto, tela)
        # Animação do avançar_dialogo
        contador = dialogo_ocioso(contador, "Príncipe", texto, principe_luto, tela)


def criar_obstaculo(obstaculo: List[bool], quantidade: int, numero: List[int], dificuldade: List[int]):
    """
    Cria obstáculos aleatoriamente com base nas configurações fornecidas.

    Args:
        obstaculo (List[bool]): Lista do obstáculo.
        quantidade (int): Quantidade total de obstáculos a serem criados.
        numero (List[int]): Lista de números gerados aleatóriamente para determinar se deve criar o obstáculo.
        dificuldade (List[int]): Lista de valores de dificuldade para a criação dos obstáculos.

    Returns:
        List[int]: Lista atualizada de números para criar o obstáculo.

    """
    for d in range(quantidade):
        if obstaculo.count(True) == d:
            for a in range(quantidade):
                if numero[a] == 0: 
                    numero[a] = random.randint(0, dificuldade[d])
                    break

    return numero



def limpar_tudo(quantidade: int, obstaculo: List[bool], box: List[List[pygame.Rect]], numero: List[int], \
                fire: bool, obstaculo_x: List[int], obstaculo_y: Optional[List[int]] = None):
    """
    Limpa todas as variáveis relacionadas aos obstáculos.

    Args:
        quantidade (int): Quantidade total de obstáculos.
        obstaculo (List[bool]): Lista de status dos obstáculos.
        box (List[List[pygame.Rect]]): Lista das hitbox.
        numero (List[int]): Lista de números associados aos obstáculos.
        fire (bool): Indica se é a bola de fogo.
        obstaculo_x (List[int]): Lista das coordenadas X dos obstáculos.
        obstaculo_y (Optional[List[int]], optional): Lista das coordenadas Y dos obstáculos. Padrão é None. 

    Returns:
        List[bool], lista atualizada de obstáculos.
        List[int], lista atualizada de números.
        List[List[pygame.Rect]], lista atualizada de hitbox.
        List[int], lista atualizada de coordenadas X dos obstáculos.
        Optional[List[int]]: lista atualizada de coordenadas Y dos obstáculos.

    """
    if fire:  # Se for bola de fogo, elas surgirão nas coordenadas da boca do dragão
        obstaculo_x = [454] * quantidade
        if obstaculo_y is not None:
            obstaculo_y = [270] * quantidade
    else:  # Se não, surgirão nas coordenadas no final da tela
        obstaculo_x = [tamanho_x] * quantidade
        if obstaculo_y is not None:
            obstaculo_y = [tamanho_y] * quantidade

    box = [[pygame.Rect(0, 0, 0, 0)] for _ in range(quantidade)]
    obstaculo = [False] * quantidade
    numero = [0] * quantidade

    return obstaculo, numero, box, obstaculo_x, obstaculo_y


def limpar_um(obstaculo: bool, box: List[pygame.Rect], numero: int, fire: bool, obstaculo_x: int, obstaculo_y: Optional[int] = None):
    """
    Limpa as variáveis relacionadas a um único obstáculo.

    Args:
        obstaculo (bool): Status do obstáculo.
        box (List[pygame.Rect]): Lista da hitbox.
        numero (int): Número associado ao obstáculo.
        fire (bool): Indica se é uma bola de fogo.
        obstaculo_x (int): Coordenada X do obstáculo.
        obstaculo_y (Optional[int], optional): Coordenada Y do obstáculo. Padrão é None.

    Returns:
        bool, atualização do obstáculo
        int, atualização do número
        List[pygame.Rect], lista atalizada da hitbox
        int, atualização da coordenada X
        Optional[int]: atualização da coordenada Y.

    """
    if fire:
        obstaculo_x = 454
        obstaculo_y = 270 if obstaculo_y is not None else None

    else:
        obstaculo_x = tamanho_x
        obstaculo_y = tamanho_y if obstaculo_y is not None else None

    box.clear()
    numero = 0
    obstaculo = False

    return obstaculo, numero, box, obstaculo_x, obstaculo_y


def movimento_jopo_balao_y(jopo_balao_x: int, jopo_balao_y: int, list_hitbox: List[pygame.Rect]):
    """
    Realiza o movimento vertical do personagem jopo_balao.

    Args:
        jopo_balao_x (int): Coordenada X do personagem jopo_balao.
        jopo_balao_y (int): Coordenada Y do personagem jopo_balao.
        list_hitbox (List[pygame.Rect]): Lista de hitbox dos obstáculos.

    Returns:
        int, a nova coordenada Y atualizada do personagem jopo_balao.

    """
    # Variável de controle da movimentação
    subindo = 0

    # Definir limites da tela
    limite_superior = 0
    limite_inferior = 600

    # Encontrar obstáculo
    movimentar, valor_y, altura = movimento_obstaculo(jopo_balao_x, jopo_balao_y, list_hitbox)

    if movimentar:  # Se detectar algum obstáculo
        if jopo_balao_y + 250 >= valor_y + altura:  
            # Se a parte inferior do jopo_balao estiver acima da parte superior do obstáculo, ele irá subir
            subindo = 1
            if limite_superior <= valor_y <= 250:  # Se o obstáculo estiver na parte superior da tela, ele irá descer
                subindo = 2

        elif 350 <= valor_y <= limite_inferior:  # Se o obstáculo estiver na parte inferior da tela, ele irá subir
                subindo = 1
        
        else:  # Se não, ele irá subir
            subindo = 1

        if subindo == 1 and jopo_balao_y > limite_superior:  # Subir respeitando o limite
            jopo_balao_y -= 4

        if subindo == 2 and jopo_balao_y + 250 < limite_inferior:  # Descer respeitando o limite
            jopo_balao_y += 4
    
    return jopo_balao_y


def movimento_obstaculo(jopo_balao_x: int, jopo_balao_y: int, list_hitbox: List[List[pygame.Rect]]):
    """
    Verifica se há obstáculos próximos ao personagem jopo_balao e retorna informações sobre eles.

    Args:
        jopo_balao_x (int): Coordenada X do personagem jopo_balao.
        jopo_balao_y (int): Coordenada Y do personagem jopo_balao.
        list_hitbox (List[List[pygame.Rect]]): Lista contendo listas de hitbox dos obstáculos.

    Returns:
        obstaculo_detectado (bool), indica se um obstáculo foi detectado próximo ao personagem jopo_balao.
        valor_y (int), coordenada Y do obstáculo detectado.
        altura (int), altura do obstáculo detectado.

    """
    # Hitbox da detecção do jopo_balao (ela é maior que a verdadeira hitbox dele, para que consiga desviar)
    box_jopo = [pygame.Rect(0, 0, 0, 0)]
    box_jopo.append(pygame.Rect(jopo_balao_x, jopo_balao_y - 10, 350, 270))

    # Variáveis de controle
    obstaculo_detectado = False
    valor_y = 0
    altura = 0

    # Verificar a lista de hitbox
    for hitbox_list in list_hitbox:  # Verificar a lista de obstáculos (árvore, nuvem, vento, pombo, bola de fogo)
        for hitbox in hitbox_list:  # Verificar a lista de cada obstáculo (árvore 1, árvore 2 ...)
            for box in box_jopo:  # Verificar a lista do jopo_balao
                if box.colliderect(hitbox):  # Se colide
                    obstaculo_detectado = True
                    valor_y = hitbox.y
                    altura = hitbox.height
                    break

    return obstaculo_detectado, valor_y, altura


def exibir_numero(tela: pygame.Surface):
    """
    Exibir os número 3 2 1 na tela com um intervalo entre eles.

    Args:
        tela (pygame.Surface): Superfície da tela onde a sequência será executada.

    """
    for numero in range(3, 0, -1):
        pygame.draw.circle(tela, (0, 0, 0), (400, 300), 185)
        exibir_mensagem(str(numero), 255, 255, 255, 398, 0, 0, tela)
        pygame.display.flip()
        tempo_inicial = pygame.time.get_ticks()
        while pygame.time.get_ticks() - tempo_inicial < 1000:  # Esperar mensagem
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()
                
                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  # Ignorar clique do mouse
                    pass
                

def manual(tela: pygame.Surface):
    """
    Função para exibir as instruções do jogo.

    Args:
        tela (pygame.Surface): A superfície onde as imagens serão exibidas.

    Returns:
        int, começando o tempo incial em 0.

    """
    tutorial = Obj('2_corrida_balao/jogo/tutorial.png', 0, 0)

    instrucao = True
    while instrucao:
        # Começo do game e as instruções
        tela.blit(ceu, (0, 0))
        tela.blit(jopo_balao, (10, 160))
        tela.blit(player_balao, (10, 15))
        tutorial.drawing(tela)
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            # Verificar o clique do botão esquerdo do mouse
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                mouse_pos = pygame.mouse.get_pos()  # Verificar a posição do mouse
                if 133 <= mouse_pos[0] <= 667 and 293 <= mouse_pos[1] <= 367:  # Se apertarem no "ok"
                    tela.blit(ceu, (0, 0))
                    tela.blit(jopo_balao, (10, 160))
                    tela.blit(player_balao, (10, 15))
                    instrucao = False

    exibir_numero(tela)

    return 0


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
    global nick
    global volume
    global superficie_preta
    global rei_derrota
    global rei_vitoria
    global quarto_castelo
    global sala_trono
    global aconselhador_invertido
    global rei_feliz
    global rei_triste
    global ceu
    global jopo_balao
    global player_balao
    global jopo
    global tamanho_x
    global tamanho_y

    # Sempre bom iniciar o pygame para evitar erros
    pygame.init()
    
    # Capturar o tamanho da tela
    tamanho_x = tela.get_width()
    tamanho_y = tela.get_height()

    # Ler o arquivo save.txt para obter o nickname e o nivel do volume
    nick, volume = nick_volume()
    som_image_index, volume = definir_volume(volume, False)

    # Tela preta
    superficie_preta = pygame.Surface((tamanho_x, tamanho_y))
    superficie_preta.fill((0, 0, 0))

    # Imagens
    # Cenário
    quarto_castelo = pygame.image.load('2_corrida_balao/quarto_castelo.png').convert()
    sala_trono = pygame.image.load('geral/trono.png').convert()
    ceu = pygame.image.load('2_corrida_balao/jogo/ceu.png').convert_alpha()
    ceu_2 = ceu

    # Personagem no cenário
    rei_triste = pygame.image.load('personagens_cenario/rei-derrota.png').convert_alpha()
    rei_feliz = pygame.image.load('personagens_cenario/rei-vitoria.png').convert_alpha()
    aconselhador_sala = pygame.image.load('personagens_cenario/aconselhador.png').convert_alpha()
    aconselhador_invertido = pygame.transform.flip(aconselhador_sala, True, False)

    # Personagens durante fala
    rei_derrota = Obj('personagens_falas/rei-derrota.png', 43, 481)
    rei_vitoria = Obj('personagens_falas/rei-vitoria.png', 43, 481)
    aconselhador = Obj('personagens_falas/aconselhador.png', 43, 481)
    jopo = Obj('personagens_falas/jopo.png', 43, 481)

    # Avisos
    opcao = Obj('geral/esc.png', 0, 0)
    aviso = Obj('2_corrida_balao/jogo/alerta.png', 307, 210)

    # Sons
    aviso_som = pygame.mixer.Sound('2_corrida_balao/jogo/alerta.wav')
    aviso_som.set_volume(volume)

    vitoria_som = pygame.mixer.Sound('geral/vitoria.wav')
    derrota_som = pygame.mixer.Sound('geral/derrota.wav')

    vitoria_som.set_volume(volume)
    derrota_som.set_volume(volume)


    # Elementos da corrida

    # Imagens
    jopo_balao = pygame.image.load('2_corrida_balao/jogo/balao_jopo.png').convert_alpha()
    jopo_balao_atingido = pygame.image.load('2_corrida_balao/jogo/balao_jopo_atingido.png').convert_alpha()

    player_balao = pygame.image.load('2_corrida_balao/jogo/balao_player.png').convert_alpha()
    player_balao_atingido = pygame.image.load('2_corrida_balao/jogo/balao_player_atingido.png').convert_alpha()

    dragao_imagens = [
        pygame.image.load('2_corrida_balao/jogo/dragao_0.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/dragao_1.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/dragao_2.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/dragao_3.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/dragao_4.png').convert_alpha()]
    dragao_imagens_invertido = [pygame.transform.flip(imagem, True, False) for imagem in dragao_imagens]

    chegada_imagens = [
        pygame.image.load('2_corrida_balao/jogo/linha_chegada_0.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/linha_chegada_1.png').convert_alpha()]

    topo_arvore = pygame.image.load('2_corrida_balao/jogo/arvore.png').convert_alpha()

    nuvem_carregada = pygame.image.load('2_corrida_balao/jogo/nuvem_carregada.png').convert_alpha()

    vento_imagens = [pygame.image.load('2_corrida_balao/jogo/vento_0.png').convert_alpha(),
            pygame.image.load('2_corrida_balao/jogo/vento_1.png').convert_alpha()]

    pombo_imagens = [
        pygame.image.load('2_corrida_balao/jogo/pomba_0.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/pomba_1.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/pomba_2.png').convert_alpha(),
        pygame.image.load('2_corrida_balao/jogo/pomba_3.png').convert_alpha()]

    fogo_imagens = [pygame.image.load('2_corrida_balao/jogo/bola_fogo_0.png').convert_alpha(),
            pygame.image.load('2_corrida_balao/jogo/bola_fogo_1.png').convert_alpha()]


    # Sprite inicial
    sprite_player = player_balao
    sprite_jopo = jopo_balao 
    indice_imagem_dragao = 0
    indice_imagem_chegada = 0
    indice_imagem_vento = 0
    indice_imagem_pombo = 0
    indice_imagem_fogo = 0


    #Sons
    dragao_chegada_som = pygame.mixer.Sound('2_corrida_balao/jogo/dragao_chegada.wav')
    dragao_som = pygame.mixer.Sound('2_corrida_balao/jogo/dragao_parado.wav')
    chegada_som = pygame.mixer.Sound('2_corrida_balao/jogo/chegada.wav')
    arvore_som = pygame.mixer.Sound('2_corrida_balao/jogo/arvore.wav')
    nuvem_som = pygame.mixer.Sound('2_corrida_balao/jogo/nuvem.wav')
    vento_som = pygame.mixer.Sound('2_corrida_balao/jogo/vento.wav')
    pombo_som = pygame.mixer.Sound('2_corrida_balao/jogo/pombo.wav')
    fogo_som = pygame.mixer.Sound('2_corrida_balao/jogo/fogo.wav')
    
    dragao_chegada_som.set_volume(volume)
    dragao_som.set_volume(volume)
    chegada_som.set_volume(volume)
    arvore_som.set_volume(volume)
    nuvem_som.set_volume(volume)
    vento_som.set_volume(volume)
    pombo_som.set_volume(volume)
    fogo_som.set_volume(volume)


    # Tamanho das Hitboxes (horizontalmente, verticalmente)
    box_hit_balao = [(52, 104), (66, 10), (88, 16), (110, 12), (130, 10), (150, 60), (134, 14), (114, 8), (96, 16)]
    box_hit_arvore = [(100, 24), (75, 30), (56, 9), (31, 5), (21, 9), (6, 13)]
    box_hit_nuvem = [(173, 97), (28, 21)]
    box_hit_vento = [100, 50]
    box_hit_pombo = [(9, 11), (31, 50), (20, 44)]
    box_hit_fogo = [90, 40]


    # Posição das hitboxes dos balões
    offsets_balao = [(49, 146), (42, 136), (31, 120), (20, 108), (10, 98), (0, 38), (8, 24), (18, 16), (27, 0)]


    # Quantidade que pode existir na tela ao mesmo tempo
    quantidade_arvore = 5
    quantidade_nuvem = 3
    quantidade_vento = 3
    quantidade_pombo = 2
    quantidade_fogo = 2


    # Variável inicial das hitboxes
    box_arvore = [[pygame.Rect(0, 0, 0, 0)] for _ in range(quantidade_arvore)]
    box_nuvem = [[pygame.Rect(0, 0, 0, 0)] for _ in range(quantidade_nuvem)]
    box_vento = [[pygame.Rect(0, 0, 0, 0)] for _ in range(quantidade_vento)]
    box_pombo = [[pygame.Rect(0, 0, 0, 0)] for _ in range(quantidade_pombo)]
    box_fogo = [[pygame.Rect(0, 0, 0, 0)] for _ in range(quantidade_fogo)]


    # Coordenadas iniciais
    ceu_x1 = 0
    ceu_x2 = tamanho_x
    player_balao_x = 10
    player_balao_y = 15
    jopo_balao_x = 10
    jopo_balao_y = 160
    dragao_x = tamanho_x
    chegada_x = 738
    chegada_y = 129
    topo_arvore_x = [tamanho_x] * quantidade_arvore
    nuvem_carregada_x = [tamanho_x] * quantidade_nuvem
    vento_x = [tamanho_x] * quantidade_vento
    vento_y = [tamanho_y] * quantidade_vento
    pombo_x = [tamanho_x] * quantidade_pombo
    pombo_y = [tamanho_y] * quantidade_pombo
    fogo_x = [454] * quantidade_fogo
    fogo_y = [270] * quantidade_fogo


    # Quantidade existente na tela
    arvore = [False] * quantidade_arvore
    nuvem = [False] * quantidade_nuvem
    vento = [False] * quantidade_vento
    pombo = [False] * quantidade_pombo
    fogo = [False] * quantidade_fogo


    # Número que indicará se é para gerar o obstáculo
    numero_aleatorio_arvore = [0] * quantidade_arvore
    numero_aleatorio_nuvem = [0] * quantidade_nuvem 
    numero_aleatorio_vento = [0] * quantidade_vento
    numero_aleatorio_pombo = [0] * quantidade_pombo
    aleatorios = [[3, 0, 0] for _ in range(quantidade_fogo)]  # Definir se a bola de fogo ficará na parte superior ou inferior
    numero_aleatorio_fogo = [0] * quantidade_fogo


    # Variáveis de Tempo
    # Variáveis para tornar o player invunerável se for atingido pelo vento
    espera_vento1 = False
    espera_vento2 = False
    tempo_espera_vento = 2
    ultimo_tempo_player = time.time()
    ultimo_tempo_jopo = time.time() 

    # Duração do jogo
    tempo_inicio = 0
    tempo_medial = 0
    tempo_final = False

    # Troca de Sprite
    ultimo_tempo_chegada = time.time()
    ultimo_tempo_vento = time.time()
    ultimo_tempo_pombo = time.time()
    ultimo_tempo_fogo = time.time()
    ultimo_tempo_dragao = time.time()
    # Intervalo entre a troca
    intervalo_tempo_dragao = 0.3
    intervalo_tempo_pomba = 0.1
    intervalo_tempo_elemento = 0.4  # Mesmo tempo usado para o vento, bola de fogo e chegada


    # Outras variáveis
    esc = False  # Se a tecla esc foi precionado
    alerta = True  # Se é para exibir o alerta
    ajeitar = True  # Arrumar o fundo dos ceús no final
    velocidade_fundo = 3  # Movimentação dos céus e dos obstáculos
    movimento = 4   # Movimentação dos balões 
    vencedor = 3  # Armazenar quem venceu a corrida
    clock = pygame.time.Clock()  # Controlar a taxa de atualização do jogo

    
    # Iniciar as cutscenes
    cutscene(tela)
    tempo_inicio = manual(tela)

    # Laço principal
    while True:
        # Controlador de tempo da primeira parte (o pygame tem o time.get_ticks e o time.set_timer, mas o primeiro é complicado de controlar
        # e o segundo faria o código ficar gigante. Eu precisaria estudar a biblioteca time, para ver se ela resolviria esse problema, pois
        # esse tipo de controlador sofre influência do tamanho do código.
        if tempo_inicio < 3000:
            tempo_inicio +=1

        for evento in pygame.event.get():
            teclas_pressionadas = pygame.key.get_pressed()

            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

            if teclas_pressionadas[pygame.K_ESCAPE]:  # Se a tecla esc doi precionada
                esc = True
            # Verificar o clique do botão esquerdo do mouse
            elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1) or esc:
                mouse_pos = pygame.mouse.get_pos()  # Verificar a posição do mouse
                if (0 <= mouse_pos[0] <= 50 and 0 <= mouse_pos[1] <= 50) or esc:  # Abrir o pause
                    pause_aberto = True
                    esc = False
                    while pause_aberto:  # Enquanto o pause estiver aberto
                        pause(tela, som_image_index)
                        fogo_som.stop()
                        aviso_som.stop()
                        dragao_som.stop()
                        arvore_som.stop()
                        pombo_som.stop()
                        vitoria_som.stop()
                        derrota_som.stop()
                        dragao_chegada_som.stop()
                        nuvem_som.stop()
                        vento_som.stop()
                        chegada_som.stop()
                        pygame.display.flip()

                        for evento in pygame.event.get():
                            teclas_pressionadas = pygame.key.get_pressed()
                            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                                pygame.quit()
                                sys.exit()

                            if teclas_pressionadas[pygame.K_ESCAPE]:  # Fechar o pause pela tecla esc
                                esc = True

                            elif (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1) or esc:
                                mouse_pos = pygame.mouse.get_pos()

                                if (515 <= mouse_pos[0] <= 555 and 200 <= mouse_pos[1] <= 240) or esc:  # Fechar pause
                                    tempo_final = False
                                    exibir_numero(tela)
                                    pause_aberto = False
                                    esc = False

                                if 277 <= mouse_pos[0] <= 389 and 251 <= mouse_pos[1] <= 333:  # Resetar
                                    # Aparecer instruções novamente e resetar o tempo inicial
                                    tempo_inicio = manual(tela)

                                    # Resetar o começo do game
                                    ceu_x1 = 0
                                    ceu_x2 = tamanho_x

                                    player_balao_x = 10
                                    player_balao_y = 15
                                    box_player_balao.clear()

                                    jopo_balao_x = 10
                                    jopo_balao_y = 160
                                    box_jopo_balao.clear()

                                    # Obstáculos
                                    arvore, numero_aleatorio_arvore, box_arvore, topo_arvore_x, _ = \
                                        limpar_tudo(quantidade_arvore, arvore, box_arvore, numero_aleatorio_arvore, False, topo_arvore_x)
                                    nuvem, numero_aleatorio_nuvem, box_nuvem, nuvem_carregada_x, _ = \
                                        limpar_tudo(quantidade_nuvem, nuvem, box_nuvem, numero_aleatorio_nuvem, False, nuvem_carregada_x)
                                    vento, numero_aleatorio_vento, box_vento, vento_x, vento_y = \
                                        limpar_tudo(quantidade_vento, vento, box_vento, numero_aleatorio_vento, False, vento_x, vento_y)
                                    espera_vento1 = False
                                    espera_vento2 = False
                                    pombo, numero_aleatorio_pombo, box_pombo, pombo_x, pombo_y = \
                                        limpar_tudo(quantidade_pombo, pombo, box_pombo, numero_aleatorio_pombo, False, pombo_x, pombo_y)
                                    dragao_x = tamanho_x
                                    fogo, numero_aleatorio_fogo, box_fogo, fogo_x, fogo_y = \
                                        limpar_tudo(quantidade_fogo, fogo, box_fogo, numero_aleatorio_fogo, True, fogo_x, fogo_y)
                                    aleatorios = [[3, 0, 0] for _ in range(quantidade_fogo)]

                                    # Variáveis
                                    alerta = True
                                    pause_aberto = False
                                    tempo_medial = 0
                                    tempo_final = False
                                    ajeitar = True
                                    vencedor = 3

                                if 410 <= mouse_pos[0] <= 522 and 251 <= mouse_pos[1] <= 333: # Alterar o volume da música
                                    som_image_index, volume = definir_volume(volume, True)
                                    pygame.mixer.music.set_volume(volume)
                                    vitoria_som.set_volume(volume)
                                    derrota_som.set_volume(volume)
                                    arvore_som.set_volume(volume)
                                    nuvem_som.set_volume(volume)
                                    vento_som.set_volume(volume)
                                    pombo_som.set_volume(volume)
                                    aviso_som.set_volume(volume)
                                    dragao_chegada_som.set_volume(volume)
                                    dragao_som.set_volume(volume)
                                    fogo_som.set_volume(volume)
                                    chegada_som.set_volume(volume)

        # Movimentação do player respeitando os limites
        teclas_pressionadas = pygame.key.get_pressed()
        if teclas_pressionadas[pygame.K_UP] and player_balao_y > 0:
            player_balao_y -= movimento
        if teclas_pressionadas[pygame.K_DOWN] and player_balao_y < 350:
            player_balao_y += movimento

        # Movimentação do Jopo
        jopo_balao_y = movimento_jopo_balao_y(jopo_balao_x, jopo_balao_y, list_hitbox)

        # Movimentação do fundo
        tela.blit(ceu, (ceu_x1, 0))
        tela.blit(ceu_2, (ceu_x2, 0))

        # Hitboxes dos balões
        box_jopo_balao = []
        box_player_balao = []

        for offset in offsets_balao:
            box_jopo_balao.append(pygame.Rect((jopo_balao_x + offset[0]), (jopo_balao_y + offset[1]), 
                                            box_hit_balao[offsets_balao.index(offset)][0], box_hit_balao[offsets_balao.index(offset)][1]))
            box_player_balao.append(pygame.Rect((player_balao_x + offset[0]), (player_balao_y + offset[1]), 
                                                box_hit_balao[offsets_balao.index(offset)][0], box_hit_balao[offsets_balao.index(offset)][1]))

        # Voltar os Sprites dos balões atingidos depois de 2 segundos
        if sprite_jopo == jopo_balao_atingido:
            if time.time() - ultimo_tempo_jopo > 2:
                sprite_jopo = jopo_balao
        
        if sprite_player == player_balao_atingido:
            if time.time() - ultimo_tempo_player > 2:
                sprite_player = player_balao

        # Desenhar os balões na tela
        tela.blit(sprite_jopo, (jopo_balao_x, jopo_balao_y))
        tela.blit(sprite_player, (player_balao_x, player_balao_y))

        # Desenhar árvore
        for a in range(quantidade_arvore):
            if numero_aleatorio_arvore[a] == 1:
                arvore[a] = True

                for i, hit_box in enumerate(box_hit_arvore):  # Criar as Hitboxes
                    hit_box_x = topo_arvore_x[a] + [0, 13, 22, 35, 40, 47][i]
                    hit_box_y = [576, 546, 537, 532, 523, 510][i]
                    arvore_hit_box = pygame.Rect(hit_box_x, hit_box_y, hit_box[0], hit_box[1])
                    box_arvore[a].append(arvore_hit_box)

                tela.blit(topo_arvore, (topo_arvore_x[a], 510))
            else:
                numero_aleatorio_arvore[a] = 0

        # Desenhar nuvem
        for n in range(quantidade_nuvem):
            if numero_aleatorio_nuvem[n] == 1:
                nuvem[n] = True

                for i, hit_box in enumerate(box_hit_nuvem):  # Criar as Hitboxes
                    hit_box_x = nuvem_carregada_x[n] + [0, 173][i]
                    hit_box_y = random.randint(0, 5) + [0, 28][i]
                    nuvem_hit_box = pygame.Rect(hit_box_x, hit_box_y, hit_box[0], hit_box[1])
                    box_nuvem[n].append(nuvem_hit_box)

                tela.blit(nuvem_carregada, (nuvem_carregada_x[n], random.randint(0, 5)))
            else:
                numero_aleatorio_nuvem[n] = 0

        # Desenhar vento
        for v in range(quantidade_vento):
            if numero_aleatorio_vento[v] == 1:
                if vento_y[v] == tamanho_y:  # Definir posição em Y
                    vento_y[v] = random.randint(0, tamanho_y-50) 
                
                box_vento[v].append(pygame.Rect(vento_x[v], vento_y[v], box_hit_vento[0], box_hit_vento[1]))
                vento[v] = True

                # Mudar os sprites
                if time.time() - ultimo_tempo_vento > intervalo_tempo_elemento:
                    indice_imagem_vento = (indice_imagem_vento + 1) % len(vento_imagens)
                    ultimo_tempo_vento = time.time()
                    tela.blit(vento_imagens[indice_imagem_vento], (vento_x[v], vento_y[v]))
                else:
                    tela.blit(vento_imagens[indice_imagem_vento], (vento_x[v], vento_y[v]))

            else:
                numero_aleatorio_vento[v] = 0

        # Desenhar pombo
        for p in range(quantidade_pombo):
            if numero_aleatorio_pombo[p] == 1:
                if pombo_y[p] == tamanho_y:    # Definir posição em Y
                    pombo_y[p] = random.randint(92, tamanho_y - 50 - 90)

                pombo[p] = True

                for i, hit_box in enumerate(box_hit_pombo):
                    hit_box_x = pombo_x[p] + [0, 9, 40][i]
                    pombo_hit_box = pygame.Rect(hit_box_x, pombo_y[p], hit_box[0], hit_box[1])
                    box_pombo[p].append(pombo_hit_box)

                # Mudar os sprites
                if time.time() - ultimo_tempo_pombo > intervalo_tempo_pomba:
                    indice_imagem_pombo = (indice_imagem_pombo + 1) % len(pombo_imagens)
                    ultimo_tempo_pombo = time.time()
                    tela.blit(pombo_imagens[indice_imagem_pombo], (pombo_x[p], pombo_y[p]))
                else:
                    tela.blit(pombo_imagens[indice_imagem_pombo], (pombo_x[p], pombo_y[p]))

            else:
                numero_aleatorio_pombo[p] = 0


        # Desenhar fogo
        for f in range(quantidade_fogo):
            if numero_aleatorio_fogo[f] == 1:
                fogo[f] = True
                box_fogo[f].append(pygame.Rect(fogo_x[f], fogo_y[f], box_hit_fogo[0], box_hit_fogo[1]))
                
                # Mudar os sprites
                if time.time() - ultimo_tempo_fogo > intervalo_tempo_elemento:
                    indice_imagem_fogo = (indice_imagem_fogo + 1) % len(fogo_imagens)
                    ultimo_tempo_fogo = time.time()
                    tela.blit(fogo_imagens[indice_imagem_fogo], (fogo_x[f], fogo_y[f]))
                else:
                    tela.blit(fogo_imagens[indice_imagem_fogo], (fogo_x[f], fogo_y[f]))
            else:
                numero_aleatorio_fogo[f] = 0

        # Adicionar as hitboxes em uma lista
        list_hitbox = []
        for a in range(quantidade_arvore):
            list_hitbox.append(box_arvore[a])
        for n in range(quantidade_nuvem):
            list_hitbox.append(box_nuvem[n])
        for v in range(quantidade_vento):
            list_hitbox.append(box_vento[v])
        for p in range(quantidade_pombo):
            list_hitbox.append(box_pombo[p])
        for f in range(quantidade_fogo):
            list_hitbox.append(box_fogo[f])
        
        # Verificar essa lista
        for hitbox_list in list_hitbox:  # Verificar a lista de obstáculos (árvore, nuvem, vento, pombo, bola de fogo)
            for hitbox in hitbox_list:  # Verificar a lista de cada obstáculo (árvore 1, árvore 2 ...)
                for box1 in box_jopo_balao:  # Verificar a lista do jopo_balao
                    if box1.colliderect(hitbox):  # Se colide
                        if espera_vento1:  # Se for com o vento, irá manter o sprite
                            sprite_jopo = jopo_balao

                        elif sprite_jopo == jopo_balao:  # Se não, irá mudar ele
                            sprite_jopo = jopo_balao_atingido
                            ultimo_tempo_jopo = time.time()

                            if jopo_balao_x <= player_balao_x:  # Se o player estiver na frente, então ele avançará
                                player_balao_x += 5
                            else:  # Se não, o jopo avançará
                                jopo_balao_x -= 5
                            
                            # Obstáculos
                            for arvores in box_arvore:
                                for hit_arvore in arvores:
                                    if hit_arvore == hitbox:
                                        arvore_som.play()

                            for nuvens in box_nuvem:
                                for hit_nuvem in nuvens:
                                    if hit_nuvem == hitbox:
                                        nuvem_som.play()

                            for ventos in box_vento:
                                for hit_vento in ventos:
                                    if hit_vento == hitbox:
                                        if not espera_vento1:
                                            sprite_jopo = jopo_balao
                                            vento_som.play()
                                            espera_vento1 = True

                            for pombos in box_pombo:
                                for hit_pombo in pombos:
                                    if hit_pombo == hitbox:
                                        pombo_som.play()

                            for fogos in box_fogo:
                                for hit_fogo in fogos:
                                    if hit_fogo == hitbox:
                                        fogo_som.play()

                for box2 in box_player_balao:  # Verificar a lista do player_balao
                    if box2.colliderect(hitbox):  # Se colide
                        if espera_vento2:  # Se for com o vento, irá manter o sprite
                            sprite_player = player_balao

                        elif sprite_player == player_balao:  # Se não, irá mudar ele
                            sprite_player = player_balao_atingido
                            ultimo_tempo_player = time.time()

                            if player_balao_x <= jopo_balao_x:  # Se o jopo estiver na frente, então ele avançará
                                jopo_balao_x += 5
                            else:  # Se não, o player avançará
                                player_balao_x -= 5

                            for arvores in box_arvore:
                                for hit_arvore in arvores:
                                    if hit_arvore == hitbox:
                                        arvore_som.play()

                            # Obstáculos
                            for nuvens in box_nuvem:
                                for hit_nuvem in nuvens:
                                    if hit_nuvem == hitbox:
                                        nuvem_som.play()

                            for ventos in box_vento:
                                for hit_vento in ventos:
                                    if hit_vento == hitbox:
                                        if not espera_vento2:
                                            sprite_player = player_balao
                                            vento_som.play()
                                            espera_vento2 = True

                            for pombos in box_pombo:
                                for hit_pombo in pombos:
                                    if hit_pombo == hitbox:
                                        pombo_som.play()

                            for fogos in box_fogo:
                                for hit_fogo in fogos:
                                    if hit_fogo == hitbox:
                                        fogo_som.play()

        # Invulnerabilidade se bater com o vento
        if espera_vento1:
            tempo_atual1 = time.time()
            if tempo_atual1 - ultimo_tempo_jopo > tempo_espera_vento:
                espera_vento1 = False

        if espera_vento2:
            tempo_atual2 = time.time()
            if tempo_atual2 - ultimo_tempo_player > tempo_espera_vento:
                espera_vento2 = False
        
        # Movimentação dos obstáculos
        # Árvores
        if not tempo_final:
            for a in range(quantidade_arvore):
                if arvore[a] == True:
                    topo_arvore_x[a] -= velocidade_fundo -1
                    if topo_arvore_x[a] <= -100:  # limpar o obstáculo
                        arvore[a], numero_aleatorio_arvore[a], box_arvore[a], topo_arvore_x[a], _ = \
                            limpar_um(arvore[a], box_arvore[a], numero_aleatorio_arvore[a], False, topo_arvore_x[a])
        # Nuvens
        for n in range(quantidade_nuvem):
            if nuvem[n] == True:
                nuvem_carregada_x[n] -= velocidade_fundo + 1
                if nuvem_carregada_x[n] <= -200:  # limpar o obstáculo
                    nuvem[n], numero_aleatorio_nuvem[n], box_nuvem[n], nuvem_carregada_x[n], _ = \
                        limpar_um(nuvem[n], box_nuvem[n], numero_aleatorio_nuvem[n], False, nuvem_carregada_x[n])
        # Vento
        for v in range(quantidade_vento):
            if vento[v] == True:
                vento_x[v] -= velocidade_fundo + 2
                if vento_x[v] <= -100:  # limpar o obstáculo
                    vento[v], numero_aleatorio_vento[v], box_vento[v], vento_x[v], vento_y[v] = \
                        limpar_um(vento[v], box_vento[v], numero_aleatorio_vento[v], False, vento_x[v], vento_y[v])
        # Pombo
        for p in range(quantidade_pombo):
            if pombo[p] == True:
                pombo_x[p] -= velocidade_fundo 
                if pombo_x[p] <= -60:  # limpar o obstáculo
                    pombo[p], numero_aleatorio_pombo[p], box_pombo[p], pombo_x[p], pombo_y[p] = \
                        limpar_um(pombo[p], box_pombo[p], numero_aleatorio_pombo[p], False, pombo_x[p], pombo_y[p])
        
        # Bola de Fogo
        for f in range(quantidade_fogo):
            if fogo[f] == True:
                fogo_x[f] -= velocidade_fundo

                if aleatorios[f][0] == 3:
                    # Definir se a bola de fogo será na parte superior ou inferior da tela e as coordenadas finais
                    aleatorios[f][0] = random.randint(0, 1)
                    aleatorios[f][1] = random.randint(95, 210)
                    aleatorios[f][2] = random.randint(360, 465)

                # Se tiver duas bolas de fogo, uma em cima e outra em baixo, aumentará a distancia entre elas
                if aleatorios[0][0] != aleatorios[1][0] and abs(aleatorios[0][1] - aleatorios[1][2]) <= 320:
                    if aleatorios[f][0] == 0:
                        aleatorios[f][1] -= velocidade_fundo
                    else:
                        aleatorios[f][2] += velocidade_fundo

                # Se a bola tiver em cima
                elif aleatorios[f][0] == 0:
                    if fogo_y[f] > aleatorios[f][1]:
                        fogo_y[f] -= velocidade_fundo

                # Se a bola tiver em baixo
                elif aleatorios[f][0] == 1:
                    if fogo_y[f] < aleatorios[f][2]:
                        fogo_y[f] += velocidade_fundo

                if fogo_x[f] <= -90:  # limpar o obstáculo
                    aleatorios[f][0] = 3
                    aleatorios[f][1] = 0
                    aleatorios[f][2] = 0
                    fogo[f], numero_aleatorio_fogo[f], box_fogo[f], fogo_x[f], fogo_y[f] = \
                        limpar_um(fogo[f], box_fogo[f], numero_aleatorio_fogo[f], True, fogo_x[f], fogo_y[f])


        if tempo_inicio < 3000:  # Começo do game
            # Obstáculos
            numero_aleatorio_arvore = criar_obstaculo(arvore, quantidade_arvore, numero_aleatorio_arvore, [200, 300, 400, 500, 600])
            numero_aleatorio_nuvem = criar_obstaculo(nuvem, quantidade_nuvem, numero_aleatorio_nuvem, [300, 500, 900])
            numero_aleatorio_vento = criar_obstaculo(vento, quantidade_vento, numero_aleatorio_vento, [200, 500, 1000])
            numero_aleatorio_pombo = criar_obstaculo(pombo, quantidade_pombo, numero_aleatorio_pombo, [200, 500])

        elif tempo_medial == 0:  # No meio do game
            if alerta:
                aviso.drawing(tela)
                aviso_som.play()
                tempo_medial = meio_corrida(tela)
                alerta = False
        
        elif tempo_medial < 3000:  # A parte que entra um intruso na corrida
            if tempo_medial < 3000:  # Controlador de tempo da segunda parte
                tempo_medial += 1

            if dragao_x >= 490:  # Movimentar o dragão até um lugar fixo
                dragao_x -= velocidade_fundo 

            for _ in range(1):  # Reproduzir 1 vez
                pygame.mixer.Channel(1).queue(dragao_chegada_som)

            for _ in range(9):  # Reproduzir 9 vezes
                    pygame.mixer.Channel(1).queue(dragao_som)

            if time.time() - ultimo_tempo_dragao > intervalo_tempo_dragao:  # Mudar o sprite dele
                    indice_imagem_dragao = (indice_imagem_dragao + 1) % len(dragao_imagens)
                    ultimo_tempo_dragao = time.time()
                    tela.blit(dragao_imagens[indice_imagem_dragao], (dragao_x, 175))
            else:
                tela.blit(dragao_imagens[indice_imagem_dragao], (dragao_x, 175))

            #Obstáculos
            # Soltar bola de fogo quando a boca estiver aberta, mas como o limite é duas, tem um intervado entre elas
            if indice_imagem_dragao == 2 and dragao_x <= 490:
                numero_aleatorio_fogo = criar_obstaculo(fogo, quantidade_fogo, numero_aleatorio_fogo, [0, 1])
                numero_aleatorio_fogo[0] = 1 

            numero_aleatorio_arvore = criar_obstaculo(arvore, quantidade_arvore, numero_aleatorio_arvore, [500, 600, 700, 800, 900])
            numero_aleatorio_nuvem = criar_obstaculo(nuvem, quantidade_nuvem, numero_aleatorio_nuvem, [500, 900, 1200])

        elif tempo_medial < 3155:  # O intruso indo embora
            if tempo_medial < 3155:
                tempo_medial += 1

            dragao_som.stop()

            if dragao_x < tamanho_x:  # Movimentar o dragão até ele sair da tela
                dragao_x += velocidade_fundo
                pygame.mixer.Channel(1).queue(dragao_chegada_som)

            if time.time() - ultimo_tempo_dragao > intervalo_tempo_dragao:    # Mudar o sprite dele
                    indice_imagem_dragao = (indice_imagem_dragao + 1) % len(dragao_imagens_invertido)
                    ultimo_tempo_dragao = time.time()
                    tela.blit(dragao_imagens_invertido[indice_imagem_dragao], (dragao_x, 175))
            else:
                tela.blit(dragao_imagens_invertido[indice_imagem_dragao], (dragao_x, 175))

            # Obstáculos
            numero_aleatorio_arvore = criar_obstaculo(arvore, quantidade_arvore, numero_aleatorio_arvore, [200, 300, 400, 500, 600])
            numero_aleatorio_nuvem = criar_obstaculo(nuvem, quantidade_nuvem, numero_aleatorio_nuvem, [300, 500, 900])
        
        elif tempo_medial < 5010:  # Reta final
            if tempo_medial < 5010:
                tempo_medial += 1

            dragao_chegada_som.stop()

            # Obstáculos
            numero_aleatorio_arvore = criar_obstaculo(arvore, quantidade_arvore, numero_aleatorio_arvore, [200, 300, 400, 500, 600])
            numero_aleatorio_nuvem = criar_obstaculo(nuvem, quantidade_nuvem, numero_aleatorio_nuvem, [300, 500, 900])
            numero_aleatorio_vento = criar_obstaculo(vento, quantidade_vento, numero_aleatorio_vento, [200, 500, 1000])
            numero_aleatorio_pombo = criar_obstaculo(pombo, quantidade_pombo, numero_aleatorio_pombo, [200, 500])

        else:  # Final
            tempo_final = True

            if ajeitar:
                ceu_x1 -= velocidade_fundo
                ajeitar = False

            pygame.mixer.Channel(1).queue(chegada_som)

            # Parar de mover os balões quando saírem da tela
            if player_balao_x < tamanho_x + 150 or jopo_balao_x < tamanho_x + 150:
                player_balao_x += velocidade_fundo
                jopo_balao_x += velocidade_fundo

            if time.time() - ultimo_tempo_chegada > intervalo_tempo_elemento:  # Mudar o sprite chegada
                indice_imagem_chegada = (indice_imagem_chegada + 1) % len(chegada_imagens)
                ultimo_tempo_chegada = time.time()
                tela.blit(chegada_imagens[indice_imagem_chegada], (chegada_x, chegada_y))
            else:
                tela.blit(chegada_imagens[indice_imagem_chegada], (chegada_x, chegada_y))

            # Imagens que estão no final
            lista_imagem_final = [ceu, (ceu_x1, 0),
                        ceu_2, (ceu_x2, 0),
                        chegada_imagens[indice_imagem_chegada], (chegada_x, chegada_y)]
            for a in range(quantidade_arvore):
                lista_imagem_final.extend([topo_arvore, (topo_arvore_x[a], 510)])
            
            # Decidir o vencedor
            if player_balao_x >= tamanho_x-150 and player_balao_x > jopo_balao_x:
                resultado(tela, True, volume, vencedor)
                vencedor = 1
            elif jopo_balao_x >= tamanho_x-150:
                resultado(tela, False, volume, vencedor)
                vencedor = 0

            if vencedor != 3:  # Avançar para sair da corrida
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    mouse_pos = pygame.mouse.get_pos()  # Verificar a posição do mouse
                    if 344 <= mouse_pos[0] <= 457 and 344 <= mouse_pos[1] <= 427:
                        chegada_som.stop()
                        final_corrida(tela, vencedor, lista_imagem_final)
                        return

        if not tempo_final:  # Movimentar o fundo
            # Mover céu
            ceu_x1 -= velocidade_fundo
            ceu_x2 -= velocidade_fundo

            # Verifica se o fundo chegou ao fim da tela e reposiciona
            if ceu_x1 <= -tamanho_x:
                ceu_x1 = tamanho_x
            if ceu_x2 <= -tamanho_x:
                ceu_x2 = tamanho_x

        # Manter o jogo atualizado
        opcao.drawing(tela)
        pygame.display.flip()
        clock.tick(60)

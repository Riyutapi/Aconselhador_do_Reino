import pygame, sys, os
from tela_inicial import tela_inicial
from corrida_balao import corrida_balao
from paintball import paintball
from futebol_carroca import futebol_carroca
from decisoes import decisoes
from debate import debate
from rpg import rpg
from cartas import cartas

# Inicialização do pygame
pygame.init()

# Definindo as dimensões da tela
largura_tela = 800
altura_tela = 600

tela = pygame.display.set_mode((largura_tela, altura_tela))

# Icone e nome do game
pygame.display.set_caption("Aconselhador do Reino")
pygame.display.set_icon(pygame.image.load('icone.jpeg'))

# Variável para controlar o estado atual do jogo
estado_jogo = "tela_inicial" # Quando abrir o jogo sempre começará na tela inicial


def verificar():
    """
    Função para verificar o estado atual do jogo com base no arquivo save.

    A função verifica a existência do arquivo save e extrai o conteúdo para determinar o estado do jogo em que o jogador parou.
    O estado do jogo é determinado pelo valor armazenado no arquivo save na linha correspondente ao avanço do jogador.

    Returns:
        estado_jogo (str): O estado atual do jogo. Pode ser do minigame1 até o minigame7.

    """
    arquivo = os.path.join("save", "save.txt")

    if os.path.exists(arquivo):  # Verificar se o arquivo save existe
        with open(arquivo, 'r') as file:
            conteudo = file.read()
            linhas = conteudo.split("\n")
            for linha in linhas:
                if "avancar = " in linha: # Verificar em qual minigame o jogador parou
                    valor_avancar = linha.split("=")[-1].strip()
                    padrao = int(valor_avancar)
            if padrao == 1:
                estado_jogo = "minigame1"
            elif padrao == 2:
                estado_jogo = "minigame2"
            elif padrao == 3:
                estado_jogo = "minigame3"
            elif padrao == 4:
                estado_jogo = "minigame4"
            elif padrao == 5:
                estado_jogo = "minigame5"
            elif padrao == 6:
                estado_jogo = "minigame6"
            elif padrao == 7:
                estado_jogo = "minigame7"

    return estado_jogo


# Loop principal do jogo
while True:

    if estado_jogo == "tela_inicial":
        tela_inicial(tela) 
        estado_jogo = verificar()

    elif estado_jogo == "minigame1":
        corrida_balao(tela)
        estado_jogo = verificar()

    elif estado_jogo == "minigame2":
        paintball(tela)
        pygame.quit()
        sys.exit()

    elif estado_jogo == "minigame3":
        futebol_carroca()
        pygame.quit()
        sys.exit()

    elif estado_jogo == "minigame4":
        decisoes()
        pygame.quit()
        sys.exit()

    elif estado_jogo == "minigame5":
        debate()
        pygame.quit()
        sys.exit()

    elif estado_jogo == "minigame6":
        rpg()
        pygame.quit()
        sys.exit()

    elif estado_jogo == "minigame7":
        cartas()
        pygame.quit()
        sys.exit()

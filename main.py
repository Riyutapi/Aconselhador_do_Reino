import pygame
import sys
import os
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
estado_jogo = "tela_inicial"
arquivo = os.path.join("save", "save.txt")
# Loop principal do jogo
while True:
    if estado_jogo == "tela_inicial":
        # Chama a função da tela inicial
        inicio = tela_inicial(tela)
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
                else:
                    estado_jogo = "sair"
    elif estado_jogo == "minigame1":
        # Chama a função do primeiro minigame
        corrida_balao(tela)
    elif estado_jogo == "minigame2":
        # Chama a função do segundo minigame
        paintball()
        pygame.quit()
        sys.exit()
    elif estado_jogo == "minigame3":
        # Chama a função do terceiro minigame
        futebol_carroca()
        pygame.quit()
        sys.exit()
    elif estado_jogo == "minigame4":
        # Chama a função do quarto minigame
        decisoes()
        pygame.quit()
        sys.exit()
    elif estado_jogo == "minigame5":
        # Chama a função do quinto minigame
        debate()
        pygame.quit()
        sys.exit()
    elif estado_jogo == "minigame6":
        # Chama a função do sexto minigame
        rpg()
        pygame.quit()
        sys.exit()
    elif estado_jogo == "minigame7":
        # Chama a função do sétimo minigame
        cartas()
        pygame.quit()
        sys.exit()
    elif estado_jogo == "sair":
        # Fecha o jogo
        pygame.quit()
        sys.exit()

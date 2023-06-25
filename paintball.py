import pygame, sys
from comum import exibir_mensagem

def paintball(tela):
    # Inicialização do pygame
    pygame.init()
    
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()

        superficie_preta = pygame.Surface((800, 600))
        superficie_preta.fill((0, 0, 0))
        tela.blit(superficie_preta, (0, 0))
        exibir_mensagem("Continua...", 255, 255, 255, 50, 0, 0, tela)
        pygame.display.flip()
        tempo_inicial = pygame.time.get_ticks()

        while pygame.time.get_ticks() - tempo_inicial < 3000:  # Esperar mensagem
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:  # Fechar o jogo pela janela
                    pygame.quit()
                    sys.exit()

                elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:  #Ignorar clicke do mouse
                    pass

        pygame.quit()
        sys.exit()

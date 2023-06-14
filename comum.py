import pygame
import sys
import os


def exibir_mensagem(mensagem: str, red: int, blue: int, green: int, tamanho: int, x: int, y: int, tela: pygame.Surface):
    """
    Exibe um texto na tela com as configurações fornecidas.

    Args:
        mensagem (str): Texto a ser exibido na tela.
        red (int): Valor RGB para a componente vermelha da cor do texto.
        blue (int): Valor RGB para a componente azul da cor do texto.
        green (int): Valor RGB para a componente verde da cor do texto.
        tamanho (int): Tamanho do texto.
        x (int): Posição X em que a mensagem será exibida na tela.
        y (int): Posição Y em que a mensagem será exibida na tela.
        tela (pygame.Surface): Superfície da tela onde a mensagem será exibida.

    """
    cor = (red, blue, green)
    fonte = pygame.font.SysFont("Bookman Old Style", tamanho)
    linhas = mensagem.split("\n")  # Divide a mensagem em linhas separadas
    
    for i, linha in enumerate(linhas):
        texto_surface = fonte.render(linha, True, cor)
        
        if x == 0 and y == 0: # Centralizar a mensagem na tela
            largura_texto = texto_surface.get_width()
            posicao_texto = ((tela.get_width() - largura_texto) // 2, (tela.get_height() // 2) - (tamanho // 2) - 5)
        elif x == 1:  # Centralizar o nome na caixa de dialogo
            largura_texto = texto_surface.get_width()
            posicao_texto = ((358 - largura_texto) // 2, y + (i * tamanho))
        elif x == 0:
            largura_texto = texto_surface.get_width()
            posicao_texto = ((tela.get_width() - largura_texto) // 2, y + (i * tamanho))
        elif y == 0:
            largura_texto = texto_surface.get_width()
            posicao_texto = (x, (tela.get_height() // 2) - (tamanho // 2) - 5)
        else: # Colocar a mensagem na posição desejada
            posicao_texto = (x, y + (i * tamanho))
        
        tela.blit(texto_surface, posicao_texto)


class Obj:
    """
    Classe objeto para receber uma imagem, converter em sprite, posicionar e desenhar.

    Métodos:
        __init__(self, image, x, y):
            Inicializa um novo objeto com a imagem fornecida e as coordenadas x e y.

        drawing(self, tela):
            Desenha o objeto na tela fornecida.

    """

    def __init__(self, image: str, x: int, y: int):
        """
        Inicializa um novo objeto com a imagem fornecida e as coordenadas x e y.

        Args:
            image (str): Caminho para o arquivo de imagem.
            x (int): Coordenada x de posicionamento do objeto.
            y (int): Coordenada y de posicionamento do objeto.

        Atributos:
            group (pygame.sprite.Group): Grupo de sprites contendo o objeto.
            sprite (pygame.sprite.Sprite): Sprite do objeto.
            sprite.image (pygame.Surface): Imagem do sprite.
            sprite.rect (pygame.Rect): Retângulo de posicionamento do sprite.
        """
        self.group = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite(self.group)
        self.sprite.image = pygame.image.load(image).convert_alpha()
        self.sprite.rect = self.sprite.image.get_rect()
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    
    def drawing(self, tela: pygame.Surface):
        """
        Desenha o objeto na tela fornecida.

        Args:
            tela (pygame.Surface): Superfície da tela onde o objeto será desenhado.
        """
        self.group.draw(tela)


def dialogo_completo(nome: str, texto: str, personagem: Obj, binario: int, boolean: bool, tela: pygame.Surface):
    """
    Realiza um diálogo completo na tela, exibindo caixa de diálogo, nome do personagem, texto, personagem e botão de avançar.

    Args:
        nome (str): Nome do personagem do diálogo.
        texto (str): Texto a ser exibido na caixa de diálogo.
        personagem (Obj): Objeto que representa o personagem em cena.
        binario (int): Valor binário (0, 1) que controla a posição do botão de avançar.
        boolean (bool): Valor booleano para controlar a atualização da tela.
        tela (pygame.Surface): Superfície da tela onde o diálogo será exibido.

    """
    # Objetos da caixa de diálogo
    caixa_dialogo = Obj('geral/caixa_dialogo.png', 15, 420)
    fundo_personagem = Obj('personagens_falas/1_placa.png', 41, 472)
    avancar_dialogo = Obj('geral/avançar_fala.png', 723, 549)
    avancar_dialogo_original_y = avancar_dialogo.sprite.rect.y
    # Colocar na tela
    caixa_dialogo.drawing(tela)
    exibir_mensagem(nome, 255, 255, 255, 30, 1, 421, tela)
    fundo_personagem.drawing(tela)
    personagem.drawing(tela)
    avancar_dialogo.sprite.rect.y = avancar_dialogo_original_y - (4 * binario)
    avancar_dialogo.drawing(tela)
    exibir_mensagem(texto, 0, 0, 0, 25, 196, 478, tela)
    # Atualizar a tela
    if boolean:
        pygame.display.flip()
        pygame.time.wait(60)


def dialogo_por_letra(nome: str, personagem: Obj, texto: str, tela: pygame.Surface):
    """
    Realiza a exibição de diálogo letra por letra na tela.

    Args:
        nome (str): Nome do personagem do diálogo.
        personagem (Obj): Objeto que representa o personagem em cena.
        texto (str): Texto a ser exibido letra por letra.
        tela (pygame.Surface): Superfície da tela onde o diálogo será exibido.

    Returns:
        Tuple[int, bool]: Uma tupla contendo o contador atual e um valor booleano indicando se o diálogo deve avançar.

    """
    # Objetos da caixa de diálogo
    caixa_dialogo = Obj('geral/caixa_dialogo.png', 15, 420)
    fundo_personagem = Obj('personagens_falas/1_placa.png', 41, 472)
    avancar_dialogo = Obj('geral/avançar_fala.png', 723, 549)
    # Volume para a fala
    arquivo = os.path.join("save", "save.txt")
    with open(arquivo, 'r') as file:
        conteudo = file.read()
        linhas = conteudo.split("\n")
        for linha in linhas:
            if "volume = " in linha:
                valor_volume = linha.split("=")[-1].strip()
                volume = float(valor_volume)
    # Som da fala
    fala_som = pygame.mixer.Sound('personagens_falas/fala.wav')
    fala_som.set_volume(volume)
    # Posição inicial do avancar_dialogo
    avancar_dialogo_original_y = avancar_dialogo.sprite.rect.y
    # Atributos do texto: cor, fonte, posição, se está completo, quantidade de linhas, 
    # armazenar trecho segundo a linha, o que está aparecendo na tela
    cor = (0, 0, 0)
    fonte = pygame.font.SysFont("Bookman Old Style", 25)
    x, y = 196, 478
    ultimo_caractere_exibido = False
    l = 0
    linha=[]
    texto_renderizado = ""
    # Variáveis para manter animação do avancar_dialogo e se é para pular essa função
    contador = 0
    passar = False

    for indice, caractere in enumerate(texto):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: # Fechar o jogo pela janela
                pygame.quit()
                sys.exit()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1: # Avançar o diálogo
                passar = True
                return (contador, passar)
        
        contador += 1
        # Colocar na tela
        caixa_dialogo.drawing(tela)
        exibir_mensagem(nome, 255, 255, 255, 30, 1, 421, tela)
        fundo_personagem.drawing(tela)
        personagem.drawing(tela)
        avancar_dialogo.sprite.rect.y = avancar_dialogo_original_y
        avancar_dialogo.drawing(tela)
        if indice % 20 == 0:
            fala_som.play()
        if not ultimo_caractere_exibido: # Se o ultimo caractere não foi exibido ainda
            if caractere == '\n': # Se tiver uma quebra de linha no texto
                linha.append(texto_renderizado)
                l += 1
                y += 25
                texto_renderizado = ''
            else: # Exibir o texto
                texto_renderizado += caractere
                superficie_texto = fonte.render(texto_renderizado, True, cor)
                for i, linha_texto in enumerate(linha): # exibir o texto que estava nas linhas anteriores
                    superficie_linha = fonte.render(linha_texto, True, cor) 
                    tela.blit(superficie_linha, (x, y - 25 * (l - i)))
                tela.blit(superficie_texto, (x, y))
                pygame.display.flip()
                pygame.time.wait(45)
            
            if indice == len(texto) - 1: # Se chegar no ultimo caractere
                contador = 10
                passar = True
                ultimo_caractere_exibido = True
                return (contador, passar)
            
            if contador >= 16: # Exibir o texto com o avançar_dialogo em outro posição
                caixa_dialogo.drawing(tela)
                exibir_mensagem(nome, 255, 255, 255, 30, 1, 421, tela)
                fundo_personagem.drawing(tela)
                personagem.drawing(tela)
                for i, linha_texto in enumerate(linha):
                    superficie_linha = fonte.render(linha_texto, True, cor)
                    tela.blit(superficie_linha, (x, y - 25 * (l - i)))
                tela.blit(superficie_texto, (x, y))
                avancar_dialogo.sprite.rect.y = avancar_dialogo_original_y - 4
                avancar_dialogo.drawing(tela)
                pygame.time.wait(10)
                pygame.display.flip()
                contador = 0

    
def dialogo_ocioso(contador: int, nome: str, texto: str, personagem: Obj, tela: pygame.Surface):
    """
    Manter a animação do avançar_dialogo quando o texto estiver completo na tela.

    Args:
        contador (int): Contador para mudar a posição do avançar_dialogo.
        nome (str): Nome do personagem do diálogo.
        texto (str): Texto a ser exibido na caixa de diálogo.
        personagem (Obj): Objeto que representa o personagem em cena.
        tela (pygame.Surface): Superfície da tela onde o diálogo será exibido.

    Returns:
        contador (int): O valor atualizado.

    """
    contador += 1
    # Exibe o diálogo com o avançar_dialogo na posição original
    dialogo_completo(nome, texto, personagem, 1, True, tela)
    # Verifica se o contador atingiu o limite
    if contador >= 10: # Exibe o diálogo com o avançar_dialogo em outra posição 
        dialogo_completo(nome, texto, personagem, 0, True, tela)
        contador = 0
        
    return contador

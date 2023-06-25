import pygame, sys, os


def nick_volume():
    """
    Função para obter o nickname e o volume do arquivo de save.

    A função verifica se o arquivo de save existe e lê seu conteúdo para extrair o nickname e o volume armazenados.
    Caso o arquivo de save não exista, a função define o nickname como None e o volume como 1.

    Returns:
        Tuple[str, float]: Uma tupla contendo o nickname e o volume obtidos do arquivo de save.

    """
    arquivo = os.path.join("save", "save.txt")
    if os.path.exists(arquivo):   # Verificar se o arquivo existe
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
    else:  # Se não existir o nickname ficará vazio e o volume no 1
        nick = None
        volume = 1

    return nick, volume


def definir_volume(volume: float, alterar: bool):
    """
    Função para definir o índice de volume e o valor do volume com base nas opções de mudar ou manter.

    A função recebe um valor de volume e um indicador booleano para indicar se o volume deve ser mudado ou ser mantido.
    Com base nesses parâmetros, a função calcula o índice de volume e o valor do volume correspondentes.

    Args:
        volume (float): O valor atual do volume.
        alterar (bool): Indicador booleano para indicar se o volume deve mudar (True) ou manter (False).

    Returns:
        tuple [int, float]: Uma tupla contendo o novo índice de volume e o novo valor do volume.

    """
    som_image_index = int(volume * 10) // 3  # Valor do Índice, utilizando o volume para determinar dentre 4 imagens
    volumes = [(3, 1), (2, 0.6), (1, 0.3), (0, 0)]  # Índice e seu respectivo volume
    current_index = 0  # Variável para armazenar o índice atual

    for i in range(len(volumes)):  # Verificar em qual volume está utilizando o índice como parâmetro
        if som_image_index == volumes[i][0]:
            current_index = i
            break

    if alterar:
        current_index = (current_index + 1) % len(volumes)
    else:
        current_index = (current_index) % len(volumes)

    # Setar a imagem e o volume
    som_image_index = volumes[current_index][0]
    volume = volumes[current_index][1]

    # Salvar o nível do volume no arquivo save.txt
    pasta = "save"
    if os.path.exists(pasta):  # Verificar se a pasta existe
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

    return som_image_index, volume


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

    Obs:
        x = 0: A mensagem vai ser colocada no meio horizontalmente
        y = 0: A mensagem vai ser colocada no meio verticalmente
        x= 1: A mensagem vai ser colocada no meio da caixa de diálogo
        
    """
    cor = (red, blue, green)
    fonte = pygame.font.SysFont("Bookman Old Style", tamanho)
    linhas = mensagem.split("\n")  # Divide a mensagem em linhas separadas
    
    for i, linha in enumerate(linhas):
        texto_surface = fonte.render(linha, True, cor)
        
        if x == 0 and y == 0: # Centralizar a mensagem na tela
            largura_texto = texto_surface.get_width()
            posicao_texto = ((tela.get_width() - largura_texto) // 2, (tela.get_height() // 2) - (tamanho // 2) - (tamanho//10))

        elif x == 1:  # Centralizar o nome na caixa de dialogo
            largura_texto = texto_surface.get_width()
            posicao_texto = ((358 - largura_texto) // 2, y + (i * tamanho))

        elif x == 0:
            largura_texto = texto_surface.get_width()
            posicao_texto = ((tela.get_width() - largura_texto) // 2, y + (i * tamanho))

        elif y == 0:
            largura_texto = texto_surface.get_width()
            posicao_texto = (x, (tela.get_height() // 2) - (tamanho // 2) - (tamanho//10))

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
    caixa_dialogo = Obj('geral/caixa_dialogo.png', 15, 425)
    fundo_personagem = Obj('personagens_falas/1_placa.png', 41, 477)
    avancar_dialogo = Obj('geral/avançar_fala.png', 723, 554)
    avancar_dialogo_original_y = avancar_dialogo.sprite.rect.y

    # Colocar na tela
    caixa_dialogo.drawing(tela)
    exibir_mensagem(nome, 255, 255, 255, 30, 1, 426, tela)
    fundo_personagem.drawing(tela)
    personagem.drawing(tela)
    avancar_dialogo.sprite.rect.y = avancar_dialogo_original_y - (4 * binario)
    avancar_dialogo.drawing(tela)
    exibir_mensagem(texto, 0, 0, 0, 25, 196, 483, tela)

    # Atualizar a tela
    if boolean:
        pygame.display.flip()
        pygame.time.wait(60)  # Aguardar um curto período de tempo entre cada quadro


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
    caixa_dialogo = Obj('geral/caixa_dialogo.png', 15, 425)
    fundo_personagem = Obj('personagens_falas/1_placa.png', 41, 477)
    avancar_dialogo = Obj('geral/avançar_fala.png', 723, 554)
    
    # Volume para a fala
    _, volume = nick_volume()
    _, volume = definir_volume(volume, False)

    # Som da fala
    fala_som = pygame.mixer.Sound('personagens_falas/fala.wav')
    fala_som.set_volume(volume)

    # Posição inicial do avancar_dialogo
    avancar_dialogo_original_y = avancar_dialogo.sprite.rect.y

    # Atributos do texto: cor, fonte, posição, se está completo, quantidade de linhas, 
    # armazenar trecho segundo a linha, o que está aparecendo na tela
    cor = (0, 0, 0)
    fonte = pygame.font.SysFont("Bookman Old Style", 25)
    x, y = 196, 483
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
        exibir_mensagem(nome, 255, 255, 255, 30, 1, 426, tela)
        fundo_personagem.drawing(tela)
        personagem.drawing(tela)
        avancar_dialogo.sprite.rect.y = avancar_dialogo_original_y
        avancar_dialogo.drawing(tela)

        if indice % 20 == 0:  # Som da fala
            fala_som.play()

        if not ultimo_caractere_exibido: # Se o ultimo caractere não foi exibido ainda
            pygame.time.wait(30)  # Aguardar um curto período de tempo entre cada quadro

            if caractere == '\n': # Se tiver uma quebra de linha no texto
                linha.append(texto_renderizado)
                l += 1
                y += 25
                texto_renderizado = ''

            else: # Se não tiver uma quebra de linha no texto
                texto_renderizado += caractere
                superficie_texto = fonte.render(texto_renderizado, True, cor)

                for i, linha_texto in enumerate(linha): # exibir o texto que estava nas linhas anteriores
                    superficie_linha = fonte.render(linha_texto, True, cor) 
                    tela.blit(superficie_linha, (x, y - 25 * (l - i)))

                tela.blit(superficie_texto, (x, y))
                pygame.display.flip()

            if indice == len(texto) - 1: # Se chegar no ultimo caractere
                contador = 10
                passar = True
                return (contador, passar)
            
            if contador >= 20 and caractere != '\n': # Exibir o texto com o avançar_dialogo em outro posição
                caixa_dialogo.drawing(tela)
                exibir_mensagem(nome, 255, 255, 255, 30, 1, 426, tela)
                fundo_personagem.drawing(tela)
                personagem.drawing(tela)

                for i, linha_texto in enumerate(linha):
                    superficie_linha = fonte.render(linha_texto, True, cor)
                    tela.blit(superficie_linha, (x, y - 25 * (l - i)))

                tela.blit(superficie_texto, (x, y))
                avancar_dialogo.sprite.rect.y = avancar_dialogo_original_y - 4
                avancar_dialogo.drawing(tela)
                contador = 0
                pygame.display.flip()

    
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
    # Verifica se o contador atingiu o limite
    if contador >= 10: # Exibe o diálogo com o avançar_dialogo em outra posição 
        dialogo_completo(nome, texto, personagem, 0, True, tela)
        contador = 0
        
    # Exibe o diálogo com o avançar_dialogo na posição original
    dialogo_completo(nome, texto, personagem, 1, True, tela)
        
    return contador


def pause(tela: pygame.Surface, som_image_index: int):
    """
    Desenha um painel com comandos do pygame na tela fornecida.

    Args:
        tela (pygame.Surface): Superfície da tela onde o pause será desenhado.

    """
    # Desenho do painel Pause
    pygame.draw.rect(tela, (100, 48, 8), pygame.Rect(350, 167, 100, 55))
    pygame.draw.rect(tela, (75, 73, 71), pygame.Rect(350, 167, 100, 55), 3)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(355, 172, 90, 45), 2)
    exibir_mensagem("Pause", 159, 84, 26, 30, 0, 176, tela)

    # Desenho do painel Opções
    pygame.draw.rect(tela, (100, 48, 8), pygame.Rect(265, 220, 270, 145))
    pygame.draw.rect(tela, (75, 73, 71), pygame.Rect(265, 220, 270, 145), 3)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(270, 225, 260, 135), 2)
    for i in range(3):
        y = (225 + (i * 45))
        pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(270, y, 260, 45), 1)

    # Desenho do botão para fechar
    pygame.draw.rect(tela, (255, 255, 255), pygame.Rect(515, 200, 40, 40))
    pygame.draw.rect(tela, (0, 0, 0), pygame.Rect(515, 200, 40, 40), 2)
    fechar_img = Obj('geral/fechar.png', 515, 200)
    fechar_img.drawing(tela)
    
    # Opções
    botao1 = Obj('geral/placa2.png', 277, 251)
    botao2 = Obj('geral/placa2.png', 410, 251)
    botao1.drawing(tela)
    botao2.drawing(tela)
    retornar = Obj('geral/reset.png', 298, 260)
    retornar.drawing(tela)
    som_images = ['geral/som(0).png', 'geral/som(0.3).png',
                  'geral/som(0.6).png', 'geral/som(1).png']
    som_images_objs = [Obj(img, 420, 252) for img in som_images]
    som_images_objs[som_image_index].drawing(tela)


def resultado(tela: pygame.Surface, boolean: bool, volume: float, continuar: int):
    """
    Desenha um painel com o resultado do jogo na tela fornecida.

    Args:
        tela (pygame.Surface): Superfície da tela onde o resultado será desenhado.
        boolean (bool): Indica se o resultado é uma vitória (True) ou derrota (False).
        volume (float): O volume do som a ser reproduzido.
        continuar (int): variável para executar os sons se for igual a 3

    """
    # Desenho do painel
    pygame.draw.rect(tela, (100, 48, 8), pygame.Rect(100, 260, 600, 85))
    pygame.draw.rect(tela, (75, 73, 71), pygame.Rect(100, 260, 600, 85), 5)
    pygame.draw.rect(tela, (64, 28, 1), pygame.Rect(105, 265, 590, 75), 4)

    # Botão para avançar
    placa = Obj('geral/placa2.png', 344, 344)
    voltar = pygame.image.load('geral/voltar.png').convert_alpha()
    avancar = pygame.transform.flip(voltar, True, False)
    placa.drawing(tela)
    tela.blit(avancar, (381, 352))

    # Efeitos sonoros
    vitoria_som = pygame.mixer.Sound('geral/vitoria.wav')
    derrota_som = pygame.mixer.Sound('geral/derrota.wav')
    vitoria_som.set_volume(volume)
    derrota_som.set_volume(volume)

    if boolean:
        exibir_mensagem("\(^-^)/ VITÓRIA \(^-^)/", 255, 255, 255, 50, 0, 0, tela)
        if continuar == 3:
            vitoria_som.play()
    else: 
        exibir_mensagem("(;-;)   DERROTA   (;-;)", 0, 0, 0, 50, 0, 0, tela)
        if continuar == 3:
                derrota_som.play()

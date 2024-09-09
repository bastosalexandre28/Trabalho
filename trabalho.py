""" Projeto: Caminhos da Memória"""
import pygame
import random
import time

# Inicializar o Pygame
pygame.init()

# Definir algumas cores
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Definir dimensões da tela
LARGURA_TELA = 600
ALTURA_TELA = 600
TAMANHO_CARTA = 100
MARGEM = 10

# Criar a tela do jogo
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption('Caminhos da Memória')

# Carregar fontes
fonte = pygame.font.Font(None, 40)

# Função para desenhar o tabuleiro de cartas
def desenhar_tabuleiro(tabuleiro, cartas_reveladas):
    tela.fill(BRANCO)
    for i in range(4):
        for j in range(4):
            x = j * (TAMANHO_CARTA + MARGEM) + MARGEM
            y = i * (TAMANHO_CARTA + MARGEM) + MARGEM
            if cartas_reveladas[i][j]:
                pygame.draw.rect(tela, VERDE, (x, y, TAMANHO_CARTA, TAMANHO_CARTA))
                texto = fonte.render(str(tabuleiro[i][j]), True, PRETO)
                tela.blit(texto, (x + 30, y + 30))
            else:
                pygame.draw.rect(tela, AZUL, (x, y, TAMANHO_CARTA, TAMANHO_CARTA))

# Função para criar o tabuleiro de cartas
def criar_tabuleiro():
    numeros = list(range(1, 9)) * 2
    random.shuffle(numeros)
    tabuleiro = []
    for i in range(4):
        linha = []
        for j in range(4):
            linha.append(numeros.pop())
        tabuleiro.append(linha)
    return tabuleiro

# Função principal do jogo
def jogo_memoria():
    tabuleiro = criar_tabuleiro()
    cartas_reveladas = [[False] * 4 for _ in range(4)]
    primeira_carta = None
    segunda_carta = None
    jogando = True
    while jogando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x_mouse, y_mouse = pygame.mouse.get_pos()
                coluna = x_mouse // (TAMANHO_CARTA + MARGEM)
                linha = y_mouse // (TAMANHO_CARTA + MARGEM)
                if not cartas_reveladas[linha][coluna]:
                    cartas_reveladas[linha][coluna] = True
                    if primeira_carta is None:
                        primeira_carta = (linha, coluna)
                    else:
                        segunda_carta = (linha, coluna)
                        if tabuleiro[primeira_carta[0]][primeira_carta[1]] != tabuleiro[segunda_carta[0]][segunda_carta[1]]:
                            time.sleep(0.5)
                            cartas_reveladas[primeira_carta[0]][primeira_carta[1]] = False
                            cartas_reveladas[segunda_carta[0]][segunda_carta[1]] = False
                        primeira_carta = None
                        segunda_carta = None

        desenhar_tabuleiro(tabuleiro, cartas_reveladas)
        pygame.display.flip()

# Função para exibir o menu inicial
def menu_inicial():
    jogando = True
    while jogando:
        tela.fill(BRANCO)
        texto = fonte.render('Caminhos da Memória', True, PRETO)
        texto_iniciar = fonte.render('Clique para começar', True, PRETO)
        tela.blit(texto, (150, 200))
        tela.blit(texto_iniciar, (150, 300))
        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                jogando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                jogo_memoria()

    pygame.quit()

# Iniciar o jogo com o menu principal
menu_inicial()

import pygame
import random
from os import path
from game_screen import SCORE_FONT,YELLOW
import os

from config import IMG_DIR, BLACK, FPS, QUIT,HEIGHT,WIDTH,INIT,FNT_DIR
from assets import load_assets



def game_over_screen(screen,score):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    assets = load_assets()


    # Carrega o fundo da tela inicial
    background = pygame.image.load(path.join(IMG_DIR, 'over.PNG')).convert()
    background_rect = background.get_rect()

    # Tentando imprimir a pontuacao
    
    running = True
    while running:

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        
        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            # Verifica se foi fechado.
            if event.type == pygame.QUIT:
                state = QUIT
                running = False
                

            if event.type == pygame.KEYUP: # QUalquer TECLA (keyup)
                state = INIT
                running = False


        # A cada loop, redesenha o fundo e os sprites
       
        screen.fill(BLACK)
        screen.blit(background, background_rect)
        # IMPRIMINDO A PONTUAÇÂO:
        text_surface = pygame.font.Font(os.path.join(FNT_DIR, 'PressStart2P.ttf'), 28).render("{:08d}".format(score), True, YELLOW)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (250, 200)
        window.blit(text_surface, text_rect)
        

        # Depois de desenhar tudo, inverte o display.
        pygame.display.flip()

    return state

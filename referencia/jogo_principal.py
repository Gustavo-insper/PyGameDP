# ===== Inicialização =====
# ----- Importa e inicia pacotes
# from referencia.jogo_v19 import DONE
#RODAR ESSE CÓDIGO PARA O JOGO FUNCIONAR
import pygame
import random
from config import WIDTH, HEIGHT, INIT, GAME, QUIT
from init_screen import init_screen
from game_screen import game_screen


pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Navinha')

state = INIT
while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game_screen(window)
    #CRIAR TELA DE GAME OVER
    # elif state==DONE:
    #     state= game_over_screen(window)
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


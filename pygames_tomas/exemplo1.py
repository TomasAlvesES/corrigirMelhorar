import pygame 
import sys

# Inicializa o pygame
pygame.init()

# Define tamanho da janela
largura, altura = 600, 400
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo Pygame - Movendo um quadrado")

# Define propriedades do jogador
X = 300
y = 200
velocidade = 5
tamanho = 40

# Loop principal
while True:
for evento in pygame.event.get():

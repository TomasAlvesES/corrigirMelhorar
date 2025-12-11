import pygame
import sys

# Inicializa o pygame
pygame.init()

# Define tamanho da janela
largura, altura = 1000,1000
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Exemplo Pygame - Movendo um Quadrado")

# Define propriedades do jogador
x = 300
y = 200
velocidade = 1
tamanho = 9

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Teclas pressionadas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        x -= velocidade
    if teclas[pygame.K_RIGHT]:
        x += velocidade
    if teclas[pygame.K_UP]:
        y -= velocidade
    if teclas[pygame.K_DOWN]:
        y += velocidade

    # Preenche a tela com preto
    janela.fill((0, 0, 0))

    # Desenha o quadrado (vermelho)
    pygame.draw.rect(janela, (255, 0, 0), (x, y, tamanho, tamanho))

    # Atualiza a tela
    pygame.display.update()

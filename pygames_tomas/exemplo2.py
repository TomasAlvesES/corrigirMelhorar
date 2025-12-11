'''import pygame
import random


pygame.init()

largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("desvie do bloco!")


branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (200, 0, 0)
azul = (0, 80, 200)

player_x = largura // 2
player_y = altura - 50
player_vel = 5
player_tam = 40

obs_x = random.randint(0, largura - 40)
obs_y = -50 
obs_vel = 5
obs_tam = 40

pontos = 0
fonte = pygame.font.SysFont(None, 40)

relogio = pygame.time.clock()

rodando = True
while rodando:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if teclas [pygame.K_RIGHT] and player_x < largura - player_tam:
        player_x += player_vel
    
        obs_y += obs_vel
    
    if obs_y > altura:
        obs_y = -obs_tam
        obs_x = random.randint(0, largura - obs_tam)
        pontos += 1
        obs_vel += 0.2

    jogador = pygame.rect(player_x, player_y, player_tam, player_tam) #???
    obstaculo = pygame.rect(obs_x, obs_y, obs_tam, obs_tam) #???

    if jogador.colliderect(obstaculo):
        print("game over! ")
        rodando = False

    tela.fill(branco)
    pygame.draw.rect(tela, azul, jogador)
    pygame.draw.rect(tela, vermelho, obstaculo)

    texto = fonte.render(f"ppontos: {pontos}", True, preto)
    tela.blit(texto (10, 10))

    pygame.display.update()

pygame.quit()'''

import pygame
import random

pygame.init()

largura = 600
altura = 400
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Desvie do bloco!")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (200, 0, 0)
azul = (0, 80, 200)

# Player
player_x = largura // 2
player_y = altura - 60
player_vel = 5
player_tam = 40

# Obstáculo
obs_x = random.randint(0, largura - 40)
obs_y = -50 
obs_vel = 5
obs_tam = 40

# Pontos
pontos = 0
fonte = pygame.font.SysFont(None, 40)

# Relógio (corrigido)
relogio = pygame.time.Clock()

rodando = True
while rodando:
    relogio.tick(60)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
    
    # Movimento do jogador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and player_x > 0:
        player_x -= player_vel
    if teclas[pygame.K_RIGHT] and player_x < largura - player_tam:
        player_x += player_vel

    # Movimento do obstáculo (estava dentro do IF errado)
    obs_y += obs_vel

    # Reseta o obstáculo e aumenta velocidade
    if obs_y > altura:
        obs_y = -obs_tam
        obs_x = random.randint(0, largura - obs_tam)
        pontos += 1
        obs_vel += 0.2

    # Rects (corrigido)
    jogador = pygame.Rect(player_x, player_y, player_tam, player_tam)
    obstaculo = pygame.Rect(obs_x, obs_y, obs_tam, obs_tam)

    # Colisão
    if jogador.colliderect(obstaculo):
        print("Game Over!")
        rodando = False

    # Desenho na tela
    tela.fill(branco)
    pygame.draw.rect(tela, azul, jogador)
    pygame.draw.rect(tela, vermelho, obstaculo)

    texto = fonte.render(f"Pontos: {pontos}", True, preto)
    tela.blit(texto, (10, 10))

    pygame.display.update()

pygame.quit()


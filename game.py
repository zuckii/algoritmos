import pygame
import random

pygame.init()

# Configuração da tela para ocupar toda a resolução
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Tela cheia
screen_width, screen_height = screen.get_size()  # Obter o tamanho da tela
clock = pygame.time.Clock()

# Velocidade da raquete
velocidade_raquete = 10

# Posições iniciais da raquete e bola
x = 200
y = screen_height // 2 - 140
player1 = (x, y)

a = screen_width - 220
b = screen_height // 2 - 140
player2 = (a, b)

# Configurações da bola
bola_x = screen_width // 2
bola_y = screen_height // 2
bola_radius = 10
bola_dx = random.choice([-1, 1]) * 5  # Direção aleatória (velocidade inicial mais rápida)
bola_dy = random.choice([-1, 1]) * 5  # Direção aleatória (velocidade inicial mais rápida)

# Flag para saber se a bola já acelerou após o primeiro contato
bola_acelerou = False

# Definindo as dimensões da tela
altura_ret = 280

# Pontuação dos jogadores
pontos_player1 = 0
pontos_player2 = 0

# Cores
cor_fundo = (0, 0, 50)  # Fundo mais escuro
cor_raquete = (255, 255, 255)  # Cor das raquetes (branco)
cor_bola = (255, 165, 0)  # Cor da bola (laranja)
cor_texto = (255, 255, 255)  # Cor do texto

# Função para reiniciar a bola
def reiniciar_bola():
    global bola_x, bola_y, bola_dx, bola_dy, bola_acelerou
    bola_x = screen_width // 2
    bola_y = screen_height // 2
    bola_dx = random.choice([-1, 1]) * 5  # Velocidade inicial mais rápida
    bola_dy = random.choice([-1, 1]) * 5  # Velocidade inicial mais rápida
    bola_acelerou = False  # Reseta a aceleração

# Função para exibir a tela de vitória
def mostrar_vencedor(vencedor):
    font = pygame.font.SysFont("Arial", 80, bold=True)
    texto = font.render(f"{vencedor} venceu!", True, cor_texto)
    screen.fill((0, 0, 0))  # Tela preta para mostrar a vitória
    screen.blit(texto, (screen_width // 4, screen_height // 3))
    pygame.display.flip()

    # Espera por 3 segundos para mostrar a vitória
    pygame.time.wait(3000)

# Função para reiniciar o jogo
def reiniciar_jogo():
    global pontos_player1, pontos_player2
    pontos_player1 = 0
    pontos_player2 = 0
    reiniciar_bola()

# Função para desenhar o rastro da bola
def desenhar_rastro(bola_x, bola_y):
    if abs(bola_dx) > 7 or abs(bola_dy) > 7:  # Quando a bola estiver muito rápida
        rastro_alpha = 50  # Transparência do rastro
        cor_rastro = (255, 165, 0, rastro_alpha)  # Cor laranja com transparência
        pygame.draw.circle(screen, cor_rastro, (bola_x, bola_y), bola_radius * 1.5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:  # Pressionar 'R' para reiniciar o jogo
            reiniciar_jogo()

    # Captura de eventos do teclado para movimentar as raquetes
    pk = pygame.key.get_pressed()
    if pk[pygame.K_UP]:
        b -= velocidade_raquete
    if pk[pygame.K_DOWN]:
        b += velocidade_raquete
    if pk[pygame.K_w]:
        y -= velocidade_raquete
    if pk[pygame.K_s]:
        y += velocidade_raquete

    # Limita a posição das raquetes para não ultrapassarem os limites da tela
    y = max(0, min(y, screen_height - altura_ret))
    b = max(0, min(b, screen_height - altura_ret))

    # Movimento da bola
    bola_x += bola_dx
    bola_y += bola_dy

    # Colisão com o teto e o chão
    if bola_y - bola_radius <= 0 or bola_y + bola_radius >= screen_height:
        bola_dy = -bola_dy  # Inverte a direção vertical

    # Colisão com a raquete do jogador 1 (esquerda)
    if x < bola_x - bola_radius < x + 15 and y < bola_y < y + altura_ret:
        bola_dx = -bola_dx  # Inverte a direção horizontal
        if not bola_acelerou:  # Acelera apenas uma vez, no primeiro toque
            bola_dx *= 2
            bola_dy *= 2
            bola_acelerou = True

    # Colisão com a raquete do jogador 2 (direita)
    if a < bola_x + bola_radius < a + 15 and b < bola_y < b + altura_ret:
        bola_dx = -bola_dx  # Inverte a direção horizontal
        if not bola_acelerou:  # Acelera apenas uma vez, no primeiro toque
            bola_dx *= 2
            bola_dy *= 2
            bola_acelerou = True

    # Checar se a bola passou da parede (marcar ponto e reiniciar a bola)
    if bola_x - bola_radius <= 0:  # Player 2 ganha ponto
        pontos_player2 += 1
        reiniciar_bola()

    if bola_x + bola_radius >= screen_width:  # Player 1 ganha ponto
        pontos_player1 += 1
        reiniciar_bola()

    # Verificar se algum jogador ganhou (pontuação máxima 5)
    if pontos_player1 == 5:
        mostrar_vencedor("Player 1")
        reiniciar_jogo()
    elif pontos_player2 == 5:
        mostrar_vencedor("Player 2")
        reiniciar_jogo()

    # Preenche o fundo da tela com cor
    screen.fill(cor_fundo)

    # Desenha as raquetes com borda arredondada e mais estilizada
    pygame.draw.rect(screen, cor_raquete, [x, y, 15, altura_ret], border_radius=10)  # Raquete jogador 1
    pygame.draw.rect(screen, cor_raquete, [a, b, 15, altura_ret], border_radius=10)  # Raquete jogador 2

    # Desenha a bola com borda arredondada
    pygame.draw.circle(screen, cor_bola, (bola_x, bola_y), bola_radius)

    # Desenha o rastro da bola (quando ela estiver rápida)
    desenhar_rastro(bola_x, bola_y)

    # Exibe a pontuação na tela
    fonte = pygame.font.SysFont("Arial", 40, bold=True)
    texto_pontos = fonte.render(f"Player 1: {pontos_player1}  Player 2: {pontos_player2}", True, cor_texto)
    screen.blit(texto_pontos, (screen_width // 2 - 150, 20))

    # Atualiza a tela
    pygame.display.flip()

    # Limita a taxa de quadros para 60 FPS
    clock.tick(60)

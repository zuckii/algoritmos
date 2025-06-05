import pygame
import random

pygame.init()

# Configuração da tela
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
clock = pygame.time.Clock()

# Velocidade da raquete
velocidade_raquete = 15

# Posições iniciais
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
bola_dx = random.choice([-1, 1]) * 5
bola_dy = random.choice([-1, 1]) * 5
bola_acelerou = False

altura_ret = 280
pontos_player1 = 0
pontos_player2 = 0

# Cores
cor_fundo = (0, 0, 50)
cor_raquete = (255, 255, 255)
cor_bola = (255, 165, 0)
cor_texto = (255, 255, 255)

def reiniciar_bola():
    global bola_x, bola_y, bola_dx, bola_dy, bola_acelerou
    bola_x = screen_width // 2
    bola_y = screen_height // 2
    bola_dx = random.choice([-1, 1]) * 5
    bola_dy = random.choice([-1, 1]) * 5
    bola_acelerou = False

def desenhar_rastro(bola_x, bola_y):
    if abs(bola_dx) > 7 or abs(bola_dy) > 7:
        rastro_alpha = 50
        cor_rastro = (255, 165, 0, rastro_alpha)
        pygame.draw.circle(screen, cor_rastro, (bola_x, bola_y), int(bola_radius * 1.5))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            pygame.quit()
            raise SystemExit

    # === Movimento automático da IA (segue a bola com limite de velocidade) ===
    if y + altura_ret // 2 < bola_y:
        y += velocidade_raquete
    elif y + altura_ret // 2 > bola_y:
        y -= velocidade_raquete

    if b + altura_ret // 2 < bola_y:
        b += velocidade_raquete
    elif b + altura_ret // 2 > bola_y:
        b -= velocidade_raquete

    # Limita posição das raquetes
    y = max(0, min(y, screen_height - altura_ret))
    b = max(0, min(b, screen_height - altura_ret))

    # Movimento da bola
    bola_x += bola_dx
    bola_y += bola_dy

    # Colisão com teto e chão
    if bola_y - bola_radius <= 0 or bola_y + bola_radius >= screen_height:
        bola_dy = -bola_dy

    # Colisão com raquetes
    if x < bola_x - bola_radius < x + 15 and y < bola_y < y + altura_ret:
        bola_dx = -bola_dx
        if not bola_acelerou:
            bola_dx *= 2
            bola_dy *= 2
            bola_acelerou = True

    if a < bola_x + bola_radius < a + 15 and b < bola_y < b + altura_ret:
        bola_dx = -bola_dx
        if not bola_acelerou:
            bola_dx *= 2
            bola_dy *= 2
            bola_acelerou = True

    # Pontuação e reinício da bola
    if bola_x - bola_radius <= 0:
        pontos_player2 += 1
        reiniciar_bola()

    if bola_x + bola_radius >= screen_width:
        pontos_player1 += 1
        reiniciar_bola()

    # Desenho da tela
    screen.fill(cor_fundo)

    pygame.draw.rect(screen, cor_raquete, [x, y, 15, altura_ret], border_radius=10)
    pygame.draw.rect(screen, cor_raquete, [a, b, 15, altura_ret], border_radius=10)

    pygame.draw.circle(screen, cor_bola, (bola_x, bola_y), bola_radius)
    desenhar_rastro(bola_x, bola_y)

    fonte = pygame.font.SysFont("Arial", 40, bold=True)
    texto_pontos = fonte.render(f"Player 1: {pontos_player1}  Player 2: {pontos_player2}", True, cor_texto)
    screen.blit(texto_pontos, (screen_width // 2 - 150, 20))

    pygame.display.flip()
    clock.tick(60)

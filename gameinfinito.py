import pygame
import random
import time

# Inicialização
pygame.init()

# Tela cheia
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
clock = pygame.time.Clock()

# Cores
COR_FUNDO = (0, 0, 50)
COR_RAQUETE = (255, 255, 255)
COR_BOLA = (255, 165, 0)
COR_TEXTO = (255, 255, 255)

# Raquetes
LARGURA_RAQUETE = 15
ALTURA_RAQUETE = 280
VEL_RAQUETE = 20
x_p1 = 200
x_p2 = screen_width - 220
y_p1 = screen_height // 2 - ALTURA_RAQUETE // 2
y_p2 = screen_height // 2 - ALTURA_RAQUETE // 2

# Pontuação
pontos_p1 = 0
pontos_p2 = 0
fonte = pygame.font.SysFont("Arial", 40, bold=True)

# Criar bola
def criar_bola(dx=None):
    if dx is None:
        dx = random.choice([-1, 1]) * random.randint(4, 7)
    dy = random.choice([-1, 1]) * random.randint(4, 7)
    return {
        "x": screen_width // 2,
        "y": screen_height // 2,
        "dx": dx,
        "dy": dy,
        "acelerou": False
    }

# Bola inicial
bolas = [criar_bola()]
ultimo_spawn = time.time()

# Loop principal
while True:
    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            pygame.quit()
            raise SystemExit

    # Spawn de novas bolas a cada 7 segundos
    if time.time() - ultimo_spawn > 7:
        for _ in range(2):
            bolas.append(criar_bola(dx=random.randint(4, 7)))   # direita
        for _ in range(2):
            bolas.append(criar_bola(dx=-random.randint(4, 7)))  # esquerda
        ultimo_spawn = time.time()

    # Atualização das bolas
    novas_bolas = []
    for bola in bolas:
        bola["x"] += bola["dx"]
        bola["y"] += bola["dy"]

        # Rebote no teto ou chão
        if bola["y"] <= 0 or bola["y"] >= screen_height - 10:
            bola["dy"] *= -1

        # Colisão com Player 1
        if (
            x_p1 <= int(bola["x"]) <= x_p1 + LARGURA_RAQUETE and
            y_p1 <= int(bola["y"]) <= y_p1 + ALTURA_RAQUETE
        ):
            bola["dx"] *= -1
            if not bola["acelerou"]:
                bola["dx"] *= 1.5
                bola["dy"] *= 1.5
                bola["acelerou"] = True

        # Colisão com Player 2
        elif (
            x_p2 <= int(bola["x"]) <= x_p2 + LARGURA_RAQUETE and
            y_p2 <= int(bola["y"]) <= y_p2 + ALTURA_RAQUETE
        ):
            bola["dx"] *= -1
            if not bola["acelerou"]:
                bola["dx"] *= 1.5
                bola["dy"] *= 1.5
                bola["acelerou"] = True

        # Saiu pela esquerda
        elif bola["x"] < 0:
            pontos_p2 += 1
            continue

        # Saiu pela direita
        elif bola["x"] > screen_width:
            pontos_p1 += 1
            continue

        # Controle de velocidade máxima
        max_vel = 20
        bola["dx"] = max(-max_vel, min(bola["dx"], max_vel))
        bola["dy"] = max(-max_vel, min(bola["dy"], max_vel))

        novas_bolas.append(bola)

    bolas = novas_bolas

    # IA Player 1 (esquerda)
    bolas_p1 = [b for b in bolas if b["dx"] < 0]
    if bolas_p1:
        bola_alvo = min(bolas_p1, key=lambda b: abs(b["x"] - x_p1))
        destino_y = bola_alvo["y"] - ALTURA_RAQUETE // 2
        y_p1 += (destino_y - y_p1) * 0.1

    # IA Player 2 (direita)
    bolas_p2 = [b for b in bolas if b["dx"] > 0]
    if bolas_p2:
        bola_alvo_2 = min(bolas_p2, key=lambda b: abs(b["x"] - x_p2))
        destino_y_2 = bola_alvo_2["y"] - ALTURA_RAQUETE // 2
        y_p2 += (destino_y_2 - y_p2) * 0.1

    # Limita raquetes dentro da tela
    y_p1 = max(0, min(y_p1, screen_height - ALTURA_RAQUETE))
    y_p2 = max(0, min(y_p2, screen_height - ALTURA_RAQUETE))

    # Desenho da tela
    screen.fill(COR_FUNDO)
    pygame.draw.rect(screen, COR_RAQUETE, [x_p1, y_p1, LARGURA_RAQUETE, ALTURA_RAQUETE], border_radius=10)
    pygame.draw.rect(screen, COR_RAQUETE, [x_p2, y_p2, LARGURA_RAQUETE, ALTURA_RAQUETE], border_radius=10)

    for bola in bolas:
        pygame.draw.circle(screen, COR_BOLA, (int(bola["x"]), int(bola["y"])), 10)

    # Placar
    placar = fonte.render(f"Esquerda: {int(pontos_p1)}  |  Direita: {int(pontos_p2)}", True, COR_TEXTO)
    screen.blit(placar, (screen_width // 2 - placar.get_width() // 2, 20))

    # Atualiza tela
    pygame.display.flip()
    clock.tick(60)

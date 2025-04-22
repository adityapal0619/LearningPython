import pygame
import sys

pygame.init()

# Window size
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jumping Dino")

clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (34, 177, 76)

# Dino setup
dino = pygame.Rect(100, 300, 50, 50)
dino_velocity = 0
is_jumping = False
gravity = 1

# Obstacle setup
obstacle = pygame.Rect(800, 300, 40, 50)

# Score setup
score = 0
font = pygame.font.SysFont(None, 40)

def show_score():
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))  # Top-left corner

# Game loop
running = True
while running:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Spacebar to jump
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                dino_velocity = -15

    # Jumping logic
    if is_jumping:
        dino.y += dino_velocity
        dino_velocity += gravity
        if dino.y >= 300:
            dino.y = 300
            is_jumping = False

    # Move obstacle
    obstacle.x -= 5
    if obstacle.x < 0:
        obstacle.x = 800
        score += 1  # Increase score when obstacle passes

    # Collision check
    if dino.colliderect(obstacle):
        print("Game Over!")
        running = False

    # Draw dino and obstacle
    pygame.draw.rect(screen, GREEN, dino)
    pygame.draw.rect(screen, BLACK, obstacle)

    # Show score
    show_score()

    # Update screen
    pygame.display.update()
    clock.tick(60)
print("Game Over! Final Score:", score)
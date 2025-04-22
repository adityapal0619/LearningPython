import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Window setup
WIDTH, HEIGHT = 400, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Car Racing Game")

# Colors
WHITE = (255, 255, 255)
GRAY = (50, 50, 50)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player Car
player_car = pygame.Rect(WIDTH//2 - 25, HEIGHT - 100, 50, 80)

# Enemy Cars
enemy_cars = []
for _ in range(3):
    x = random.randint(0, WIDTH - 50)
    y = random.randint(-600, -100)
    enemy_cars.append(pygame.Rect(x, y, 50, 80))

speed = 5

# Game loop
def game_loop():
    run = True
    while run:
        clock.tick(60)
        win.fill(GRAY)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

        # Key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_car.x > 0:
            player_car.x -= 5
        if keys[pygame.K_RIGHT] and player_car.x < WIDTH - player_car.width:
            player_car.x += 5

        # Move enemy cars
        for enemy in enemy_cars:
            enemy.y += speed
            if enemy.y > HEIGHT:
                enemy.y = random.randint(-600, -100)
                enemy.x = random.randint(0, WIDTH - 50)

            # Collision detection
            if player_car.colliderect(enemy):
                print("Game Over!")
                run = False

        # Draw everything
        pygame.draw.rect(win, BLUE, player_car)
        for enemy in enemy_cars:
            pygame.draw.rect(win, RED, enemy)

        pygame.display.update()

game_loop()

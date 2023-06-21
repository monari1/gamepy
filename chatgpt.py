import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sample Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define player properties
player_width = 50
player_height = 50
player_x = (WIDTH - player_width) // 2
player_y = HEIGHT - player_height - 10
player_speed = 5

# Define item properties
item_width = 30
item_height = 30
item_x = random.randint(0, WIDTH - item_width)
item_y = -item_height
item_speed = 3

# Define obstacle properties
obstacle_width = 50
obstacle_height = 50
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 4

# Initialize game variables
score = 0
time_limit = 30  # seconds
clock = pygame.time.Clock()

# Load game fonts
font = pygame.font.SysFont(None, 36)

# Game loop
running = True
start_time = pygame.time.get_ticks()

while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Update item position
    item_y += item_speed
    if item_y > HEIGHT:
        item_x = random.randint(0, WIDTH - item_width)
        item_y = -item_height
        score += 1

    # Update obstacle position
    obstacle_y += obstacle_speed
    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height

    # Collision detection
    if player_x < item_x + item_width and player_x + player_width > item_x and player_y < item_y + item_height and player_y + player_height > item_y:
        item_x = random.randint(0, WIDTH - item_width)
        item_y = -item_height
        score += 1

    if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
        running = False

    # Clear the screen
    # window.fill(BLACK)

    # Draw the player, items, and obstacles
    pygame.draw.rect(window, WHITE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(window, WHITE, (item_x, item_y, item_width, item_height))
    pygame.draw.rect(window, WHITE, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))

    # Display the score
    score_text = font.render("Score: " + str(score), True, WHITE)
    window.blit(score_text, (10, 10))

    # Display the time
    elapsed_time = (pygame.time.get_ticks() - start_time) // 1000
